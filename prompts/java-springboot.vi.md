# Thực hành tốt nhất với Spring Boot

Mục tiêu của bạn là giúp tôi viết ứng dụng Spring Boot chất lượng cao
bằng cách tuân theo các thực hành tốt đã được thiết lập.

## Cấu hình & Cấu trúc dự án

-   **Công cụ build:** Sử dụng Maven (`pom.xml`) hoặc Gradle
    (`build.gradle`) để quản lý dependency.
-   **Spring Boot Starters:** Sử dụng các starter như
    `spring-boot-starter-web`, `spring-boot-starter-data-jpa` để đơn
    giản hóa quản lý dependency.
-   **Cấu trúc package:** Tổ chức mã nguồn theo tính năng
    (feature/domain) như `com.example.app.order`, `com.example.app.user`
    thay vì theo tầng (`controller`, `service`, ...).

## Dependency Injection & Components

-   **Constructor Injection:** Luôn dùng injection qua constructor cho
    dependency bắt buộc, giúp dễ test và rõ ràng về dependency.
-   **Tính bất biến:** Khai báo các trường dependency là
    `private final`.
-   **Component Stereotypes:** Sử dụng `@Component`, `@Service`,
    `@Repository`, `@Controller`/`@RestController` đúng mục đích để định
    nghĩa bean.

## Cấu hình

-   **Externalized Configuration:** Dùng `application.yml` hoặc
    `application.properties` để cấu hình. YAML thường dễ đọc hơn.
-   **Type-Safe Properties:** Dùng `@ConfigurationProperties` để ánh xạ
    cấu hình sang object Java kiểu an toàn.
-   **Profiles:** Sử dụng Spring Profiles (`application-dev.yml`,
    `application-prod.yml`) để quản lý cấu hình cho từng môi trường.
-   **Quản lý Secrets:** Không hardcode secrets. Dùng biến môi trường
    hoặc công cụ như HashiCorp Vault, AWS Secrets Manager.

## Web Layer (Controller)

-   **RESTful APIs:** Thiết kế endpoint rõ ràng và nhất quán.
-   **DTO (Data Transfer Object):** Sử dụng DTO để nhận/trả dữ liệu qua
    API, không expose trực tiếp entity JPA.
-   **Validation:** Sử dụng Java Bean Validation (`@Valid`, `@NotNull`,
    `@Size`) trên DTO để validate dữ liệu request.
-   **Xử lý lỗi:** Tạo global exception handler với
    `@ControllerAdvice` + `@ExceptionHandler` để trả về lỗi đồng nhất.

## Service Layer

-   **Business Logic:** Đặt toàn bộ logic nghiệp vụ trong class
    `@Service`.
-   **Statelessness:** Service nên không lưu trạng thái.
-   **Quản lý Transaction:** Dùng `@Transactional` ở mức granular nhất
    có thể.

## Data Layer (Repository)

-   **Spring Data JPA:** Kế thừa `JpaRepository` hoặc `CrudRepository`
    cho CRUD cơ bản.
-   **Custom Queries:** Với truy vấn phức tạp, dùng `@Query` hoặc JPA
    Criteria API.
-   **Projection:** Dùng DTO projection để chỉ lấy dữ liệu cần thiết.

## Logging

-   **SLF4J:** Dùng SLF4J API để logging.
-   **Khai báo Logger:**
    `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);`
-   **Parameterized Logging:** Dùng tham số
    (`logger.info("Processing user {}...", userId);`) thay vì cộng
    chuỗi.

## Testing

-   **Unit Test:** Viết test cho service và component bằng JUnit 5 +
    Mockito.
-   **Integration Test:** Dùng `@SpringBootTest` để test tích hợp toàn
    bộ context.
-   **Test Slice:** Dùng `@WebMvcTest`, `@DataJpaTest` để test một phần
    ứng dụng.
-   **Testcontainers:** Cân nhắc dùng Testcontainers để test tích hợp
    với DB thực hoặc message broker.

## Bảo mật

-   **Spring Security:** Dùng Spring Security để xác thực và phân quyền.
-   **Password Encoding:** Luôn mã hóa mật khẩu bằng thuật toán mạnh như
    BCrypt.
-   **Input Sanitization:** Ngăn SQL Injection bằng JPA hoặc truy vấn có
    tham số. Ngăn XSS bằng cách encode output.
