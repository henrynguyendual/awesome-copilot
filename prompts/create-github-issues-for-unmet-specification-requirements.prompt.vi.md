# Tạo GitHub Issue cho Các Yêu Cầu Chưa Được Thực Hiện trong Đặc Tả

Tạo các GitHub Issue cho những yêu cầu chưa được triển khai trong bản đặc tả tại `${file}`.

## Quy Trình

1. Phân tích file đặc tả để trích xuất tất cả yêu cầu
2. Kiểm tra trạng thái triển khai của từng yêu cầu trong codebase
3. Tìm kiếm issue hiện có bằng `search_issues` để tránh trùng lặp
4. Tạo issue mới cho từng yêu cầu chưa được thực hiện bằng `create_issue`
5. Sử dụng template `feature_request.yml` (nếu không có thì dùng mặc định)

## Yêu Cầu

- Mỗi yêu cầu chưa được thực hiện tương ứng **một** issue
- Tiêu đề phải chứa ID yêu cầu và mô tả ngắn
- Bao gồm hướng dẫn triển khai và tiêu chí chấp nhận
- Xác minh với các issue hiện tại trước khi tạo mới

## Nội Dung Issue

- **Tiêu đề**: ID yêu cầu và mô tả ngắn
- **Mô tả**: Yêu cầu chi tiết, phương pháp triển khai và bối cảnh
- **Nhãn**: feature, enhancement (nếu phù hợp)

## Kiểm Tra Triển Khai

- Tìm kiếm các mẫu code liên quan trong codebase
- Kiểm tra các file đặc tả liên quan trong thư mục `/spec/`
- Đảm bảo yêu cầu chưa được thực hiện một phần