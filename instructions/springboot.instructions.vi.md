---
description: "Hướng dẫn xây dựng các ứng dụng Spring Boot cơ bản"
applyTo: "**/*.java, **/*.kt"
---

# Phát triển Spring Boot

## Hướng dẫn Chung

- Chỉ đưa ra các đề xuất có độ tin cậy cao khi xem xét các thay đổi về mã.
- Viết mã với các phương pháp bảo trì tốt, bao gồm các bình luận về lý do đưa ra các quyết định thiết kế nhất định.
- Xử lý các trường hợp biên và viết xử lý ngoại lệ rõ ràng.
- Đối với các thư viện hoặc phụ thuộc bên ngoài, hãy đề cập đến cách sử dụng và mục đích của chúng trong các bình luận.

## Hướng dẫn Spring Boot

### Dependency Injection (Tiêm phụ thuộc)

- Sử dụng constructor injection cho tất cả các phụ thuộc bắt buộc.
- Khai báo các trường phụ thuộc là `private final`.

### Configuration (Cấu hình)

- Sử dụng tệp YAML (`application.yml`) cho cấu hình bên ngoài.
- Environment Profiles (Hồ sơ môi trường): Sử dụng Spring profiles cho các môi trường khác nhau (dev, test, prod).
- Configuration Properties (Thuộc tính cấu hình): Sử dụng @ConfigurationProperties để liên kết cấu hình an toàn về kiểu.
- Secrets Management (Quản lý bí mật): Đưa các bí mật ra ngoài bằng cách sử dụng biến môi trường hoặc hệ thống quản lý bí mật.

### Code Organization (Tổ chức mã nguồn)

- Package Structure (Cấu trúc gói): Tổ chức theo tính năng/miền thay vì theo lớp.
- Separation of Concerns (Phân tách các mối quan tâm): Giữ cho controller gọn nhẹ, service tập trung và repository đơn giản.
- Utility Classes (Lớp tiện ích): Đặt các lớp tiện ích là final với constructor private.

### Service Layer (Lớp dịch vụ)

- Đặt logic nghiệp vụ trong các lớp được chú thích bằng `@Service`.
- Các service phải không có trạng thái (stateless) và có thể kiểm thử được.
- Tiêm các repository thông qua constructor.
- Chữ ký phương thức của service nên sử dụng ID miền hoặc DTO, không để lộ trực tiếp các entity của repository trừ khi cần thiết.

### Logging (Ghi nhật ký)

- Sử dụng SLF4J cho tất cả việc ghi nhật ký (`private static final Logger logger = LoggerFactory.getLogger(MyClass.class);`).
- Không sử dụng trực tiếp các triển khai cụ thể (Logback, Log4j2) hoặc `System.out.println()`.
- Sử dụng ghi nhật ký có tham số: `logger.info("Người dùng {} đã đăng nhập", userId);`.

### Security & Input Handling (Bảo mật & Xử lý đầu vào)

- Sử dụng truy vấn có tham số | Luôn sử dụng Spring Data JPA hoặc `NamedParameterJdbcTemplate` để ngăn chặn SQL injection.
- Xác thực các request body và tham số bằng cách sử dụng các chú thích JSR-380 (`@NotNull`, `@Size`, v.v.) và `BindingResult`.

## Build and Verification (Xây dựng và xác minh)

- Sau khi thêm hoặc sửa đổi mã, hãy xác minh rằng dự án vẫn xây dựng thành công.
- Nếu dự án sử dụng Maven, hãy chạy `mvn clean install`.
- Nếu dự án sử dụng Gradle, hãy chạy `./gradlew build` (hoặc `gradlew.bat build` trên Windows).
- Đảm bảo tất cả các bài kiểm thử đều vượt qua như một phần của quá trình xây
