import os, cv2

pathlabel = "C:\\Users\\HP G7\\Desktop\\IMPORTANT\\KuliahNew\\Side Quest\\Latihan Program\\Personal\\Personal Project\\DSProjects\\CV\\Object Detection\\dataset\\train\\labels"
pathimage = "C:\\Users\\HP G7\\Desktop\\IMPORTANT\\KuliahNew\\Side Quest\\Latihan Program\\Personal\\Personal Project\\DSProjects\\CV\\Object Detection\\dataset\\train\\images"

names = os.listdir(pathlabel)
for name in names:
    newstr = []
    f = open(os.path.join(pathlabel,name), 'r+')
    text = f.read().splitlines()
    imgname = str(name.split('.')[0] + '.jpg')

    img = cv2.imread(os.path.join(pathimage, imgname))
    H, W = img.shape[:2]
    
    for arg in text:
        c, x1, y1, x2, y2 = arg.split()
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        cx, cy  = (x1 + x2)/2, (y1 + y2)/2
        w, h = abs(x2 - x1), abs(y1 - y2)
        cx, w = cx/W, w/W
        cy, h = cy/H, h/H
        new = ' '.join([str(0), str(cx), str(cy), str(w), str(h)])   
        newstr.append(new)
    f.seek(0)
    f.write('\n'.join(newstr))
    f.close()
    