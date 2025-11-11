FROM node:18-alpine
WORKDIR /app
COPY ./contact_ui_ng_app_testing/. .
RUN npm install 
ENTRYPOINT ["npm","start"]
EXPOSE 4200


