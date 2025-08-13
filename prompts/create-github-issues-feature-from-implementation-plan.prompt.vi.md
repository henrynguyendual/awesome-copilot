# Tạo GitHub Issue từ Kế Hoạch Triển Khai

Tạo các GitHub Issue cho kế hoạch triển khai tại `${file}`.

## Quy Trình

1. Phân tích file kế hoạch để xác định các giai đoạn
2. Kiểm tra các issue hiện tại bằng `search_issues`
3. Tạo issue mới cho từng giai đoạn bằng `create_issue` hoặc cập nhật issue đã có bằng `update_issue`
4. Sử dụng template `feature_request.yml` hoặc `chore_request.yml` (nếu không có thì dùng mặc định)

## Yêu Cầu

- Mỗi giai đoạn triển khai tương ứng **một** issue
- Tiêu đề và mô tả rõ ràng, có cấu trúc
- Chỉ bao gồm các thay đổi được yêu cầu trong kế hoạch
- Xác minh với các issue hiện có trước khi tạo mới

## Nội Dung Issue

- **Tiêu đề**: Tên giai đoạn từ kế hoạch triển khai
- **Mô tả**: Chi tiết giai đoạn, yêu cầu và bối cảnh
- **Nhãn**: Phù hợp với loại issue (feature/chore)