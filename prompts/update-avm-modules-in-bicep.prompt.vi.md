---
mode: "agent"
description: "Cập nhật các Mô-đun đã được xác minh của Azure (AVM) lên phiên bản mới nhất trong các tệp Bicep."
tools: ["changes", "codebase", "editFiles", "fetch", "runCommands", "azure_get_deployment_best_practices", "azure_get_schema_for_Bicep"]
---

# Cập nhật các Mô-đun đã được xác minh của Azure trong tệp Bicep

Cập nhật tệp Bicep `${file}` để sử dụng các phiên bản Mô-đun đã được xác minh của Azure (AVM) mới nhất.

## Quy trình

1.  **Quét**: Trích xuất các mô-đun AVM và phiên bản hiện tại từ `${file}`
2.  **Kiểm tra**: Lấy các phiên bản mới nhất từ MCR: `https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`
3.  **So sánh**: Phân tích cú pháp các phiên bản ngữ nghĩa để xác định các bản cập nhật
4.  **Xem xét**: Đối với các thay đổi có thể gây lỗi, hãy lấy tài liệu từ: `https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
5.  **Cập nhật**: Áp dụng các bản cập nhật phiên bản và thay đổi tham số
6.  **Xác thực**: Chạy `bicep lint` để đảm bảo tuân thủ

## Chính sách về thay đổi có thể gây lỗi

⚠️ **TẠM DỪNG để chờ phê duyệt** nếu các bản cập nhật liên quan đến:

- Các thay đổi tham số không tương thích
- Các sửa đổi về bảo mật/tuân thủ
- Các thay đổi về hành vi

## Định dạng đầu ra

Hiển thị kết quả trong bảng với các biểu tượng:

| Mô-đun                  | Hiện tại | Mới nhất | Trạng thái | Hành động   | Tài liệu   |
| ----------------------- | -------- | -------- | ---------- | ----------- | ---------- |
| avm/res/compute/vm      | 0.1.0    | 0.2.0    | 🔄         | Đã cập nhật | [📖](link) |
| avm/res/storage/account | 0.3.0    | 0.3.0    | ✅         | Hiện tại    | [📖](link) |

## Biểu tượng

- 🔄 Đã cập nhật
- ✅ Hiện tại
- ⚠️ Cần xem xét thủ công
- ❌ Thất bại
- 📖 Tài liệu

## Yêu cầu

- Chỉ sử dụng API thẻ MCR để khám phá phiên bản
- Phân tích cú pháp mảng thẻ JSON và sắp xếp theo phiên bản ngữ nghĩa
- Duy trì tính hợp lệ của tệp Bicep
