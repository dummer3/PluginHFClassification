# parent image
FROM python:3
LABEL maintainer="National Institute of Standards and Technology"

#copy file from host to current working directory
COPY VERSION /

# Our environment, do not modified
ENV DEBIAN_FRONTEND noninteractive
ARG EXEC_DIR="/opt/executables"
ARG DATA_DIR="/data"

#Create folders (like every other plugin), do not modified
RUN mkdir -p ${EXEC_DIR} \
    && mkdir -p ${DATA_DIR}/inputs \
    && mkdir ${DATA_DIR}/outputs

#Run pip install for Hugging Face transformers
RUN pip3 install transformers[torch] \
    && pip3 install datasets \ 
    && pip3 install pillow 

COPY ResNet50 ${EXEC_DIR}


# To put it simply, we call a bash file which call a python3 file with path to our different folder
# Training 
FROM resnet50base as train
ARG LMDB_DIR="/lmdb"
ARG EXEC_DIR="/opt/executables"
RUN mkdir -p ${LMDB_DIR}
COPY create_lmdb_and_train.sh ${EXEC_DIR} 
WORKDIR ${EXEC_DIR}
# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["/bin/bash", "create_lmdb_and_train.sh"]

# Inference
FROM resnet50base as inference
ARG EXEC_DIR="/opt/executables"
RUN mkdir -p ${DATA_DIR}/model
COPY inference.sh ${EXEC_DIR} 
WORKDIR ${EXEC_DIR}
# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["/bin/bash", "inference.sh"]

