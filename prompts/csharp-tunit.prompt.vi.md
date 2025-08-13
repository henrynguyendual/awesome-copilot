# Thực hành tốt nhất với TUnit

Mục tiêu của bạn là giúp tôi viết các bài kiểm thử đơn vị hiệu quả với TUnit, bao gồm cả cách tiếp cận kiểm thử tiêu chuẩn và kiểm thử dựa trên dữ liệu.

## Thiết lập dự án

- Sử dụng một dự án kiểm thử riêng với quy tắc đặt tên `[ProjectName].Tests`
- Tham chiếu gói TUnit và TUnit.Assertions để sử dụng fluent assertions
- Tạo các lớp kiểm thử tương ứng với các lớp được kiểm thử (ví dụ: `CalculatorTests` cho `Calculator`)
- Sử dụng lệnh test của .NET SDK: `dotnet test` để chạy kiểm thử
- TUnit yêu cầu .NET 8.0 hoặc cao hơn

## Cấu trúc kiểm thử

- Không cần thuộc tính lớp kiểm thử (như xUnit/NUnit)
- Sử dụng thuộc tính `[Test]` cho các phương thức kiểm thử (không phải `[Fact]` như xUnit)
- Tuân thủ mô hình Arrange-Act-Assert (AAA)
- Đặt tên kiểm thử theo mẫu `MethodName_Scenario_ExpectedBehavior`
- Sử dụng hook vòng đời: `[Before(Test)]` cho thiết lập và `[After(Test)]` cho dọn dẹp
- Sử dụng `[Before(Class)]` và `[After(Class)]` cho ngữ cảnh chung giữa các kiểm thử trong một lớp
- Sử dụng `[Before(Assembly)]` và `[After(Assembly)]` cho ngữ cảnh chung giữa các lớp kiểm thử
- TUnit hỗ trợ các hook nâng cao như `[Before(TestSession)]` và `[After(TestSession)]`

## Kiểm thử tiêu chuẩn

- Tập trung kiểm thử một hành vi duy nhất
- Tránh kiểm thử nhiều hành vi trong cùng một phương thức
- Sử dụng cú pháp fluent assertion của TUnit với `await Assert.That()`
- Chỉ bao gồm các assertion cần thiết để xác minh trường hợp kiểm thử
- Đảm bảo kiểm thử độc lập và idempotent (có thể chạy theo bất kỳ thứ tự nào)
- Tránh phụ thuộc giữa các kiểm thử (sử dụng `[DependsOn]` nếu cần)

## Kiểm thử dựa trên dữ liệu

- Sử dụng `[Arguments]` cho dữ liệu inline (tương đương `[InlineData]` của xUnit)
- Sử dụng `[MethodData]` cho dữ liệu dựa trên phương thức (tương đương `[MemberData]` của xUnit)
- Sử dụng `[ClassData]` cho dữ liệu dựa trên lớp
- Tạo nguồn dữ liệu tùy chỉnh bằng cách triển khai `ITestDataSource`
- Đặt tên tham số có ý nghĩa trong các kiểm thử dựa trên dữ liệu
- Có thể áp dụng nhiều `[Arguments]` cho cùng một phương thức kiểm thử

## Assertions

- Sử dụng `await Assert.That(value).IsEqualTo(expected)` để kiểm tra bằng giá trị
- Sử dụng `await Assert.That(value).IsSameReferenceAs(expected)` để kiểm tra bằng tham chiếu
- Sử dụng `await Assert.That(value).IsTrue()` hoặc `.IsFalse()` cho điều kiện boolean
- Sử dụng `await Assert.That(collection).Contains(item)` hoặc `.DoesNotContain(item)` cho tập hợp
- Sử dụng `await Assert.That(value).Matches(pattern)` cho kiểm tra regex
- Sử dụng `await Assert.That(action).Throws<TException>()` hoặc `.ThrowsAsync<TException>()` để kiểm thử ngoại lệ
- Kết hợp assertions với `.And`: `await Assert.That(value).IsNotNull().And.IsEqualTo(expected)`
- Sử dụng `.Or` cho điều kiện thay thế: `await Assert.That(value).IsEqualTo(1).Or.IsEqualTo(2)`
- Sử dụng `.Within(tolerance)` cho so sánh DateTime và số với sai số cho phép
- Tất cả assertions đều bất đồng bộ và cần `await`

## Tính năng nâng cao

- Sử dụng `[Repeat(n)]` để lặp lại kiểm thử nhiều lần
- Sử dụng `[Retry(n)]` để tự động thử lại khi thất bại
- Sử dụng `[ParallelLimit<T>]` để giới hạn số lượng chạy song song
- Sử dụng `[Skip("reason")]` để bỏ qua kiểm thử có điều kiện
- Sử dụng `[DependsOn(nameof(OtherTest))]` để tạo quan hệ phụ thuộc giữa các kiểm thử
- Sử dụng `[Timeout(milliseconds)]` để đặt giới hạn thời gian cho kiểm thử
- Tạo thuộc tính tùy chỉnh bằng cách kế thừa thuộc tính cơ sở của TUnit

## Tổ chức kiểm thử

- Nhóm kiểm thử theo tính năng hoặc thành phần
- Sử dụng `[Category("CategoryName")]` để phân loại kiểm thử
- Sử dụng `[DisplayName("Custom Test Name")]` cho tên kiểm thử tùy chỉnh
- Cân nhắc sử dụng `TestContext` cho chẩn đoán và thông tin kiểm thử
- Sử dụng thuộc tính điều kiện như `[WindowsOnly]` cho kiểm thử đặc thù nền tảng

## Hiệu năng và chạy song song

- TUnit chạy kiểm thử song song theo mặc định (khác xUnit yêu cầu cấu hình)
- Sử dụng `[NotInParallel]` để vô hiệu chạy song song cho kiểm thử cụ thể
- Sử dụng `[ParallelLimit<T>]` với giới hạn tùy chỉnh để kiểm soát đồng thời
- Các kiểm thử trong cùng lớp chạy tuần tự theo mặc định
- Sử dụng `[Repeat(n)]` với `[ParallelLimit<T>]` cho kiểm thử tải

## Di chuyển từ xUnit

- Thay `[Fact]` bằng `[Test]`
- Thay `[Theory]` bằng `[Test]` và sử dụng `[Arguments]` cho dữ liệu
- Thay `[InlineData]` bằng `[Arguments]`
- Thay `[MemberData]` bằng `[MethodData]`
- Thay `Assert.Equal` bằng `await Assert.That(actual).IsEqualTo(expected)`
- Thay `Assert.True` bằng `await Assert.That(condition).IsTrue()`
- Thay `Assert.Throws<T>` bằng `await Assert.That(action).Throws<T>()`
- Thay constructor/IDisposable bằng `[Before(Test)]`/`[After(Test)]`
- Thay `IClassFixture<T>` bằng `[Before(Class)]`/`[After(Class)]`

**Tại sao chọn TUnit thay vì xUnit?**

TUnit mang lại trải nghiệm kiểm thử hiện đại, nhanh và linh hoạt với các tính năng nâng cao mà xUnit không có, như assertion bất đồng bộ, hook vòng đời phong phú, và khả năng kiểm thử dựa trên dữ liệu tốt hơn. Fluent assertions của TUnit giúp việc xác minh kiểm thử rõ ràng và dễ đọc hơn, đặc biệt phù hợp cho các dự án .NET phức tạp.
