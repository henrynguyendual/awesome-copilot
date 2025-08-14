---
description: "Tạo, cập nhật hoặc xem xét Azure IaC trong Terraform bằng cách sử dụng Azure Verified Modules (AVM)."
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp", "azure_get_deployment_best_practices", "azure_get_schema_for_Bicep"]
---

# Chế độ Azure AVM Terraform

Sử dụng Azure Verified Modules cho Terraform để thực thi các phương pháp hay nhất của Azure thông qua các mô-đun được xây dựng sẵn.

## Khám phá các mô-đun

- Terraform Registry: tìm kiếm "avm" + tài nguyên, lọc theo thẻ Partner.
- Chỉ mục AVM: `https://azure.github.io/Azure-Verified-Modules/indexes/terraform/tf-resource-modules/`

## Cách sử dụng

- **Ví dụ**: Sao chép ví dụ, thay thế `source = learning_python_core"` bằng `source = "Azure/avm-res-{service}-{resource}/azurerm"`, thêm `version`, đặt `enable_telemetry`.
- **Tùy chỉnh**: Sao chép Hướng dẫn Cung cấp (Provision Instructions), đặt các đầu vào, ghim `version`.

## Quản lý phiên bản

- Điểm cuối (Endpoint): `https://registry.terraform.io/v1/modules/Azure/{module}/azurerm/versions`

## Nguồn

- Registry: `https://registry.terraform.io/modules/Azure/{module}/azurerm/latest`
- GitHub: `https://github.com/Azure/terraform-azurerm-avm-res-{service}-{resource}`

## Quy ước đặt tên

- Tài nguyên (Resource): Azure/avm-res-{service}-{resource}/azurerm
- Mẫu (Pattern): Azure/avm-ptn-{pattern}/azurerm
- Tiện ích (Utility): Azure/avm-utl-{utility}/azurerm

## Các phương pháp hay nhất

- Ghim phiên bản của mô-đun và nhà cung cấp (provider).
- Bắt đầu với các ví dụ chính thức.
- Xem xét các đầu vào và đầu ra.
- Bật đo lường từ xa (telemetry).
- Sử dụng các mô-đun tiện ích AVM.
- Tuân thủ các yêu cầu của nhà cung cấp AzureRM.
- Luôn chạy `terraform fmt` và `terraform validate` sau khi thực hiện thay đổi.
- Sử dụng công cụ `azure_get_deployment_best_practices` để được hướng dẫn triển khai.
- Sử dụng công cụ `microsoft.docs.mcp` để tra cứu hướng dẫn cụ thể cho từng dịch vụ Azure.

## Hướng dẫn tùy chỉnh cho các Agent của GitHub Copilot

**QUAN TRỌNG**: Khi GitHub Copilot Agent hoặc GitHub Copilot Coding Agent làm việc trên kho lưu trữ này, các bài kiểm tra đơn vị (unit test) cục bộ sau đây PHẢI được thực thi để tuân thủ các kiểm tra PR. Việc không chạy các bài kiểm tra này sẽ gây ra lỗi xác thực PR:

```bash
./avm pre-commit
./avm tflint
./avm pr-check
```

Các lệnh này phải được chạy trước khi bất kỳ pull request nào được tạo hoặc cập nhật để đảm bảo tuân thủ các tiêu chuẩn của Azure Verified Modules và ngăn ngừa lỗi trong quy trình CI/CD.
Thông tin chi tiết hơn về quy trình AVM có thể được tìm thấy trong [Tài liệu đóng góp cho Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/contributing/terraform/testing/).
