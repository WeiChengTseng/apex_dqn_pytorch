import cv2 as cv
import pickle
import torch

x = pickle.load(open('memory0.pt', 'rb'))
model = torch.load('memory0.pt')
print(type(x))
print(x)
print(model)