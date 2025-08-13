# Thực hành tốt nhất với NUnit

Mục tiêu của bạn là giúp tôi viết các bài kiểm thử đơn vị hiệu quả với NUnit, bao gồm cả cách tiếp cận kiểm thử tiêu chuẩn và kiểm thử dựa trên dữ liệu.

## Thiết lập dự án

- Sử dụng một dự án kiểm thử riêng với quy tắc đặt tên `[ProjectName].Tests`
- Tham chiếu các gói Microsoft.NET.Test.Sdk, NUnit và NUnit3TestAdapter
- Tạo các lớp kiểm thử tương ứng với các lớp được kiểm thử (ví dụ: `CalculatorTests` cho `Calculator`)
- Sử dụng lệnh test của .NET SDK: `dotnet test` để chạy kiểm thử

## Cấu trúc kiểm thử

- Áp dụng thuộc tính `[TestFixture]` cho các lớp kiểm thử
- Sử dụng thuộc tính `[Test]` cho các phương thức kiểm thử
- Tuân thủ mô hình Arrange-Act-Assert (AAA)
- Đặt tên kiểm thử theo mẫu `MethodName_Scenario_ExpectedBehavior`
- Sử dụng `[SetUp]` và `[TearDown]` cho thiết lập và dọn dẹp mỗi kiểm thử
- Sử dụng `[OneTimeSetUp]` và `[OneTimeTearDown]` cho thiết lập và dọn dẹp mỗi lớp
- Sử dụng `[SetUpFixture]` cho thiết lập và dọn dẹp ở cấp độ assembly

## Kiểm thử tiêu chuẩn

- Tập trung kiểm thử một hành vi duy nhất
- Tránh kiểm thử nhiều hành vi trong cùng một phương thức
- Sử dụng các câu lệnh assert rõ ràng để thể hiện ý định
- Chỉ bao gồm các assert cần thiết để xác minh trường hợp kiểm thử
- Đảm bảo các kiểm thử độc lập và idempotent (có thể chạy theo bất kỳ thứ tự nào)
- Tránh sự phụ thuộc giữa các kiểm thử

## Kiểm thử dựa trên dữ liệu

- Sử dụng `[TestCase]` cho dữ liệu kiểm thử inline
- Sử dụng `[TestCaseSource]` cho dữ liệu kiểm thử được tạo động
- Sử dụng `[Values]` cho các kết hợp tham số đơn giản
- Sử dụng `[ValueSource]` cho dữ liệu từ property hoặc phương thức
- Sử dụng `[Random]` cho giá trị kiểm thử ngẫu nhiên
- Sử dụng `[Range]` cho giá trị kiểm thử dạng chuỗi số
- Sử dụng `[Combinatorial]` hoặc `[Pairwise]` để kết hợp nhiều tham số

## Assertions

- Sử dụng `Assert.That` với mô hình constraint (phong cách ưu tiên của NUnit)
- Sử dụng các constraint như `Is.EqualTo`, `Is.SameAs`, `Contains.Item`
- Sử dụng `Assert.AreEqual` cho so sánh giá trị đơn giản (phong cách cổ điển)
- Sử dụng `CollectionAssert` cho so sánh tập hợp
- Sử dụng `StringAssert` cho các assert đặc thù chuỗi
- Sử dụng `Assert.Throws<T>` hoặc `Assert.ThrowsAsync<T>` để kiểm thử ngoại lệ
- Sử dụng thông điệp mô tả trong assert để rõ ràng khi thất bại

## Mocking và Isolation

- Cân nhắc sử dụng Moq hoặc NSubstitute cùng NUnit
- Mock các dependency để cô lập unit được kiểm thử
- Sử dụng interface để dễ dàng mock
- Cân nhắc sử dụng container DI cho các thiết lập kiểm thử phức tạp

## Tổ chức kiểm thử

- Nhóm kiểm thử theo tính năng hoặc thành phần
- Sử dụng category với `[Category("CategoryName")]`
- Sử dụng `[Order]` để điều khiển thứ tự chạy kiểm thử khi cần thiết
- Sử dụng `[Author("DeveloperName")]` để chỉ định người phụ trách
- Sử dụng `[Description]` để cung cấp thông tin bổ sung về kiểm thử
- Cân nhắc `[Explicit]` cho các kiểm thử không nên chạy tự động
- Sử dụng `[Ignore("Reason")]` để tạm thời bỏ qua kiểm thử
