import numpy as np
import keras.backend as K
from keras.models import Model
from keras.layers import Input
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.normalization import BatchNormalization
from keras.layers.core import Flatten, Dense, Activation, Reshape
from keras.layers.convolutional import Convolution2D, Deconvolution2D, UpSampling2D
from keras.layers.pooling import AveragePooling2D, GlobalAveragePooling2D


def conv2D_init(shape, name=None):
    return initializations.normal(shape, scale=0.02, name=name)


def wasserstein(y_true, y_pred):
    return K.mean(y_true * y_pred)

def generator(noise_dim, model_name="generator"):
    gen_input = Input(shape=noise_dim, name="generator_input")

    x = Dense(128)(gen_input)
    x = Activation("tanh")(x)
    x = Dense(128)(x)
    x = Activation("tanh")(x)
    x = Dense(2)(x)

    generator_model = Model(input=[gen_input], output=[x], name=model_name)

    return generator_model


def discriminator(model_name="discriminator"):
    disc_input = Input(shape=(2,), name="discriminator_input")

    x = Dense(128)(disc_input)
    x = Activation("tanh")(x)
    x = Dense(128)(x)
    x = Activation("tanh")(x)
    x = Dense(1)(x)

    discriminator_model = Model(input=[disc_input], output=[x], name=model_name)

    return discriminator_model


def GAN(generator, discriminator, noise_dim):
    gen_input = Input(shape=noise_dim, name="noise_input")
    generated_sample = generator(gen_input)
    GAN_output = discriminator(generated_sample)

    GAN = Model(input=[gen_input], output=[GAN_output], name="GAN")

    return GAN
