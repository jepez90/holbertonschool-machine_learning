<div align=center>

***holbertonschool-machine_learning***
<hr />
 <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="Logo Python" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.MachineLearning.supervisedLearing.0x02&" alt="badget visitors"></a>
</div>

# Project: 0x02. Tensorflow

> Excercises about:
    <ul>
    <li>What is tensorflow?</li>
    <li>What is a session? graph?</li>
    <li>What are tensors?</li>
    <li>What are variables? constants? placeholders? How do you use them?</li>
    <li>What are operations? How do you use them?</li>
    <li>What are namespaces? How do you use them?</li>
    <li>How to train a neural network in tensorflow</li>
    <li>What is a checkpoint?</li>
    <li>How to save/load a model with tensorflow</li>
    <li>What is the graph collection?</li>
    <li>How to add and get variables from the collection</li>
    </ul>



## Files in this Folder:

* <a href='0-create_placeholders.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **0-create_placeholders.py**</a><br />

Write the function ***def create_placeholders(nx, classes):*** that returns two placeholders, ***x*** and ***y***, for the neural network:

* <a href='1-create_layer.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **1-create_layer.py**</a><br />

Write the function ***def create_layer(prev, n, activation):***

* <a href='2-forward_prop.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **2-forward_prop.py**</a><br />

Write the function ***def forward_prop(x, layer_sizes=[], activations=[]):*** that creates the forward propagation graph for the neural network:

* <a href='3-calculate_accuracy.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **3-calculate_accuracy.py**</a><br />

Write the function ***def calculate_accuracy(y, y_pred):*** that calculates the accuracy of a prediction:

* <a href='4-calculate_loss.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **4-calculate_loss.py**</a><br />

Write the function ***def calculate_loss(y, y_pred):*** that calculates the softmax cross-entropy loss of a prediction:

* <a href='5-create_train_op.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **5-create_train_op.py**</a><br />

Write the function ***def create_train_op(loss, alpha):*** that creates the training operation for the network:

* <a href='6-train.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **6-train.py**</a><br />

Write the function ***def train(X_train, Y_train, X_valid, Y_valid, layer_sizes, activations, alpha, iterations, save_path=&quot;/tmp/model.ckpt&quot;):*** that builds, trains, and saves a neural network classifier:

* <a href='7-evaluate.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **7-evaluate.py**</a><br />

Write the function ***def evaluate(X, Y, save_path):*** that evaluates the output of a neural network:
