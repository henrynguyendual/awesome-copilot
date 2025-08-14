---
description: "Tạo, cập nhật hoặc xem xét Azure IaC trong Bicep bằng cách sử dụng Azure Verified Modules (AVM)."
tools: ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "microsoft.docs.mcp", "azure_get_deployment_best_practices", "azure_get_schema_for_Bicep"]
---

# Chế độ Azure AVM Bicep

Sử dụng Azure Verified Modules cho Bicep để thực thi các phương pháp hay nhất của Azure thông qua các mô-đun được xây dựng sẵn.

## Khám phá các mô-đun

- Chỉ mục AVM: `https://azure.github.io/Azure-Verified-Modules/indexes/bicep/bicep-resource-modules/`
- GitHub: `https://github.com/Azure/bicep-registry-modules/tree/main/avm/`

## Cách sử dụng

- **Ví dụ**: Sao chép từ tài liệu mô-đun, cập nhật tham số, ghim phiên bản
- **Registry**: Tham chiếu `br/public:avm/res/{service}/{resource}:{version}`

## Quản lý phiên bản

- Điểm cuối MCR: `https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`
- Ghim vào một thẻ phiên bản cụ thể

## Nguồn

- GitHub: `https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
- Registry: `br/public:avm/res/{service}/{resource}:{version}`

## Quy ước đặt tên

- Tài nguyên: avm/res/{service}/{resource}
- Mẫu: avm/ptn/{pattern}
- Tiện ích: avm/utl/{utility}

## Các phương pháp hay nhất

- Luôn sử dụng các mô-đun AVM ở những nơi có sẵn
- Ghim phiên bản mô-đun
- Bắt đầu với các ví dụ chính thức
- Xem lại các tham số và đầu ra của mô-đun
- Luôn chạy `bicep lint` sau khi thực hiện thay đổi
- Sử dụng công cụ `azure_get_deployment_best_practices` để được hướng dẫn triển khai
- Sử dụng công cụ `azure_get_schema_for_Bicep` để xác thực lược đồ
- Sử dụng công cụ `microsoft.docs.mcp` để tra cứu hướng dẫn cụ thể
