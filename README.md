# A3R
Implementation of A#R accepted in DSAA 2022

## Description

In this paper we propose A3R, Attribute -Aware Argumentative Recommender. Our framework harnesses the power of argumentation by treating each feature as an argument that can either support, attack or neutralize a prediction. Additionally, A3R formulates feature attribution as an argumentation procedure, and each computation has explicit semantics, which makes it inherently interpretable. 

## A toy example
![A graphical representation of an argumentation procedure in a recommendation scenario. Each node represents an argument, at represents a feature of an item, the central node represents an argument "This item can be recommended to the target user". The value on the arc denotes the strength and polarity of the argument, "+" denotes supports, "-" denotes attacks, and "0" denotes neutralizes. ](https://github.com/JinfengZh/ca-fata/blob/master/figures/toy.png)

A graphical representation of an argumentation procedure in a recommendation scenario. Each node represents an argument, at represents a feature of an item, the central node represents an argument "This item can be recommended to the target user". The value on the arc denotes the strength and polarity of the argument, "+" denotes supports, "-" denotes attacks, and "0" denotes neutralizes.

## Major steps

![The major steps A3R](https://github.com/JinfengZh/a3r/blob/master/Figures/dsaa_steps.png)
## Structure of files
* data file contains the data used to generate results, to generate the training and the test set, please refer to the data_processing_frappe.ipynb for the Frappe dataset and data_processing_yelp.ipynb for the Yelp dataset.

## Executing codes

* name controls the selection of dataset, n_epochs defines the number of epochs, dim is the dimension of embedding, l2_weight is the regularization rate, lr is the learning rate.

* On the netflix dataset
```
python3 main.py --name 'netflix'
```
* On the movielens100k dataset
 ``` 
python3 main.py --name 'movielens100k' 
```
* On the mivielendevelop dataset
```
python3 main.py --name 'mivielendevelop'
```
* On the book dataset
```
python3 main.py --name 'book' 
```


## Explanation scenarios of A3R
At least three applications for generating explanations can be envisaged: 
### Toy templates
### Interactive explanations
### Contrsative explanations
