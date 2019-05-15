from math import ceil, log10
from tensorflow.python.keras.backend import binary_crossentropy, softmax
from tensorflow.python.keras.engine.sequential import Sequential
from tensorflow.python.keras.layers import LSTM, RepeatVector, TimeDistributed, Dense
from tensorflow.python.keras.metrics import accuracy
from tensorflow.python.keras.optimizer_v2 import adam

from src.utilities.converter import Converter
from src.utilities.generator import Generator

generator = Generator()
converter = Converter()

samples = 200000
numbers = 2
epoch = 50
batch = 100
num_chars = converter.char_len()
largest = converter.max_value()

n_out_seq_length = ceil(log10(numbers * (largest + 1)))

model = Sequential([
    LSTM(100, input_shape=(converter.max_number_length, num_chars)),
    RepeatVector(n_out_seq_length),
    LSTM(50, return_sequences=True),
    TimeDistributed(Dense(1, activation=softmax))
])

model.compile(loss=binary_crossentropy, optimizer=adam, metrics=[accuracy])
for i in range(epoch):
    x, y = generator.build_sample(samples, largest)
    model.fit(x, y, epochs=1, batch_size=batch)

model.save('training/classifier.h5')

# evaluate on some new patterns
x, y = generator.build_sample(samples, largest)
result = model.predict(x, batch_size=batch, verbose=0)

# calculate error
expected = [converter.invert(x) for x in y]
predicted = [converter.invert(x) for x in result]
# show some examples
for i in range(20):
    print('Expected=%s, Predicted=%s' % (expected[i], predicted[i]))
