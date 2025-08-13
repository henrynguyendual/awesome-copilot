# Tạo Skeleton Dự Án Spring Boot Kotlin

## Yêu Cầu Phần Mềm

Đảm bảo đã cài đặt các phần mềm sau:

- Java 21
- Docker
- Docker Compose

Nếu muốn tùy chỉnh tên dự án, thay đổi `artifactId` và `packageName` trong phần [Tải template dự án Spring Boot](#tải-template-dự-án-spring-boot).

Nếu muốn cập nhật phiên bản Spring Boot, thay đổi `bootVersion` trong phần [Tải template dự án Spring Boot](#tải-template-dự-án-spring-boot).

## 1. Kiểm Tra Phiên Bản Java

Chạy lệnh sau:

```shell
java -version
```

## 2. Tải Template Dự Án Spring Boot

Chạy lệnh:

```shell
curl https://start.spring.io/starter.zip   -d artifactId=demo   -d bootVersion=3.4.5   -d dependencies=configuration-processor,webflux,data-r2dbc,postgresql,data-redis-reactive,data-mongodb-reactive,validation,cache,testcontainers   -d javaVersion=21   -d language=kotlin   -d packageName=com.example   -d packaging=jar   -d type=gradle-project-kotlin   -o starter.zip
```

## 3. Giải Nén File

```shell
unzip starter.zip -d .
```

## 4. Xóa File ZIP

```shell
rm -f starter.zip
```

## 5. Thêm Dependency Bổ Sung

Trong `build.gradle.kts`:

```gradle.kts
dependencies {
  implementation("org.springdoc:springdoc-openapi-starter-webflux-ui:2.8.6")
  testImplementation("com.tngtech.archunit:archunit-junit5:1.2.1")
}
```

## 6. Thêm Cấu Hình

### SpringDoc (`application.properties`):

```properties
# SpringDoc
springdoc.swagger-ui.doc-expansion=none
springdoc.swagger-ui.operations-sorter=alpha
springdoc.swagger-ui.tags-sorter=alpha
```

### Redis:

```properties
spring.data.redis.host=localhost
spring.data.redis.port=6379
spring.data.redis.password=rootroot
```

### R2DBC:

```properties
spring.r2dbc.url=r2dbc:postgresql://localhost:5432/postgres
spring.r2dbc.username=postgres
spring.r2dbc.password=rootroot

spring.sql.init.mode=always
spring.sql.init.platform=postgres
spring.sql.init.continue-on-error=true
```

### MongoDB:

```properties
spring.data.mongodb.host=localhost
spring.data.mongodb.port=27017
spring.data.mongodb.authentication-database=admin
spring.data.mongodb.username=root
spring.data.mongodb.password=rootroot
spring.data.mongodb.database=test
```

## 7. Thêm `docker-compose.yaml`

Tại thư mục gốc dự án, tạo các service:

- **redis:6**
  - password: `rootroot`
  - port 6379:6379
  - volume `./redis_data:/data`
- **postgresql:17**
  - password: `rootroot`
  - port 5432:5432
  - volume `./postgres_data:/var/lib/postgresql/data`
- **mongo:8**
  - user: `root`
  - password: `rootroot`
  - port 27017:27017
  - volume `./mongo_data:/data/db`

## 8. Thêm `.gitignore`

```
redis_data
postgres_data
mongo_data
```

## 9. Chạy Test

```shell
./gradlew clean test
```

## 10. (Tùy Chọn) Chạy Dự Án

```shell
docker-compose up -d
./gradlew spring-boot:run
docker-compose rm -sf
```

---

**Thực hiện từng bước để đảm bảo dự án hoạt động ổn định.**