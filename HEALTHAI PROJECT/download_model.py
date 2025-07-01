from huggingface_hub import snapshot_download

def download_model():
    print("Downloading IBM Granite model locally...")
    snapshot_download(
        repo_id="ibm-granite/granite-3.3-2b-instruct",
        local_dir="./granite-3.3-2b-instruct",
        local_dir_use_symlinks=False
    )
    print("Download complete.")

if __name__ == "__main__":
    download_model()
