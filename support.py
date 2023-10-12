import os,shutil,json
from tkinter import filedialog

class Support:
    def __init__(self) -> None:
        self.path = None
        self.list_years = ["2014","2015","2016","2017","2018","2019","2020","2021","2022","2023"]
        
    def sortImages(self):
        try:
            source = self.path
            destination = self.path+"/"+"YourAlbum"
            
            if not os.path.exists(destination):
                os.mkdir(destination)
            
            for img_file in os.listdir(source):
                for year in self.list_years:
                    if str(year) in img_file:
                        if os.path.exists(destination+"/"+year):
                            if not os.path.exists(destination+"/"+img_file):
                                shutil.move(source+"/"+img_file,destination+"/"+year+"/"+img_file)
                        else:
                            os.mkdir(destination+"/"+str(year))
                            shutil.move(source+"/"+img_file,destination+"/"+year+"/"+img_file)
                    
            return True
        except Exception as e:
            print(str(e))
            return False
        
    def select_path(self):
        try:
            self.path= filedialog.askdirectory()
            return self.path
        except Exception as e:
            print(str(e))
            return False
                        
support = Support()