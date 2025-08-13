# Thực hành tốt nhất với MSTest

Mục tiêu của bạn là giúp tôi viết các bài kiểm thử đơn vị hiệu quả với MSTest, bao gồm cả cách tiếp cận kiểm thử tiêu chuẩn và kiểm thử dựa trên dữ liệu.

## Thiết lập dự án

- Sử dụng một dự án kiểm thử riêng với quy tắc đặt tên `[ProjectName].Tests`
- Tham chiếu gói MSTest
- Tạo các lớp kiểm thử tương ứng với các lớp được kiểm thử (ví dụ: `CalculatorTests` cho `Calculator`)
- Sử dụng lệnh test của .NET SDK: `dotnet test` để chạy kiểm thử

## Cấu trúc kiểm thử

- Sử dụng thuộc tính `[TestClass]` cho các lớp kiểm thử
- Sử dụng thuộc tính `[TestMethod]` cho các phương thức kiểm thử
- Tuân thủ mô hình Arrange-Act-Assert (AAA)
- Đặt tên kiểm thử theo mẫu `MethodName_Scenario_ExpectedBehavior`
- Sử dụng `[TestInitialize]` và `[TestCleanup]` cho thiết lập và dọn dẹp mỗi kiểm thử
- Sử dụng `[ClassInitialize]` và `[ClassCleanup]` cho thiết lập và dọn dẹp mỗi lớp
- Sử dụng `[AssemblyInitialize]` và `[AssemblyCleanup]` cho thiết lập và dọn dẹp ở cấp độ assembly

## Kiểm thử tiêu chuẩn

- Tập trung kiểm thử một hành vi duy nhất
- Tránh kiểm thử nhiều hành vi trong cùng một phương thức
- Sử dụng các câu lệnh assert rõ ràng để thể hiện ý định
- Chỉ bao gồm các assert cần thiết để xác minh trường hợp kiểm thử
- Đảm bảo các kiểm thử độc lập và idempotent (có thể chạy theo bất kỳ thứ tự nào)
- Tránh sự phụ thuộc giữa các kiểm thử

## Kiểm thử dựa trên dữ liệu

- Sử dụng `[TestMethod]` kết hợp với các thuộc tính nguồn dữ liệu
- Sử dụng `[DataRow]` cho dữ liệu kiểm thử inline
- Sử dụng `[DynamicData]` cho dữ liệu kiểm thử được tạo động
- Sử dụng `[TestProperty]` để thêm metadata vào kiểm thử
- Đặt tên tham số có ý nghĩa trong các kiểm thử dựa trên dữ liệu

## Assertions

- Sử dụng `Assert.AreEqual` để kiểm tra bằng giá trị
- Sử dụng `Assert.AreSame` để kiểm tra bằng tham chiếu
- Sử dụng `Assert.IsTrue`/`Assert.IsFalse` cho điều kiện boolean
- Sử dụng `CollectionAssert` cho so sánh tập hợp
- Sử dụng `StringAssert` cho các assert đặc thù chuỗi
- Sử dụng `Assert.Throws<T>` để kiểm thử ngoại lệ
- Đảm bảo các assert đơn giản và có thông điệp rõ ràng khi thất bại

## Mocking và Isolation

- Cân nhắc sử dụng Moq hoặc NSubstitute cùng MSTest
- Mock các dependency để cô lập unit được kiểm thử
- Sử dụng interface để dễ dàng mock
- Cân nhắc sử dụng container DI cho các thiết lập kiểm thử phức tạp

## Tổ chức kiểm thử

- Nhóm kiểm thử theo tính năng hoặc thành phần
- Sử dụng category cho kiểm thử với `[TestCategory("Category")]`
- Sử dụng độ ưu tiên với `[Priority(1)]` cho các kiểm thử quan trọng
- Sử dụng `[Owner("DeveloperName")]` để chỉ định người phụ trách
