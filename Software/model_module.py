import torch
from torchvision.models import resnet18, ResNet18_Weights
from torchvision import transforms
from PIL import Image

class BananaClassifier:
    def __init__(self, model_path):
        self.weights = ResNet18_Weights.IMAGENET1K_V1
        self.model = resnet18(weights=self.weights)
        
        # Replace the final layer with two classes
        num_classes = 2
        self.model.fc = torch.nn.Linear(self.model.fc.in_features, num_classes)
        
        # Load model parameters
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        self.model.eval()  # Set the model to evaluation mode

        # Define image transformations
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])

    def preprocess_frame(self, frame):
        """Preprocess the frame for model input."""
        image = Image.fromarray(frame)  # Convert NumPy array to PIL Image
        return self.transform(image).unsqueeze(0)  # Add batch dimension

    def classify(self, frame):
        """Classify the given frame."""
        input_tensor = self.preprocess_frame(frame)
        output = self.model(input_tensor)
        prediction = torch.argmax(output, dim=1).item()
        return prediction
