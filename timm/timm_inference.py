import os
import timm
import sys
import argparse
import torch
import urllib
from PIL import Image
import csv

if sys.version_info[0] < 3:
    raise RuntimeError('Python3 Required')

def get_prediction(model, transform, image_filepath):
    img = Image.open(image_filepath)
    img_tensor = transform(img).unsqueeze(0)
    outputs = model(img_tensor)
    _, preds = torch.max(outputs, 1)
    return preds.item()

def inference(modelPath, image_folder, output_filepath,image_format):
    model = timm.create_model(modelPath, pretrained=True)
    model.eval()
    labels = model.pretrained_cfg['labels']

    transform = timm.data.create_transform(**timm.data.resolve_data_config(model.pretrained_cfg))

    img_filepath_list = [os.path.join(image_folder, fn) for fn in os.listdir(image_folder) if
    fn.endswith('.{}'.format(image_format))]
    with open(output_filepath, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Image", "Prediction"])
        for filepath in img_filepath_list:
            prediction = get_prediction(model, transform, filepath)
            writer.writerow([filepath, labels[prediction]])

                
if __name__=="__main__":
    print("Start argument fetch")
    parser = argparse.ArgumentParser(prog='inference',
                                     description='Script to inference the selected module')

    parser.add_argument('--model-path', dest='model_path', type=str,
                        help='Model path to the model to use', required=True)
    parser.add_argument('--image-folder', dest='image_folder', type=str,
                        help='filepath to the folder containing tif images to inference (Required)', required=True)
    parser.add_argument('--output-filepath', dest='output_filepath', type=str, required=True)
    parser.add_argument('--image-format', dest='image_format', type=str, help='format (extension) of the input images. E.g {tif, jpg, png)', default='tif')

    args = parser.parse_args()

    model_path = args.model_path
    image_folder = args.image_folder
    output_filepath = os.path.join(args.output_filepath, "results.csv")
    image_format = args.image_format

    print('Arguments:')
    print('model-path = {}'.format(model_path))
    print('image-folder = {}'.format(image_folder))
    print('output-filepath = {}'.format(output_filepath))
    print('image-format = {}'.format(image_format))

    inference(model_path, image_folder, output_filepath, image_format)
