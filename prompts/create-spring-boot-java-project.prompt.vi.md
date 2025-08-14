---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "findTestFiles", "problems", "runCommands", "runTests", "search", "searchResults", "terminalLastCommand", "testFailure", "usages"]
description: "Tạo khung sườn dự án Spring Boot Java"
---

# Hướng dẫn tạo dự án Spring Boot Java

- Vui lòng đảm bảo bạn đã cài đặt các phần mềm sau trên hệ thống của mình:

  - Java 21
  - Docker
  - Docker Compose

- Nếu bạn cần tùy chỉnh tên dự án, vui lòng thay đổi `artifactId` và `packageName` trong [tải về mẫu dự án Spring Boot](https://www.google.com/search?q=./create-spring-boot-java-project.prompt.md%23download-spring-boot-project-template)

- Nếu bạn cần cập nhật phiên bản Spring Boot, vui lòng thay đổi `bootVersion` trong [tải về mẫu dự án Spring Boot](https://www.google.com/search?q=./create-spring-boot-java-project.prompt.md%23download-spring-boot-project-template)

## Kiểm tra phiên bản Java

- Chạy lệnh sau trong terminal và kiểm tra phiên bản Java

<!-- end list -->

```shell
java -version
```

## Tải về mẫu dự án Spring Boot

- Chạy lệnh sau trong terminal để tải về một mẫu dự án Spring Boot

<!-- end list -->

```shell
curl https://start.spring.io/starter.zip \
  -d artifactId=demo \
  -d bootVersion=3.4.5 \
  -d dependencies=lombok,configuration-processor,web,data-jpa,postgresql,data-redis,data-mongodb,validation,cache,testcontainers \
  -d javaVersion=21 \
  -d packageName=com.example \
  -d packaging=jar \
  -d type=maven-project \
  -o starter.zip
```

## Giải nén tập tin đã tải về

- Chạy lệnh sau trong terminal để giải nén tập tin đã tải về

<!-- end list -->

```shell
unzip starter.zip -d .
```

## Xóa tập tin zip đã tải về

- Chạy lệnh sau trong terminal để xóa tập tin zip đã tải về

<!-- end list -->

```shell
rm -f starter.zip
```

## Thêm các phụ thuộc bổ sung

- Chèn phụ thuộc `springdoc-openapi-starter-webmvc-ui` và `archunit-junit5` vào tệp `pom.xml`

<!-- end list -->

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

## Thêm cấu hình cho SpringDoc, Redis, JPA và MongoDB

- Chèn cấu hình SpringDoc vào tệp `application.properties`

<!-- end list -->

```properties
# Cấu hình SpringDoc
springdoc.swagger-ui.doc-expansion=none
springdoc.swagger-ui.operations-sorter=alpha
springdoc.swagger-ui.tags-sorter=alpha
```

- Chèn cấu hình Redis vào tệp `application.properties`

<!-- end list -->

```properties
# Cấu hình Redis
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.password=rootroot
```

- Chèn cấu hình JPA vào tệp `application.properties`

<!-- end list -->

```properties
# Cấu hình JPA
spring.datasource.driver-class-name=org.postgresql.Driver
spring.datasource.url=jdbc:postgresql://localhost:5432/postgres
spring.datasource.username=postgres
spring.datasource.password=rootroot
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
```

- Chèn cấu hình MongoDB vào tệp `application.properties`

<!-- end list -->

```properties
# Cấu hình MongoDB
spring.data.mongodb.host=localhost
spring.data.mongodb.port=27017
spring.data.mongodb.authentication-database=admin
spring.data.mongodb.username=root
spring.data.mongodb.password=rootroot
spring.data.mongodb.database=test
```

## Thêm tệp `docker-compose.yaml` với các dịch vụ Redis, PostgreSQL và MongoDB

- Tạo tệp `docker-compose.yaml` ở thư mục gốc của dự án và thêm các dịch vụ sau: `redis:6`, `postgresql:17` và `mongo:8`.

  - Dịch vụ redis cần có
    - mật khẩu `rootroot`
    - ánh xạ cổng 6379 tới 6379
    - gắn volume `./redis_data` vào `/data`
  - Dịch vụ postgresql cần có
    - mật khẩu `rootroot`
    - ánh xạ cổng 5432 tới 5432
    - gắn volume `./postgres_data` vào `/var/lib/postgresql/data`
  - Dịch vụ mongo cần có
    - tên người dùng root khởi tạo là `root`
    - mật khẩu root khởi tạo là `rootroot`
    - ánh xạ cổng 27017 tới 27017
    - gắn volume `./mongo_data` vào `/data/db`

## Thêm tệp `.gitignore`

- Chèn các thư mục `redis_data`, `postgres_data` và `mongo_data` vào tệp `.gitignore`

## Chạy lệnh kiểm thử của Maven

- Chạy lệnh `maven clean test` để kiểm tra xem dự án có hoạt động không

<!-- end list -->

```shell
./mvnw clean test
```

## Chạy lệnh thực thi của Maven (Tùy chọn)

- (Tùy chọn) `docker-compose up -d` để khởi động các dịch vụ, `./mvnw spring-boot:run` để chạy dự án Spring Boot, `docker-compose rm -sf` để dừng các dịch vụ.

## Hãy thực hiện từng bước một
