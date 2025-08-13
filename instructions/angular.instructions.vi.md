---
description: "Các tiêu chuẩn và thực hành tốt nhất khi lập trình dành riêng cho Angular"
applyTo: "**/*.ts, **/*.html, **/*.scss, **/*.css"
---

# Hướng dẫn Phát triển Angular

Hướng dẫn tạo các ứng dụng Angular chất lượng cao với TypeScript, sử dụng Angular Signals để quản lý trạng thái, tuân thủ các thực hành tốt nhất của Angular như được nêu tại https://angular.dev.

## Bối cảnh Dự án

- Phiên bản Angular mới nhất (sử dụng component độc lập theo mặc định)
- TypeScript để đảm bảo an toàn kiểu dữ liệu
- Angular CLI để thiết lập và khởi tạo dự án
- Tuân thủ Hướng dẫn Phong cách Angular (https://angular.dev/style-guide)
- Sử dụng Angular Material hoặc các thư viện UI hiện đại khác để có phong cách nhất quán (nếu được chỉ định)

## Tiêu chuẩn Phát triển

### Kiến trúc

- Sử dụng component độc lập (standalone components) trừ khi module được yêu cầu rõ ràng
- Tổ chức mã nguồn theo các module tính năng hoặc theo lĩnh vực để dễ dàng mở rộng
- Triển khai tải lười (lazy loading) cho các module tính năng để tối ưu hóa hiệu suất
- Sử dụng hiệu quả hệ thống dependency injection tích hợp sẵn của Angular
- Cấu trúc các component với sự phân tách rõ ràng về chức năng (component thông minh và component trình bày)

### TypeScript

- Bật chế độ nghiêm ngặt (strict mode) trong `tsconfig.json` để đảm bảo an toàn kiểu dữ liệu
- Định nghĩa các interface và type rõ ràng cho component, service và model
- Sử dụng type guards và union types để kiểm tra kiểu dữ liệu một cách mạnh mẽ
- Triển khai xử lý lỗi đúng cách với các toán tử RxJS (ví dụ: `catchError`)
- Sử dụng các form có kiểu dữ liệu (ví dụ: `FormGroup`, `FormControl`) cho reactive forms

### Thiết kế Component

- Tuân thủ các thực hành tốt nhất về vòng đời hook của component trong Angular
- Khi sử dụng Angular >= 19, sử dụng các hàm `input()`, `output()`, `viewChild()`, `viewChildren()`, `contentChild()` và `contentChildren()` thay vì decorator; nếu không thì sử dụng decorator
- Tận dụng chiến lược phát hiện thay đổi của Angular (mặc định hoặc `OnPush` để tăng hiệu suất)
- Giữ cho template sạch sẽ và logic nằm trong các lớp component hoặc service
- Sử dụng các directive và pipe của Angular cho các chức năng có thể tái sử dụng

### Định dạng Giao diện (Styling)

- Sử dụng cơ chế đóng gói CSS ở cấp component của Angular (mặc định: ViewEncapsulation.Emulated)
- Ưu tiên sử dụng SCSS để tạo kiểu với chủ đề (theming) nhất quán
- Triển khai thiết kế đáp ứng (responsive design) bằng CSS Grid, Flexbox, hoặc các tiện ích Layout của Angular CDK
- Tuân thủ hướng dẫn về chủ đề của Angular Material nếu sử dụng
- Duy trì khả năng truy cập (a11y) với các thuộc tính ARIA và HTML ngữ nghĩa

### Quản lý Trạng thái

- Sử dụng Angular Signals để quản lý trạng thái phản ứng (reactive state) trong các component và service
- Tận dụng `signal()`, `computed()`, và `effect()` để cập nhật trạng thái một cách phản ứng
- Sử dụng writable signals cho trạng thái có thể thay đổi và computed signals cho trạng thái được suy ra
- Xử lý các trạng thái tải (loading) và lỗi (error) bằng signals và phản hồi UI phù hợp
- Sử dụng `AsyncPipe` của Angular để xử lý các observable trong template khi kết hợp signals với RxJS

### Lấy Dữ liệu

- Sử dụng `HttpClient` của Angular cho các lệnh gọi API với kiểu dữ liệu phù hợp
- Triển khai các toán tử RxJS để chuyển đổi dữ liệu và xử lý lỗi
- Sử dụng hàm `inject()` của Angular để dependency injection trong các component độc lập
- Triển khai các chiến lược bộ nhớ đệm (caching) (ví dụ: `shareReplay` cho các observable)
- Lưu trữ dữ liệu phản hồi từ API trong signals để cập nhật một cách phản ứng
- Xử lý lỗi API bằng các interceptor toàn cục để xử lý lỗi nhất quán

### Bảo mật

- Làm sạch đầu vào của người dùng bằng cách sử dụng tính năng sanitization tích hợp sẵn của Angular
- Triển khai các route guard để xác thực và phân quyền
- Sử dụng `HttpInterceptor` của Angular để bảo vệ chống lại CSRF và thêm các header xác thực API
- Xác thực đầu vào của form bằng reactive forms của Angular và các validator tùy chỉnh
- Tuân thủ các thực hành tốt nhất về bảo mật của Angular (ví dụ: tránh thao tác trực tiếp với DOM)

### Hiệu suất

- Bật bản dựng production với `ng build --prod` để tối ưu hóa
- Sử dụng tải lười (lazy loading) cho các route để giảm kích thước gói ban đầu
- Tối ưu hóa việc phát hiện thay đổi với chiến lược `OnPush` và signals để có khả năng phản ứng chi tiết
- Sử dụng trackBy trong các vòng lặp `ngFor` để cải thiện hiệu suất hiển thị
- Triển khai kết xuất phía máy chủ (SSR) hoặc tạo trang tĩnh (SSG) với Angular Universal (nếu được chỉ định)

### Kiểm thử

- Viết unit test cho các component, service, và pipe bằng Jasmine và Karma
- Sử dụng `TestBed` của Angular để kiểm thử component với các dependency được giả lập (mock)
- Kiểm thử các cập nhật trạng thái dựa trên signal bằng các tiện ích kiểm thử của Angular
- Viết các bài kiểm thử end-to-end với Cypress hoặc Playwright (nếu được chỉ định)
- Giả lập các yêu cầu HTTP bằng `HttpClientTestingModule`
- Đảm bảo độ bao phủ kiểm thử (test coverage) cao cho các chức năng quan trọng

## Quy trình Triển khai

1. Lên kế hoạch cấu trúc dự án và các module tính năng
2. Định nghĩa các interface và model TypeScript
3. Khởi tạo các component, service, và pipe bằng Angular CLI
4. Triển khai các service dữ liệu và tích hợp API với trạng thái dựa trên signal
5. Xây dựng các component có thể tái sử dụng với các input và output rõ ràng
6. Thêm reactive forms và xác thực
7. Áp dụng định dạng giao diện với SCSS và thiết kế đáp ứng
8. Triển khai các route tải lười và các guard
9. Thêm xử lý lỗi và các trạng thái tải bằng signals
10. Viết unit test và end-to-end test
11. Tối ưu hóa hiệu suất và kích thước gói

## Hướng dẫn Bổ sung

- Tuân thủ các quy ước đặt tên của Angular (ví dụ: `feature.component.ts`, `feature.service.ts`)
- Sử dụng các lệnh Angular CLI để tạo mã boilerplate
- Ghi lại tài liệu cho các component và service bằng các bình luận JSDoc rõ ràng
- Đảm bảo tuân thủ khả năng truy cập (WCAG 2.1) khi có thể
- Sử dụng tính năng i18n tích hợp sẵn của Angular để quốc tế hóa (nếu được chỉ định)
- Giữ mã nguồn theo nguyên tắc DRY (Không lặp lại chính mình) bằng cách tạo các tiện ích có thể tái sử dụng và các module dùng chung
- Sử dụng signals một cách nhất quán để quản lý trạng thái nhằm đảm bảo các
