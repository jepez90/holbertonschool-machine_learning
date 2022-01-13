<div align=center>

***holbertonschool-machine_learning***
<hr />
 <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="Logo Python" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.MachineLearning.supervisedLearing.0x03&" alt="badget visitors"></a>
</div>

# Project: 0x03. Optimization

> Excercises about:
    <ul>
    <li>What is a hyperparameter?</li>
    <li>How and why do you normalize your input data?</li>
    <li>What is a saddle point?</li>
    <li>What is stochastic gradient descent?</li>
    <li>What is mini-batch gradient descent?</li>
    <li>What is a moving average? How do you implement it?</li>
    <li>What is gradient descent with momentum? How do you implement it?</li>
    <li>What is RMSProp? How do you implement it?</li>
    <li>What is Adam optimization? How do you implement it?</li>
    <li>What is learning rate decay? How do you implement it?</li>
    <li>What is batch normalization? How do you implement it?</li>
    </ul>


## Files in this Folder:
* <a href='0-norm_constants.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **0-norm_constants.py**</a><br />
Function ***def normalization_constants(X):*** that calculates the normalization (standardization) constants of a matrix:

* <a href='1-normalize.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **1-normalize.py**</a><br />
Function ***def normalize(X, m, s):*** that normalizes (standardizes) a matrix:

* <a href='2-shuffle_data.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **2-shuffle_data.py**</a><br />
Function ***def shuffle_data(X, Y):*** that shuffles the data points in two matrices the same way:

* <a href='3-mini_batch.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **3-mini_batch.py**</a><br />
Function ***def train_mini_batch(X_train, Y_train, X_valid, Y_valid, batch_size=32, epochs=5, load_path=&quot;/tmp/model.ckpt&quot;, save_path=&quot;/tmp/model.ckpt&quot;):*** that trains a loaded neural network model using mini-batch gradient descent:

* <a href='4-moving_average.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **4-moving_average.py**</a><br />
Function ***def moving_average(data, beta):*** that calculates the weighted moving average of a data set:

* <a href='5-momentum.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **5-momentum.py**</a><br />
Function ***def update_variables_momentum(alpha, beta1, var, grad, v):*** that updates a variable using the gradient descent with momentum optimization algorithm:

* <a href='6-momentum.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **6-momentum.py**</a><br />
Function ***def create_momentum_op(loss, alpha, beta1):*** that creates the training operation for a neural network in ***tensorflow*** using the gradient descent with momentum optimization algorithm:

* <a href='7-RMSProp.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **7-RMSProp.py**</a><br />
Function ***def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):*** that updates a variable using the RMSProp optimization algorithm:

* <a href='8-RMSProp.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **8-RMSProp.py**</a><br />
Function ***def create_RMSProp_op(loss, alpha, beta2, epsilon):*** that creates the training operation for a neural network in ***tensorflow*** using the RMSProp optimization algorithm:

* <a href='9-Adam.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **9-Adam.py**</a><br />
Function ***def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):*** that updates a variable in place using the Adam optimization algorithm:

* <a href='10-Adam.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **10-Adam.py**</a><br />
Function ***def create_Adam_op(loss, alpha, beta1, beta2, epsilon):*** that creates the training operation for a neural network in ***tensorflow*** using the Adam optimization algorithm:

* <a href='11-learning_rate_decay.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **11-learning_rate_decay.py**</a><br />
Function ***def learning_rate_decay(alpha, decay_rate, global_step, decay_step):*** that updates the learning rate using inverse time decay in ***numpy***:

* <a href='12-learning_rate_decay.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **12-learning_rate_decay.py**</a><br />
Function ***def learning_rate_decay(alpha, decay_rate, global_step, decay_step):*** that creates a learning rate decay operation in ***tensorflow*** using inverse time decay:

* <a href='13-batch_norm.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **13-batch_norm.py**</a><br />
Function ***def batch_norm(Z, gamma, beta, epsilon):*** that normalizes an unactivated output of a neural network using batch normalization:

* <a href='14-batch_norm.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **14-batch_norm.py**</a><br />
Function ***def create_batch_norm_layer(prev, n, activation):*** that creates a batch normalization layer for a neural network in ***tensorflow***:

* <a href='15-model.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **15-model.py**</a><br />
Complete the script ***15-model.py*** to write the function ***def model(Data_train, Data_valid, layers, activations, alpha=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, decay_rate=1, batch_size=32, epochs=5, save_path=&#39;/tmp/model.ckpt&#39;):*** that builds, trains, and saves a neural network model in ***tensorflow*** using Adam optimization, mini-batch gradient descent, learning rate decay, and batch normalization:
