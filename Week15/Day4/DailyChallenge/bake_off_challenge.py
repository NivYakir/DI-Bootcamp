import numpy as np
import matplotlib.pyplot as plt
import statsmodels
from statsmodels.stats.power import zt_ind_solve_power
from statsmodels.stats.proportion import proportion_effectsize

# ==========================================
# TASK 1: Calculate Required Sample Size
# ==========================================
print("=" * 60)
print("TASK 1: Sample Size Calculation for Bakery A/B Test")
print("=" * 60)

# Given parameters
current_conversion = 0.05  # 5% current conversion rate
new_conversion = 0.07      # 7% expected new conversion rate
alpha = 0.05               # Significance level
power = 0.8                # Desired power (1 - beta)
effect_size_given = 0.2    # Given effect size

# Calculate Cohen's h effect size for proportions
effect_size_calculated = proportion_effectsize(new_conversion, current_conversion)

print(f"\nGiven Information:")
print(f"  Current conversion rate: {current_conversion*100}%")
print(f"  New conversion rate: {new_conversion*100}%")
print(f"  Significance level (α): {alpha}")
print(f"  Desired power: {power}")
print(f"  Given effect size: {effect_size_given}")
print(f"  Calculated Cohen's h: {effect_size_calculated:.4f}")

# Calculate sample size per group using the GIVEN effect size
sample_size_per_group = zt_ind_solve_power(
    effect_size=effect_size_given,
    alpha=alpha,
    power=power,
    ratio=1.0,  # Equal sample sizes in both groups
    alternative='two-sided'
)

print(f"\n📊 RESULTS:")
print(f"  Sample size per group: {int(np.ceil(sample_size_per_group))}")
print(f"  Total sample size needed: {int(np.ceil(sample_size_per_group)) * 2}")

# ==========================================
# TASK 2: Analyze Impact of Different Effect Sizes
# ==========================================
print("\n" + "=" * 60)
print("TASK 2: Impact of Different Effect Sizes")
print("=" * 60)

effect_sizes = [0.1, 0.2, 0.3, 0.4]
sample_sizes = []

print("\nSample Size Requirements for Different Effect Sizes:")
print("-" * 60)

for es in effect_sizes:
    n = zt_ind_solve_power(
        effect_size=es,
        alpha=alpha,
        power=power,
        ratio=1.0,
        alternative='two-sided'
    )
    sample_sizes.append(int(np.ceil(n)))
    print(f"  Effect Size: {es:.1f} → Sample per group: {int(np.ceil(n)):,} → Total: {int(np.ceil(n))*2:,}")

# ==========================================
# TASK 3: Visualization
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Sample Size vs Effect Size
ax1.plot(effect_sizes, sample_sizes, 'bo-', linewidth=2, markersize=10)
ax1.set_xlabel('Effect Size (Cohen\'s h)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Sample Size per Group', fontsize=12, fontweight='bold')
ax1.set_title('Sample Size Requirements vs Effect Size\n(α=0.05, power=0.8)', 
              fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, max(sample_sizes) * 1.1)

# Add value labels on points
for es, ss in zip(effect_sizes, sample_sizes):
    ax1.annotate(f'{ss:,}', xy=(es, ss), xytext=(0, 10),
                textcoords='offset points', ha='center', fontweight='bold')

