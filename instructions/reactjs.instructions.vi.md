---
description: "Tiêu chuẩn và các phương pháp hay nhất để phát triển ReactJS"
applyTo: "**/*.jsx, **/*.tsx, **/*.js, **/*.ts, **/*.css, **/*.scss"
---

# Hướng dẫn Phát triển ReactJS

Hướng dẫn xây dựng các ứng dụng ReactJS chất lượng cao với các mẫu hiện đại, hooks, và các phương pháp hay nhất theo tài liệu chính thức của React tại https://react.dev.

## Bối cảnh Dự án

- Phiên bản React mới nhất (React 19+)
- TypeScript để đảm bảo an toàn kiểu dữ liệu (khi áp dụng)
- Sử dụng functional components với hooks làm mặc định
- Tuân thủ hướng dẫn về phong cách và các phương pháp hay nhất chính thức của React
- Sử dụng các công cụ xây dựng hiện đại (Vite, Create React App, hoặc cấu hình Webpack tùy chỉnh)
- Triển khai các mẫu composition và tái sử dụng component phù hợp

## Tiêu chuẩn Phát triển

### Kiến trúc

- Sử dụng functional components với hooks làm mẫu chính
- Triển khai component composition thay vì kế thừa
- Tổ chức các component theo tính năng hoặc miền để dễ dàng mở rộng
- Phân tách rõ ràng các component trình bày (presentational) và component chứa logic (container)
- Sử dụng custom hooks cho logic có trạng thái (stateful) có thể tái sử dụng
- Triển khai hệ thống phân cấp component phù hợp với luồng dữ liệu rõ ràng

### Tích hợp TypeScript

- Sử dụng interface của TypeScript cho props, state, và định nghĩa component
- Định nghĩa các kiểu dữ liệu phù hợp cho các trình xử lý sự kiện (event handlers) và refs
- Triển khai các component generic khi thích hợp
- Sử dụng chế độ nghiêm ngặt (strict mode) trong `tsconfig.json` để đảm bảo an toàn kiểu dữ liệu
- Tận dụng các kiểu dữ liệu tích hợp sẵn của React (`React.FC`, `React.ComponentProps`, v.v.)
- Tạo các kiểu union cho các biến thể và trạng thái của component

### Thiết kế Component

- Tuân thủ nguyên tắc trách nhiệm đơn lẻ (single responsibility principle) cho các component
- Sử dụng quy ước đặt tên mang tính mô tả và nhất quán
- Triển khai xác thực prop phù hợp với TypeScript hoặc PropTypes
- Thiết kế các component để có thể kiểm thử và tái sử dụng
- Giữ cho các component nhỏ và tập trung vào một mối quan tâm duy nhất
- Sử dụng các mẫu composition (render props, children as functions)

### Quản lý Trạng thái (State Management)

- Sử dụng `useState` cho trạng thái cục bộ của component
- Triển khai `useReducer` cho logic trạng thái phức tạp
- Tận dụng `useContext` để chia sẻ trạng thái giữa các cây component
- Cân nhắc sử dụng các thư viện quản lý trạng thái bên ngoài (Redux Toolkit, Zustand) cho các ứng dụng phức tạp
- Triển khai chuẩn hóa trạng thái và cấu trúc dữ liệu phù hợp
- Sử dụng React Query hoặc SWR để quản lý trạng thái từ máy chủ (server state)

### Hooks và Effects

- Sử dụng `useEffect` với mảng phụ thuộc (dependency array) phù hợp để tránh vòng lặp vô hạn
- Triển khai các hàm dọn dẹp (cleanup functions) trong effects để ngăn chặn rò rỉ bộ nhớ
- Sử dụng `useMemo` và `useCallback` để tối ưu hóa hiệu suất khi cần thiết
- Tạo custom hooks cho logic có trạng thái có thể tái sử dụng
- Tuân thủ các quy tắc của hooks (chỉ gọi ở cấp cao nhất)
- Sử dụng `useRef` để truy cập các phần tử DOM và lưu trữ các giá trị có thể thay đổi

### Tạo kiểu (Styling)

- Sử dụng CSS Modules, Styled Components, hoặc các giải pháp CSS-in-JS hiện đại
- Triển khai thiết kế đáp ứng (responsive design) với phương pháp mobile-first
- Tuân thủ phương pháp BEM hoặc các quy ước đặt tên tương tự cho các lớp CSS
- Sử dụng các thuộc tính tùy chỉnh của CSS (biến) để tạo chủ đề (theming)
- Triển khai hệ thống khoảng cách, kiểu chữ và màu sắc nhất quán
- Đảm bảo khả năng truy cập (accessibility) với các thuộc tính ARIA và HTML ngữ nghĩa phù hợp

### Tối ưu hóa Hiệu suất

- Sử dụng `React.memo` để ghi nhớ (memoization) component khi thích hợp
- Triển khai tách mã (code splitting) với `React.lazy` và `Suspense`
- Tối ưu hóa kích thước gói (bundle size) bằng tree shaking và dynamic imports
- Sử dụng `useMemo` và `useCallback` một cách hợp lý để ngăn chặn các lần render lại không cần thiết
- Triển khai cuộn ảo (virtual scrolling) cho các danh sách lớn
- Phân tích các component bằng React DevTools để xác định các điểm nghẽn hiệu suất

### Lấy dữ liệu (Data Fetching)

- Sử dụng các thư viện lấy dữ liệu hiện đại (React Query, SWR, Apollo Client)
- Triển khai các trạng thái tải (loading), lỗi (error), và thành công (success) phù hợp
- Xử lý các điều kiện tranh chấp (race conditions) và hủy yêu cầu (request cancellation)
- Sử dụng cập nhật lạc quan (optimistic updates) để cải thiện trải nghiệm người dùng
- Triển khai các chiến lược lưu vào bộ nhớ đệm (caching) phù hợp
- Xử lý các tình huống ngoại tuyến (offline) và lỗi mạng một cách linh hoạt

