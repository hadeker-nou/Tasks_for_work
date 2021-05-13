from xml.dom import minidom
import shutil
doc_xml= minidom.parse('config.xml')
#считаем что хмл файл валиден
errorout = ""
successout=""
List_of_files=doc_xml.getElementsByTagName('file')
for el in List_of_files:
    copy_file=el.attributes['source_path'].value + '/' + el.attributes['file_name'].value
    dest=el.attributes['destionation_path'].value
    try:
        shutil.copy(copy_file, dest)
    except:
        errorout+=f"File {el.attributes['file_name'].value} wasn't copied\n"
        print(errorout)
        continue
    successout+=f"File {el.attributes['file_name'].value} was copied\n"
with open('Errorlog.txt','w') as f:
    f.write(errorout)
with open('Successlog.txt','w') as f:
    f.write(successout)