# Plot 2: Inverse Relationship (Hyperbolic curve)
ax2.plot(effect_sizes, sample_sizes, 'ro-', linewidth=2, markersize=10)
ax2.set_xlabel('Effect Size', fontsize=12, fontweight='bold')
ax2.set_ylabel('Sample Size per Group', fontsize=12, fontweight='bold')
ax2.set_title('The Inverse Relationship:\nSmaller Effect = More Samples Needed', 
              fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_yscale('log')  # Log scale shows the relationship more clearly

# Add annotations
ax2.annotate('Small effects need\nLOTS of samples!', 
            xy=(0.1, sample_sizes[0]), xytext=(0.15, sample_sizes[0]*2),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, color='red', fontweight='bold')

ax2.annotate('Large effects need\nfewer samples', 
            xy=(0.4, sample_sizes[3]), xytext=(0.35, sample_sizes[3]/2),
            arrowprops=dict(arrowstyle='->', color='green', lw=2),
            fontsize=10, color='green', fontweight='bold')

plt.tight_layout()
plt.savefig('sample_size_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# ==========================================
# TASK 3: Explanation
# ==========================================
print("\n" + "=" * 60)
print("TASK 3: Understanding the Relationship")
print("=" * 60)

print("""
🥐 THE BAKERY'S GUIDE TO A/B TESTING 🥐

Imagine you're tasting pastries to find the best recipe:

1️⃣  WHAT IS EFFECT SIZE?
   Effect size is like the DIFFERENCE in deliciousness between two recipes.
   
   - SMALL effect (0.1): "Hmm, this croissant is slightly flakier"
   - LARGE effect (0.4): "WOW! This croissant is DRAMATICALLY better!"

2️⃣  WHY DOES SAMPLE SIZE CHANGE?
   
   The SMALLER the difference, the MORE taste tests you need to be sure!
   
   📊 Our Results Show:
   • Effect 0.1 → Need {:,} customers per group (tiny improvement, need lots of data!)
   • Effect 0.2 → Need {:,} customers per group
   • Effect 0.3 → Need {:,} customers per group  
   • Effect 0.4 → Need {:,} customers per group (big improvement, fewer tests needed!)

3️⃣  THE INVERSE RELATIONSHIP:
   
   Sample Size ≈ 1 / (Effect Size)²
   
   When effect size DOUBLES (0.2 → 0.4):
   Sample size drops to about 1/4 (from {:,} to {:,})!
   
   Think of it like this:
   - Spotting a GIANT cake (large effect) → Easy! Don't need many looks
   - Spotting a tiny sprinkle difference (small effect) → Hard! Need many looks

4️⃣  WHY THIS MATTERS FOR YOUR BAKERY:
   
   ⏰ TIME: Detecting small improvements takes WEEKS of data collection
   💰 COST: More samples = more resources spent on testing
   🎯 CONFIDENCE: Proper sample size ensures you're not fooled by random luck
   
   Real example from YOUR test:
   - Going from 5% → 7% conversion (effect ~0.04-0.05 in reality)
   - Using effect size 0.2 needs {:,} customers per group
   - That's {:,} total customers!
   - At 100 visitors/day = about {:,} days per group

5️⃣  THE GOLDEN BALANCE:
   
   ✅ TOO SMALL sample → Might miss real improvements (lose money!)
   ✅ TOO LARGE sample → Waste time testing when you could be selling!
   ✅ JUST RIGHT → Confidently detect real improvements efficiently!

🎯 BOTTOM LINE FOR THE BAKERY TEAM:
   "Bigger differences are easier to spot with fewer customers.
    Tiny improvements need lots of data to confirm they're real.
    Plan your sample size BEFORE testing to avoid wasted effort!"
""".format(sample_sizes[0], sample_sizes[1], sample_sizes[2], sample_sizes[3],
           sample_sizes[1], sample_sizes[3],
           sample_sizes[1], sample_sizes[1]*2, 
           int(np.ceil(sample_sizes[1]/100))))

print("\n" + "=" * 60)
print("📈 Key Takeaway:")
print("=" * 60)
print("""
As effect size INCREASES → Sample size DECREASES (inverse relationship)

Why? Statistics works like detective work:
- BIG clues (large effects) → Easy to spot → Need less evidence
- SMALL clues (small effects) → Hard to spot → Need more evidence

This is why balancing effect size and sample size is crucial for:
✓ Efficient resource allocation
✓ Timely decision-making
✓ Statistical confidence
✓ Avoiding false positives or false negatives
""")