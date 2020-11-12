import tensorflow as tf
from os import path

dataset_name = "flower_photos"
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
num_classes = 5

batch_size = 32
img_height = 180
img_width = 180

num_training_runs = 10
export_dir = path.abspath(path.join(__file__, 'saved_models'))

AUTOTUNE = tf.data.experimental.AUTOTUNE
