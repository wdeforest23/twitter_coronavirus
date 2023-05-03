# Coronavirus twitter analysis

## Background
This project scans all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media. This project was completed as an assignment in Claremont McKenna College's CS046 Data Structures and Algorithms course taught by Mike Izbicki. 

It uses the MapReduce divide-and-conquer paradigm to create parallel code and handle large quantities of data.

## Background

**About the Data:**

Approximately 500 million tweets are sent everyday.
Of those tweets, about 2% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
The data set used in this project contains all geotagged tweets that were sent in 2020.
In total, there are about 1.1 billion tweets in this dataset.

## Process

I first created a `map.py` file that tracks the usage of a specific list of hashtags on both a language and country level. I created a shell script using the `nohup` and `&` operator to ensure that my program continued to run after I disconnected and that all the commands ran in parallel.

Next, I used a provided `reduced.py` file to combine all of the language files into a single file and all of the country files into a single file.

To create the first four plots seen below, I then modified a `visualize.py` file to output the bar charts.

Lastly, I created the `alternative_reduce.py` file to produce the line chart seen in the fifth figure.
 
## Results and Figures

![Coronavirus Hashtag Usage by Language](lang_coronavirus_barchart.png)

This figure displays the total number of times the hashtag `#coronavirus` was used during 2020 in each of the languages supported by twitter. As we can see, `#coronavirus` is tweeted in english by far the most amount of times.

![코로나바이러스 Hashtag Usage by Language](lang_korean_barchart.png)

This figure displays the total number of times the korean hashtag `#코로나바이러스` was used during 2020 in each of the languages supported by twitter. As we can see, `#코로나바이러스` is tweeted in Korean the most often.

![Coronavirus Hashtag Usage by Country](country_coronavirus_barchart.png)

This figure displays the total number of times the hashtag `#coronavirus` was used durin 2020 in each of the countries supported by twitter. The figure shows that `#coronavirus` is tweeted in the United States the most, followed by India, then Great Britain.

![코로나바이러스 Hashtag Usage by Country](country_korean_barchart.png)

This figure displays the total number of times the korean hashtag `#코로나바이러스` was used during 2020 in each of the countries supported by twitter. The figure shows that `#코로나바이러스` is tweeted in South Korea the most, followed by Hong Kong, then Spain.

![coronavirus, nurse, and covid2019 Hastag Usage Level During 2020](Alternative_reduce_plot.png)

This figure displays the number of times '#coronavirus', '#nurse', and '#covid2019' were tweeted each day during 2020. It is interesting to see that '#covid2019' follows a similar timeline to '#coronavirus' and that '#nurse' appears to peak about a month after the peak of '#coronavirus' and '#covid2019'. This might be due to the increased demand for nurses caused by the virus.
