FROM --platform=linux/amd64 ubuntu:latest

# Essential tools and xvfb
RUN apt-get update && apt-get install -y \
    software-properties-common \
    unzip \
    curl \
    xvfb

# Chrome Browser
RUN mkdir -p /opt/downloads \
    && curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /opt/downloads/google-chrome-stable_current_amd64.deb \
    && cd /opt/downloads; dpkg -i google-chrome-stable_current_amd64.deb; apt-get install -f -y


# Chrome Driver
RUN mkdir -p /opt/selenium \
    && curl http://chromedriver.storage.googleapis.com/112.0.5615.49/chromedriver_linux64.zip -o /opt/selenium/chromedriver_linux64.zip \
    && cd /opt/selenium; unzip /opt/selenium/chromedriver_linux64.zip; rm -rf chromedriver_linux64.zip; ln -fs /opt/selenium/chromedriver /usr/local/bin/chromedriver;


RUN apt update
RUN apt install python3 -y
RUN apt-get -y install python3-pip
RUN apt-get -y install vim
ENV DISPLAY=:99
WORKDIR /usr/app/src
COPY . .
RUN apt install -y  python3-venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install --upgrade pip
RUN pip3 install -r Requirements.txt
# RUN sed -i 's/"$@"/"$@" --no-sandbox/g' /usr/bin/google-chrome

CMD ["pytest"]

