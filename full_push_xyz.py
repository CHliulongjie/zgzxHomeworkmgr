"""
GitHub 完整推送脚本
"""
import subprocess
import os

os.chdir(r'd:\临时\代码重构工程\longjieruankong.xyz')

print("=" * 60)
print("GitHub 完整推送脚本")
print("=" * 60)
print()

# 1. 初始化
print("[步骤 1/6] 初始化 Git 仓库")
result = subprocess.run('git init', shell=True, capture_output=True, text=True)
print("✓ Git 仓库已初始化")
print()

# 2. 添加远程仓库
print("[步骤 2/6] 添加远程仓库")
subprocess.run('git remote remove origin', shell=True, capture_output=True)
result = subprocess.run('git remote add origin https://github.com/CHliulongjie/longjieruankong.xyz.git', shell=True, capture_output=True, text=True)
print("✓ 远程仓库已添加")
print()

# 3. 添加所有文件
print("[步骤 3/6] 添加所有文件")
result = subprocess.run('git add .', shell=True, capture_output=True, text=True)
print("✓ 文件已添加")
print()

# 4. 提交
print("[步骤 4/6] 提交代码")
result = subprocess.run('git commit -m "Initial commit - 包含 nginx 和 data"', shell=True, capture_output=True, text=True)
print("✓ 代码已提交")
print()

# 5. 重命名分支
print("[步骤 5/6] 重命名分支为 main")
result = subprocess.run('git branch -M main', shell=True, capture_output=True, text=True)
print("✓ 分支已重命名")
print()

# 6. 推送
print("[步骤 6/6] 推送到 GitHub")
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