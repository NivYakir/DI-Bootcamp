import math
# Pagination

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []

        self.items = list(items)
        self.page_size = page_size
        self.current_idx = 0

    @property
    def total_pages(self):
        return math.ceil(len(self.items) / self.page_size)
    
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = (self.current_idx * self.page_size) + self.page_size
        return self.items[start: end]
    
    def go_to_page(self, page_num):
        if isinstance(page_num, int) and (page_num in range(1, self.total_pages + 1)):
            self.current_idx = page_num - 1
        else:
            raise IndexError("Page number is outside the valid range.")
        return self
    
    def first_page(self):
        self.current_idx = 0
        return self
    
    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self
    
    def next_page(self):
        if self.current_idx == self.total_pages - 1:
            raise IndexError("You are on the last page.")
        self.current_idx += 1
        return self
    
    def prev_page(self):
        if self.current_idx == 0:
            raise IndexError("You are on the first page.")
        self.current_idx -= 1
        return self
    
    def __str__(self):
        result = '\n'.join(str(item) for item in self.get_visible_items())
        return result




alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

# print(p.get_visible_items())
print(p.go_to_page(8).get_visible_items())