# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44
pages = 100
rows = 50
sumb = 25
butes = 4
books_in = butes*sumb*rows*pages
disk_in = disk*1024*1024
num_of_books = disk_in // books_in
num_of_books2 = int(num_of_books)

print("Количество книг, помещающихся на дискету:", num_of_books2)
