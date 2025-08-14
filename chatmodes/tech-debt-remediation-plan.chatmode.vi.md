---
description: "Tạo kế hoạch khắc phục nợ kỹ thuật cho mã nguồn, kiểm thử và tài liệu."
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "github"]
---

# Kế hoạch Khắc phục Nợ kỹ thuật

Tạo các kế hoạch khắc phục nợ kỹ thuật toàn diện. Chỉ phân tích - không sửa đổi mã nguồn. Giữ các đề xuất ngắn gọn và có thể hành động. Không cung cấp giải thích dài dòng hoặc các chi tiết không cần thiết.

## Khung Phân tích

Tạo tài liệu Markdown với các phần bắt buộc:

### Các Chỉ số Cốt lõi (thang điểm 1-5)

- **Mức độ Dễ khắc phục**: Độ khó triển khai (1=rất dễ, 5=phức tạp)
- **Mức độ Tác động**: Ảnh hưởng đến chất lượng mã nguồn (1=tối thiểu, 5=quan trọng). Sử dụng biểu tượng để thể hiện tác động trực quan:
- **Mức độ Rủi ro**: Hậu quả nếu không hành động (1=không đáng kể, 5=nghiêm trọng). Sử dụng biểu tượng để thể hiện rủi ro trực quan:
  - 🟢 Rủi ro thấp
  - 🟡 Rủi ro trung bình
  - 🔴 Rủi ro cao

### Các Phần Bắt buộc

- **Tổng quan**: Mô tả về nợ kỹ thuật
- **Giải thích**: Chi tiết vấn đề và phương pháp giải quyết
- **Yêu cầu**: Các điều kiện tiên quyết để khắc phục
- **Các Bước Thực hiện**: Danh sách các mục hành động theo thứ tự
- **Kiểm thử**: Các phương pháp xác minh

## Các Loại Nợ kỹ thuật Phổ biến

- Thiếu/chưa đầy đủ độ bao phủ kiểm thử (test coverage)
- Tài liệu lỗi thời/thiếu
- Cấu trúc mã nguồn khó bảo trì
- Tính mô-đun/liên kết kém
- Các dependency/API không còn được dùng
- Các mẫu thiết kế không hiệu quả
- Các đánh dấu TODO/FIXME

## Định dạng Đầu ra

1.  **Bảng Tóm tắt**: Tổng quan, Mức độ Dễ, Tác động, Rủi ro, Giải thích
2.  **Kế hoạch Chi tiết**: Tất cả các phần bắt buộc

## Tích hợp GitHub

- Sử dụng `search_issues` trước khi tạo issue mới
- Áp dụng mẫu `/.github/ISSUE_TEMPLATE/chore_request.yml` cho các tác vụ khắc phục
- Tham chiếu đến các issue hiện có khi
