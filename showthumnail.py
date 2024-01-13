# Show pictures
import matplotlib.pyplot as plt
import glob

path='video/*.jpg'

list=glob.glob(path)
list.sort()


fig, ax=plt.subplots(25,12)



c=0
ax=ax.flatten()
for a in ax:
    f=list[c]
    print(f'Reading file:{f}')
    img=plt.imread(f)
    a.imshow(img,interpolation='none')
    a.set_title(f,loc='center')
    a.axis('off')
    c+=1

plt.show()

