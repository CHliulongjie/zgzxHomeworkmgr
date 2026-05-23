"""
GitHub 更新推送脚本 - 包含 nginx 和 data 文件夹
"""
import subprocess
import os

os.chdir(r'd:\临时\代码重构工程\longjieruankong.xyz')

print("=" * 60)
print("GitHub 更新推送脚本")
print("=" * 60)
print()

# 1. 添加所有文件
print("[步骤 1/3] 添加所有文件（包括 nginx 和 data）")
result = subprocess.run('git add .', shell=True, capture_output=True, text=True)
print("✓ 文件已添加")
print()

# 2. 提交
print("[步骤 2/3] 提交代码")
commit_msg = "Update - 包含 nginx 配置和 data 数据文件夹"
result = subprocess.run(f'git commit -m "{commit_msg}"', shell=True, capture_output=True, text=True)
if result.returncode == 0:
    print("✓ 代码已提交")
    if result.stdout:
        print(result.stdout)
else:
    print("提交信息:", result.stderr if result.stderr else "无")
print()

# 3. 推送
print("[步骤 3/3] 推送到 GitHub")
print("-" * 60)

result = subprocess.run('git push -u origin main --force', shell=True, capture_output=True, text=True)
print()

if result.returncode == 0:
    print("=" * 60)
    print("✓ 成功！代码已推送到 GitHub")
    print("=" * 60)
    print()
    print("仓库地址: https://github.com/CHliulongjie/longjieruankong.xyz")
else:
    print("✗ 推送失败")
    print()
    print("错误信息:")
    print(result.stderr if result.stderr else result.stdout)

print()
input("按 Enter 键退出...")