---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "findTestFiles", "problems", "runCommands", "runTests", "search", "searchResults", "terminalLastCommand", "testFailure", "usages"]
description: "Tạo bộ khung dự án Spring Boot Kotlin"
---

# Hướng dẫn tạo dự án Spring Boot Kotlin

- Vui lòng đảm bảo bạn đã cài đặt các phần mềm sau trên hệ thống của mình:

  - Java 21
  - Docker
  - Docker Compose

- Nếu bạn cần tùy chỉnh tên dự án, vui lòng thay đổi `artifactId` và `packageName` trong tải mẫu dự án Spring Boot

- Nếu bạn cần cập nhật phiên bản Spring Boot, vui lòng thay đổi `bootVersion` trong tải mẫu dự án Spring Boot

## Kiểm tra phiên bản Java

- Chạy lệnh sau trong terminal và kiểm tra phiên bản Java

```shell
java -version
```

## Tải mẫu dự án Spring Boot

- Chạy lệnh sau trong terminal để tải về một mẫu dự án Spring Boot

```shell
curl https://start.spring.io/starter.zip \
  -d artifactId=demo \
  -d bootVersion=3.4.5 \
  -d dependencies=configuration-processor,webflux,data-r2dbc,postgresql,data-redis-reactive,data-mongodb-reactive,validation,cache,testcontainers \
  -d javaVersion=21 \
  -d language=kotlin \
  -d packageName=com.example \
  -d packaging=jar \
  -d type=gradle-project-kotlin \
  -o starter.zip
```

## Giải nén tệp đã tải về

- Chạy lệnh sau trong terminal để giải nén tệp đã tải về

```shell
unzip starter.zip -d .
```

## Xóa tệp zip đã tải về

- Chạy lệnh sau trong terminal để xóa tệp zip đã tải về

```shell
rm -f starter.zip
```

## Thêm các dependency bổ sung

- Chèn dependency `springdoc-openapi-starter-webmvc-ui` và `archunit-junit5` vào tệp `build.gradle.kts`

```gradle.kts
dependencies {
  implementation("org.springdoc:springdoc-openapi-starter-webflux-ui:2.8.6")
  testImplementation("com.tngtech.archunit:archunit-junit5:1.2.1")
}
```

- Chèn cấu hình SpringDoc vào tệp `application.properties`

```properties
# Cấu hình SpringDoc
springdoc.swagger-ui.doc-expansion=none
springdoc.swagger-ui.operations-sorter=alpha
springdoc.swagger-ui.tags-sorter=alpha
```

- Chèn cấu hình Redis vào tệp `application.properties`

```properties
# Cấu hình Redis
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.password=rootroot
```

- Chèn cấu hình R2DBC vào tệp `application.properties`

```properties
# Cấu hình R2DBC
spring.r2dbc.url=r2dbc:postgresql://localhost:5432/postgres
spring.r2dbc.username=postgres
spring.r2dbc.password=rootroot

spring.sql.init.mode=always
spring.sql.init.platform=postgres
spring.sql.init.continue-on-error=true
```

- Chèn cấu hình MongoDB vào tệp `application.properties`

```properties
# Cấu hình MongoDB
spring.data.mongodb.host=localhost
spring.data.mongodb.port=27017
spring.data.mongodb.authentication-database=admin
spring.data.mongodb.username=root
spring.data.mongodb.password=rootroot
spring.data.mongodb.database=test
```

- Tạo tệp `docker-compose.yaml` ở thư mục gốc của dự án và thêm các dịch vụ sau: `redis:6`, `postgresql:17` và `mongo:8`.

  - Dịch vụ redis cần có:
    - mật khẩu `rootroot`
    - ánh xạ cổng 6379 tới 6379
    - gắn volume `./redis_data` vào `/data`
  - Dịch vụ postgresql cần có:
    - mật khẩu `rootroot`
    - ánh xạ cổng 5432 tới 5432
    - gắn volume `./postgres_data` vào `/var/lib/postgresql/data`
  - Dịch vụ mongo cần có:
    - tên người dùng root khởi tạo `root`
    - mật khẩu root khởi tạo `rootroot`
    - ánh xạ cổng 27017 tới 27017
    - gắn volume `./mongo_data` vào `/data/db`

- Chèn các thư mục `redis_data`, `postgres_data` và `mongo_data` vào tệp `.gitignore`

- Chạy lệnh `gradle clean test` để kiểm tra xem dự án có hoạt động không

```shell
./gradlew clean test
```

- (Tùy chọn) `docker-compose up -d` để khởi động các dịch vụ, `./gradlew spring-boot:run` để chạy dự án Spring Boot, `docker-compose rm -sf` để dừng các dịch vụ.

Hãy thực hiện từng bước một.
