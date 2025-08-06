# Pagination
import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            self.items = []
        else:
            self.items = list(items)

        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        '''Returns the list of items visible on the current page'''
        start = self.current_idx * self.page_size
        end = start + self.page_size

        return self.items[start : end]

    def go_to_page(self, page_num):
        '''Goes to specified page number (1-based indexing)'''
        try:
            if not isinstance(page_num, int):
                raise TypeError("Input must be an integer")
            if page_num not in range(1, self.total_pages + 1):
                raise ValueError("Page Number Out of Range")
            self.current_idx = page_num - 1
            return self
        except Exception as e:
            print(f"Invalid Entry: {e}")
    
    def first_page(self):
        '''Navigate to the first page'''
        self.current_idx = 0
        return self
    
    def last_page(self):
        '''Navigate to the last page'''
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        '''Navigate forward one page'''
        if self.current_idx == self.total_pages - 1:
            raise IndexError("You are on the last page")
        else:
            self.current_idx += 1
            return self
    
    def previous_page(self):
        '''Navigate back one page'''
        if self.current_idx == 0:
            raise IndexError("You are on the first page")
        else:
            self.current_idx -= 1
            return self
        
    def __str__(self):
        visible_items = self.get_visible_items()
        return '\n'.join(str(item) for item in visible_items)


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(10)
print(p.current_idx + 1)
# Output: 7

p.go_to_page(0)
# Raises ValueError

print(str(p))