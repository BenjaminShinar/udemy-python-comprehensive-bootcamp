<!--
// cSpell:ignore Kaggle jupyterlab
-->

[previous](section_26_27_api_crud.md)\
[main](../README.md)

## Section 28: Data Science

<!-- <details> -->
<summary>
//TODO: add Summary
</summary>

### What is Data Science

many definitions of data science

> "data science is the study of data"
>
> - Recording data
> - Storing data
> - Analyzing data to extract useful information.

neighboring fields:

- data engineering
- statistics
- business analysts

getting information and knowledge from data. not the same as data engineering, data science is about the data processing, rather than the data flow. the two fields work together.

statisticians rely on more traditional methods, usually with limited and smaller scale data, data science involves dealing with large data (BIG DATA), as well as more infrastructure and automation tasks.

examples

> - analyzing nasa pictures to find new planets or asteroids
> - using automation to pilot planes, cars
> - book recommendations on amazon, friends recommendation on facebook.
> - computational chemistry models to simulate new molecules.
> - estimating house values and prices
> - matching adds to users
> - fraud detection
> - weather forecasts

### Impact of Data Science

some fields that get benefits from data science

- customer service
- navigation
- product recommendation
- voice to text
- image processing
- fraud detection
- robotics
- health care

### Data Science Life Cycle

1. formulate a question or problem
2. acquire and clean relevant data
3. exploratory data analysis
4. draw conclusions using predictions

### Data Science Terminologies

_Modules_ are reusable collections of code. _Libraries_ are made from modules. in this course we will use libraries such as **Numpy**, **Pandas** and **Seaborn**

a _Dataset_ is a collection of related sets of information. a pandas DataFrame is a two-dimensional data structure (tabular data). it has rows, columns and the data itself. a _panda series_ is a single column of data.

```py
players = pd.Series(df['Name']) # column name
teams = pd.Series(df['Team']) # column name
```

### Data Design and Probability Sampling

data design is how we gather our data, probability sampling methods are different ways that we can use to reduce bias in our data.

Simple Random sampling (SRS)\
Taking elements by random (without repetition) from the population.

Cluster Sampling\
dividing the data into clusters, and then choosing clusters at random. an example of a cluster can be a family, a school or any other unit that holds elements.

Stratified Sampling\
dividing the population into stratas, and then sample from each strate according to the desired weight. an example of strata can be gender, age, or any other trait that an observation has. stratified sampling can ensure that all relevant groups are represented in the data.

### What is Jupyter Notebook

jupyter notebook is a computing environment to experiment and share code.
Jupyter stands for Julia, Python and R, as the three languages which were first supported in jupyter notebooks.

the notebooks contains,live code, rich text, interactive widget and media.

### Installing Jupyter Notebook Server

we first install [anaconda](https://www.anaconda.com/), the package manager which is used in many data science projects.
we can also use pip to install jupyter notebook.

```sh
pip install -upgrade pip
pip install jupyter
pip install jupyterlab

```

### Running Jupyter Notebook Server

starting jupyter notebook

```sh
jupyter notebook
```

this will open the notebook on the browser.

### Common Jupyter Notebook Commands

| command                 | description                                      | flags          |
| ----------------------- | ------------------------------------------------ | -------------- |
| `jupyter notebook`      | start the jupyter application                    | `--no-browser` |
| `jupyter --help`        | help                                             |
| `jupyter --config-dir`  | show the location of the configuration directory |
| `jupyter --data-dir`    | show the location of the data directory          |
| `jupyter --runtime-dir` | show the location of the runtime directory       |
| `jupyter --paths`       | list all jupyter directories and search paths    | ` --json`      |

### Jupyter Notebook Components

### Jupyter Notebook Dashboard

### Jupyter Notebook User Interface

### Creating a new Notebook

### Kaggle Data Sets

### Tabular Data

### Exploring Pandas DataFrame

### Manipulating a Pandas DataFrame

### What is Data Cleaning

### Basic Data Cleaning Process

### Data Visualization

### Visualizing Qualitative Data

</details>

## Section 29: Machine Learning
