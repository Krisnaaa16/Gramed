library = []

def add_book():
    # fungsi untuk menambahkan buku ke dalam perpustakaan
    title = input('masukkan judul buku: ')
    author = input('masukkan nama penulis: ')
    year = input('masukkan tahun terbit: ')
    
    book = {"title": title, "author": author, "year": year}
    library.append(book)
    print(f'buku "{title}" berhasil ditambahkan ke perpustakaan')

def search_books(keyword):
    results = []
    for book in library:
        if keyword.lower() in book['title'].lower():
            results.append(book)
    return results

def display_books(books):
    if not books:
        print('tidak ada buku yang ditemukan.')
    else:
        print('buku yang ditemukan :')
        for book in books:
            print(f"judul: {book['title']}, penulis: {book['author']}, tahun: {book['year']}")

def main():
    while True:
        print('\nmenu perpustakaan :')
        print('1. tambah buku')
        print('2. cari buku')
        print('3. keluar')
        choice = input('pilih menu 1/2/3 : ')
        
        if choice == '1':
            add_book()
        elif choice == '2':
            keyword = input('masukkan kata kunci yang ingin dicari: ')
            results = search_books(keyword)
            display_books(results)
        elif choice == '3':
            print('terimakasih telah mengunjungi perpustakaan kami')
            break
        else:
            print('input tidak valid')

if __name__ == "__main__":
    main()
