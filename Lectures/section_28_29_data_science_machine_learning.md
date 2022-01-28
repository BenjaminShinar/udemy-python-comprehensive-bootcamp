<!--
// cSpell:ignore Kaggle jupyterlab ipynb iloc pyplot isnull neighbourhood countplot barplot
-->

[previous](section_26_27_api_crud.md)\
[main](../README.md)

## Section 28: Data Science

<details>
<summary>
Jupyter notebook and basic data science.
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

the jupyter notebook is a client-server application. the web browser is the client in the case of jupyter notebook.

- notebook web application - the interactive part.
- kernel - separate process, either python or some other languages, this handles computation.
- notebook documents - self contained document that is the representation of all the content in the notebook

### Jupyter Notebook Dashboard

lets open the notebook.

```sh
jupyter notebook
```

we can see the files, the running process, cluster, we can add files, etc

### Jupyter Notebook User Interface

- Menu
- Toolbar
- Notebook area and cells.

a cell is a block of code.

### Creating a New Notebook

a notebook has `ipynb` extension.

- code cells
- markdown cells
- raw cells - unformatted text

we can export the notebook into a format like pdf of html

### Kaggle Data Sets

[kaggle](www.kaggle.com) is a website that has many datasets which we can use.

we need to register in order to download a dataset.

- names
- new york city airbnb open data
- crime in boston

### Tabular Data

many data sets are arranged as tables, tabular data. rows and columns, csv files, or sql data.

now we will use the pandas library to read data.

```
import pandas as pd
data = pd.read_csv("file.csv")
print data
```

### Pandas DataFrame

a DataFrame is a tabular data structure where each row and column are labelled.

```py
print(type(data))

```

lets start asking questions.

**what were the 5 most popular baby names in 2014 in the US?**

- slice out (filter) row for 2014
- sort rows in descending order by count
- get the top five rows

```py
data["Year"] #series
data["Year"]==2014 #logical
#data_2014 = data[data["Year"]==2014]
data_2014 = data.loc[daa['Year']==2014],:] #other option to do the same thing
data_2014_sorted = data_2014.sort_values('Count',ascending=False)
print(data_2014_sorted_top.iloc[0:5])
```

### Data Cleaning

Combing through data and transforming it to a form that we can analyze. this includes fixing the data if there are inconsistent data values, duplicates or malformed observations.

- missing values
- misspellings
- duplicates rows
- inconsistent formats.

we will use the crimes boston data. we first read it with the correct encoding and then check for missing data.

```py
import pandas as pd
crime = pd.read_csv("crime.csv", encoding='latin-1')
crime.isnull()
rows_with_missing_values= crime.isnull().any(axis=1) #panda series
crime[rows_with_missing_values]
```

now we want to drop some columns, we already have te date, so we don't need the repeated data. we also check manually for values which were spelled wrong.

```py
cleaned_crime = crime.drop(columns=['YEAR','MONTH','HOUR','LOCATION'])
cleaned_crime["OFFENSE_CODE_GROUP"].unique()
cleaned_crime["OFFENSE_DESCRIPTION"].unique()
cleaned_crime["DAY_OF_WEEK"].unique()
```

### Visualizing Qualitative Data

data visualization is taking the data and making a visual story out of it.
we will use the **matplotlib** and **seaborn** libraries.

Qualitative data is non-numeric data, it can be observed and recorded. it can nominal data, which is categorical and has no inherent order, while ordinal data has no inherit values, it does have a sensible ordering between the categories.

we will use the new york AirBnB listing data.

```py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

listings = pd.read_csv("AB_NYC_2019.csv")
listings
```

the first thing we want is a bar chart showing the amount of airbnb listings for each neighborhood.

```py
sn.countplot(x= "neighbourhood_group", data=listings)
plt.show()
```

now lets get the average price, this will show us the confidence intervals.

```py
sn.barplot(x= "neighbourhood_group", data=listings,y="price")
plt.show()
sn.barplot(x= "neighbourhood_group", data=listings,y="price", ci=False)
plt.show()
```

### Visualizing Quantitative Data

quantitative data is numerical data that can be compared: amounts or quantities. we can use histograms and scatter plots.

```py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

listings = pd.read_csv("AB_NYC_2019.csv")
listings
```

we start with a histogram of the prices, which we also label.

```py
plt.hist(listings['price'])
plt.xlabel('price (in US Dollars)')
plt.show()
```

unfortunately, the histogram doesn't tell us much, because we didn't perform proper data analysis and cleaning beforehand, so we probably have an outlier data that throws our calculations out of order.

```py
listings['price'].describe()
```

so rather than clean the data, the course sets the histogram bins.the `np.arange` function which takes we provide with three arguments, _start_,_stop_ and _step_

```py
plt.hist(listings['price'], bins=np.arrange(0, 1100, 40))
plt.xlabel('price (in US Dollars)')
plt.show()
```

the next thing we want is a scatter plot, which compares two numerical properties of the data. so lets look at which listings has more reviews based on their price?

```py
#plt.scatter(x="price", y="number_of_reviews", data=listings)
plt.scatter(x=listings["price"], y=listings["number_of_reviews"])
plt.xlabel('Price')
plt.ylabel('Number of reviews')
plt.show()
```

again, like with the histogram, we want to limit the range of prices to avoid the outliers

```py
plt.scatter(x=listings["price"], y=listings["number_of_reviews"])
plt.xlabel('Price')
plt.ylabel('Number of reviews')
plt.xlim(0,1100) #restricting the x-axis
plt.show()
```

the points are too large, so we want to make them smaller and more visible.

```py
plt.scatter(x=listings["price"], y=listings["number_of_reviews"],s=5)
plt.title("smaller points") # lets start titling our plots!
plt.xlabel('Price')
plt.ylabel('Number of reviews')
plt.xlim(0,1100)
plt.show()
```

visualizing the data makes it easier for us to discover trends, which drives further analysis of the data.

</details>

## Section 29: Machine Learning

<!-- <details> -->
<summary>
Machine Learning in Python
</summary>

### What is Machine Learning

### Machine Learning Frameworks

### Machine Learning Vocabulary

### Installing Anaconda

### Supervised machine learning

### Where Machine Learning is used

### Creating a basic house value estimator

### Using Scikit-Learn

### Loading a Dataset

### Making Predictions part 1

### Making Predictions part 2

</details>
