# parent image
FROM python:3 as py
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

#Run pip install for Hugging Face transformers
RUN pip3 install datasets  
RUN pip3 install pillow 
RUN pip3 install transformers[torch]
# Inference
FROM py as inference
ARG EXEC_DIR="/opt/executables"
RUN mkdir -p ${DATA_DIR}/inputs ${DATA_DIR}/outputs
COPY inference.py ${EXEC_DIR}
WORKDIR ${EXEC_DIR}

# Default command. Additional arguments are provided through the command line
ENTRYPOINT ["python3", "inference.py"]

