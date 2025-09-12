import csv
arquivo = open("dados.csv" , "a", newline="" )
arquivo_csv = csv.writer(arquivo)
arquivo_csv.writerow(["Kaua \t 33"])
arquivo_csv.writerow(['Kaua' , 33])