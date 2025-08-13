---
description: "Các tiêu chuẩn và phương pháp thực hành tốt nhất để phát triển VueJS 3 với Composition API và TypeScript"
applyTo: "**/*.vue, **/*.ts, **/*.js, **/*.scss"
---

# Hướng dẫn Phát triển VueJS 3

Hướng dẫn xây dựng các ứng dụng VueJS 3 chất lượng cao với Composition API, TypeScript và các phương pháp thực hành tốt nhất hiện đại.

## Bối cảnh Dự án

- Vue 3.x với Composition API làm mặc định
- TypeScript để đảm bảo an toàn kiểu dữ liệu
- Single File Components (`.vue`) với cú pháp `<script setup>`
- Công cụ build hiện đại (khuyến nghị dùng Vite)
- Pinia để quản lý trạng thái ứng dụng
- Hướng dẫn về phong cách và các phương pháp thực hành tốt nhất chính thức của Vue

## Tiêu chuẩn Phát triển

### Kiến trúc

- Ưu tiên Composition API (`setup` functions và composables) hơn Options API
- Sắp xếp các component và composable theo tính năng hoặc miền để dễ dàng mở rộng
- Tách biệt các component tập trung vào giao diện người dùng (presentational) khỏi các component tập trung vào logic (containers)
- Tách logic có thể tái sử dụng vào các hàm composable trong thư mục `composables/`
- Cấu trúc các module store (Pinia) theo miền, với các actions, state, và getters được định nghĩa rõ ràng

### Tích hợp TypeScript

- Bật chế độ `strict` trong `tsconfig.json` để đảm bảo an toàn kiểu dữ liệu tối đa
- Sử dụng `defineComponent` hoặc `<script setup lang="ts">` với `defineProps` và `defineEmits`
- Tận dụng `PropType<T>` cho các prop được định kiểu và giá trị mặc định
- Sử dụng interface hoặc type alias cho các hình dạng prop và state phức tạp
- Định nghĩa kiểu cho các trình xử lý sự kiện, ref, và các hook `useRoute`/`useRouter`
- Triển khai các component và composable generic khi có thể

### Thiết kế Component

- Tuân thủ nguyên tắc trách nhiệm đơn lẻ (single responsibility principle) cho các component
- Sử dụng PascalCase cho tên component và kebab-case cho tên tệp
- Giữ cho các component nhỏ và tập trung vào một vấn đề duy nhất
- Sử dụng cú pháp `<script setup>` để ngắn gọn và hiệu suất cao
- Xác thực prop bằng TypeScript; chỉ sử dụng kiểm tra runtime khi thực sự cần thiết
- Ưu tiên slot và scoped slot để có thành phần linh hoạt

### Quản lý Trạng thái

- Sử dụng Pinia cho trạng thái toàn cục: định nghĩa các store bằng `defineStore`
- Đối với trạng thái cục bộ đơn giản, sử dụng `ref` và `reactive` trong `setup`
- Sử dụng `computed` cho trạng thái dẫn xuất
- Giữ trạng thái được chuẩn hóa cho các cấu trúc phức tạp
- Sử dụng actions trong các store Pinia cho logic bất đồng bộ
- Tận dụng các plugin của store để lưu trữ hoặc gỡ lỗi

### Các Mẫu Composition API

- Tạo các composable có thể tái sử dụng cho logic dùng chung, ví dụ: `useFetch`, `useAuth`
- Sử dụng `watch` và `watchEffect` với danh sách phụ thuộc chính xác
- Dọn dẹp các hiệu ứng phụ (side effects) trong `onUnmounted` hoặc các callback dọn dẹp của `watch`
- Sử dụng `provide`/`inject` một cách tiết kiệm cho việc chèn phụ thuộc sâu
- Sử dụng `useAsyncData` hoặc các tiện ích dữ liệu của bên thứ ba (Vue Query)

### Định dạng Giao diện (Styling)

- Sử dụng `<style scoped>` cho các kiểu ở cấp độ component hoặc CSS Modules
- Cân nhắc các framework utility-first (Tailwind CSS) để tạo kiểu nhanh chóng
- Tuân theo các quy ước BEM hoặc functional CSS để đặt tên class
- Tận dụng các thuộc tính tùy chỉnh CSS (custom properties) cho việc tạo chủ đề và design tokens
- Triển khai thiết kế đáp ứng, ưu tiên di động (mobile-first) với CSS Grid và Flexbox
- Đảm bảo các kiểu có thể truy cập được (độ tương phản, trạng thái focus)

### Tối ưu hóa Hiệu suất

- Tải lười (Lazy-load) các component bằng dynamic imports và `defineAsyncComponent`
- Sử dụng `<Suspense>` cho các fallback khi tải component bất đồng bộ
- Áp dụng `v-once` và `v-memo` cho các phần tử tĩnh hoặc ít thay đổi
- Phân tích hiệu suất với tab Performance của Vue DevTools
- Tránh các watcher không cần thiết; ưu tiên `computed` khi có thể
- Loại bỏ code không sử dụng (Tree-shake) và tận dụng các tính năng tối ưu hóa của Vite

### Lấy Dữ liệu (Data Fetching)

