import cv2
import numpy
import random



def imtoArrGrayScaleConverter(image):
    ArrayG=cv2.imread(image,0)
    return ArrayG


def imtoArrColorConverter(image):
    ArrayC=cv2.imread(image,1)
    return ArrayC

def ArrtoImConverter(Array):
    newImageName=input("Enter new image name with extension: ")
    Image=cv2.imwrite(newImageName,Array)
    MyImage=imtoArrColorConverter(newImageName)
    resized_image=cv2.resize(MyImage,(1000,500))
    cv2.imshow(newImageName,resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    return Image


def ArrayGenerator():
    List1=[]
    
    for i in range(0,64):
        List1.append(random.randint(0,255))
        
        
    Array=numpy.asarray(List1)
    FinalArray=Array.reshape(4,4,4)
        
    return FinalArray
    

def menu():
    
    print("MAIN MENU")
    print("==========")
    
    print("1. Convert Image to array (Grayscale) ")
    print("2. Convert Image to array (RGB)")
    print("3. Computer Generated Image (Small Dimensions in V.01 of this program)")
    
        
    
    
def main():
    
    menu()
    
    userInput=int(input("Enter One of the Above (1-3): "))
    
    if userInput==1:
        ImageName=input("Enter Image File Title With Extension: ")
        GrayImage=imtoArrGrayScaleConverter(ImageName)
        print(GrayImage)
    
        
    elif userInput==2:
        ImageName=input("Enter Image File Title With Extension: ")
        ColorImage=imtoArrColorConverter(ImageName)
        print(ColorImage.ndim)
        print(ColorImage.shape)
        print(ColorImage)
        
    elif userInput==3:
        Array=ArrayGenerator()
        Image=ArrtoImConverter(Array)
        print(Image)
    


main()




















