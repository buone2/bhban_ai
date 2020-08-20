"""
Author : Byunghyun Ban
Date : 2020.07.24.
This code uses DCGAN sample codes from Tensorflow.org
which has Apache 2.0 License.
"""
import data_reader
import gan

# 몇 에포크 만큼 학습을 시킬 것인지 결정합니다.
EPOCHS = 100  # 예제 기본값은 100입니다.

# 데이터를 읽어옵니다.
dr = data_reader.DataReader("mnist")
#dr = data_reader.DataReader("fashion_mnist")

# GAN을 불러옵니다.
# Generator
generator = gan.make_generator()
# Discriminator
discriminator = gan.make_discriminator()

# 인공신경망을 학습시킵니다.
print("\n\n************ TRAINING START ************ ")
gan.train(generator, discriminator, dr.train_dataset, EPOCHS)

# GIF 애니메이션을 저장합니다.
gan.gif_generation()
