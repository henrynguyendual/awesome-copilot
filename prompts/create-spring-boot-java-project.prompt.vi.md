# Tạo Skeleton Dự Án Spring Boot Java

## Yêu Cầu Phần Mềm

Đảm bảo bạn đã cài đặt sẵn:

- Java 21
- Docker
- Docker Compose

Nếu muốn tùy chỉnh tên dự án, hãy thay đổi `artifactId` và `packageName` trong phần [Tải template dự án Spring Boot](#tải-template-dự-án-spring-boot).

Nếu muốn cập nhật phiên bản Spring Boot, hãy thay đổi `bootVersion` trong phần [Tải template dự án Spring Boot](#tải-template-dự-án-spring-boot).

## 1. Kiểm Tra Phiên Bản Java

Chạy lệnh sau để kiểm tra:

```shell
java -version
```

## 2. Tải Template Dự Án Spring Boot

Chạy lệnh:

```shell
curl https://start.spring.io/starter.zip   -d artifactId=demo   -d bootVersion=3.4.5   -d dependencies=lombok,configuration-processor,web,data-jpa,postgresql,data-redis,data-mongodb,validation,cache,testcontainers   -d javaVersion=21   -d packageName=com.example   -d packaging=jar   -d type=maven-project   -o starter.zip
```

## 3. Giải Nén File Đã Tải

```shell
unzip starter.zip -d .
```

## 4. Xóa File ZIP

```shell
rm -f starter.zip
```

## 5. Thêm Dependency Bổ Sung

Thêm vào `pom.xml`:

```xml
<dependency>
  <groupId>org.springdoc</groupId>
  <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
  <version>2.8.6</version>
</dependency>
<dependency>
  <groupId>com.tngtech.archunit</groupId>
  <artifactId>archunit-junit5</artifactId>
  <version>1.2.1</version>
  <scope>test</scope>
</dependency>
```

## 6. Thêm Cấu Hình SpringDoc, Redis, JPA, MongoDB

Trong `application.properties`:

```properties
# SpringDoc
springdoc.swagger-ui.doc-expansion=none
springdoc.swagger-ui.operations-sorter=alpha
springdoc.swagger-ui.tags-sorter=alpha

# Redis
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.password=rootroot

# JPA
spring.datasource.driver-class-name=org.postgresql.Driver
spring.datasource.url=jdbc:postgresql://localhost:5432/postgres
spring.datasource.username=postgres
spring.datasource.password=rootroot
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true

# MongoDB
spring.data.mongodb.host=localhost
spring.data.mongodb.port=27017
spring.data.mongodb.authentication-database=admin
spring.data.mongodb.username=root
spring.data.mongodb.password=rootroot
spring.data.mongodb.database=test
```

## 7. Thêm `docker-compose.yaml`

Tạo file tại root dự án với các service:

- **redis:6**
  - password `rootroot`
  - port 6379:6379
  - volume `./redis_data:/data`
- **postgresql:17**
  - password `rootroot`
  - port 5432:5432
  - volume `./postgres_data:/var/lib/postgresql/data`
- **mongo:8**
  - user: `root`
  - password: `rootroot`
  - port 27017:27017
  - volume `./mongo_data:/data/db`

## 8. Thêm `.gitignore`

Bỏ qua thư mục:

```
redis_data
postgres_data
mongo_data
```

## 9. Chạy Test Maven

```shell
./mvnw clean test
```

## 10. Chạy Dự Án (Tùy Chọn)

```shell
docker-compose up -d
./mvnw spring-boot:run
docker-compose rm -sf
```

---

**Thực hiện từng bước một để hoàn thiện dự án.**