## RUN DOCKER IMAGE :

```/bin/bash build.sh```

Example with a model taken from HugingFace Hub
```docker run -v /data:/data timm --model_path=hf-hub:nateraw/resnet50-oxford-iiit-pet --image_folder=/data/inputs  --output_filepath=/data/outputs/file.csv --image_format=jpg```