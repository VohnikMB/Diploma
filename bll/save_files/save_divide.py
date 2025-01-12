def save_file(index_range, decrypted_data, files_location):
    """Зберігає дані у файли."""
    try:
        for i in index_range:
            with open(files_location[i], 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data[i])
        return True
    except Exception as e:
        print(f"Помилка збереження файлу: {e}")
        return False