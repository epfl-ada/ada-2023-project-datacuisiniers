## Projet datacuisiniers : How to quantify the actors success ? ##

# Abstract : #
Using the CMU Movie Summary Corpus dataset, we want to dive into the drivers of an actor's success. As the aspiration to become an actor is a dream for many, uncovering the factors or combinations of factors that contribute to an actor's accomplishment can provide valuable insights. 

However, quantifying an actor's success is inherently subjective, because there are numerous ways to assess this problem. Some seek peer recognition through awards, others prioritize financial gains, positive ratings, public attendance, or long-lasting careers. Given these diverse goals, the factors driving success may differ.

Our objective is to develop a model capable of various factors, including an actor's career longevity, accumulated awards, revenue attributed to their involvement in films, and the ratings received by their movies. Considering several potential biases—such as  local cinematographic productions, historical period of activity, available data, gender, and more—we address these issues through geographical, historical, economic, and ethical analyses. Moreover, it's important to note that supplementary datasets, particularly those related to ratings and awards, might be biased too, such as a focus on awards from Western productions exclusively for example. 

Through our analysis, we aim to offer a nuanced understanding of what drives success tailored to individual preferences. Ultimately, we want to allow our readers to identify the attributes maximizing a specified success index (e.g., prioritizing 50% for revenues, 25% for winning an Oscar, and 25% for sustaining a long career) and to predict their success across all dimensions based on input features.

# Research questions : #
- What are the different ways to be successful and are they correlated?
- What drives these different dimensions of success?
- How much do personal characteristics matter (age, height etc)?
- How much do movie characteristics matter (genre, country, plot, etc)?
- Can actors make some smart choices about their career (choose a specific country/languages to work with or pick the genre/role they play in a movie) or are the determinants of success intrinsic characteristics?


# Proposed additional datasets : #
- [Oscars dataset](https://www.kaggle.com/datasets/unanimad/the-oscar-award)
- IMDb ratings
- Google trends score

# Methods : #

First, we tried to find insights concerning the longevity of the actors and the number of appearances they have. We identified two main limits of this analysis : it is unequal through time and geographically. 
E plan on using regressions to see the correlation between our variables and success indices, including interactions of relevant variables (eg. age may matter more for women than men). We will look at R squared to see what models explains most of someone’s success.

Supervised ML methods will help us predict success from input features and create an interactive tool where users choose their input and how they view success.

//insert other parts

# Timeline : #

Proposition:
Now - December: Each team member works on their definition of success
  Malo: Presence in many movies/longevity?
  Nino: Revenues
  Quentin: Google trends?
  Anaëlle: Awards?
  Pascal: Ratings

December: 
  We group our analysis and see whether there are trade-off in success. Do the same features guarantee success along many dimensions?
  Based on our results, work on interactive tools described above

December - January: Text and writing of the story

//insert Gantt diagram

# Organization within the team : #

//insert

ada-2023-project-datacuisiniers created by GitHub Classroom
