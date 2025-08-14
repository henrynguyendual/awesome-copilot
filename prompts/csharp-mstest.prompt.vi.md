---
mode: "agent"
tools: ["changes", "codebase", "editFiles", "problems", "search"]
description: "Nhận các phương pháp hay nhất cho unit test MSTest, bao gồm cả các bài kiểm thử theo hướng dữ liệu"
---

# Các phương pháp hay nhất cho MSTest

Mục tiêu của bạn là giúp tôi viết các unit test hiệu quả với MSTest, bao gồm cả các phương pháp kiểm thử tiêu chuẩn và kiểm thử theo hướng dữ liệu.

## Thiết lập dự án

- Sử dụng một dự án kiểm thử riêng biệt với quy ước đặt tên `[TênDựÁn].Tests`
- Tham chiếu đến gói MSTest
- Tạo các lớp kiểm thử khớp với các lớp đang được kiểm thử (ví dụ: `CalculatorTests` cho `Calculator`)
- Sử dụng các lệnh kiểm thử của .NET SDK: `dotnet test` để chạy các bài kiểm thử

## Cấu trúc bài kiểm thử

- Sử dụng thuộc tính `[TestClass]` cho các lớp kiểm thử
- Sử dụng thuộc tính `[TestMethod]` cho các phương thức kiểm thử
- Tuân theo mẫu Arrange-Act-Assert (AAA)
- Đặt tên các bài kiểm thử theo mẫu `TênPhươngThức_KịchBản_HànhViMongĐợi`
- Sử dụng `[TestInitialize]` và `[TestCleanup]` để thiết lập và dọn dẹp cho mỗi bài kiểm thử
- Sử dụng `[ClassInitialize]` và `[ClassCleanup]` để thiết lập và dọn dẹp cho mỗi lớp
- Sử dụng `[AssemblyInitialize]` và `[AssemblyCleanup]` để thiết lập và dọn dẹp ở cấp độ assembly

## Các bài kiểm thử tiêu chuẩn

- Giữ cho các bài kiểm thử tập trung vào một hành vi duy nhất
- Tránh kiểm thử nhiều hành vi trong một phương thức kiểm thử
- Sử dụng các khẳng định (assertion) rõ ràng thể hiện ý định
- Chỉ bao gồm các khẳng định cần thiết để xác minh trường hợp kiểm thử
- Làm cho các bài kiểm thử độc lập và có tính lũy đẳng (có thể chạy theo bất kỳ thứ tự nào)
- Tránh sự phụ thuộc lẫn nhau giữa các bài kiểm thử

## Các bài kiểm thử theo hướng dữ liệu (Data-Driven Tests)

- Sử dụng `[TestMethod]` kết hợp với các thuộc tính nguồn dữ liệu
- Sử dụng `[DataRow]` cho dữ liệu kiểm thử nội tuyến (inline)
- Sử dụng `[DynamicData]` cho dữ liệu kiểm thử được tạo theo chương trình
- Sử dụng `[TestProperty]` để thêm siêu dữ liệu vào các bài kiểm thử
- Sử dụng tên tham số có ý nghĩa trong các bài kiểm thử theo hướng dữ liệu

## Khẳng định (Assertions)

- Sử dụng `Assert.AreEqual` để so sánh bằng giá trị
- Sử dụng `Assert.AreSame` để so sánh bằng tham chiếu
- Sử dụng `Assert.IsTrue`/`Assert.IsFalse` cho các điều kiện boolean
- Sử dụng `CollectionAssert` để so sánh các tập hợp (collection)
- Sử dụng `StringAssert` cho các khẳng định dành riêng cho chuỗi
- Sử dụng `Assert.Throws<T>` để kiểm thử ngoại lệ (exception)
- Đảm bảo các khẳng định có bản chất đơn giản và cung cấp thông báo để làm rõ khi thất bại

## Mocking và Cô lập (Isolation)

- Cân nhắc sử dụng Moq hoặc NSubstitute cùng với MSTest
- Mock các phụ thuộc để cô lập các đơn vị đang được kiểm thử
- Sử dụng interface để tạo điều kiện thuận lợi cho việc mocking
- Cân nhắc sử dụng DI container cho các thiết lập kiểm thử phức tạp

## Tổ chức bài kiểm thử

- Nhóm các bài kiểm thử theo tính năng hoặc thành phần
- Sử dụng các danh mục kiểm thử với `[TestCategory("TênDanhMục")]`
- Sử dụng mức độ ưu tiên của bài kiểm thử với `[Priority(1)]` cho các bài kiểm thử quan trọng
- Sử dụng `[Owner("TênLậpTrìnhViên")]` để chỉ định quyền
