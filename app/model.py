import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import io

model = models.resnet18(weights = models.ResNet18_Weights.DEFAULT)
model.eval()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean = [0.485,0.456,0.406],
        std = [0.229,0.224,0.225]
    )
])

def preprocess(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    return transform(image).unsqueeze(0)

def predict(image_bytes):
    tensor = preprocess(image_bytes)
    outputs = model(tensor)
    probs = torch.nn.functional.softmax(outputs[0],dim = 0)
    top3_prob, top3_catid = torch.topk(probs,3)
    return [(int(catid),float(prob)) for prob, catid in zip(top3_prob,top3_catid)]
