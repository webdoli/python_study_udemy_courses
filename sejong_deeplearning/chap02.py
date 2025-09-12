import tensorflow as tf
import numpy as np
import tensorflow_datasets as tfds


ds = tfds.load('mnist', split='train', shuffle_files=True)


num_elements = tf.data.experimental.cardinality(ds).numpy()
print(f'Number of elements in the dataset: {num_elements}')