- Sử dụng các composable như `useFetch` (Nuxt) hoặc các thư viện như Vue Query
- Xử lý các trạng thái loading, error, và success một cách rõ ràng
- Hủy các yêu cầu đã cũ khi component bị unmount hoặc tham số thay đổi
- Triển khai cập nhật lạc quan (optimistic updates) với khả năng khôi phục khi thất bại
- Lưu trữ phản hồi vào bộ đệm (cache) và sử dụng xác thực lại trong nền

### Xử lý Lỗi

- Sử dụng trình xử lý lỗi toàn cục (`app.config.errorHandler`) cho các lỗi không được bắt
- Bao bọc logic có rủi ro trong `try/catch`; cung cấp thông báo thân thiện với người dùng
- Sử dụng hook `errorCaptured` trong các component cho các ranh giới cục bộ
- Hiển thị giao diện người dùng dự phòng hoặc cảnh báo lỗi một cách mượt mà
- Ghi lại lỗi vào các dịch vụ bên ngoài (Sentry, LogRocket)

### Form và Xác thực

- Sử dụng các thư viện như VeeValidate hoặc @vueuse/form để xác thực theo kiểu khai báo
- Xây dựng form với các ràng buộc `v-model` được kiểm soát
- Xác thực khi blur hoặc input với debouncing để tăng hiệu suất
- Xử lý việc tải lên tệp và các form nhiều bước phức tạp trong các composable
- Đảm bảo nhãn, thông báo lỗi và quản lý focus có thể truy cập được

### Định tuyến (Routing)

- Sử dụng Vue Router 4 với `createRouter` và `createWebHistory`
- Triển khai các route lồng nhau và chia tách code theo route (route-level code splitting)
- Bảo vệ các route bằng navigation guards (`beforeEnter`, `beforeEach`)
- Sử dụng `useRoute` và `useRouter` trong `setup` để điều hướng theo chương trình
- Quản lý các tham số truy vấn (query params) và các đoạn động (dynamic segments) đúng cách
- Triển khai dữ liệu breadcrumb thông qua các trường meta của route

### Kiểm thử (Testing)

- Viết unit test với Vue Test Utils và Jest
- Tập trung vào hành vi, không phải chi tiết triển khai
- Sử dụng `mount` và `shallowMount` để cô lập component
- Mock các plugin toàn cục (router, Pinia) khi cần
- Thêm các bài kiểm thử end-to-end với Cypress hoặc Playwright
- Kiểm tra khả năng truy cập bằng tích hợp axe-core

### Bảo mật

- Tránh sử dụng `v-html`; làm sạch (sanitize) mọi đầu vào HTML một cách nghiêm ngặt
- Sử dụng header CSP để giảm thiểu các cuộc tấn công XSS và injection
- Xác thực và thoát (escape) dữ liệu trong các template và directive
- Sử dụng HTTPS cho tất cả các yêu cầu API
- Lưu trữ các token nhạy cảm trong cookie HTTP-only, không phải `localStorage`

### Khả năng Truy cập (Accessibility)

- Sử dụng các phần tử HTML ngữ nghĩa và thuộc tính ARIA
- Quản lý focus cho các modal và nội dung động
- Cung cấp điều hướng bằng bàn phím cho các component tương tác
- Thêm văn bản `alt` có ý nghĩa cho hình ảnh và biểu tượng
- Đảm bảo độ tương phản màu sắc đáp ứng tiêu chuẩn WCAG AA

## Quy trình Triển khai

1.  Lên kế hoạch kiến trúc component và composable
2.  Khởi tạo dự án Vite với Vue 3 và TypeScript
3.  Định nghĩa các store Pinia và composable
4.  Tạo các component giao diện người dùng cốt lõi và layout
5.  Tích hợp định tuyến và điều hướng
6.  Triển khai logic lấy dữ liệu và trạng thái
7.  Xây dựng form với xác thực và trạng thái lỗi
8.  Thêm xử lý lỗi toàn cục và giao diện người dùng dự phòng
9.  Thêm unit test và E2E test
10. Tối ưu hóa hiệu suất và kích thước gói (bundle size)
11. Đảm bảo tuân thủ khả năng truy cập
12. Ghi tài liệu cho các component, composable, và store

## Hướng dẫn Bổ sung

- Tuân theo hướng dẫn phong cách chính thức của Vue (vuejs.org/style-guide)
- Sử dụng ESLint (với `plugin:vue/vue3-recommended`) và Prettier để đảm bảo tính nhất quán của code
- Viết các thông điệp commit có ý nghĩa và duy trì lịch sử git sạch sẽ
- Giữ các phụ thuộc được cập nhật và kiểm tra các lỗ hổng bảo mật
- Ghi tài liệu cho logic phức tạp bằng JSDoc/TSDoc
- Sử dụng Vue DevTools để gỡ lỗi và phân tích hiệu suất

## Các Mẫu Phổ biến

- Các component không có giao diện (Renderless components) và scoped slots cho giao diện người dùng linh hoạt
- Các component phức hợp (Compound components) sử dụng provide/inject
- Các directive tùy chỉnh cho các mối quan tâm xuyên suốt (cross-cutting concerns)
- Teleport cho các modal và overlay
- Hệ thống plugin cho các tiện ích toàn cục (i18n, analytics)
- Các factory composable cho
