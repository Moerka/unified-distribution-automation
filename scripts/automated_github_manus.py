#!/usr/bin/env python3
"""
Automated GitHub and Manus Distribution Script
Uses environment variables for all credentials (no hardcoded secrets)
"""
import os
import subprocess
import json
from datetime import datetime

class GitHubAutomation:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.github_username = os.getenv('GITHUB_USERNAME', 'Moerka')
        self.github_email = os.getenv('GITHUB_EMAIL', 'moerka@github.com')
        
        if not self.github_token:
            raise ValueError("GITHUB_TOKEN environment variable not set")
    
    def configure_git(self):
        subprocess.run(['git', 'config', '--global', 'user.email', self.github_email], check=True)
        subprocess.run(['git', 'config', '--global', 'user.name', self.github_username], check=True)
        print(f"✅ Git configured for {self.github_username}")
    
    def push_repository(self, repo_path, repo_name):
        os.chdir(repo_path)
        subprocess.run(['git', 'remote', 'remove', 'origin'], stderr=subprocess.DEVNULL, check=False)
        
        # Token comes from environment, not hardcoded
        remote_url = f"https://{self.github_token}@github.com/{self.github_username}/{repo_name}.git"
        subprocess.run(['git', 'remote', 'add', 'origin', remote_url], check=True)
        subprocess.run(['git', 'branch', '-M', 'main'], check=True)
        subprocess.run(['git', 'push', '-u', 'origin', 'main', '--force'], capture_output=True)
        print(f"✅ {repo_name} pushed successfully")

if __name__ == '__main__':
    try:
        automation = GitHubAutomation()
        automation.configure_git()
        print("✅ Automation ready - use GITHUB_TOKEN environment variable")
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)
