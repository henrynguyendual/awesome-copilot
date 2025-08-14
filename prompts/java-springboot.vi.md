---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "Nhận các phương pháp hay nhất để phát triển ứng dụng với Spring Boot."
---

# Các phương pháp hay nhất cho Spring Boot

Mục tiêu của bạn là giúp tôi viết các ứng dụng Spring Boot chất lượng cao bằng cách tuân theo các phương pháp hay nhất đã được thiết lập.

## Thiết lập & Cấu trúc dự án

- **Công cụ xây dựng (Build Tool):** Sử dụng Maven (`pom.xml`) hoặc Gradle (`build.gradle`) để quản lý phụ thuộc.
- **Starters:** Sử dụng Spring Boot starters (ví dụ: `spring-boot-starter-web`, `spring-boot-starter-data-jpa`) để đơn giản hóa việc quản lý phụ thuộc.
- **Cấu trúc gói (Package Structure):** Tổ chức mã nguồn theo tính năng/miền (ví dụ: `com.example.app.order`, `com.example.app.user`) thay vì theo lớp (ví dụ: `com.example.app.controller`, `com.example.app.service`).

## Tiêm phụ thuộc (Dependency Injection) & Các thành phần (Components)

- **Tiêm phụ thuộc qua Constructor (Constructor Injection):** Luôn sử dụng tiêm phụ thuộc qua constructor cho các phụ thuộc bắt buộc. Điều này giúp các thành phần dễ kiểm thử hơn và các phụ thuộc được thể hiện rõ ràng.
- **Tính bất biến (Immutability):** Khai báo các trường phụ thuộc là `private final`.
- **Các stereotype của Component:** Sử dụng các chú thích `@Component`, `@Service`, `@Repository`, và `@Controller`/`@RestController` một cách thích hợp để định nghĩa các bean.

## Cấu hình

- **Cấu hình bên ngoài (Externalized Configuration):** Sử dụng `application.yml` (hoặc `application.properties`) để cấu hình. YAML thường được ưa chuộng hơn vì tính dễ đọc và cấu trúc phân cấp của nó.
- **Các thuộc tính an toàn về kiểu (Type-Safe Properties):** Sử dụng `@ConfigurationProperties` để liên kết cấu hình với các đối tượng Java có kiểu dữ liệu rõ ràng.
- **Profiles:** Sử dụng Spring Profiles (`application-dev.yml`, `application-prod.yml`) để quản lý các cấu hình dành riêng cho từng môi trường.
- **Quản lý bí mật (Secrets Management):** Không mã hóa cứng các thông tin bí mật. Sử dụng biến môi trường hoặc một công cụ quản lý bí mật chuyên dụng như HashiCorp Vault hoặc AWS Secrets Manager.

## Tầng Web (Controllers)

- **API RESTful:** Thiết kế các điểm cuối (endpoint) RESTful rõ ràng và nhất quán.
- **DTOs (Data Transfer Objects):** Sử dụng DTO để trao đổi dữ liệu ở tầng API. Không để lộ trực tiếp các thực thể JPA (JPA entities) cho client.
- **Xác thực (Validation):** Sử dụng Java Bean Validation (JSR 380) với các chú thích (`@Valid`, `@NotNull`, `@Size`) trên DTO để xác thực dữ liệu yêu cầu (request payloads).
- **Xử lý lỗi (Error Handling):** Triển khai một trình xử lý ngoại lệ toàn cục bằng cách sử dụng `@ControllerAdvice` và `@ExceptionHandler` để cung cấp các phản hồi lỗi nhất quán.

## Tầng dịch vụ (Service Layer)

- **Logic nghiệp vụ (Business Logic):** Đóng gói tất cả logic nghiệp vụ trong các lớp `@Service`.
- **Tính không trạng thái (Statelessness):** Các service nên không có trạng thái.
- **Quản lý giao dịch (Transaction Management):** Sử dụng `@Transactional` trên các phương thức của service để quản lý các giao dịch cơ sở dữ liệu một cách khai báo. Áp dụng nó ở mức độ chi tiết cần thiết nhất.

## Tầng dữ liệu (Data Layer - Repositories)

- **Spring Data JPA:** Sử dụng các repository của Spring Data JPA bằng cách kế thừa `JpaRepository` hoặc `CrudRepository` cho các hoạt động cơ sở dữ liệu tiêu chuẩn.
- **Truy vấn tùy chỉnh (Custom Queries):** Đối với các truy vấn phức tạp, hãy sử dụng `@Query` hoặc JPA Criteria API.
- **Projections:** Sử dụng DTO projections để chỉ lấy dữ liệu cần thiết từ cơ sở dữ liệu.

## Ghi log (Logging)

- **SLF4J:** Sử dụng API SLF4J để ghi log.
- **Khai báo Logger:** `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);`
- **Ghi log tham số hóa (Parameterized Logging):** Sử dụng các thông điệp được tham số hóa (`logger.info("Đang xử lý người dùng {}...", userId);`) thay vì nối chuỗi để cải thiện hiệu suất.

## Kiểm thử (Testing)

- **Kiểm thử đơn vị (Unit Tests):** Viết các bài kiểm thử đơn vị cho các service và component bằng JUnit 5 và một framework mô phỏng (mocking) như Mockito.
- **Kiểm thử tích hợp (Integration Tests):** Sử dụng `@SpringBootTest` cho các bài kiểm thử tích hợp tải ngữ cảnh ứng dụng Spring (Spring application context).
- **Test Slices:** Sử dụng các chú thích test slice như `@WebMvcTest` (cho controllers) hoặc `@DataJpaTest` (cho repositories) để kiểm thử các phần cụ thể của ứng dụng một cách riêng biệt.
- **Testcontainers:** Cân nhắc sử dụng Testcontainers để có các bài kiểm thử tích hợp đáng tin cậy với cơ sở dữ liệu, message broker, v.v. thực tế.

## Bảo mật (Security)

- **Spring Security:** Sử dụng Spring Security để xác thực và ủy quyền.
- **Mã hóa mật khẩu (Password Encoding):** Luôn mã hóa mật khẩu bằng một thuật toán băm mạnh như BCrypt.
- **Làm sạch đầu vào (Input Sanitization):** Ngăn chặn SQL injection bằng cách sử dụng Spring Data JPA hoặc các truy vấn tham số hóa. Ngăn chặn Cross-Site Scripting (XSS) bằng cách mã hóa đầu ra một cách hợp
