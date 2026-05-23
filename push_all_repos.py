"""
GitHub 推送脚本 - 更新 xyz 和 apps 仓库
"""
import subprocess
import os

print("=" * 60)
print("GitHub 推送脚本")
print("=" * 60)
print()

# 1. 推送 xyz 仓库
print("[1/2] 推送 xyz 仓库")
print("-" * 60)
os.chdir(r'd:\临时\代码重构工程\longjieruankong.xyz')

subprocess.run('git add .', shell=True)
subprocess.run('git commit -m "Fix API parameters - class to class_name"', shell=True)
result = subprocess.run('git push -u origin main --force', shell=True, capture_output=True, text=True)

if result.returncode == 0:
    print("✓ xyz 仓库推送成功")
else:
    print("✗ xyz 仓库推送失败")
    print(result.stderr if result.stderr else result.stdout)
print()

# 2. 推送 apps 仓库
print("[2/2] 推送 apps 仓库")
print("-" * 60)
os.chdir(r'd:\临时\代码重构工程\apps')

subprocess.run('git add .', shell=True)
subprocess.run('git commit -m "Fix API parameters - class to class_name"', shell=True)
result = subprocess.run('git push -u origin main --force', shell=True, capture_output=True, text=True)

if result.returncode == 0:
    print("✓ apps 仓库推送成功")
else:
    print("✗ apps 仓库推送失败")
    print(result.stderr if result.stderr else result.stdout)
print()

print("=" * 60)
print("推送完成")
print("=" * 60)
print()
print("仓库地址：")
print("- xyz: https://github.com/CHliulongjie/longjieruankong.xyz")
print("- apps: https://github.com/CHliulongjie/zgzxHomeworkmgr")

input("\n按 Enter 键退出...")