## RUN DOCKER IMAGE :

```/bin/bash build.sh```

Example with a model taken from PytorchHub
```docker run -v /data:/data pytorchhub --model-path pytorch/vision:v0.10.0  --model-name alexnet --images-folder ./data/inputs --csv-file ./data/outputs/pytorch.csv --image-format jpg```