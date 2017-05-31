import os
from six.moves import urllib
import zipfile
import tensorflow as tf
import collections
import csv

class DatasetLoader:
    def __init__(self):
        self.url = 'http://mattmahoney.net/dc/'
        filename = self._maybe_download('text8.zip', 31344016)
        self._words = self._read_data(filename)

    def _maybe_download(self, filename, expected_bytes):
      """Download a file if not present, and make sure it's the right size."""
      if not os.path.exists(filename):
        filename, _ = urllib.request.urlretrieve(self.url + filename, filename)
      statinfo = os.stat(filename)
      if statinfo.st_size == expected_bytes:
        print('Found and verified', filename)
      else:
        print(statinfo.st_size)
        raise Exception(
          'Failed to verify ' + filename + '. Can you get to it with a browser?')
      return filename

    # Read the data into a list of strings.
    def _read_data(self, filename):
      """Extract the first file enclosed in a zip file as a list of words"""
      with zipfile.ZipFile(filename) as f:
        data = tf.compat.as_str(f.read(f.namelist()[0])).split()
      return data

    def build_dataset(self, vocabulary_size):
      count = [['UNK', -1]]
      count.extend(collections.Counter(self._words).most_common(vocabulary_size - 1))
      dictionary = dict()
      for word, _ in count:
        dictionary[word] = len(dictionary)
      data = list()
      unk_count = 0
      for word in self._words:
        if word in dictionary:
          index = dictionary[word]
        else:
          index = 0  # dictionary['UNK']
          unk_count += 1
        data.append(index)
      count[0][1] = unk_count
      reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
      return data, count, dictionary, reverse_dictionary


if __name__=='__main__':
    vocabulary_size = 50000
    loader = DatasetLoader()
    data, count, dictionary, reverse_dictionary = loader.build_dataset(vocabulary_size)
    word_strs = [[v] for v in reverse_dictionary.values()]
    print(len(reverse_dictionary.values()))
    with open('tb_files/metadata.tsv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(word_strs)