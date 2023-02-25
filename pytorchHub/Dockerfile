# parent image
FROM python:3.8 as pyt
LABEL maintainer="National Institute of Standards and Technology"

#copy file from host to current working directory
#COPY VERSION /

# Our environment, do not modified
ENV DEBIAN_FRONTEND noninteractive
ARG EXEC_DIR="/opt/executables"
ARG DATA_DIR="/data"
 
#Create folders (like every other plugin), do not modified
RUN mkdir -p ${EXEC_DIR}
RUN mkdir -p ${DATA_DIR}/inputs \
    && mkdir ${DATA_DIR}/outputs

#Run pip install for Hugging Face transformers docker
RUN pip install torch


# Inference
FROM pyt as inference
ARG EXEC_DIR="/opt/executables"
RUN mkdir -p ${DATA_DIR}/inputs ${DATA_DIR}/outputs
COPY pytorch_inference.py ${EXEC_DIR}
WORKDIR ${EXEC_DIR}

# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["python3", "pytorch_inference.py"]
