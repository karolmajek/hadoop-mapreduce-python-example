# Hadoop MapReduce Python Example
Map Reduce example for Hadoop in Python based on [Udacity: Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617)

# Download data

Use following script to download data:

`./download_data.sh`

# Input data

First ten lines of the input file using command `head data/purchases.txt`. Each line have 6 values separated with `\t`:

```
2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
2012-01-01	09:00	San Diego	Music	66.08	Cash
2012-01-01	09:00	Pittsburgh	Pet Supplies	493.51	Discover
2012-01-01	09:00	Omaha	Children's Clothing	235.63	MasterCard
2012-01-01	09:00	Stockton	Men's Clothing	247.18	MasterCard
2012-01-01	09:00	Austin	Cameras	379.6	Visa
2012-01-01	09:00	New York	Consumer Electronics	296.8	Cash
2012-01-01	09:00	Corpus Christi	Toys	25.38	Discover
2012-01-01	09:00	Fort Worth	Toys	213.88	Visa
```

# Mapper

Mapper converts each row to a **key, value** pair: category, cost.

Run code without Hadoop on first ten rows of input file `head -n 10  data/purchases.txt | python2 mapper.py`:

```
Men's Clothing	214.05
Women's Clothing	153.57
Music	66.08
Pet Supplies	493.51
Children's Clothing	235.63
Men's Clothing	247.18
Cameras	379.6
Consumer Electronics	296.8
Toys	25.38
Toys	213.88
```

# Reducer

*There is no* ***shuffle and sort*** *bewtween mapper and reducer, so it will not work the same as with Hadoop:* `head -n 10  data/purchases.txt | python2 mapper.py | python2 reducer.py`

```
Men's Clothing 	214.05
Men's Clothing 	214.05
Women's Clothing 	153.57
Women's Clothing 	153.57
Music 	66.08
Music 	66.08
Pet Supplies 	493.51
Pet Supplies 	493.51
Children's Clothing 	235.63
Children's Clothing 	235.63
Men's Clothing 	247.18
Men's Clothing 	247.18
Cameras 	379.6
Cameras 	379.6
Consumer Electronics 	296.8
Consumer Electronics 	296.8
Toys 	25.38
Toys 	239.26
```
