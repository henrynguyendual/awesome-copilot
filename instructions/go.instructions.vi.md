---
description: "Hướng dẫn viết mã Go theo các thực hành Go thành ngữ và tiêu chuẩn cộng đồng"
applyTo: "**/*.go,**/go.mod,**/go.sum"
---

# Hướng dẫn Phát triển Go

Tuân thủ các thực hành Go thành ngữ (idiomatic) và tiêu chuẩn cộng đồng khi viết mã Go. Các hướng dẫn này dựa trên [Effective Go](https://go.dev/doc/effective_go), [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments), và [Hướng dẫn Phong cách Go của Google](https://google.github.io/styleguide/go/).

## Hướng dẫn Chung

- Viết mã Go đơn giản, rõ ràng và thành ngữ
- Ưu tiên sự rõ ràng và đơn giản hơn là sự thông minh
- Tuân theo nguyên tắc ít gây ngạc nhiên nhất (principle of least surprise)
- Giữ luồng xử lý chính (happy path) thẳng hàng bên trái (giảm thiểu thụt lề)
- Trả về sớm để giảm lồng nhau
- Làm cho giá trị zero (zero value) trở nên hữu ích
- Viết tài liệu cho các kiểu, hàm, phương thức và gói được xuất (exported)
- Sử dụng Go modules để quản lý phụ thuộc

## Quy ước Đặt tên

### Gói (Packages)

- Sử dụng tên gói bằng chữ thường, một từ
- Tránh dấu gạch dưới, dấu gạch nối hoặc chữ hoa hỗn hợp (mixedCaps)
- Chọn tên mô tả những gì gói cung cấp, không phải những gì nó chứa
- Tránh các tên chung chung như `util`, `common`, hoặc `base`
- Tên gói nên ở dạng số ít, không phải số nhiều

### Biến và Hàm

- Sử dụng mixedCaps hoặc MixedCaps (camelCase) thay vì dấu gạch dưới
- Giữ tên ngắn gọn nhưng mang tính mô tả
- Chỉ sử dụng biến một chữ cái cho phạm vi rất ngắn (như chỉ số vòng lặp)
- Tên được xuất (exported) bắt đầu bằng chữ hoa
- Tên không được xuất (unexported) bắt đầu bằng chữ thường
- Tránh lặp từ (ví dụ: tránh `http.HTTPServer`, ưu tiên `http.Server`)

### Interfaces

- Đặt tên interface với hậu tố -er khi có thể (ví dụ: `Reader`, `Writer`, `Formatter`)
- Interface có một phương thức nên được đặt tên theo phương thức đó (ví dụ: `Read` → `Reader`)
- Giữ cho interface nhỏ và tập trung

### Hằng số

- Sử dụng MixedCaps cho hằng số được xuất
- Sử dụng mixedCaps cho hằng số không được xuất
- Nhóm các hằng số liên quan bằng khối `const`
- Cân nhắc sử dụng hằng số có kiểu để an toàn kiểu tốt hơn

## Phong cách và Định dạng Code

### Định dạng

- Luôn sử dụng `gofmt` để định dạng mã
- Sử dụng `goimports` để quản lý import tự động
- Giữ độ dài dòng hợp lý (không có giới hạn cứng, nhưng hãy xem xét khả năng đọc)
- Thêm dòng trống để tách các nhóm mã logic

### Bình luận (Comments)

- Viết bình luận bằng câu hoàn chỉnh
- Bắt đầu câu với tên của đối tượng đang được mô tả
- Bình luận gói nên bắt đầu bằng "Package [tên]"
- Sử dụng bình luận dòng (`//`) cho hầu hết các bình luận
- Sử dụng bình luận khối (`/* */`) một cách tiết kiệm, chủ yếu cho tài liệu gói
- Ghi lại lý do (why), không phải cái gì (what), trừ khi cái gì đó phức tạp

### Xử lý Lỗi

- Kiểm tra lỗi ngay sau khi gọi hàm
- Đừng bỏ qua lỗi bằng `_` trừ khi bạn có lý do chính đáng (ghi lại lý do)
- Bọc lỗi với ngữ cảnh bằng `fmt.Errorf` với động từ `%w`
- Tạo các kiểu lỗi tùy chỉnh khi bạn cần kiểm tra các lỗi cụ thể
- Đặt giá trị trả về lỗi làm giá trị trả về cuối cùng
- Đặt tên biến lỗi là `err`
- Giữ thông báo lỗi bằng chữ thường và không kết thúc bằng dấu câu

## Kiến trúc và Cấu trúc Dự án

### Tổ chức Gói

- Tuân theo các quy ước bố cục dự án Go tiêu chuẩn
- Giữ các gói `main` trong thư mục `cmd/`
- Đặt các gói có thể tái sử dụng trong `pkg/` hoặc `internal/`
- Sử dụng `internal/` cho các gói không nên được import bởi các dự án bên ngoài
- Nhóm các chức năng liên quan vào các gói
- Tránh phụ thuộc vòng tròn (circular dependencies)

### Quản lý Phụ thuộc

- Sử dụng Go modules (`go.mod` và `go.sum`)
- Giữ số lượng phụ thuộc ở mức tối thiểu
- Thường xuyên cập nhật các phụ thuộc để có các bản vá bảo mật
- Sử dụng `go mod tidy` để dọn dẹp các phụ thuộc không sử dụng
- Chỉ vendor các phụ thuộc khi cần thiết

## An toàn Kiểu và Tính năng Ngôn ngữ

### Định nghĩa Kiểu

- Định nghĩa các kiểu để thêm ý nghĩa và an toàn kiểu
- Sử dụng struct tags cho các ánh xạ JSON, XML, cơ sở dữ liệu
- Ưu tiên chuyển đổi kiểu tường minh
- Sử dụng type assertion cẩn thận và kiểm tra giá trị trả về thứ hai

### Con trỏ và Giá trị (Pointers vs Values)

- Sử dụng con trỏ cho các struct lớn hoặc khi bạn cần sửa đổi receiver
- Sử dụng giá trị cho các struct nhỏ và khi mong muốn tính bất biến (immutability)
- Nhất quán trong tập hợp phương thức của một kiểu
- Xem xét giá trị zero khi chọn receiver là con trỏ hay giá trị

### Interfaces và Composition

- Chấp nhận interface, trả về kiểu cụ thể
- Giữ interface nhỏ (lý tưởng là 1-3 phương thức)
- Sử dụng embedding cho composition
- Định nghĩa interface gần nơi chúng được sử dụng, không phải nơi chúng được triển khai
- Đừng xuất (export) interface trừ khi cần thiết

## Lập trình Đồng thời (Concurrency)

### Goroutines

- Đừng tạo goroutine trong thư viện; hãy để người gọi kiểm soát sự đồng thời
- Luôn biết một goroutine sẽ kết thúc như thế nào
- Sử dụng `sync.WaitGroup` hoặc channel để đợi goroutine
- Tránh rò rỉ goroutine bằng cách đảm bảo dọn dẹp

### Channels

- Sử dụng channel để giao tiếp giữa các goroutine
- Đừng giao tiếp bằng cách chia sẻ bộ nhớ; hãy chia sẻ bộ nhớ bằng cách giao tiếp
- Đóng channel từ phía người gửi, không phải người nhận
- Sử dụng channel có bộ đệm (buffered channels) khi bạn biết dung lượng
- Sử dụng `select` cho các hoạt động không chặn (non-blocking)

### Đồng bộ hóa

- Sử dụng `sync.Mutex` để bảo vệ trạng thái được chia sẻ
- Giữ các vùng tranh chấp (critical sections) nhỏ
- Sử dụng `sync.RWMutex` khi bạn có nhiều người đọc
- Ưu tiên channel hơn mutex khi có thể
- Sử dụng `sync.Once` để khởi tạo một lần

## Các Mẫu Xử lý Lỗi

### Tạo Lỗi

- Sử dụng `errors.New` cho các lỗi tĩnh đơn giản
- Sử dụng `fmt.Errorf` cho các lỗi động
- Tạo các kiểu lỗi tùy chỉnh cho các lỗi cụ thể của miền (domain-specific)
- Xuất các biến lỗi cho các lỗi sentinel
- Sử dụng `errors.Is` và `errors.As` để kiểm tra lỗi

### Lan truyền Lỗi

- Thêm ngữ cảnh khi lan truyền lỗi lên ngăn xếp cuộc gọi (call stack)
- Đừng vừa ghi log vừa trả về lỗi (chọn một)
- Xử lý lỗi ở cấp độ phù hợp
- Cân nhắc sử dụng lỗi có cấu trúc để gỡ lỗi tốt hơn

## Thiết kế API

### Trình xử lý HTTP (HTTP Handlers)

- Sử dụng `http.HandlerFunc` cho các trình xử lý đơn giản
- Triển khai `http.Handler` cho các trình xử lý cần trạng thái
- Sử dụng middleware cho các mối quan tâm xuyên suốt (cross-cutting concerns)
- Đặt mã trạng thái (status codes) và header phù hợp
- Xử lý lỗi một cách duyên dáng và trả về các phản hồi lỗi phù hợp

### API JSON

- Sử dụng struct tags để kiểm soát việc chuyển đổi JSON (marshaling)
- Xác thực dữ liệu đầu vào
- Sử dụng con trỏ cho các trường tùy chọn (optional)
- Cân nhắc sử dụng `json.RawMessage` để phân tích cú pháp trì hoãn
- Xử lý lỗi JSON một cách thích hợp

## Tối ưu hóa Hiệu năng

### Quản lý Bộ nhớ

- Giảm thiểu việc cấp phát bộ nhớ trong các đường dẫn nóng (hot paths)
- Tái sử dụng đối tượng khi có thể (xem xét `sync.Pool`)
- Sử dụng value receiver cho các struct nhỏ
- Cấp phát trước slice khi biết kích thước
- Tránh chuyển đổi chuỗi không cần thiết

### Hồ sơ hóa (Profiling)

- Sử dụng các công cụ profiling tích hợp (`pprof`)
- Đo điểm chuẩn (benchmark) các đường dẫn mã quan trọng
- Profiling trước khi tối ưu hóa
- Tập trung vào các cải tiến thuật toán trước tiên
- Cân nhắc sử dụng `testing.B` cho các benchmark

## Kiểm thử (Testing)

### Tổ chức Test

- Giữ các test trong cùng một gói (kiểm thử hộp trắng)
- Sử dụng hậu tố gói `_test` cho kiểm thử hộp đen
- Đặt tên tệp test với hậu tố `_test.go`
- Đặt tệp test bên cạnh mã mà chúng kiểm thử

### Viết Test

- Sử dụng kiểm thử theo bảng (table-driven tests) cho nhiều trường hợp kiểm thử
- Đặt tên test một cách mô tả bằng cách sử dụng `Test_functionName_scenario`
- Sử dụng các subtest với `t.Run` để tổ chức tốt hơn
- Kiểm thử cả trường hợp thành công và thất bại
- Sử dụng các thư viện như `testify` một cách tiết kiệm

### Hàm hỗ trợ Test

- Đánh dấu các hàm trợ giúp bằng `t.Helper()`
- Tạo các test fixture cho việc thiết lập phức tạp
- Sử dụng interface `testing.TB` cho các hàm được sử dụng trong cả test và benchmark
- Dọn dẹp tài nguyên bằng `t.Cleanup()`

## Các Thực hành Bảo mật Tốt nhất

### Xác thực Đầu vào

- Xác thực tất cả đầu vào từ bên ngoài
- Sử dụng kiểu mạnh để ngăn chặn các trạng thái không hợp lệ
- Làm sạch dữ liệu trước khi sử dụng trong các truy vấn SQL
- Cẩn thận với đường dẫn tệp từ đầu vào của người dùng
- Xác thực và thoát dữ liệu cho các ngữ cảnh khác nhau (HTML, SQL, shell)

### Mật mã học

- Sử dụng các gói crypto của thư viện chuẩn
- Đừng tự triển khai mật mã của riêng bạn
- Sử dụng crypto/rand để tạo số ngẫu nhiên
- Lưu trữ mật khẩu bằng bcrypt hoặc tương tự
- Sử dụng TLS cho giao tiếp mạng

## Tài liệu

### Tài liệu trong Code

- Ghi tài liệu cho tất cả các ký hiệu được xuất (exported)
- Bắt đầu tài liệu với tên của ký hiệu
- Sử dụng ví dụ trong tài liệu khi hữu ích
- Giữ tài liệu gần với mã
- Cập nhật tài liệu khi mã thay đổi

### Tệp README và Tài liệu

- Bao gồm hướng dẫn cài đặt rõ ràng
- Ghi lại các phụ thuộc và yêu cầu
- Cung cấp ví dụ sử dụng
- Ghi lại các tùy chọn cấu hình
- Bao gồm phần khắc phục sự cố

## Công cụ và Quy trình Phát triển

### Các Công cụ Thiết yếu

- `go fmt`: Định dạng mã
- `go vet`: Tìm các cấu trúc đáng ngờ
- `golint` hoặc `golangci-lint`: Linting bổ sung
- `go test`: Chạy test
- `go mod`: Quản lý phụ thuộc
- `go generate`: Tạo mã

### Thực hành Phát triển

- Chạy test trước khi commit
- Sử dụng pre-commit hooks để định dạng và linting
- Giữ các commit tập trung và nguyên tử
- Viết thông điệp commit có ý nghĩa
- Xem lại các thay đổi (diffs) trước khi commit

## Những Cạm bẫy Thường gặp cần Tránh

- Không kiểm tra lỗi
- Bỏ qua các điều kiện tranh chấp (race conditions)
- Tạo ra rò rỉ goroutine
- Không sử dụng defer để dọn dẹp
- Sửa đổi map đồng thời
- Không hiểu sự khác biệt giữa interface nil và con trỏ nil
- Quên đóng tài nguyên (tệp, kết nối)
- Sử dụng biến toàn cục không cần thiết
- Lạm dụng interface rỗng (`interface{}`)
- Không xem xét giá trị zero của
