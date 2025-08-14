---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "Nhận các phương pháp hay nhất để kiểm thử đơn vị NUnit, bao gồm cả các kiểm thử dựa trên dữ liệu"
---

# Các phương pháp hay nhất cho NUnit

Mục tiêu của bạn là giúp tôi viết các bài kiểm thử đơn vị hiệu quả với NUnit, bao gồm cả các phương pháp kiểm thử tiêu chuẩn và dựa trên dữ liệu.

## Thiết lập dự án

- Sử dụng một dự án kiểm thử riêng biệt với quy ước đặt tên `[TênDựÁn].Tests`
- Tham chiếu đến các gói Microsoft.NET.Test.Sdk, NUnit, và NUnit3TestAdapter
- Tạo các lớp kiểm thử khớp với các lớp đang được kiểm thử (ví dụ: `CalculatorTests` cho `Calculator`)
- Sử dụng các lệnh kiểm thử của .NET SDK: `dotnet test` để chạy các bài kiểm thử

## Cấu trúc bài kiểm thử

- Áp dụng thuộc tính `[TestFixture]` cho các lớp kiểm thử
- Sử dụng thuộc tính `[Test]` cho các phương thức kiểm thử
- Tuân theo mẫu Arrange-Act-Assert (AAA)
- Đặt tên các bài kiểm thử theo mẫu `TênPhươngThức_KịchBản_HànhViMongĐợi`
- Sử dụng `[SetUp]` và `[TearDown]` để thiết lập và dọn dẹp cho mỗi bài kiểm thử
- Sử dụng `[OneTimeSetUp]` và `[OneTimeTearDown]` để thiết lập và dọn dẹp cho mỗi lớp
- Sử dụng `[SetUpFixture]` để thiết lập và dọn dẹp ở cấp độ assembly

## Các bài kiểm thử tiêu chuẩn

- Giữ cho các bài kiểm thử tập trung vào một hành vi duy nhất
- Tránh kiểm thử nhiều hành vi trong một phương thức kiểm thử
- Sử dụng các khẳng định (assertion) rõ ràng để thể hiện ý định
- Chỉ bao gồm các khẳng định cần thiết để xác minh trường hợp kiểm thử
- Làm cho các bài kiểm thử độc lập và không thay đổi trạng thái (có thể chạy theo bất kỳ thứ tự nào)
- Tránh sự phụ thuộc lẫn nhau giữa các bài kiểm thử

## Các bài kiểm thử dựa trên dữ liệu (Data-Driven Tests)

- Sử dụng `[TestCase]` cho dữ liệu kiểm thử nội tuyến
- Sử dụng `[TestCaseSource]` cho dữ liệu kiểm thử được tạo theo chương trình
- Sử dụng `[Values]` cho các kết hợp tham số đơn giản
- Sử dụng `[ValueSource]` cho các nguồn dữ liệu dựa trên thuộc tính hoặc phương thức
- Sử dụng `[Random]` cho các giá trị kiểm thử số ngẫu nhiên
- Sử dụng `[Range]` cho các giá trị kiểm thử số tuần tự
- Sử dụng `[Combinatorial]` hoặc `[Pairwise]` để kết hợp nhiều tham số

## Khẳng định (Assertions)

- Sử dụng `Assert.That` với mô hình ràng buộc (constraint model) (kiểu NUnit được ưa thích)
- Sử dụng các ràng buộc như `Is.EqualTo`, `Is.SameAs`, `Contains.Item`
- Sử dụng `Assert.AreEqual` để so sánh giá trị đơn giản (kiểu cổ điển)
- Sử dụng `CollectionAssert` để so sánh các tập hợp
- Sử dụng `StringAssert` cho các khẳng định dành riêng cho chuỗi
- Sử dụng `Assert.Throws<T>` hoặc `Assert.ThrowsAsync<T>` để kiểm thử các ngoại lệ
- Sử dụng các thông báo mô tả trong các khẳng định để làm rõ khi thất bại

## Mocking và Cô lập

- Cân nhắc sử dụng Moq hoặc NSubstitute cùng với NUnit
- Mock các phụ thuộc để cô lập các đơn vị đang được kiểm thử
- Sử dụng interface để tạo điều kiện thuận lợi cho việc mocking
- Cân nhắc sử dụng một DI container cho các thiết lập kiểm thử phức tạp

## Tổ chức bài kiểm thử

- Nhóm các bài kiểm thử theo tính năng hoặc thành phần
- Sử dụng các danh mục với `[Category("TênDanhMục")]`
- Sử dụng `[Order]` để kiểm soát thứ tự thực thi bài kiểm thử khi cần thiết
- Sử dụng `[Author("TênLậpTrìnhViên")]` để chỉ định quyền sở hữu
- Sử dụng `[Description]` để cung cấp thông tin bổ sung cho bài kiểm thử
- Cân nhắc `[Explicit]` cho các bài kiểm thử không nên chạy tự động
- Sử dụng `[Ignore("LýDo")]` để tạm thời bỏ qua
