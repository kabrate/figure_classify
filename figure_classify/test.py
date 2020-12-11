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

input_size = 500
batch_size = 128
data_dir = "./trainsleep"
num=1
frs =np.zeros(250)
fas =np.zeros(250)
fr=0
fa=0
test_imgs = datasets.ImageFolder('E:/data/dev/test', transforms.Compose([
            transforms.Resize(input_size),
            transforms.RandomResizedCrop(input_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]))
test_data = torch.utils.data.DataLoader(test_imgs, batch_size=batch_size, shuffle=False)

model = models.resnet18(pretrained=False,num_classes=2)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
criterion = nn.CrossEntropyLoss()
#optimizer = optim.Adam(model.parameters(),lr=0.001,weight_decay=5e-4)
optimizer = optim.Adam(model.parameters(),lr=0.0001)
print('device:',device)
print(model)
model.load_state_dict(torch.load('model95.pth'))
#model = torch.load(path)
print(model)
start_time = time.time()
#test_loss = 0
#num_correct = 0.0

#model.eval()
zes=torch.zeros(128).type(torch.LongTensor).to(device)#全0变量
ons=torch.ones(128).type(torch.LongTensor).to(device)#全1变量
ons=ons.resize_(12)
#194
with torch.no_grad():
    model.eval()
    test_loss = 0
    num_correct = 0.0
    out=open('preds.txt','a')
    print( 'output1'+' ' +'output2'+' ' +'score' +' ' + 'labels' +' ' + 'preds' +' '+ 'probability0'+' ' +'probability1',file=out)
    out.close()
    for index, [img, labels] in enumerate(test_data):
        inputs, labels = img.to(device).float(), labels.to(device)      
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        test_loss += float(loss.cpu().item())
        scores, preds = outputs.max(1)
        probability = torch.nn.functional.softmax(outputs,dim=1)#计算softmax，即该图片属于各类的概率
        out=open('preds.txt','a')
        for i in range(0,len(labels)): 
            score=round(scores[i].cpu().item(),4)
            output0= round(outputs[i][0].cpu().item(),4)
            output1= round(outputs[i][1].cpu().item(),4)
            probability0=round(probability[i][0].cpu().item(),4)
            probability1=round(probability[i][1].cpu().item(),4)
            print( str(output0)+' ' +str(output1)+' ' +str(score) +' ' + str(labels[i].cpu().item()) +' ' + str(preds[i].cpu().item())+' '+ str(probability0)+' ' +str(probability1) ,file=out)
        out.close()
        #num_correct += preds.eq(labels).sum().float().item()
        num_correct += (preds == labels).sum()
        torch.cuda.empty_cache()
        #if (preds.size()!=ons.size() or preds.size()!=zes.size()):
        #    ons=ons.resize_(preds.size())
        #    zes=zes.resize_(preds.size())
        #frs[num] = ((preds==zes)&(labels==ons)).sum()+ frs[num-1] #原标签为1，预测为 0 的总数 false reject
        #fr+=((preds==zes)&(labels==ons)).sum().float() #原标签为1，预测为 0 的总数 false reject
        #fa+=((preds==ons)&(labels==zes)).sum().float() #原标签为0，预测为 1 的总数 false accept

        #fas[num] = ((preds==ons)&(labels==zes)).sum() + fas[num-1] #原标签为0，预测为1 的总数 false accept
        #num=num+1
        #tan = ((preds==ons)&(labels==ons)).sum() #原标签为1，预测为1 的总数 true accept
        #trn = ((preds==zes)&(labels==zes)).sum() #原标签为0，预测为1 的总数 true reject
    #np.savetxt(fr.txt,frs)
    #np.savetxt(fa.txt,fas)
    logger1 = 'test loss:{:.6f}'.format(test_loss)
    logger1 += ', test acc:{:.6f}'.format(num_correct / len(test_data.dataset))
    logger1 = 'Time:{}, '.format(int(time.time() - start_time)) + logger1
    print(logger1)
    #plt.plot(fas,frs)
    #y=range(0,1)
    #x=range(0,1)
    #plt.plot(x,y)
    #plt.show()
