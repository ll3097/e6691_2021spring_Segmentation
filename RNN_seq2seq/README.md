# RNN_seq2seq Repository

This directory contains example code for the the RNN / Sequence-to-sequence models. 

## Presentation Slides
Our presentation slides can be found in the `E6691.2021Spring.StudentLogsPresentationsAndProjects` folder with the name `PaperReview.ac4788.tx2208.RNN/seq2seq`.

## Related Work
Our presentation mainly covered Vanilla RNN, LSTM, GRU, Seq2Seq models and the attention mechanism. Some of the recommended readings are:

- [LONG SHORT-TERM MEMORY](http://www.bioinf.jku.at/publications/older/2604.pdf) (original LSTM paper)
- [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/pdf/1409.3215.pdf) (original seq2seq NMT paper)
- [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473.pdf) (original seq2seq+attention paper)

More related blogs and tutorials can be found in the references section.


## Code Demo

In this repo, we included the following demo codes:

### seq2seq_translation_tutorial.ipynb: 
Jupyter notebook contains the tutorial for sequence-to-sequence in Pytorch. The dataset for this tutorial could be found at <https://download.pytorch.org/tutorial/data.zip>. The tutorial used the dataset 'data/eng-fra.txt' since the English to French pairs are too big to include in the repo but feel free to try yourself for the entire dataset. 

### seq2seq_with_attention_time_series.ipynb:
Jupyter notebook contains a demo for the application of Seq2Seq in solving time series problems. Two Models are discussed: a simple Seq2Seq LSTM Model, and a Seq2Seq LSTM Model with Luong Attention.


### Additional resources:

- [A Neural-Machine-Translation Project between English and Hindi](https://github.com/ArushiSinghal/Neural-Machine-Translation-English-Hindi-for-domain-data)

- [Demo for Feedforward Networks (Vanishing Gradients)](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1174/lectures/vanishing_grad_example.html)



## Questions?

For any questions, please feel free to contact Chelsea Cui (ac4788@columbia.edu), Tong Xue (tx2208@columbia.edu).

## References

[1] https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks

[2] https://lena-voita.github.io/nlp_course/seq2seq_and_attention.html

[3] https://medium.com/analytics-vidhya/intuitive-understanding-of-seq2seq-model-attention-mechanism-in-deep-learning-1c1c24aace1e

[4] https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes06-NMT_seq2seq_attention.pdf

[5] Bahdanau, D., Cho, K., & Bengio, Y. (2014). Neural machine translation by jointly learning to align and translate. arXiv preprint arXiv:1409.0473.

[6] Sutskever, I., Vinyals, O., & Le, Q. V. (2014). Sequence to sequence learning with neural networks. arXiv preprint arXiv:1409.3215.

[7] [Stanford CS224N notes](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/index.html#schedule)

[8] https://medium.com/analytics-vidhya/intuitive-understanding-of-seq2seq-model-attention-mechanism-in-deep-learning-1c1c24aace1e

[9] Luong, M. T., Pham, H., & Manning, C. D. (2015). Effective approaches to attention-based neural machine translation. arXiv preprint arXiv:1508.04025.

[10] http://colah.github.io/posts/2015-08-Understanding-LSTMs/ 

[11] https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html

[12] https://levelup.gitconnected.com/building-seq2seq-lstm-with-luong-attention-in-keras-for-time-series-forecasting-1ee00958decb

[13] Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural computation, 9(8), 1735-1780.