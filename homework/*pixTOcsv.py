import cv2     # h, w, c
import numpy
import matplotlib.pyplot as plt


img = cv2.imread("/Users/lintzu-chi/Documents/python/VS/20180118-132700.jpg" ,0)
print("圖像的形状,返回一个圖像的(行數,列數,通道數):", img.shape)
print("圖像的像素數目:", img.size)
print("圖像的數據類型:", img.dtype)
#img = cv2.resize(img,(280,280))    可以改變圖片的大小

fname = open("/Users/lintzu-chi/Documents/python/VS/20180118-132700.csv",'w')
#fname.write("圖像的形状,返回一个圖像的(行數,列數,通道數):"+str(img.shape)+'\n')
#fname.write("圖像的像素數目:"+str(img.size)+'\n')
#fname.write("圖像的數據類型:"+str(img.dtype)+'\n')
Xlenth = img.shape[1]          # 圖片列數
Ylenth = img.shape[0]          # 圖片行數

a = 1
for i in range(Ylenth):
    #fname.write(str(a) + ':'+'\n')
    for j in range(Xlenth):
        fname.write(str(img[i][j])+',')
    a += 1
    fname.write('\n')
fname.close()

#v2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()