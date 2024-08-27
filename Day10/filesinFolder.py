import os 
folder_path = input("Enter list of folder separated by spaces : ").split()


for folder in folder_path:
      print("dir in folder : ",folder)
      for dir in os.listdir(folder):
          print(dir)