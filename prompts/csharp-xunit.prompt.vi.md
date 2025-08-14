---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "Nhận các phương pháp hay nhất cho unit testing XUnit, bao gồm cả các bài test theo hướng dữ liệu"
---

# Các phương pháp hay nhất cho XUnit

Mục tiêu của bạn là giúp tôi viết các unit test hiệu quả với XUnit, bao gồm cả các phương pháp kiểm thử tiêu chuẩn và kiểm thử theo hướng dữ liệu.

## Thiết lập dự án

- Sử dụng một dự án test riêng biệt với quy ước đặt tên `[TênDựÁn].Tests`
- Tham chiếu đến các gói Microsoft.NET.Test.Sdk, xunit, và xunit.runner.visualstudio
- Tạo các lớp test tương ứng với các lớp đang được kiểm thử (ví dụ: `CalculatorTests` cho `Calculator`)
- Sử dụng các lệnh test của .NET SDK: `dotnet test` để chạy các bài test

## Cấu trúc Test

- Không yêu cầu thuộc tính cho lớp test (không giống như MSTest/NUnit)
- Sử dụng các bài test dựa trên fact với thuộc tính `[Fact]` cho các bài test đơn giản
- Tuân theo mẫu Arrange-Act-Assert (AAA)
- Đặt tên các bài test theo mẫu `TênPhươngThức_KịchBản_HànhViMongMuốn`
- Sử dụng constructor để thiết lập (setup) và `IDisposable.Dispose()` để dọn dẹp (teardown)
- Sử dụng `IClassFixture<T>` cho ngữ cảnh được chia sẻ giữa các bài test trong một lớp
- Sử dụng `ICollectionFixture<T>` cho ngữ cảnh được chia sẻ giữa nhiều lớp test

## Các bài test tiêu chuẩn

- Giữ cho các bài test tập trung vào một hành vi duy nhất
- Tránh kiểm thử nhiều hành vi trong một phương thức test
- Sử dụng các khẳng định (assertion) rõ ràng thể hiện ý định
- Chỉ bao gồm các khẳng định cần thiết để xác minh trường hợp test
- Làm cho các bài test độc lập và không thay đổi trạng thái (idempotent - có thể chạy theo bất kỳ thứ tự nào)
- Tránh sự phụ thuộc lẫn nhau giữa các bài test

## Các bài test theo hướng dữ liệu (Data-Driven Tests)

- Sử dụng `[Theory]` kết hợp với các thuộc tính nguồn dữ liệu
- Sử dụng `[InlineData]` cho dữ liệu test nội tuyến
- Sử dụng `[MemberData]` cho dữ liệu test dựa trên phương thức
- Sử dụng `[ClassData]` cho dữ liệu test dựa trên lớp
- Tạo các thuộc tính dữ liệu tùy chỉnh bằng cách triển khai `DataAttribute`
- Sử dụng tên tham số có ý nghĩa trong các bài test theo hướng dữ liệu

## Khẳng định (Assertions)

- Sử dụng `Assert.Equal` để so sánh bằng giá trị
- Sử dụng `Assert.Same` để so sánh bằng tham chiếu
- Sử dụng `Assert.True`/`Assert.False` cho các điều kiện boolean
- Sử dụng `Assert.Contains`/`Assert.DoesNotContain` cho các tập hợp (collection)
- Sử dụng `Assert.Matches`/`Assert.DoesNotMatch` để khớp mẫu regex
- Sử dụng `Assert.Throws<T>` hoặc `await Assert.ThrowsAsync<T>` để kiểm tra ngoại lệ
- Sử dụng thư viện fluent assertions để có các khẳng định dễ đọc hơn

## Mocking và Cô lập (Isolation)

- Cân nhắc sử dụng Moq hoặc NSubstitute cùng với XUnit
- Mock các phụ thuộc để cô lập các đơn vị đang được kiểm thử
- Sử dụng interface để tạo điều kiện thuận lợi cho việc mocking
- Cân nhắc sử dụng DI container cho các thiết lập test phức tạp

## Tổ chức Test

- Nhóm các bài test theo tính năng hoặc thành phần
- Sử dụng `[Trait("Category", "TênDanhMục")]` để phân loại
- Sử dụng collection fixtures để nhóm các bài test có chung các phụ thuộc
- Cân nhắc sử dụng output helpers (`ITestOutputHelper`) để chẩn đoán test
- Bỏ qua các bài test có điều kiện với `Skip = "lý do"` trong các thuộc tính
