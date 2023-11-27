FROM node:21-alpine

# Set work dir for relative paths
WORKDIR /app

# Install dependencies
COPY ./package*.json .
COPY ./pnpm-lock.yaml .
RUN npm install -g pnpm
RUN pnpm install

# Copy code from context to image
COPY . .

CMD ["pnpm", "run", "dev", "--host", "0.0.0.0"]
