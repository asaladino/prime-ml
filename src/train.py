from tensorflow.python.keras.engine.sequential import Sequential
from tensorflow.python.keras.layers import LSTM, RepeatVector, TimeDistributed, Dense

model = Sequential([
    LSTM(100, input_shape=(n_in_seq_length, n_chars)),
    RepeatVector(n_out_seq_length),
    LSTM(50, return_sequences=True),
    TimeDistributed(Dense(n_chars, activation='softmax'))
])
