FROM node:20
WORKDIR /app
COPY ./src /app/src
COPY package*.json ./
RUN npm install
CMD ["npm", "run", "dev", "--host"]

