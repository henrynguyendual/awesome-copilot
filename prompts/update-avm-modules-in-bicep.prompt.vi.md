---
mode: 'agent'
description: 'Cập nhật Azure Verified Modules (AVM) lên phiên bản mới nhất trong các tệp Bicep.'
tools: ['changes', 'codebase', 'editFiles', 'fetch', 'runCommands', 'azure_get_deployment_best_practices', 'azure_get_schema_for_Bicep']
---

# Cập Nhật Azure Verified Modules Trong Các Tệp Bicep

Cập nhật tệp Bicep `${file}` để sử dụng phiên bản mới nhất của Azure Verified Module (AVM).

## Quy Trình

1. **Quét**: Trích xuất các module AVM và phiên bản hiện tại từ `${file}`
2. **Kiểm Tra**: Lấy phiên bản mới nhất từ MCR: `https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`
3. **So Sánh**: Phân tích phiên bản theo chuẩn semantic để xác định bản cập nhật
4. **Xem Xét**: Với các thay đổi phá vỡ tương thích, lấy tài liệu từ: `https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
5. **Cập Nhật**: Áp dụng bản cập nhật phiên bản và các thay đổi tham số
6. **Xác Thực**: Chạy `bicep lint` để đảm bảo tuân thủ

## Chính Sách Xử Lý Thay Đổi Phá Vỡ Tương Thích

⚠️ **TẠM DỪNG để phê duyệt** nếu bản cập nhật liên quan đến:

- Thay đổi tham số không tương thích
- Các sửa đổi về bảo mật/tuân thủ
- Thay đổi hành vi

## Định Dạng Kết Quả

Hiển thị kết quả dưới dạng bảng với biểu tượng:

| Module | Hiện Tại | Mới Nhất | Trạng Thái | Hành Động | Tài Liệu |
|--------|----------|---------|------------|-----------|----------|
| avm/res/compute/vm | 0.1.0 | 0.2.0 | 🔄 | Đã cập nhật | [📖](link) |
| avm/res/storage/account | 0.3.0 | 0.3.0 | ✅ | Đang dùng bản mới nhất | [📖](link) |

## Biểu Tượng

- 🔄 Đã cập nhật
- ✅ Đang dùng bản mới nhất
- ⚠️ Cần xem xét thủ công
- ❌ Thất bại
- 📖 Tài liệu

## Yêu Cầu

- Chỉ sử dụng API tags của MCR để tìm phiên bản
- Phân tích mảng JSON tags và sắp xếp theo semantic versioning
- Duy trì tính hợp lệ của tệp Bicep và tuân thủ linting