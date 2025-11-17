from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("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"))
api.upload_folder(
    folder_path="/content/drive/MyDrive/mlops/deployment",     # the local folder containing your files
    repo_id="siddhesh1981/Bank-Customer-Churn",          # the target repo
    repo_type="space",                      # dataset, model, or space
                              # optional: subfolder path inside the repo
)
