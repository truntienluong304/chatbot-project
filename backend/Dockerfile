# Backend Dockerfile
FROM node:14

WORKDIR /app

COPY package*.json ./
RUN npm install

# Cài đặt Python và pip3
RUN apt-get update && apt-get install -y python3 python3-pip curl

# Cài đặt Rust compiler
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Cài đặt các thư viện cần thiết cho Hugging Face
RUN pip3 install transformers torch

COPY . .

EXPOSE 3000
CMD ["node", "index.js"]
