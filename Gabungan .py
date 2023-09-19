import mysql.connector
from mysql.connector import Error

# ... Translation dictionary and translate function ...
translation_dict = {
    'PILIH': 'SELECT',
    '*' : '*',
    'DARI': 'FROM',
    "PERBEDAAN": "DISTINCT",
    "KEDALAM": "INTO",
    "PERSEN": "PERCENT",
    "SEBAGAI": "AS",
    "DIMANA": "WHERE",
    "BUAT": "CREATE",
    "TABEL": "TABLE",
    "DIATAS": "ON",
    "INDEKS": 'INDEX',
    'LIHAT': "VIEW",
    'TARUH': "DROP",
    'PERBARUI': "UPDATE",
    'HAPUS': "DELETE",
    'UBAH': 'ALTER',
    'TAMBAH': "ADD",
    'KOLOM': 'COLUMN',
    'HITUNG': "COUNT",
    "JUMLAH": "SUM",
    "RATA2": "AVG",
    'MINIMAL': 'MIN',
    'MAKSIMAL': "MAKS",
    'GRUP': "GROUP",
    "OLEH": 'BY',
    'HITUNG': "COUNT",
    "MEMPUNYAI": 'HAVING',
    "MENURUN": "DESC",
    "GRANT": "GRANT",
    "OFFSET": "OFFSET",
    "FETCH": "FETCH",
    "GABUNG DALAM": "INNER JOIN",
    "GABUNG KIRI": "LEFT JOIN",
    "GABUNGKANAN": "RIGHT JOIN",
    "GABUNGSEMUA": "FULL JOIN",
    "EKSIS": "EXISTS",
    "GRANT": "GRANT",
    "HAPUSPERIZINAN": "REVOKE",
    "POINAMAN": "SAVEPOINT",
    "KOMIT": "COMMIT",
    "PUTARULANG": "ROLLBACK",
    "HAPUSSEMUAINPUTAN": "TRUNCATE",
    "SATUKAN": "UNION",
    "SATUKANSEMUA": "UNION ALL",
    "KELOMPOKKANBERDASARKAN": "GROUPBY"
}

def translate(text):
    for key, value in translation_dict.items():
        text = text.replace(key, value)
    return text

perintah = input("Masukkan kode : ")
translated_sql = translate(perintah)







conn = mysql.connector.connect(host='127.0.0.1', password='akuanakhebat', user='root',database='world')

if conn.is_connected():
    print("Connection established.....")
    cursor = conn.cursor()
    cursor.execute(translated_sql)
    results = cursor.fetchall()
    for row in results:
        print(row)

print("Connection established...")




