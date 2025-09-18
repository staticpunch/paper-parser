#!/usr/bin/env python3

import argparse
import os
from huggingface_hub import snapshot_download, repo_exists

def detect_repo_type(repo_id, token):
    if repo_exists(repo_id, repo_type="model", token=token):
        return "model"
    elif repo_exists(repo_id, repo_type="dataset", token=token):
        return "dataset"
    else:
        return "model"  # default

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo_id", required=True)
    parser.add_argument("--local_dir", required=True)
    parser.add_argument("--token", default=os.getenv("HF_TOKEN"))
    args = parser.parse_args()
    
    repo_type = detect_repo_type(args.repo_id, args.token)
    print(f"Downloading {repo_type}: {args.repo_id}")
    
    snapshot_download(
        repo_id=args.repo_id,
        repo_type=repo_type,
        local_dir=args.local_dir,
        token=args.token
    )
    
    print("Done!")

if __name__ == "__main__":
    main()
