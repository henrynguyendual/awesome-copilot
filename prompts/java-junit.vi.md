---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "Nhận các phương pháp hay nhất cho kiểm thử đơn vị JUnit 5, bao gồm cả các bài kiểm thử theo hướng dữ liệu"
---

# Các phương pháp hay nhất cho JUnit 5+

Mục tiêu của bạn là giúp tôi viết các bài kiểm thử đơn vị hiệu quả với JUnit 5, bao gồm cả phương pháp kiểm thử tiêu chuẩn và theo hướng dữ liệu.

## Thiết lập dự án

- Sử dụng cấu trúc dự án Maven hoặc Gradle tiêu chuẩn.
- Đặt mã nguồn kiểm thử trong `src/test/java`.
- Bao gồm các dependency cho `junit-jupiter-api`, `junit-jupiter-engine`, và `junit-jupiter-params` cho các bài kiểm thử tham số hóa.
- Sử dụng các lệnh của công cụ build để chạy kiểm thử: `mvn test` hoặc `gradle test`.

## Cấu trúc bài kiểm thử

- Các lớp kiểm thử nên có hậu tố `Test`, ví dụ: `CalculatorTests` cho lớp `Calculator`.
- Sử dụng `@Test` cho các phương thức kiểm thử.
- Tuân theo mẫu Arrange-Act-Assert (AAA).
- Đặt tên các bài kiểm thử theo quy ước mô tả, như `tenPhuongThuc_nen_hanhViMongDoi_khi_tinhHuong`.
- Sử dụng `@BeforeEach` và `@AfterEach` để thiết lập và dọn dẹp trước và sau mỗi bài kiểm thử.
- Sử dụng `@BeforeAll` và `@AfterAll` để thiết lập và dọn dẹp trước và sau mỗi lớp (phải là các phương thức static).
- Sử dụng `@DisplayName` để cung cấp tên dễ đọc cho các lớp và phương thức kiểm thử.

## Các bài kiểm thử tiêu chuẩn

- Giữ cho các bài kiểm thử tập trung vào một hành vi duy nhất.
- Tránh kiểm tra nhiều điều kiện trong một phương thức kiểm thử.
- Làm cho các bài kiểm thử độc lập và có thể chạy lại nhiều lần mà không thay đổi kết quả (có thể chạy theo bất kỳ thứ tự nào).
- Tránh sự phụ thuộc lẫn nhau giữa các bài kiểm thử.

## Các bài kiểm thử theo hướng dữ liệu (Tham số hóa)

- Sử dụng `@ParameterizedTest` để đánh dấu một phương thức là một bài kiểm thử tham số hóa.
- Sử dụng `@ValueSource` cho các giá trị đơn giản (chuỗi, số nguyên, v.v.).
- Sử dụng `@MethodSource` để tham chiếu đến một phương thức factory cung cấp các đối số kiểm thử dưới dạng `Stream`, `Collection`, v.v.
- Sử dụng `@CsvSource` cho các giá trị được phân tách bằng dấu phẩy ngay trong mã.
- Sử dụng `@CsvFileSource` để sử dụng một tệp CSV từ classpath.
- Sử dụng `@EnumSource` để sử dụng các hằng số enum.

## Khẳng định (Assertions)

- Sử dụng các phương thức static từ `org.junit.jupiter.api.Assertions` (ví dụ: `assertEquals`, `assertTrue`, `assertNotNull`).
- Để có các khẳng định trôi chảy và dễ đọc hơn, hãy cân nhắc sử dụng một thư viện như AssertJ (`assertThat(...).is...`).
- Sử dụng `assertThrows` hoặc `assertDoesNotThrow` để kiểm tra ngoại lệ.
- Nhóm các khẳng định liên quan với `assertAll` để đảm bảo tất cả các khẳng định đều được kiểm tra trước khi bài kiểm thử thất bại.
- Sử dụng các thông báo mô tả trong các khẳng định để cung cấp sự rõ ràng khi có lỗi.

## Mocking và Cô lập

- Sử dụng một framework mocking như Mockito để tạo các đối tượng mock cho các dependency.
- Sử dụng các annotation `@Mock` và `@InjectMocks` từ Mockito để đơn giản hóa việc tạo và tiêm mock.
- Sử dụng interface để tạo điều kiện thuận lợi cho việc mocking.

## Tổ chức bài kiểm thử

- Nhóm các bài kiểm thử theo tính năng hoặc thành phần bằng cách sử dụng các package.
- Sử dụng `@Tag` để phân loại các bài kiểm thử (ví dụ: `@Tag("fast")`, `@Tag("integration")`).
- Sử dụng `@TestMethodOrder(MethodOrderer.OrderAnnotation.class)` và `@Order` để kiểm soát thứ tự thực thi kiểm thử khi thực sự cần thiết.
- Sử dụng `@Disabled` để tạm thời bỏ qua một phương thức hoặc lớp kiểm thử, kèm theo lý do.
- Sử dụng `@Nested` để nhóm các bài kiểm thử trong một lớp lồng nhau (nested inner class) để tổ chức và cấu
