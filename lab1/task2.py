pages_per_book = 100
lines_per_page = 50
symbols_per_line = 25
bytes_per_symbol = 4

Kb = 1024
Mb = 1024 * Kb
disk = 1.44 * Mb

bytes_per_book = bytes_per_symbol * symbols_per_line * lines_per_page * pages_per_book
books_quantity = int(disk / bytes_per_book)

print("Количество книг, помещающихся на дискету:", books_quantity)
