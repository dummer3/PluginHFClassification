## RUN DOCKER IMAGE :

```/bin/bash build.sh```


To run the docker image, the parameters must be --model-path with the path of the model and name as 'path/name', --image-folder which is the path of the folder with the data, --output-filepath which is the csv file in which to write the results, and --image-format.

Example with a model taken from PytorchHub
```docker run -v /data:/data pytorchhub --model-path pytorch/vision:v0.10.0/alexnet --image-folder ./data/inputs --output-filepath ./data/outputs/pytorch.csv --image-format jpg```

Since the PytorchHub models all store their metadatas and labels in a different way, the results written are only indexes. The labels aren't used as each model stores them their own way.