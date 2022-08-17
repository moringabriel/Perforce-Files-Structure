import os
import os.path
import datetime
import string
import time
import webbrowser
from collections import defaultdict
import csv


# Create directory
class PropagatePeforceProjectFilesStructure():
    """notes"""

    def __init__(self):
        """Constructeur de la class PropagatePeforceProjectFilesStructure"""

        self.directory = {'AssetsPublish': {'HDRI': None, 'Meshes': {'EnvCuisine': None, 'EnvWar': None}},
                          'MayaProject': {'assets': None, 'autosave': None, 'cache': None, 'clips': None, 'data': None,
                                          'FBX_UnrealExport': None, 'images': None, 'movies': None, 'renderData': None,
                                          'sceneAssembly': None, 'scenes': None, 'scripts': None, 'sound': None,
                                          'sourceimages': None, 'Time Edtitor': None},
                          'UnrealBuild': {'Config': None,
                                          'Content': {'Blueprints': None, 'Levels': None, 'Materials': None,
                                                      'Meshes': None,
                                                      'Particles': None, 'Sequencer': None, 'Textures': None}}
                          }

        self.availabledrives = self.listAvailableDrives()
        self.version = '1.04'

    def create_project_directory(self):
        """Create directory and notify if directory already exists"""

        #
        self.driveLetter = ""
        self.projectName = ""
        # logo
        self.p3pfs()
        # author credits
        self.gm()

        # Ask user to propagate an other project

        propagate = input("Press 1 to create a new project, 0 to exit.")

        while True:
            #
            if propagate == "1":

                # printpoints1
                self.printPoints()

                print("")

                # List available drives
                print('Available drives:', end=" ")
                ndl = []
                for i in range(len(self.drives)):
                    print(self.drives[i][0], end=" ")
                    ndl.append(self.drives[i][0])

                print("")

                # self.ask_user()
                # self.driveLetter = (input("Input drive letter or enter to use default. (If no user input, default drive will be M):") or "M")

                response = ""
                while response.upper() not in ndl:
                    response = input(
                        F'Input drive letter or enter to use default. (If no user input,'
                        F' default drive will be {self.drives[-1]})')
                    print(response, 'allo')
                    response = response.capitalize()
                    print(response, 'allo')
                    if response == "":
                        response = self.drives[-1]

                        break

                    else:
                        print("Choose an available drive.")

                self.driveLetter = response
                self.driveLetter = self.driveLetter.capitalize()



                print(F'\n{self.driveLetter}:')
                print("")

                self.projectName = (input("Input project name or enter to use default. (If no user input,"
                                          " default project name will be: Project):") or "Project")

                print(F'\nPropagating:\n\n{self.driveLetter[0]}:\{self.projectName}')
                print("")
                time.sleep(.5)

                conventionUrl = (
                    "URL=https://docs.google.com/document/d/1jY9_PTYNg8OV80ZgoPAtB65Gf8KJH6YQ0LIObX1fotw/edit")

                self.save_path = (F'{self.driveLetter[0]}:/{self.projectName}')

                d = datetime.datetime.now()

                # Project
                try:
                    # Create target directory Project
                    os.mkdir(F'{self.driveLetter[0]}:/{self.projectName}')
                    print("Directory ", self.projectName, " Created ")

                except FileExistsError:
                    print("Directory", self.projectName, "already exists")

                # link to Perforce Stucture Convention
                try:
                    file1 = open(F'{self.save_path}/PleaseRead_{self.projectName}_StructureConvention.url', 'w+')
                    file1.writelines(F'[InternetShortcut]\n{conventionUrl}')
                    file1.close()
                    print("PlEASE_READ_AND_USE_StructureConvention.url ", " Created ")

                except FileExistsError:
                    print("URL", "already exists")

                # Create folders
                self.make_dirs_from_dict(self.directory)

                # Create .uproject
                try:
                    file1 = open(F'{self.driveLetter[0]}:/{self.projectName}/UnrealBuild/{self.projectName}.uproject', 'w+')
                    file1.writelines('{ \n'
                                     '  "FileVersion": 3,\n'
                                     '  "EngineAssociation": "4.26",\n'
                                     '  "Category": "",\n'
                                     '  "Description": "",\n'
                                     '  "TargetPlatforms": [\n'
                                     '    "PS4",\n'
                                     '    "WindowsNoEditor"\n'
                                     '  ]'
                                     '\n}')
                    file1.close()

                except FileExistsError:
                    print("URL", "already exists")

                print('\n', 'Project directory created ', d.date(), '\n')

                print(F'Make sure to read and use the {self.projectName} structure convention.'
                      "\nhttps://docs.google.com/document/d/1jY9_PTYNg8OV80ZgoPAtB65Gf8KJH6YQ0LIObX1fotw/edit")

                # webbrowser.open("https://docs.google.com/document/d/1jY9_PTYNg8OV80ZgoPAtB65Gf8KJH6YQ0LIObX1fotw/edit")

                print("")

                propagate = input("Press 1 to create an other project, 0 to exit.")

                continue
            elif propagate == "0":
                print('Done')
                break
            else:
                print("\nInvalid input - Press 1 to create an other project, 0 to exit.")
                propagate = input("Press 1 to create an other project, 0 to exit.")

    def listAvailableDrives(self):
        """List all available drives connected to computer"""

        dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

    def p3pfs(self):
        """"""
        l = """
        ---------------------------------------------

            ========  =======  =======  =======
                   =  =     =  =        =
                   =  =     =  =        =
               =====  =======  =====    =======
                   =  =        =              =
                   =  =        =              =
            ========  =        =        ======= 

        -------------------------------------------- 
        PROPAGATE PERFORCE PROJECT FILLING STRUCTURE
        """
        print(l)
        print(self.version)

    def gm(self):
        """my credits"""
        print("")
        print('written by: Gabriel Morin\nhttps://www.linkedin.com/in/gabriel-morin-vfx-46a1bb168\n')

    def printPoints(self):
        """print points"""

        for i in range(3):
            print(".", end="")
            time.sleep(.5)
        print("")

    def createTexteFile(self, path):
        """Create .txt file"""
        file1 = open(F'{path}/{self.projectName}.txt', 'w+')
        file1.close()

    def make_dirs_from_dict(self, d, current_dir='./'):
        """"""

        for key, val in d.items():

            try:
                # Create target directory
                os.mkdir(F'{self.driveLetter[0]}:/{self.projectName}/{current_dir}/{key}')

                file1 = open(F'{self.driveLetter[0]}:/{self.projectName}/{current_dir}/{key}/{key}.txt', 'w+')
                file1.close()

                if type(val) == dict:
                    self.make_dirs_from_dict(val, os.path.join(current_dir, key))

            except FileExistsError:
                print("Directory", key, "already exists")

    def dictionary_from_csv(self):
        """"""
        #input_file = csv.DictReader(open("projectdirectory.csv"))
        #for row in input_file:
         #   print(row)

        reader = csv.DictReader(open('projectdirectory.csv'))
        dictobj = next(reader)

        print(dictobj)






if __name__ == '__main__':
    p = PropagatePeforceProjectFilesStructure()
    p.dictionary_from_csv()
    #p.create_project_directory()
    # listAvailableDrives()
    # p.td()

# to compile script: pyinstaller --onefile --icon=app.ico propagatePerforceProjectFillingStructure.py