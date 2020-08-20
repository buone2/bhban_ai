"""
Author : Byunghyun Ban
Date : 2020.07.24.
"""
from tensorflow import keras
import data_reader


# 몇 에포크 만큼 학습을 시킬 것인지 결정합니다.
EPOCHS = 2  # 예제 기본값은 20입니다.

# 데이터를 읽어옵니다.
dr = data_reader.DataReader()

# 인공신경망을 제작합니다.
# 총 3층짜리 신경망입니다.
graph = keras.Sequential([
    keras.layers.Dense(20000),
    keras.layers.Dense(2048, activation="relu"),
    keras.layers.Dropout(rate=0.5),
    keras.layers.Dense(256, activation="relu"),
    keras.layers.Dropout(rate=0.5),
    keras.layers.Dense(4, activation='softmax')
])

# 인공신경망을 컴파일합니다.
graph.compile(optimizer="adam", metrics=["accuracy"],
              loss="sparse_categorical_crossentropy")

# 인공신경망을 학습시킵니다.
print("\n\n************ TRAINING START ************ ")
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
history = graph.fit(dr.train_X, dr.train_Y, epochs=EPOCHS,
                    validation_data=(dr.test_X, dr.test_Y),
                    callbacks=[early_stop])

# 학습 결과를 그래프로 출력합니다.
data_reader.draw_graph(history)
