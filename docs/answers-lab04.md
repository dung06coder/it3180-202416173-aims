# BÀI THẢO LUẬN LAB 04 – IT3180

## Câu 1 (Slide 52): Vì sao `release/*` không bao giờ merge ngược vào `master`?

- Theo quy tắc Release Flow, nhánh `release/*` sinh ra với mục đích đóng băng phiên bản và duy trì bảo trì độc lập.
- Nếu thực hiện merge ngược lại, chúng ta có nguy cơ mang những đoạn sửa lỗi đặc thù (hotfix) hoặc các file cấu hình riêng của phiên bản cũ ghi đè lên các tính năng mới đang phát triển ở `master`, gây lỗi hệ thống. (Để mang bản vá lỗi từ release sang master, quy trình chuẩn là dùng `cherry-pick`).

## Câu 2 (Slide 52): So sánh Release Flow với GitFlow?

- **Release Flow:** Đơn giản và linh hoạt. Lấy `master` làm trung tâm và luôn sẵn sàng phát hành. Nhánh `release` rẽ ngang trực tiếp từ `master` khi cần đóng gói. Cực kỳ phù hợp cho môi trường cần phát hành liên tục hoặc nộp bài tập theo tuần (nhiều bản song song).
- **GitFlow:** Cồng kềnh và phức tạp hơn, duy trì 2 nhánh dài hạn là `main` và `develop`. Tính năng gộp vào `develop`, rẽ nhánh `release` từ `develop`, sau khi hoàn thiện `release` phải merge ngược về cả 2 nhánh gốc. Mô hình này chỉ hợp với phần mềm có chu kỳ phát hành định kỳ khắt khe, môi trường deploy rạch ròi.

## Câu 3 (Slide 52): Vì sao nâng lên phiên bản `1.0.0` mà không phải `0.4.0`?

- Theo chuẩn **Semantic Versioning (SemVer)**, các phiên bản đầu `0.y.z` đại diện cho giai đoạn thử nghiệm, cấu trúc chưa ổn định.
- Tại Lab 04, dự án đã hoàn thiện đủ các chức năng cốt lõi (Giỏ hàng, DVD, Tìm kiếm, Test coverage 100%) và đạt đến trạng thái sẵn sàng để nộp bài hoàn chỉnh. Do đó, ta phải tăng Major version lên `1.0.0` để chính thức đánh dấu cột mốc phiên bản ổn định đầu tiên.
