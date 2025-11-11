FROM maven:3.9.11-eclipse-temurin-17 AS build
WORKDIR /app
COPY ./maven-web-app-testing/. .
RUN mvn clean package -DskipTests

FROM tomcat:latest
COPY --from=build /app/target/*.war  /usr/local/tomcat/webapps/tomcat.war
EXPOSE 8080

