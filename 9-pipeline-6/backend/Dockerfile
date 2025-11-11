FROM maven:3.9.6-eclipse-temurin-17 AS build
WORKDIR /app
COPY ./contact_backend_app_testing/. .
RUN mvn clean package -DskipTests

FROM eclipse-temurin:17-jre-alpine 
WORKDIR /app
COPY --from=build /app/target/*.jar /app/backend.jar
ENTRYPOINT ["java","-jar","/app/backend.jar"]

