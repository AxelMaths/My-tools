import os


specials_keys = ["@exit","@help","@cats","@cat","@new","@ls","@input"]

dicoHelp = {"@exit":"To stop the program","@help":"To print help","@cats":"To load data from all files","@cat":" To load data from main file","@new":"To create or open a dictionnary file to input data","@ls":"To print all files availables to avoid an error of name for a field","@input":"To input data in the main file"} 

def key_value(fichier,sep_k_v,sep_bloc_current_following):
    global dico
    with open(fichier,"r") as f:
         for ligne in f :
             key,value = ligne.split(sep_k_v)
             dico[key]=value

def inputDict(fichier,sep_k_v,sep_bloc_current_following):
    with open(fichier,"a") as f:
        key = ""
        while key!="exit":
            key = input("<<(key) ")
            if key!="exit":
                value = input(" <<(value) ")
                f.write(key+sep_k_v+value+sep_bloc_current_following)
            

fichiers = [file for file in os.listdir('.') if ("vocabulaire" in file and "csv" in file)]
fichier = "vocabulaire.csv"

key = ""
dico = dict()
while key != "@exit":
    
    key = input(">> ")
    
    if key == "help" or key == "exit" or key=="@help":
        print("Maybe you mistook")
        print("If you want to find details, you can use these commands :")
        for specKey in specials_keys:
            print(f"Input {specKey} :")
            print(dicoHelp[specKey])
            print("")
        print(":::::\n")
        
    if key == "@ls":
        print(fichiers)
    
    if key == "@cat":
        key_value(fichier,";","\n")
        
    if key == "@cats":
        for f in fichiers:
            key_value(f,";","\n")
            
    if key == "@new":
        field=input("@ which (new) field ?")
        f = "vocabulaire"+"_"+field+".csv"
        if f not in fichiers:
            fichiers.append(f)
        inputDict(f,";","\n")
        
    if key == "@input":
        inputDict(fichier,";","\n")
        
    
    for k in dico.keys():
        if key in k:
            print(k+" --> " + dico[k])
        

