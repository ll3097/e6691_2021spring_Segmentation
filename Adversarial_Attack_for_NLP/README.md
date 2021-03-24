# Adversarial_Attack_for_NLP Repository

This directory contains example code for the the Adversarial Attack for NLP / TextAttack models. 

## Presentation Slides
Our presentation slides can be found in the `E6691.2021Spring.StudentLogsPresentationsAndProjects` folder with the name `PaperReview.ac4788.tx2208.Adversarial_Attack_for_NLP`.

## Related Work
Our presentation mainly covered Vanilla RNN, LSTM, GRU, Seq2Seq models and the attention mechanism. Some of the recommended readings are:

- [LONG SHORT-TERM MEMORY](http://www.bioinf.jku.at/publications/older/2604.pdf) (original LSTM paper)
- [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/pdf/1409.3215.pdf) (original seq2seq NMT paper)
- [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473.pdf) (original seq2seq+attention paper)

More related blogs and tutorials can be found in the references section.


## Code Demo

In this repo, we included the following demo codes:

### Augmentations.ipynb
Jupyter notebook shows how to Augmenting a dataset using TextAttack.

### End_to_End.ipynb: 
Jupyter notebook contains the tutorial for a broad end-to-end overview of training, evaluating, and attacking a model using TextAttack.

### Example_tensorflow.ipynb:
Jupyter notebook contains a demo for implementing the TextAttack on a text classification model using TensorFlow. It contains two parts: training and attacking.

### Introduction_and_Transformations(BananaWordSwap).ipynb
Jupyter notebook contains a basic introduction for TextAttack and a simple example of using transformations to create adversarial attack.

### TextAttack Demo.ipynb
Jupyter notebook contains basic installation for TextAttack and how to use command line to utilize TextAttack for attacking, training and evaluation. 

### models
A folder contains the pre-trained models that TextAttack includes. 

### Additional resources:

- [Full TextAttack Details in Github](https://github.com/QData/TextAttack )


## Questions?

For any questions, please feel free to contact Chelsea Cui (ac4788@columbia.edu), Tong Xue (tx2208@columbia.edu).

## References

[1] Morris, J. X., Lifland, E., Yoo, J. Y., Grigsby, J., Jin, D., & Qi, Y. (2020). TextAttack: A Framework for Adversarial Attacks, Data Augmentation, and Adversarial Training in NLP.

[2] https://www.dropbox.com/s/s7rr3fnfmnfg6bp/2020-07-30%20TextAttack.pdf?dl=0

[3] https://github.com/QData/TextAttack 

[4] I. J. Goodfellow, J. Shlens, and C. Szegedy, “Explaining and harnessing adversarial examples,” in Proceedings of the International Conference on Learning Representations, 2015.

[5] A. Ilyas, S. Santurkar, D. Tsipras, L. Engstrom, B. Tran, and A. Madry, “Adversarial examples are not bugs, they are features,” arXiv preprint arXiv:1905.02175, 2019.

[6] Bin Liang, Hongcheng Li, Miaoqiang Su, Pan Bian, Xirong Li, and Wenchang Shi. 2017. Deep Text Classification Can be Fooled. arXiv preprint arXiv:1704.08006 (2017)

[7] Towards a Robust Deep Neural Network in Texts: A Survey. Wenqi Wang, Lina Wang, Benxiao Tang, Run Wang, Aoshuang Ye. arXiv 2020. 

[8] Adversarial Attacks on Deep Learning Models in Natural Language Processing: A Survey. Wei Emma Zhang, Quan Z. Sheng, Ahoud Alhazmi, Chenliang Li. ACM TIST 2020.

[9] Generating Natural Language Adversarial Examples. Moustafa Alzantot, Yash Sharma, Ahmed Elgohary, Bo-Jhang Ho, Mani Srivastava, Kai-Wei Chang. EMNLP 2018. 