### Xử lý Lỗi (Error Handling)

- Triển khai Error Boundaries để xử lý lỗi ở cấp component
- Sử dụng các trạng thái lỗi phù hợp trong quá trình lấy dữ liệu
- Triển khai giao diện người dùng dự phòng (fallback UI) cho các tình huống lỗi
- Ghi lại (log) lỗi một cách thích hợp để gỡ lỗi
- Xử lý các lỗi bất đồng bộ trong effects và trình xử lý sự kiện
- Cung cấp thông báo lỗi có ý nghĩa cho người dùng

### Biểu mẫu và Xác thực (Forms and Validation)

- Sử dụng các component được kiểm soát (controlled components) cho các đầu vào của biểu mẫu
- Triển khai xác thực biểu mẫu phù hợp với các thư viện như Formik, React Hook Form
- Xử lý việc gửi biểu mẫu và các trạng thái lỗi một cách thích hợp
- Triển khai các tính năng trợ năng cho biểu mẫu (nhãn, thuộc tính ARIA)
- Sử dụng xác thực trì hoãn (debounced validation) để cải thiện trải nghiệm người dùng
- Xử lý tải lên tệp và các kịch bản biểu mẫu phức tạp

### Định tuyến (Routing)

- Sử dụng React Router để định tuyến phía máy khách (client-side routing)
- Triển khai các tuyến đường lồng nhau (nested routes) và bảo vệ tuyến đường (route protection)
- Xử lý các tham số tuyến đường (route parameters) và chuỗi truy vấn (query strings) một cách phù hợp
- Triển khai tải lười (lazy loading) để tách mã dựa trên tuyến đường
- Sử dụng các mẫu điều hướng và xử lý nút quay lại phù hợp
- Triển khai breadcrumbs và quản lý trạng thái điều hướng

### Kiểm thử (Testing)

- Viết unit tests cho các component bằng React Testing Library
- Kiểm thử hành vi của component, không phải chi tiết triển khai
- Sử dụng Jest làm trình chạy kiểm thử và thư viện xác nhận (assertion)
- Triển khai integration tests cho các tương tác component phức tạp
- Mô phỏng (mock) các phụ thuộc bên ngoài và các lệnh gọi API một cách thích hợp
- Kiểm thử các tính năng trợ năng và điều hướng bằng bàn phím

### Bảo mật (Security)

- Làm sạch (sanitize) đầu vào của người dùng để ngăn chặn các cuộc tấn công XSS
- Xác thực và thoát (escape) dữ liệu trước khi hiển thị
- Sử dụng HTTPS cho tất cả các lệnh gọi API bên ngoài
- Triển khai các mẫu xác thực và ủy quyền phù hợp
- Tránh lưu trữ dữ liệu nhạy cảm trong localStorage hoặc sessionStorage
- Sử dụng tiêu đề Content Security Policy (CSP)

### Khả năng truy cập (Accessibility)

- Sử dụng các phần tử HTML ngữ nghĩa một cách thích hợp
- Triển khai các thuộc tính và vai trò ARIA phù hợp
- Đảm bảo điều hướng bằng bàn phím hoạt động cho tất cả các phần tử tương tác
- Cung cấp văn bản thay thế (alt text) cho hình ảnh và văn bản mô tả cho các biểu tượng
- Triển khai tỷ lệ tương phản màu sắc phù hợp
- Kiểm thử bằng trình đọc màn hình và các công cụ trợ năng

## Quy trình Triển khai

1. Lập kế hoạch kiến trúc component và luồng dữ liệu
2. Thiết lập cấu trúc dự án với tổ chức thư mục phù hợp
3. Định nghĩa các interface và kiểu dữ liệu TypeScript
4. Triển khai các component cốt lõi với kiểu dáng phù hợp
5. Thêm logic quản lý trạng thái và lấy dữ liệu
6. Triển khai định tuyến và điều hướng
7. Thêm xử lý biểu mẫu và xác thực
8. Triển khai xử lý lỗi và các trạng thái tải
9. Thêm phạm vi kiểm thử cho các component và chức năng
10. Tối ưu hóa hiệu suất và kích thước gói
11. Đảm bảo tuân thủ khả năng truy cập
12. Thêm tài liệu và bình luận mã nguồn

## Hướng dẫn Bổ sung

- Tuân thủ các quy ước đặt tên của React (PascalCase cho component, camelCase cho hàm)
- Sử dụng các thông điệp commit có ý nghĩa và duy trì lịch sử git sạch sẽ
- Triển khai các chiến lược tách mã và tải lười phù hợp
- Ghi lại tài liệu cho các component phức tạp và custom hooks bằng JSDoc
- Sử dụng ESLint và Prettier để định dạng mã nhất quán
- Giữ các phụ thuộc được cập nhật và kiểm tra các lỗ hổng bảo mật
- Triển khai cấu hình môi trường phù hợp cho các giai đoạn triển khai khác nhau
- Sử dụng React Developer Tools để gỡ lỗi và phân tích hiệu suất

## Các Mẫu Phổ biến

- Higher-Order Components (HOCs) cho các mối quan tâm xuyên suốt (cross-cutting concerns)
- Mẫu Render props cho component composition
- Compound components cho các chức năng liên quan
- Mẫu Provider để chia sẻ trạng thái dựa trên context
- Tách biệt component Container/Presentational
- Custom hooks để trích xuất logic có thể tái
