# Thực hành tốt nhất với JUnit 5+

Mục tiêu của bạn là giúp tôi viết các bài kiểm thử đơn vị (unit test)
hiệu quả với JUnit 5, bao gồm cả kiểm thử tiêu chuẩn và kiểm thử theo dữ
liệu (data-driven).

## Cấu hình dự án

-   Sử dụng cấu trúc dự án chuẩn của Maven hoặc Gradle.
-   Đặt mã nguồn kiểm thử trong thư mục `src/test/java`.
-   Thêm các dependency: `junit-jupiter-api`, `junit-jupiter-engine`, và
    `junit-jupiter-params` (cho kiểm thử tham số hóa).
-   Sử dụng lệnh của công cụ build để chạy test: `mvn test` hoặc
    `gradle test`.

## Cấu trúc bài test

-   Lớp test nên có hậu tố `Test`, ví dụ: `CalculatorTests` cho lớp
    `Calculator`.
-   Sử dụng `@Test` cho phương thức test.
-   Tuân theo mô hình Arrange-Act-Assert (AAA).
-   Đặt tên test theo quy tắc mô tả:
    `methodName_should_expectedBehavior_when_scenario`.
-   Sử dụng `@BeforeEach` và `@AfterEach` cho setup/teardown trước và
    sau mỗi test.
-   Sử dụng `@BeforeAll` và `@AfterAll` cho setup/teardown của toàn lớp
    (phải là static method).
-   Sử dụng `@DisplayName` để đặt tên dễ đọc cho lớp và phương thức
    test.

## Kiểm thử tiêu chuẩn

-   Mỗi test chỉ tập trung vào một hành vi cụ thể.
-   Tránh kiểm thử nhiều điều kiện trong cùng một phương thức test.
-   Đảm bảo test độc lập và idempotent (chạy được ở bất kỳ thứ tự nào).
-   Tránh sự phụ thuộc giữa các test.

## Kiểm thử theo dữ liệu (Parameterized Tests)

-   Sử dụng `@ParameterizedTest` để đánh dấu phương thức test có tham
    số.
-   Sử dụng `@ValueSource` cho các giá trị đơn giản (string, int, ...).
-   Sử dụng `@MethodSource` để gọi method cung cấp dữ liệu (Stream,
    Collection, ...).
-   Sử dụng `@CsvSource` cho dữ liệu CSV inline.
-   Sử dụng `@CsvFileSource` để lấy dữ liệu từ file CSV trong classpath.
-   Sử dụng `@EnumSource` để lấy các giá trị enum.

## Assertion

-   Sử dụng các phương thức tĩnh từ `org.junit.jupiter.api.Assertions`
    (vd: `assertEquals`, `assertTrue`, `assertNotNull`).
-   Để assertion dễ đọc hơn, có thể dùng AssertJ
    (`assertThat(...).is...`).
-   Sử dụng `assertThrows` hoặc `assertDoesNotThrow` để kiểm thử
    exception.
-   Gom nhóm các assertion liên quan với `assertAll` để đảm bảo tất cả
    được kiểm tra trước khi test fail.
-   Thêm thông báo mô tả trong assertion để dễ hiểu khi lỗi.

## Mocking và tách biệt

-   Sử dụng thư viện Mockito để tạo mock object cho dependency.
-   Dùng annotation `@Mock` và `@InjectMocks` từ Mockito để đơn giản hóa
    việc tạo và inject mock.
-   Sử dụng interface để dễ mocking hơn.

## Tổ chức bài test

-   Nhóm các test theo chức năng hoặc component bằng package.
-   Sử dụng `@Tag` để phân loại test (vd: `@Tag("fast")`,
    `@Tag("integration")`).
-   Sử dụng `@TestMethodOrder(MethodOrderer.OrderAnnotation.class)` và
    `@Order` để điều khiển thứ tự chạy test khi cần thiết.
-   Sử dụng `@Disabled` để tạm thời bỏ qua test, kèm lý do.
-   Sử dụng `@Nested` để nhóm các test trong inner class nhằm tổ chức
    tốt hơn.
