# Template offsets and source img sizes are defined here
# Written by Devin A


from PIL import Image

# where the image is placed on the template
class Templates:

    def reSizeImg(self, img, w, h):
            img = img.resize((w, h), Image.ANTIALIAS)
            return img

    # Define template offsets
    # This is shit code and should be done with a dict or something else        
    def getOffset(self, template):
            if 'template1' in template:
                w, h = 40, 80
            elif 'template2' in template:
                w, h = 90, 550
            elif 'template3' in template:
                w, h = 580, 50
            elif 'template4' in template:
                w, h = 430, 290
            elif 'template5' in template:
                w, h = 420, 80
            elif 'template6' in template:
                w, h = 440, 220
            elif 'template7' in template:
                w, h = 380, 90
            elif 'template8' in template:
                w, h = 360, 90
            elif 'template9' in template:
                w, h = 305, 50
            elif 't_10' in template:
                w, h = 460, 250
            elif 't_11' in template:
                w, h = 555, 235
            elif 't_12' in template:
                w, h = 350, 200
            elif 't_13' in template:
                w, h = 332, 20
            elif 't_14' in template:
                w, h = 610, 125
            elif 't_15' in template:
                w, h = 350, 100
            elif 't_16' in template:
                w, h = 373, 205
            elif 't_17' in template:
                w, h = 350, 100
            elif 't_18' in template:
                w, h = 370, 40
            elif 't_19' in template:
                w, h = 200, 0
            else:
                w, h = 40, 80
            return w, h

    # Define the shape of the source needed to fit the template
    # also shit code
    def getResizeShape(self, source, template, source_name, template_name):
        if 'template1' in template_name:
            source = self.reSizeImg(source, 400, 300)
        elif 'template2' in template_name:
            source = self.reSizeImg(source, 400, 420)
        elif 'template3' in template_name:
            source = self.reSizeImg(source, 325, 325)
        elif 'template4' in template_name:
            source = self.reSizeImg(source, 120, 120)
        elif 'template5' in template_name:
            source = self.reSizeImg(source, 300, 250)
        elif 'template6' in template_name:
            source = self.reSizeImg(source, 230, 190)
        elif 'template7' in template_name:
            source = self.reSizeImg(source, 350, 300)
        elif 'template8' in template_name:
            source = self.reSizeImg(source, 400, 200)
        elif 'template9' in template_name:
            source = self.reSizeImg(source, 500, 270)
        elif 't_10' in template_name: # Template name must be changed due to first if statement
            source = self.reSizeImg(source, 170, 160)
        elif 't_11' in template_name:
            source = self.reSizeImg(source, 135, 125)
        elif 't_12' in template_name:
            source = self.reSizeImg(source, 205, 235)
        elif 't_13' in template_name:
            source = self.reSizeImg(source, 170, 200)
        elif 't_14' in template_name:
            source = self.reSizeImg(source, 135, 150)
        elif 't_15' in template_name:
            source = self.reSizeImg(source, 450, 350)
        elif 't_16' in template_name:
            source = self.reSizeImg(source, 210, 120)
        elif 't_17' in template_name:
            source = self.reSizeImg(source, 420, 350)
        elif 't_18' in template_name:
            source = self.reSizeImg(source, 370, 355)
        elif 't_19' in template_name:
            source = self.reSizeImg(source, 360, 400)
        else:
            source = self.reSizeImg(source, 100, 100)
        return source