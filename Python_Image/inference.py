from datasets import load_dataset
from transformers import AutoImageProcessor
from transformers import pipeline
from transformers import AutoModelForImageClassification
import sys
import argparse
import os
import csv
from PIL import Image

if sys.version_info[0] < 3:
    raise RuntimeError('Python3 Required')


def inference(modelPath, image_folder, output_filepath,image_format):
    img_filepath_list = [os.path.join(image_folder, fn) for fn in os.listdir(image_folder) if
    fn.endswith('.{}'.format(image_format))]

    classifier = pipeline("image-classification", model=modelPath)
    image_processor = AutoImageProcessor.from_pretrained(modelPath)
    model = AutoModelForImageClassification.from_pretrained(modelPath)

    with open(output_filepath,'w',newline='') as f_out:
        print('starting inference')
        writer = csv.DictWriter(f_out,fieldnames=['image','score','label'])
        writer.writeheader()

        for i in range(len(img_filepath_list)):
            img_filepath = img_filepath_list[i]
            _, img_name = os.path.split(img_filepath)
            print('{}/{} : {}'.format(i, len(img_filepath_list), img_name))
            img = Image.open(img_filepath)

            result = classifier(img)
            result[0]['image'] = img_name
            writer.writerow(result[0])
                
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
    output_filepath = args.output_filepath
    image_format = args.image_format

    print('Arguments:')
    print('model-path = {}'.format(model_path))
    print('image-folder = {}'.format(image_folder))
    print('output-filepath = {}'.format(output_filepath))
    print('image-format = {}'.format(image_format))

    inference(model_path, image_folder, output_filepath, image_format)
