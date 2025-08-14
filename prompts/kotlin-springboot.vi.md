---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "Nhận các phương pháp hay nhất để phát triển ứng dụng với Spring Boot và Kotlin."
---

# Các phương pháp hay nhất cho Spring Boot với Kotlin

Mục tiêu của bạn là giúp tôi viết các ứng dụng Spring Boot chất lượng cao, mang tính thành ngữ (idiomatic) bằng Kotlin.

## Thiết lập & Cấu trúc dự án

- **Công cụ xây dựng (Build Tool):** Sử dụng Maven (`pom.xml`) hoặc Gradle (`build.gradle`) với các plugin Kotlin (`kotlin-maven-plugin` hoặc `org.jetbrains.kotlin.jvm`).
- **Plugin Kotlin:** Đối với JPA, hãy bật plugin `kotlin-jpa` để tự động làm cho các lớp entity `open` mà không cần mã soạn sẵn (boilerplate).
- **Starters:** Sử dụng Spring Boot starters (ví dụ: `spring-boot-starter-web`, `spring-boot-starter-data-jpa`) như bình thường.
- **Cấu trúc gói (Package Structure):** Tổ chức mã theo tính năng/miền (ví dụ: `com.example.app.order`, `com.example.app.user`) thay vì theo lớp (layer).

## Tiêm phụ thuộc & Các thành phần (Dependency Injection & Components)

- **Constructor chính (Primary Constructors):** Luôn sử dụng constructor chính để tiêm các phụ thuộc bắt buộc. Đây là cách tiếp cận thành ngữ và ngắn gọn nhất trong Kotlin.
- **Tính bất biến (Immutability):** Khai báo các phụ thuộc là `private val` trong constructor chính. Ưu tiên `val` hơn `var` ở mọi nơi để thúc đẩy tính bất biến.
- **Các stereotype thành phần (Component Stereotypes):** Sử dụng các chú thích `@Service`, `@Repository`, và `@RestController` giống như trong Java.

## Cấu hình (Configuration)

- **Cấu hình bên ngoài (Externalized Configuration):** Sử dụng `application.yml` vì cấu trúc phân cấp và dễ đọc của nó.
- **Thuộc tính an toàn kiểu (Type-Safe Properties):** Sử dụng `@ConfigurationProperties` với `data class` để tạo các đối tượng cấu hình bất biến, an toàn về kiểu.
- **Hồ sơ (Profiles):** Sử dụng Spring Profiles (`application-dev.yml`, `application-prod.yml`) để quản lý các cấu hình dành riêng cho từng môi trường.
- **Quản lý bí mật (Secrets Management):** Không bao giờ mã hóa cứng (hardcode) các bí mật. Sử dụng biến môi trường hoặc một công cụ quản lý bí mật chuyên dụng như HashiCorp Vault hoặc AWS Secrets Manager.

## Lớp Web (Controllers)

- **API RESTful:** Thiết kế các điểm cuối (endpoint) RESTful rõ ràng và nhất quán.
- **Data class cho DTO:** Sử dụng `data class` của Kotlin cho tất cả các DTO. Điều này cung cấp miễn phí các hàm `equals()`, `hashCode()`, `toString()`, và `copy()` và thúc đẩy tính bất biến.
- **Xác thực (Validation):** Sử dụng Java Bean Validation (JSR 380) với các chú thích (`@Valid`, `@NotNull`, `@Size`) trên các data class DTO của bạn.
- **Xử lý lỗi (Error Handling):** Triển khai một trình xử lý ngoại lệ toàn cục bằng cách sử dụng `@ControllerAdvice` và `@ExceptionHandler` để có các phản hồi lỗi nhất quán.

## Lớp Dịch vụ (Service Layer)

- **Logic nghiệp vụ (Business Logic):** Đóng gói logic nghiệp vụ trong các lớp `@Service`.
- **Không trạng thái (Statelessness):** Các dịch vụ nên không có trạng thái.
- **Quản lý giao dịch (Transaction Management):** Sử dụng `@Transactional` trên các phương thức dịch vụ. Trong Kotlin, điều này có thể được áp dụng ở cấp lớp hoặc hàm.

## Lớp Dữ liệu (Data Layer - Repositories)

- **Entity JPA:** Định nghĩa các entity dưới dạng class. Hãy nhớ rằng chúng phải là `open`. Rất khuyến khích sử dụng plugin trình biên dịch `kotlin-jpa` để xử lý việc này một cách tự động.
- **An toàn null (Null Safety):** Tận dụng tính năng an toàn null của Kotlin (`?`) để xác định rõ ràng trường entity nào là tùy chọn hoặc bắt buộc ở cấp kiểu dữ liệu.
- **Spring Data JPA:** Sử dụng các repository của Spring Data JPA bằng cách kế thừa `JpaRepository` hoặc `CrudRepository`.
- **Coroutines:** Đối với các ứng dụng phản ứng (reactive), hãy tận dụng sự hỗ trợ của Spring Boot cho Kotlin Coroutines trong lớp dữ liệu.

## Ghi log (Logging)

- **Logger trong Companion Object:** Cách thành ngữ để khai báo một logger là trong một companion object.
  ```kotlin
  companion object {
      private val logger = LoggerFactory.getLogger(MyClass::class.java)
  }
  ```
- **Ghi log có tham số (Parameterized Logging):** Sử dụng các thông điệp có tham số (`logger.info("Đang xử lý người dùng {}...", userId)`) để tăng hiệu suất và sự rõ ràng.

## Kiểm thử (Testing)

- **JUnit 5:** JUnit 5 là mặc định và hoạt động liền mạch với Kotlin.
- **Thư viện kiểm thử thành ngữ:** Để có các bài kiểm thử trôi chảy và thành ngữ hơn, hãy xem xét sử dụng **Kotest** cho các khẳng định (assertions) và **MockK** để tạo đối tượng giả (mocking). Chúng được thiết kế cho Kotlin và cung cấp cú pháp biểu cảm hơn.
- **Test Slices:** Sử dụng các chú thích test slice như `@WebMvcTest` hoặc `@DataJpaTest` để kiểm thử các phần cụ thể của ứng dụng.
- **Testcontainers:** Sử dụng Testcontainers để có các bài kiểm thử tích hợp đáng tin cậy với cơ sở dữ liệu thực, message broker, v.v.

## Coroutines & Lập trình bất đồng bộ

- **Hàm `suspend`:** Đối với mã bất đồng bộ không chặn, hãy sử dụng các hàm `suspend` trong controllers và services của bạn. Spring Boot có hỗ trợ tuyệt vời cho coroutines.
- **Đồng thời có cấu trúc (Structured Concurrency):** Sử dụng `coroutineScope` hoặc `supervisorScope` để quản lý vòng đời của các
