# Thực hành tốt nhất với Spring Boot và Kotlin

Mục tiêu của bạn là giúp tôi viết ứng dụng Spring Boot chất lượng cao,
đúng chuẩn Kotlin.

## Cấu hình & Cấu trúc dự án

-   **Công cụ build:** Sử dụng Maven (`pom.xml`) hoặc Gradle
    (`build.gradle`) với plugin Kotlin (`kotlin-maven-plugin` hoặc
    `org.jetbrains.kotlin.jvm`).
-   **Kotlin Plugins:** Với JPA, bật plugin `kotlin-jpa` để tự động làm
    cho các entity `open` mà không cần code rườm rà.
-   **Spring Boot Starters:** Sử dụng các starter như
    `spring-boot-starter-web`, `spring-boot-starter-data-jpa` như bình
    thường.
-   **Cấu trúc package:** Tổ chức code theo tính năng (feature/domain)
    thay vì theo tầng.

## Dependency Injection & Components

-   **Primary Constructor:** Luôn sử dụng constructor chính để inject
    dependency --- đây là cách viết chuẩn Kotlin.
-   **Tính bất biến:** Khai báo dependency với `private val` trong
    constructor. Ưu tiên `val` thay vì `var` để giữ bất biến.
-   **Component Stereotypes:** Sử dụng `@Service`, `@Repository`,
    `@RestController` như Java.

## Cấu hình

-   **Externalized Configuration:** Dùng `application.yml` vì dễ đọc và
    hỗ trợ cấu trúc phân cấp.
-   **Type-Safe Properties:** Dùng `@ConfigurationProperties` với
    `data class` để tạo object cấu hình bất biến, type-safe.
-   **Profiles:** Dùng Spring Profiles (`application-dev.yml`,
    `application-prod.yml`) để quản lý cấu hình theo môi trường.
-   **Quản lý Secrets:** Không hardcode secrets. Sử dụng biến môi trường
    hoặc công cụ như HashiCorp Vault, AWS Secrets Manager.

## Web Layer (Controller)

-   **RESTful APIs:** Thiết kế endpoint REST rõ ràng, nhất quán.
-   **Data Class cho DTO:** Dùng `data class` cho DTO để có sẵn
    `equals()`, `hashCode()`, `toString()`, `copy()` và bất biến.
-   **Validation:** Sử dụng Java Bean Validation (`@Valid`, `@NotNull`,
    `@Size`) trên DTO.
-   **Xử lý lỗi:** Tạo global exception handler với
    `@ControllerAdvice` + `@ExceptionHandler`.

## Service Layer

-   **Business Logic:** Đặt toàn bộ logic nghiệp vụ trong class
    `@Service`.
-   **Statelessness:** Service nên không lưu trạng thái.
-   **Quản lý Transaction:** Dùng `@Transactional` ở class hoặc method
    khi cần.

## Data Layer (Repository)

-   **JPA Entities:** Entity phải là `open`. Nên dùng plugin
    `kotlin-jpa` để tự động xử lý.
-   **Null Safety:** Tận dụng null-safety của Kotlin để phân biệt rõ
    field bắt buộc và tùy chọn.
-   **Spring Data JPA:** Kế thừa `JpaRepository` hoặc `CrudRepository`.
-   **Coroutines:** Với app reactive, dùng hỗ trợ coroutine của Spring
    Boot.

## Logging

-   **Companion Object Logger:** Khai báo logger trong companion object:

    ``` kotlin
    companion object {
        private val logger = LoggerFactory.getLogger(MyClass::class.java)
    }
    ```

-   **Parameterized Logging:** Dùng message có tham số để tối ưu hiệu
    năng.

## Testing

-   **JUnit 5:** Mặc định hoạt động tốt với Kotlin.
-   **Thư viện Test chuẩn Kotlin:** Dùng **Kotest** (assertion) và
    **MockK** (mocking) để có cú pháp Kotlin rõ ràng.
-   **Test Slice:** Dùng `@WebMvcTest`, `@DataJpaTest` để test một phần
    app.
-   **Testcontainers:** Dùng Testcontainers để test tích hợp với DB hoặc
    message broker thực.

## Coroutines & Lập trình async

-   **Hàm `suspend`:** Dùng cho code async non-blocking trong controller
    và service.
-   **Structured Concurrency:** Dùng `coroutineScope` hoặc
    `supervisorScope` để quản lý vòng đời coroutine.
