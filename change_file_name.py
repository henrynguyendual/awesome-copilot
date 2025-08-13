#!/usr/bin/env python3
"""Đổi tên tất cả các file trong dự án có mẫu "<base> copy.<ext>" thành "<base>.vi.<ext>".

Yêu cầu cụ thể:
- Tìm các file chứa chuỗi " copy" ngay trước phần mở rộng cuối cùng.
  Ví dụ: a11y.instructions copy.md -> a11y.instructions.vi.md
- Hỗ trợ nhiều phần mở rộng kép (vd: .tar.gz) => chỉ chèn ".vi" trước phần mở rộng đầu tiên trong chuỗi mở rộng.
  Quy ước: Dùng phần sau dấu chấm đầu tiên sau " copy" làm phần mở rộng nguyên vẹn.
- Bỏ qua thư mục ẩn (.git, .venv, node_modules, v.v.) theo một danh sách exclude.
- Có chế độ dry-run (mặc định) để in ra các cặp rename mà không áp dụng.
- Tránh ghi đè: nếu tên đích đã tồn tại, bỏ qua và cảnh báo.

Cách dùng:
    python change_file_name.py            # Dry-run (không đổi tên thật)
    python change_file_name.py --apply    # Thực hiện đổi tên thật
    python change_file_name.py --root .   # Chỉ định thư mục gốc

"""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
from typing import Iterable

EXCLUDE_DIRS = {'.git', '.hg', '.svn', '.venv', 'venv', 'node_modules', '.idea', '.vscode', '__pycache__'}
TARGET_TOKEN = ' copy'
INSERT_TOKEN = '.vi'

def iter_files(root: Path) -> Iterable[Path]:
    for p in root.rglob('*'):
        if p.is_dir():
            # Skip excluded dirs early by not descending into them
            if p.name in EXCLUDE_DIRS:
                # Prevent recursion into excluded
                dirs_to_skip = [d for d in p.iterdir() if d.is_dir()]
                continue
        elif p.is_file():
            yield p

def build_new_name(file_path: Path) -> Path | None:
    name = file_path.name
    # Tìm vị trí " copy" trước phần mở rộng đầu tiên (tức dấu chấm đầu tiên từ trái sang phải sau token)
    if TARGET_TOKEN not in name:
        return None
    # Tách phần trước và sau token
    prefix, suffix = name.split(TARGET_TOKEN, 1)
    if not suffix:
        return None  # Không có phần mở rộng tiếp theo
    # Nếu suffix bắt đầu bằng '.' thì đó là phần mở rộng (có thể phức tạp: .md, .tar.gz ...). Giữ nguyên toàn bộ suffix.
    if not suffix.startswith('.'):
        # Không đúng dạng mong muốn: yêu cầu phải có .ext
        return None
    new_name = f"{prefix}{INSERT_TOKEN}{suffix}"
    if new_name == name:
        return None
    return file_path.with_name(new_name)

def should_skip(path: Path) -> bool:
    # Bỏ qua nếu bất kỳ phần nào trong parts thuộc EXCLUDE_DIRS
    return any(part in EXCLUDE_DIRS for part in path.parts)

def process(root: Path, apply: bool) -> int:
    count = 0
    for fp in iter_files(root):
        if should_skip(fp):
            continue
        new_path = build_new_name(fp)
        if not new_path:
            continue
        if new_path.exists():
            print(f"[WARN] Bỏ qua vì đã tồn tại: {new_path}")
            continue
        print(f"{'RENAME' if apply else 'DRY-RUN'}: {fp} -> {new_path}")
        if apply:
            try:
                fp.rename(new_path)
                count += 1
            except OSError as e:
                print(f"[ERROR] Không thể đổi tên {fp}: {e}", file=sys.stderr)
        else:
            count += 1
    return count

def parse_args():
    parser = argparse.ArgumentParser(description='Đổi tên các file chứa " copy" thành thêm hậu tố .vi trước phần mở rộng.')
    parser.add_argument('--root', type=Path, default=Path('.'), help='Thư mục gốc để quét (mặc định: .)')
    parser.add_argument('--apply', action='store_true', help='Thực hiện đổi tên thật (mặc định chỉ dry-run).')
    return parser.parse_args()

def main():
    args = parse_args()
    root = args.root.resolve()
    if not root.exists() or not root.is_dir():
        print(f"Thư mục không hợp lệ: {root}", file=sys.stderr)
        sys.exit(1)
    apply = args.apply
    total = process(root, apply)
    print(f"Tổng số file {'đã đổi tên' if apply else 'sẽ đổi tên'}: {total}")

if __name__ == '__main__':
    main()
