FROM node:16.13.0-alpine

# Specify the Sampo UI version
ARG VERSION="3.0.0"

RUN apk update && apk add bash

# Create app directory
WORKDIR /usr/src/app

# Download Sampo UI from GitHub and unzip
# mv commands: install app dependencies, Babel 7 presets and plugins, and bundle app source
# Remove redundant files
RUN <<EOF
wget https://github.com/SemanticComputing/sampo-ui/archive/refs/tags/v$VERSION.zip
unzip v$VERSION.zip
mv ./sampo-ui-$VERSION/package*.json ./
mv ./sampo-ui-$VERSION/webpack*.js ./
mv ./sampo-ui-$VERSION/babel.config.js ./
mv ./sampo-ui-$VERSION/src ./src
rm -rf sampo-ui-$VERSION v$VERSION.zip
EOF

# Run the scripts defined in package.json using build arguments
RUN npm install

# Install nodemon
RUN npm install -g nodemon 

EXPOSE 8080 3001

# https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md#non-root-user
USER node

# Run dev server
CMD ["npm", "run", "dev"]
