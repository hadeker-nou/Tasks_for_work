import sys
import hashlib
if len (sys.argv) != 3:
            print ("Ошибка. Число параметров должно быть равно 3.")
            sys.exit (1)
input_file = sys.argv[1]
check_dir = sys.argv[2]
try:
    with open(input_file) as f:
        data = f.readlines()
except:
    print ("Ошибка. Нет input файла.")
    sys.exit (1)
for line in data:
    list_of_file = line.split()
    if len(list_of_file) != 3:
        print("Неправильная сторка")
        continue
    file_name, hash_alg, original_hash = list_of_file
    file_to_check = check_dir + '/' + file_name
    try:
        with open(file_to_check,'br') as check_file:
            bytes_from_file = check_file.read()
    except:
        print(f"{file_name} NOT FOUND")
        continue
    if hash_alg == 'md5':
            hash_returned=hashlib.md5(bytes_from_file).hexdigest()
    elif hash_alg == 'sha1':
        hash_returned=hashlib.sha1(bytes_from_file).hexdigest()
    elif hash_alg == 'sha256':
        hash_returned=hashlib.sha256(bytes_from_file).hexdigest()
    else:
        print(f"{file_name} UNKNOWN HASH ALGORITM")
        continue
    if original_hash == hash_returned:
        print(f"{file_name} OK")
    else:
        print(f"{file_name} FAIL")

            
            


        