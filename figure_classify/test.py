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

input_size = 200
batch_size = 128
data_dir = "./trainsleep"

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
test_loss = 0
num_correct = 0.0

model.eval()

with torch.no_grad():
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
