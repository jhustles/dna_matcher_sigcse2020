# Matching Short Tandem Repeats (STR) in Human DNA Using Python & The Command Line

![intro1](./images/intro1.png)
![intro2](./images/intro2.png)
![intro3](./images/intro3.png)



## About This Project
Our project consists of two components:

-  Build a Supervised machine learning (ML) classification model that can predict whether a person innately is a striker or grappler based on a set of user inputs
- Webscraping the UFC's Fighter Stats Section, transforming the data, and creating meaningful visualizations
  
One of the most efficient ways to discover this about a person (without having to actually throw them into an octagon to fight) is by engaging their mind with a hypthetical scenario, and surveying them. With that said, we created ML model to make predictions based on a set of user inputs on the backend, and created a survey on the frontend. Our ML model that we designed uses UFC fighter data related to strikes and grappling metrics including: estimated timed on each activitiy, both attempts and landed for volume and accuracy, and their win-by and lose-by methods.

As MMA fans ourselves, we understand that this a grossly oversimplification because there are a large subset of talented and unique fighters that make it truly difficult to put them in a box, let alone program a model to pinpoint styles one possesses. For the purposes of this project, our thesis is that we believe that individuals innately lean towards either being a striker or a grappler, slightly or greatly.


[Visit this project here.](https://fighterinyoumlv2-api-heroku.herokuapp.com/)
## OR Running this project locally - System Prerequisites
* Python >= 3.6 and the associated libraries:
* flask import Flask, render_template, url_for, request, redirect, jsonify
* flask_cors import CORS, cross_origin
* pandas as pd
* pickle 
* Sci-kit Learn
* joblib
* JavaScript ES6
* Survey.js
* BootStrap4
* CSS
* HTML


## I. Data Source And Preparation
 We extracted our data from two sources:
 * [ Kaggle.com's UFC Fighter Dataset - Jan 2014 - Oct 2018](https://www.kaggle.com/rajeevw/ufcdata) - the original data source has been updated, and format has changed. The original file we used is in the repository archives.

 *  [UFC Fighter Stats Section](http://ufcstats.com/statistics/fighters)

These were the best available datasets at the time. We then transformed the raw datasets using Python, Pandas, and then used MS Excel for quick percentile ranking analysis to see how figthers ranked next to each other in terms of metrics.

## II. Data Analysis
                  
After transformation of the Kaggle and webscraped datasets, we performed statistical analysis to created custom ratios to classify 1,100 fighters based on UFC fighter stats described above. We then used this output to train three different ML models, using Sci-Kit Learn. The models we analyzed were: linear regression, logistic regression, and a decision tree model. We chose the logistic regression model because it gave us 86% accuracy on both training and test data, to prevent potential overfitting.

## III. Visualization

After transforming both datasets using Python, we used Tableau to create visualizations in our analysis section. For ML model, we used a Pickle file, and a Flask app as the backend engine to render our ML model. Front-end wise, we used Survey.js, JavaScript (ES6), BootStrap4, CSS, and HTML to showcase our final product, the "Ultimate Fighter In You"ML powered survey. Stay tuned.



## Findings

Here are snapshots of all of our findings. We encourage you to [Visit our project here. ](https://fighterinyoumlv2-api-heroku.herokuapp.com/) for the final product.


### UFC Fighter Stats - Our WebScraped Data And Tableau Visualizations - July 2019

![fightingStances](./static/img/portfolio/fullsize/fightingStylePie.png)

* The most common stance is Orthodox, which is often seen with right-handed fighters. This is because by leading with their weaker left-hand and foot first, it allow the fighter to keep their strong arm loaded for a power-shot often seen in boxing. Conversely, southpaw is for most common for left-handed figthers. The least common fighting style are Open Stance and Sideways, often used by figthers with a wrestling and Karate background, respectively. By definition Open Stance is the position where your feet are facing when facing your opponent. They are squared up and the body is about a 45 degree angle to the other fighter. Sideways stance the name speaks for itself. The fighter also stands with a slight bend in their knees, and often keeps a healthy distance, enabling mobility to move in-and-out for calculated timed strikes, and even throw kicks at the head, body or legs.

![weightClasses](./static/img/portfolio/fullsize/histogramWeightClasses.png)

* The histogram illustrates the weight group with the most fighters are the 155lb to 170lb group. We can infer from the chart that if we were able to increase the population of fighters in this dataset to include fighters from all legitmate MMA promotions across the world, we would see a normal distrubtion of fighters across the weight classes.

![winsLossesDraws](./static/img/portfolio/fullsize/stackedBarWLD.png)

* This chart shows the selected top 9 figters UFC history, their total professional matches, and results. This chart at a glance and with no domain knowledge can be very misleading. One could easily percieve Travis Fulton is one of the best fighter in UFC history. However, that is far from the truth. One can argrue that Jon Jones is one of the greatest UFC fighters of all time; and he is the undisputed greatest light heavy weight champion of all time. Although the chart does show he is nearly undefeated (only lost 1 by disqualification, and another by No Contest), he holds the best and longest winning record in that division against top- tier adversaries.

![wrestlerScatter](./static/img/portfolio/fullsize/ATD_vs_TA_July2019.PNG)

![wrestlerBikiniBar](./static/img/portfolio/fullsize/wrestlerAllTime_big.png)

* As the number of Average Takedowns Completed increases, you see wavering trend of Average Takedown Accuracy percentage, suggesting moderate relationship between the two measures. However, in the middle of the chart illustrates that wrestlers who completed half as many takedowns compared to the fighters at the top, tend to be more accurate. Unless the figther is in the top 20% of wrestlers, we can infer that those who choose to be more patient in setting up, and selective with takedown opportunities, are likelier to experience a higher success rate.

![strikingScatter](./static/img/portfolio/fullsize/StrikingAttemptsLandedvsAccuracy.PNG)

* The key take away is that Strikes Landed Per Minute has a less moderate relationship with a fighter's Striking Accuracy. A possible explaination is Strikers that land the most strikes on their opponents are not not always the most accurate due to the sheer volume of attempts thrown in a round, which reduces accuracy percentage when they miss. This is also holds true in boxing as well. In the sport of MMA, any fighter has a punchers chance to win, which makes the nature of the sport very unpredictable, and statistics only tells a portion of the story without domain knowledge.

![WinningVsMeasures](./static/img/portfolio/fullsize/WinningVsSelectedMeasures.PNG)

* The data suggests that that there is not a single measure that determines winning. There are many layers to a fighter that enable them to be great, particularly their background, style, coaching, preparation, physical attributes, and raw talent. On a seperate note, this chart also provided us insight that a linear regression model may not be a suitable candidate for our ML Model.

## ML Powered Survey Using Kaggle UFC Dataset - January 2014 - October 2018

![ratios](./static/img/portfolio/fullsize/ratios.png)

* Here are all the metrics we calculated from the raw round by round UFC fight dataset from Kaggle in the Data Preparation and Analysis phases. We tested different combinations of these metrics in our ML model candidates. Majority of the time, bouts always start off with striking, so we decided to prioritize the Striking metrics as the numerator, and Grappling as the denominator for our ratios. Subsequently, we performed a Percentile Rank view where all fighters fell on a distrubtion for both attempts and time ratios. We used this to classify fighters either as Strikers or Grapplers, along with consideration of their total knockout and submission victories. We then split up 80% of this newly formed dataset to be training, and 20% to be test data for our ML model.

![parametersTested](./static/img/portfolio/fullsize/parametersTested.png)

* The key takeaway here is that we decided on using the logistic regression model, which allows us to build our model around multivariables. These are all the different combination of measures we exluded from the The Inputs, leaving us only measures we wanted to test, with notes of training and testing results. Our goal here was to select the most logical set of inputs while ensuring our model would not be prone to overfitting or memorizing, which we will go over more in The Results.

![confusionMatrix](./static/img/portfolio/fullsize/confusionMatrix.png)

* This is a Confusion Matrix we created with Python using the Seaborn library. Here we were working to understand the intricacies of our ML model. The color scale on the right from top to bottom illustrates what our machine learning model finds to be most valuable feature (tan) to the most confusing (black) when making predictions. We found that the Percent Rank of Striking to Grappling Attempts Ratio was the best indicator of predicting whether a user was a grappler or a striker at heart. We used this information when determining weights for each feature we tied to each survey question in our final product.

![results](./static/img/portfolio/fullsize/resultsUpdated_fullsize.PNG)

* Lastly, here you can see that our ML model performed consistently on both training and unseen test datasets with an 86% accuracy, which gave us confidence that our model was not overfitting. Overfitting means when the model learns and memorizes the details and noise from the training dataset, and does not generalize well to unseen data. As humans, we're making decisions in the grey everyday with the experience and data we've acquired through life. We are far from perfect and even make mistakes with tasks we've done a million times. However, if we're able to get 80% of our decisions right, let alone program a ML model to yield 86% accuracy on unseen data, I'd say we should smile and be happy with ourselves until the next iteration.


### Personal Note
* Hope you enjoyed it. Thank you for your time!

## Author

* **Johneson Giang** - Lead Developer & Analyst - [Github](https://github.com/jhustles)
* Jeffery Anthony - Data Engineer - Webscraping
* David Pham - Data Analyst

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* I definitely want to give a shout out to my dear teacher, mentor, and friend @CodingWithCorgis!
*  Thanks to BootSrapMade (https://bootstrapmade.com/) for the template.