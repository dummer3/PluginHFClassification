import argparse
import os
import csv
import torch
import torchvision.transforms as T
import torchvision.models as models
from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
from PIL import Image




def get_prediction(model, transform, image_filepath):
    img = Image.open(image_filepath)
    img_tensor = transform(img).unsqueeze(0)
    outputs = model(img_tensor)
    _, preds = torch.max(outputs, 1)
    return preds.item()

def inference(model_path, model_name, image_folder, output_filepath, image_format):
    model = torch.hub.load(model_path, model_name, pretrained=True)
    model.eval()

    preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    img_filepath_list = [os.path.join(image_folder, fn) for fn in os.listdir(image_folder) if
    fn.endswith('.{}'.format(image_format))]
    with open(output_filepath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Image", "Prediction"])
        for filepath in img_filepath_list:
            prediction = get_prediction(model, preprocess, filepath)
            writer.writerow([filepath, prediction])




if __name__ == '__main__':
    # Parse the command-line arguments

    parser = argparse.ArgumentParser(prog='inference',
                                     description='Script to inference the selected module')

    parser.add_argument('--model-path', dest='model_path', type=str,
                        help='Model path to the model to use', required=True)
    parser.add_argument('--model-name', dest='model_name', type=str,
                        help='Model path to the model to use', required=True)
    parser.add_argument('--images-folder', dest='images_folder', type=str,
                        help='filepath to the folder containing tif images to inference (Required)', required=True)
    parser.add_argument('--csv-file', dest='csv_file', type=str, required=True)
    parser.add_argument('--image-format', dest='image_format', type=str, help='format (extension) of the input images. E.g {tif, jpg, png)', default='tif')


    args = parser.parse_args()

    model_path = args.model_path
    model_name = args.model_name
    images_folder = args.images_folder
    csv_file = args.csv_file
    image_format = args.image_format

    inference(model_path, model_name, images_folder, csv_file, image_format)
