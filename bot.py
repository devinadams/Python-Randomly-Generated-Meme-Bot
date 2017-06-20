# Randomly generated MemeBot
# By Devin A

from __future__ import print_function
from PIL import Image
import os
import random
import templates
import lolz


class MemeBot:

    def allfiles(self, directory):
            allFiles = []
            for root, subfiles, files in os.walk(os.getcwd() + directory):
                    for names in files:
                            allFiles.append(os.path.join(root, names))
            return allFiles

    def readImg(self, img):
        img = Image.open(img)
        return img

    def getImgSize(self, img):
        img_w, img_h = img.size
        return img_w, img_h

    def getName(self, fname_path):
        if not os.path.exists(fname_path):
            return fname_path
        filename, file_extension = os.path.splitext(fname_path)
        i = 1
        new_fname = "{}-{}{}".format(filename, i, file_extension)
        while os.path.exists(new_fname):
            i += 1
            new_fname = "{}-{}{}".format(filename, i, file_extension)
        return new_fname

    def paste(self, template, source, template_name, source_name):
        Templates = templates.Templates()
        template_w, template_h = self.getImgSize(template)
        source_w, source_h = self.getImgSize(source)
        offset = Templates.getOffset(template_name)
        template.paste(source, offset)
        name = self.getName(self.OUT_DIRECTORY)
        template.save(name)

    def getRandomSource(self):
        all_sources = self.allfiles("\\source\\")
        random_source = random.choice(all_sources)
        return random_source

    def getRandomTemplate(self):
        all_templates = self.allfiles("\\template\\")
        random_template = random.choice(all_templates)
        return random_template

    def make_meme(self):
        Templates = templates.Templates()
        template = self.getRandomTemplate()
        source = self.getRandomSource()
        template_name = template
        source_name = source
        template = self.readImg(template)
        source = self.readImg(source)
        source = Templates.getResizeShape(source, template, source_name, template_name)
        self.paste(template, source, template_name, source_name)

    def mainLoop(self):
        Lolz = lolz.Lolz() # create retarded banner class instance

        print(""" 
        
                Random Meme Generator

                    
                    """)
                    
        bullshit = Lolz.printBullshit() # print retarded ascii banners
        
        amt = int(input("How many memers do you want to make?: "))

        print("""
        
        Generating""", amt, """memes..""")

        amt = amt + 1
        while amt > 0:
            self.make_meme()
            amt = amt - 1
        if amt == 0:
            print("\nDone!")

    def __init__(self):
      self.OUT_DIRECTORY = "C:\Users\Devin\Desktop\memer\out\out.jpg" # CHANGE TO YOUR OUTPUT DIRECTORY! END IT WITH THE FILE NAME!'
      self.mainLoop()

MEMER = MemeBot()