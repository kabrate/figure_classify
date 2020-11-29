import torch
import torch.nn as nn
import torch.utils.data as Data
import torchvision      # 数据库模块
import matplotlib.pyplot as plt
import numpy as np
import torchvision
import torch.optim as optim
from torchvision import datasets, transforms, models
import time
import os
import copy
import matplotlib.pyplot as plt


input_size = 500
batch_size = 64

# 数据的读取
data_dir = "./trainsleep"
train_imgs = datasets.ImageFolder(os.path.join(data_dir, "train"), transforms.Compose([
            transforms.Resize(input_size),
            transforms.RandomResizedCrop(input_size),
            #transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
            #Cutout(n_holes=1, length=32)
        ]))

print(train_imgs.classes)
train_data = torch.utils.data.DataLoader(train_imgs, batch_size=batch_size, shuffle=True)

test_imgs = datasets.ImageFolder(os.path.join(data_dir, "test"), transforms.Compose([
            transforms.Resize(input_size),
            transforms.RandomResizedCrop(input_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]))
test_data = torch.utils.data.DataLoader(test_imgs, batch_size=batch_size, shuffle=False)
#print(train_data)


# 模型的建立

model = models.resnet18(pretrained=False,num_classes=2)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
criterion = nn.CrossEntropyLoss()
#optimizer = optim.Adam(model.parameters(),lr=0.001,weight_decay=5e-4)
optimizer = optim.Adam(model.parameters(),lr=0.0001)
print('device:',device)
print(model)

epoch = 150

# for _,[img,label] in enumerate(train_data):
#     print(img)
#     print(label)
#acc_train = np.zeros(401)
#acc_test = np.zeros(20)
k = 0
acc_best = 0
q = 5
for epo in range(1,epoch+1):
    logger = 'epoch:{}'.format(epo)
    start_time = time.time()
    train_loss = 0
    num_correct=0.0
    model.train()
    for _,[img,labels] in enumerate(train_data):
        inputs, labels = img.to(device).float(), labels.to(device)
        optimizer.zero_grad()
        #if hasattr(torch.cuda, 'empty_cache'):
            #torch.cuda.empty_cache()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        train_loss += float(loss.cpu().item())
        _, preds = outputs.max(1)
        num_correct += preds.eq(labels).sum().float().item()
    logger += ', train loss:{:.6f}'.format(train_loss)
    logger += ', train acc:{:.6f}'.format(num_correct/len(train_data.dataset))
    logger = 'Time:{}, '.format(int(time.time()-start_time)) + logger
    #acc_train[epo] = num_correct/len(train_data.dataset)
    print(logger)

    if epo % 5 == 0:
        with torch.no_grad():
            model.eval()
            test_loss = 0
            num_correct = 0.0
            for _, [img, labels] in enumerate(test_data):
                inputs, labels = img.to(device).float(), labels.to(device)
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                test_loss += float(loss.cpu().item())
                _, preds = outputs.max(1)
                num_correct += preds.eq(labels).sum().float().item()
            logger1 = 'test loss:{:.6f}'.format(test_loss)
            logger1 += ', test acc:{:.6f}'.format(num_correct / len(test_data.dataset))
            logger1 = 'Time:{}, '.format(int(time.time() - start_time)) + logger1
            print(logger1)
            #acc_test[k] = num_correct / len(test_data.dataset)
            #if(acc_test[k]>acc_best):
            torch.save(model.state_dict(), 'model'+str(q)+'.pth')

            k = k+1
            q = q+5


#plt.figure(1)
#plt.plot(acc_train)
#plt.show()

#plt.figure(2)
#plt.plot(acc_test)
#plt.show()