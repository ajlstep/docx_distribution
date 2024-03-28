# from docx import Document
import docx2txt
import re
import os
import shutil

director = "map"
output = "out"
log_read = "read.log"
log_write = "write.log"

def extrage_tot_textul(cale_fisier):
  text = docx2txt.process(cale_fisier)
  text = text.replace("\n", "")
  text = text.replace("\t", "")
  text = text.replace(" ", "")
  return text

# def extrage_tot_textul_docx(cale_fisier):
#   document = Document(cale_fisier)
  
#   text = ""
#   # Parcurgeți paragrafele din document
#   for paragraph in document.paragraphs:
#     text += paragraph.text

#   # Parcurgeți tabelele din document
#   for table in document.tables:
#     for row in table.rows:
#       for cell in row.cells:
#         text += cell.text

#   text = text.replace("\n", "")

#   # Inlocuieste toate caracterele Tab cu un sir gol
#   text = text.replace("\t", "")

#     # Inlocuieste toate spatiile cu un sir gol
#   text = text.replace(" ", "")
#   return text

def get_ds(text):
  constructii = re.findall(r"PS(\d{2})(?:DM)?:?\d{4}", text)
  if len(constructii) > 0:
    return constructii[0]
  else:
    return ""

def create_path(name):
    if os.path.isdir(output + "/" + name):
      return
    else:
        os.makedirs(output + "/" + name)

def print_log(filename, text):
  with open(filename, "a") as f:
      f.write(text+"\n")
  f.close()

with open(log_read, "w") as f:
  f.write("\n")
f.close()

with open(log_write, "w") as f:
  f.write("\n")
f.close()

# Obțineți o listă cu toate fișierele din director
fisiere = os.listdir(director)

# Afișați fișierele
for fisier in fisiere:
  path = director + "/" + fisier
  fis_text = extrage_tot_textul(path)
#   print(fis_text)
  ds = get_ds(fis_text)
  if ds != "":
    create_path(ds)
    shutil.copy(path, output + "/" + ds + "/" + fisier)
    if not os.path.isfile(output + "/" + ds + "/" + fisier):
        print_log(log_write, "error on copy <" + fisier + ">")
   
  else:
    print_log(log_read, fisier)
    # fis_text = extrage_tot_textul_docx(path)
    # ds = get_ds(fis_text)
    # if ds != "":
    #   create_path(ds)
    #   shutil.copy(path, output + "/" + ds + "/" + fisier)
    #   if not os.path.isfile(output + "/" + ds + "/" + fisier):
    #       print_log(log_write, "error on copy <" + fisier + ">")
    # else:
    #   print_log(log_read, "does not find ps in <" + fisier + ">")



