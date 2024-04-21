import os
import time
from urllib.parse import quote

def generate_md_toc(root_dir):
    toc = ""
    for root, dirs, files in os.walk(root_dir):
        # 忽略.assets结尾的文件夹和.git文件夹及其子文件夹
        if os.path.basename(root).endswith(".assets") or ".git" in root.split(os.path.sep):
            continue
        # 忽略没有.md文件的文件夹
        has_files = [f for f in files]
        if not has_files:
            continue
        # 当前目录和README文档不作为标题
        if root == root_dir or "README.md" in has_files:
            continue
        # 大标题为文件夹名
        toc += f"### {os.path.basename(root)}\n"
        for file in sorted(has_files):
            # 文件名作为小标题，去掉扩展名
            title = os.path.splitext(file)[0]
            # 相对路径，并进行URL编码
            relative_path = quote(os.path.relpath(os.path.join(root, file), root_dir))
            # 添加链接
            toc += f"  - [{title}](Android/{relative_path})"
            # 获取文件上次修改时间
            last_update_time = time.strftime(" _Last updated: %Y-%m-%d %H:%M:%S_", time.localtime(os.path.getmtime(os.path.join(root, file))))
            # 在文件链接后面添加上次更新时间的备注
            toc += last_update_time + "\n"
    return toc

def write_to_readme(toc):
    with open("README.md", "w") as f:
        f.write(toc)

def main():
    root_dir = "."
    toc = generate_md_toc(root_dir)
    write_to_readme(toc)

if __name__ == "__main__":
    main()

input()
