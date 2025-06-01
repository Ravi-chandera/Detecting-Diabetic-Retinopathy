import os 
import plotly.express as px

def count_images(folder_path):
  image_count = 0
  for file in os.listdir(folder_path):
    image_count+=1
  return image_count

train_folder_path_list = [
    '/content/diabetic_retinopathy_data/augmented_resized_V2/train/0',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/train/1',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/train/2',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/train/3',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/train/4'
]

train_images_class_counts = []
for folder_path in train_folder_path_list:
  train_images_class_counts.append(count_images(folder_path))


fig = px.bar(x=classes, y=train_images_class_counts, labels={'x': 'Classes', 'y': 'Value counts'}, text=train_images_class_counts)
fig.update_traces(marker_color='skyblue', hovertemplate='Class: %{x}<br>Value counts: %{y}')
fig.update_layout(title='Train set distribution')
fig.show()

val_folder_path_list = [
    '/content/diabetic_retinopathy_data/augmented_resized_V2/val/0',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/val/1',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/val/2',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/val/3',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/val/4'
]


val_images_class_counts = []
for folder_path in val_folder_path_list:
  val_images_class_counts.append(count_images(folder_path))

fig = px.bar(x=classes, y=val_images_class_counts, labels={'x': 'Classes', 'y': 'Value counts'}, text=val_images_class_counts)
fig.update_traces(marker_color='skyblue', hovertemplate='Class: %{x}<br>Value counts: %{y}')
fig.update_layout(title='Val set distribution')
fig.show()


test_folder_path_list = [
    '/content/diabetic_retinopathy_data/augmented_resized_V2/test/0',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/test/1',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/test/2',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/test/3',
    '/content/diabetic_retinopathy_data/augmented_resized_V2/test/4'
]

test_images_class_counts = []
for folder_path in test_folder_path_list:
  test_images_class_counts.append(count_images(folder_path))

fig = px.bar(x=classes, y=test_images_class_counts, labels={'x': 'Classes', 'y': 'Value counts'}, text=test_images_class_counts)
fig.update_traces(marker_color='skyblue', hovertemplate='Class: %{x}<br>Value counts: %{y}')
fig.update_layout(title='Test set distribution')
fig.show()