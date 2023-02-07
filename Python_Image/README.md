# HOW TO USE THIS PLUGIN

Create an image "inference"

`/bin/bash build-docker.sh` 

Create the container "inference"

`docker run -v /data:/data --name inference inference --model-path nateraw/vit-base-beans --image-folder /data/inputs --output-filepath /data/outputs/result.csv`

where   model-path is the hugging face hub path of the model you want to use,
	image-folder the folder containing your inputs 
	output-filepath the csv file path which contains the result of the inference
	image-format is an optional parameter (jpg,png, ...), by default tif
   
Before create the container, don't forget to write in the project folder :
[mv/cp] -r ../data /data 
(we use a mounted folder data to communicate between the container and the local machine). 
