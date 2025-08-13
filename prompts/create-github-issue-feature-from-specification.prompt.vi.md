# Tạo GitHub Issue từ Bản Đặc Tả

Tạo GitHub Issue cho bản đặc tả tại `${file}`.

## Quy Trình

1. Phân tích file đặc tả để trích xuất yêu cầu
2. Kiểm tra issue hiện có bằng `search_issues`
3. Tạo issue mới bằng `create_issue` hoặc cập nhật issue đã có bằng `update_issue`
4. Sử dụng template `feature_request.yml` (nếu không có thì dùng mặc định)

## Yêu Cầu

- Chỉ tạo **một** issue cho toàn bộ đặc tả
- Tiêu đề rõ ràng, phản ánh tên đặc tả
- Chỉ bao gồm các thay đổi yêu cầu trong đặc tả
- Xác minh với các issue hiện tại trước khi tạo mới

## Nội Dung Issue

- **Tiêu đề**: Tên tính năng từ đặc tả
- **Mô tả**: Nêu vấn đề, giải pháp đề xuất và bối cảnh
- **Nhãn**: feature, enhancement (nếu phù hợp)