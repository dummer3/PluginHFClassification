## RUN DOCKER IMAGE :

```/bin/bash build.sh```

Example with a model taken from HugingFace Hub
```docker run -v /data:/data timm --model-path=hf-hub:nateraw/resnet50-oxford-iiit-pet --image-folder=/data/inputs  --output-filepath=/data/outputs/file.csv --image-format=jpg```

Timm is a supported library in HuggingFace so some models are stored in the HuggingFace Hub. These models all have the same way to store their metadatas, making it easier to retreive the labels when writing the results. This plugin uses those models.