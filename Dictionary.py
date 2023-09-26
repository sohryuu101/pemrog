import string

translation_dict_root = {
    'PILIH': 'SELECT',
    '*' : '*',
    'DARI': 'FROM',
    'PERBEDAAN': 'DISTINCT',
    'MASUKKAN': 'INSERT',
    'KEDALAM': 'INTO',
    'PERSEN': 'PERCENT',
    'SEBAGAI': 'AS',
    'DIMANA': 'WHERE',
    'BUAT': 'CREATE',
    'TABEL': 'TABLE',
    'DIATAS': 'ON',
    'INDEKS': 'INDEX',
    'LIHAT': 'VIEW',
    'TARUH': 'DROP',
    'PERBARUI': 'UPDATE',
    'HAPUS': 'DELETE',
    'UBAH': 'ALTER',
    'TAMBAH': 'ADD',
    'KOLOM': 'COLUMN',
    'HITUNG': 'COUNT',
    'JUMLAH': 'SUM',
    'RATA2': 'AVG',
    'MINIMAL': 'MIN',
    'MAKSIMAL': 'MAX',
    'GRUP': 'GROUP',
    'OLEH': 'BY',
    'MEMPUNYAI': 'HAVING',
    'MENURUN': 'DESC',
    'GRANT': 'GRANT',
    'OFFSET': 'OFFSET',
    'FETCH': 'FETCH',
    'GABUNG DALAM': 'INNER JOIN',
    'GABUNG KIRI': 'LEFT JOIN',
    'GABUNG KANAN': 'RIGHT JOIN',
    'GABUNG SEMUA': 'FULL JOIN',
    'ADA': 'EXISTS',
    'GRANT': 'GRANT',
    'HAPUS PERIZINAN': 'REVOKE',
    'POINAMAN': 'SAVEPOINT',
    'KOMIT': 'COMMIT',
    'PUTAR ULANG': 'ROLLBACK',
    'HAPUS SEMUA INPUTAN': 'TRUNCATE',
    'SATUKAN': 'UNION',
    'SATUKAN SEMUA': 'UNION ALL',
    'KELOMPOKKAN BERDASARKAN': 'GROUPBY'
}

translation_dict_user = {
    'PILIH': 'SELECT',
    '*' : '*',
    'HAPUS': 'DELETE',
    'MASUKKAN': 'INSERT'
}

def encrypt_decrypt(text, key, characters=string.ascii_lowercase, decrypt=False, shift_type="right"):
    if key < 0:
        print("K tidak valid (tidak boleh negatif)")
        return None
    n = len(characters)
    if decrypt == True:
        key = n - key
    if shift_type == "left":
        key = -key
    rumus_sulap = str.maketrans(characters, characters[key:] + characters[:key])
    tersulap = text.translate(rumus_sulap)
    return tersulap