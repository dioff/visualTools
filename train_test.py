import glob, os

# 数据集的位置
imgs_dir = r'C:\Users\Lazzy\Desktop\liu'
print(imgs_dir)

#用作 test 的图片数据的比例
percentage_test = 10;

#创建训练数据集和测试数据集：train.txt 和 test.txt
file_train = open('C:\\Users\\Lazzy\\Desktop\\train.txt', 'w')
file_test = open('C:\\Users\\Lazzy\\Desktop\\test.txt', 'w')

counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(imgs_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(imgs_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(imgs_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1

