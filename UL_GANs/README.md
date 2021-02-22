# Unsupervised Learning and Deep Generative Models

This directory holds a pytorch implementation of DCGAN and (a not particularly well-tuned) CycleGAN.

## Prerequisites
Python 3.8+

Install Requirements in `requirements.txt` via `python -m pip install -r requirements.txt`

## DCGAN [1]
Deep Convolutional Generative Adversarial Network. Uses specific CNN architecture to allow for generation of synthetic images.

## CycleGAN [2]
Cycle-Consistent Adversarial Network. Building off of DCGAN, uses cycle consistency to allow for unpaired image-to-image translation. One discriminator is trained for each image domain, and one generator is trained for each direction of translation.

## References

[1] https://arxiv.org/abs/1511.06434

[2] https://arxiv.org/abs/1703.10593
