import kagglehub

# Download latest version
path = kagglehub.dataset_download("sovitrath/diabetic-retinopathy-224x224-2019-data", path='colored_images/Mild/0024cdab0c1e.png')

print("Path to dataset files:", path)