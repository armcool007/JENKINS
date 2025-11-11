FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app
COPY ./maven-web-app-testing/. .
RUN mvn clean package -DskipTests
#use DskipTests otherwise the war file will not be present in the docker images


FROM tomcat:latest
COPY --from=build /app/target/*.war /usr/local/tomcat/webapps/maven-web-app.war
EXPOSE 8080
