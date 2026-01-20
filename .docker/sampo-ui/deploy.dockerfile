FROM node:22.21.1-alpine
ARG API_URL
ARG VERSION="3.0.0-1"

# Based on https://nodejs.org/en/docs/guides/nodejs-docker-webapp/

# Create app directory
WORKDIR /usr/src/app

# Download Sampo UI from GitHub and unzip
# mv commands: install app dependencies, Babel 7 presets and plugins, and bundle app source
# Remove redundant files
RUN <<EOF
wget https://github.com/UoMResearchIT/sampo-ui/archive/refs/tags/v$VERSION.zip
unzip v$VERSION.zip
mv ./sampo-ui-$VERSION/package*.json ./
mv ./sampo-ui-$VERSION/webpack*.js ./
mv ./sampo-ui-$VERSION/babel.config.js ./
mv ./sampo-ui-$VERSION/src ./src
rm -rf sampo-ui-$VERSION v$VERSION.zip
EOF

COPY ./src ./src

# Run the scripts defined in package.json using build arguments
RUN npm install && \ 
API_URL=$API_URL npm run build

EXPOSE 3001

# https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md#non-root-user
USER node

# Express server handles the backend functionality and also serves the React app
CMD ["node", "/usr/src/app/dist/server"]
