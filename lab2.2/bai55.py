import zipfile
import os

def compress_file(file_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, os.path.basename(file_path))
    print(f"Đã nén {file_path} thành {zip_path}")

def decompress_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"Đã giải nén {zip_path} vào thư mục {extract_to}")

def main():
    print("1. Nén file")
    print("2. Giải nén file")
    choice = input("Chọn (1/2): ").strip()

    if choice == "1":
        file_path = input("Nhập đường dẫn file cần nén: ").strip()
        zip_path = input("Nhập tên file zip đầu ra (vd: file.zip): ").strip()
        compress_file(file_path, zip_path)
    elif choice == "2":
        zip_path = input("Nhập đường dẫn file zip: ").strip()
        extract_to = input("Nhập thư mục giải nén: ").strip()
        decompress_file(zip_path, extract_to)
    else:
        print("Lựa chọn không hợp lệ!")
if __name__ == "__main__":
    main()
