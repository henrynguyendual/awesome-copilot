---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "Nhận các phương pháp hay nhất cho kiểm thử đơn vị TUnit, bao gồm cả kiểm thử theo hướng dữ liệu"
---

# Các phương pháp hay nhất với TUnit

Mục tiêu của bạn là giúp tôi viết các bài kiểm thử đơn vị (unit test) hiệu quả với TUnit, bao gồm cả phương pháp kiểm thử tiêu chuẩn và kiểm thử theo hướng dữ liệu.

## Thiết lập dự án

- Sử dụng một dự án kiểm thử riêng biệt với quy ước đặt tên `[TênDựÁn].Tests`
- Tham chiếu gói TUnit và TUnit.Assertions để sử dụng các khẳng định (assertion) fluent
- Tạo các lớp kiểm thử khớp với các lớp đang được kiểm thử (ví dụ: `CalculatorTests` cho `Calculator`)
- Sử dụng các lệnh kiểm thử của .NET SDK: `dotnet test` để chạy kiểm thử
- TUnit yêu cầu .NET 8.0 trở lên

## Cấu trúc Kiểm thử

- Không yêu cầu thuộc tính (attribute) cho lớp kiểm thử (như xUnit/NUnit)
- Sử dụng thuộc tính `[Test]` cho các phương thức kiểm thử (không phải `[Fact]` như xUnit)
- Tuân theo mẫu Arrange-Act-Assert (AAA)
- Đặt tên kiểm thử theo mẫu `TênPhươngThức_KịchBản_HànhViMongMuốn`
- Sử dụng các hook vòng đời: `[Before(Test)]` để thiết lập và `[After(Test)]` để dọn dẹp
- Sử dụng `[Before(Class)]` và `[After(Class)]` cho ngữ cảnh dùng chung giữa các kiểm thử trong một lớp
- Sử dụng `[Before(Assembly)]` và `[After(Assembly)]` cho ngữ cảnh dùng chung trên các lớp kiểm thử
- TUnit hỗ trợ các hook vòng đời nâng cao như `[Before(TestSession)]` và `[After(TestSession)]`

## Kiểm thử Tiêu chuẩn

- Giữ cho các bài kiểm thử tập trung vào một hành vi duy nhất
- Tránh kiểm thử nhiều hành vi trong một phương thức kiểm thử
- Sử dụng cú pháp khẳng định fluent của TUnit với `await Assert.That()`
- Chỉ bao gồm các khẳng định cần thiết để xác minh trường hợp kiểm thử
- Làm cho các bài kiểm thử độc lập và không thay đổi trạng thái (có thể chạy theo bất kỳ thứ tự nào)
- Tránh sự phụ thuộc lẫn nhau giữa các bài kiểm thử (sử dụng thuộc tính `[DependsOn]` nếu cần)

## Kiểm thử theo hướng dữ liệu (Data-Driven Tests)

- Sử dụng thuộc tính `[Arguments]` cho dữ liệu kiểm thử nội tuyến (tương đương với `[InlineData]` của xUnit)
- Sử dụng `[MethodData]` cho dữ liệu kiểm thử dựa trên phương thức (tương đương với `[MemberData]` của xUnit)
- Sử dụng `[ClassData]` cho dữ liệu kiểm thử dựa trên lớp
- Tạo các nguồn dữ liệu tùy chỉnh bằng cách triển khai `ITestDataSource`
- Sử dụng tên tham số có ý nghĩa trong các bài kiểm thử theo hướng dữ liệu
- Có thể áp dụng nhiều thuộc tính `[Arguments]` cho cùng một phương thức kiểm thử

## Khẳng định (Assertions)

