## RUN DOCKER IMAGE :

```/bin/bash build.sh```

Example with a model taken from HugingFace Hub
```docker run -v /data:/data timm --model-path=hf-hub:nateraw/resnet50-oxford-iiit-pet --image-folder=/data/inputs  --output-filepath=/data/outputs/file.csv --image-format=jpg```