- Sử dụng `await Assert.That(value).IsEqualTo(expected)` để so sánh bằng giá trị
- Sử dụng `await Assert.That(value).IsSameReferenceAs(expected)` để so sánh bằng tham chiếu
- Sử dụng `await Assert.That(value).IsTrue()` hoặc `await Assert.That(value).IsFalse()` cho các điều kiện boolean
- Sử dụng `await Assert.That(collection).Contains(item)` hoặc `await Assert.That(collection).DoesNotContain(item)` cho các tập hợp
- Sử dụng `await Assert.That(value).Matches(pattern)` để khớp mẫu regex
- Sử dụng `await Assert.That(action).Throws<TException>()` hoặc `await Assert.That(asyncAction).ThrowsAsync<TException>()` để kiểm tra ngoại lệ
- Nối chuỗi các khẳng định bằng toán tử `.And`: `await Assert.That(value).IsNotNull().And.IsEqualTo(expected)`
- Sử dụng toán tử `.Or` cho các điều kiện thay thế: `await Assert.That(value).IsEqualTo(1).Or.IsEqualTo(2)`
- Sử dụng `.Within(tolerance)` để so sánh DateTime và số với một khoảng dung sai
- Tất cả các khẳng định đều là bất đồng bộ và phải được `await`

## Các tính năng nâng cao

- Sử dụng `[Repeat(n)]` để lặp lại các bài kiểm thử nhiều lần
- Sử dụng `[Retry(n)]` để tự động thử lại khi thất bại
- Sử dụng `[ParallelLimit<T>]` để kiểm soát giới hạn thực thi song song
- Sử dụng `[Skip("lý do")]` để bỏ qua các bài kiểm thử một cách có điều kiện
- Sử dụng `[DependsOn(nameof(OtherTest))]` để tạo sự phụ thuộc giữa các bài kiểm thử
- Sử dụng `[Timeout(milliseconds)]` để đặt thời gian chờ cho kiểm thử
- Tạo các thuộc tính tùy chỉnh bằng cách kế thừa từ các thuộc tính cơ sở của TUnit

## Tổ chức Kiểm thử

- Nhóm các bài kiểm thử theo tính năng hoặc thành phần
- Sử dụng `[Category("TênDanhMục")]` để phân loại kiểm thử
- Sử dụng `[DisplayName("Tên kiểm thử tùy chỉnh")]` để đặt tên hiển thị tùy chỉnh cho kiểm thử
- Cân nhắc sử dụng `TestContext` để chẩn đoán và lấy thông tin kiểm thử
- Sử dụng các thuộc tính có điều kiện như `[WindowsOnly]` tùy chỉnh cho các bài kiểm thử dành riêng cho nền tảng

## Hiệu suất và Thực thi song song

- TUnit chạy các bài kiểm thử song song theo mặc định (không giống như xUnit yêu cầu cấu hình rõ ràng)
- Sử dụng `[NotInParallel]` để tắt thực thi song song cho các bài kiểm thử cụ thể
- Sử dụng `[ParallelLimit<T>]` với các lớp giới hạn tùy chỉnh để kiểm soát đồng thời
- Các bài kiểm thử trong cùng một lớp chạy tuần tự theo mặc định
- Sử dụng `[Repeat(n)]` với `[ParallelLimit<T>]` cho các kịch bản kiểm thử tải

## Di chuyển từ xUnit

- Thay thế `[Fact]` bằng `[Test]`
- Thay thế `[Theory]` bằng `[Test]` và sử dụng `[Arguments]` cho dữ liệu
- Thay thế `[InlineData]` bằng `[Arguments]`
- Thay thế `[MemberData]` bằng `[MethodData]`
- Thay thế `Assert.Equal` bằng `await Assert.That(actual).IsEqualTo(expected)`
- Thay thế `Assert.True` bằng `await Assert.That(condition).IsTrue()`
- Thay thế `Assert.Throws<T>` bằng `await Assert.That(action).Throws<T>()`
- Thay thế constructor/IDisposable bằng `[Before(Test)]`/`[After(Test)]`
- Thay thế `IClassFixture<T>` bằng `[Before(Class)]`/`[After(Class)]`

**Tại sao chọn TUnit thay vì xUnit?**

TUnit cung cấp trải nghiệm kiểm thử hiện đại, nhanh chóng và linh hoạt với các tính năng nâng cao không có trong xUnit, chẳng hạn như khẳng định bất đồng bộ, các hook vòng đời tinh vi hơn và khả năng kiểm thử theo hướng dữ liệu được cải thiện. Các khẳng định fluent của TUnit cung cấp khả năng xác thực kiểm thử rõ ràng và biểu cảm hơn, làm cho nó đặc biệt phù hợp cho các dự án
