## Projet datacuisiniers : How to quantify the actors success ? ##

# Abstract : #
Using the CMU Movie Summary Corpus dataset, we want to dive into the drivers of an actor's success. Since the aspiration to become an actor is a dream for many, uncovering the factors or combinations of factors that contribute to an actor's accomplishment can provide valuable insights.

However, quantifying an actor's success is inherently subjective, because there are numerous ways to assess it. Some seek peer recognition through awards, others prioritize financial gains, positive ratings, public attendance, or long-lasting careers. Given these diverse goals we consider, the factors driving success may differ.

Through our analysis, we aim to offer a nuanced understanding of what drives an actor’s accomplishments. Ultimately, we want to allow our readers to identify the attributes maximizing a specified success indicator and to predict their success across all dimensions based on input features.

# Research questions : #
- What are the different ways to be successful and are they correlated?
- What drives these different dimensions of success?
- How much do personal characteristics matter (age, gender, height, etc)?
- How much do movie characteristics matter (genre, country, etc)?
- Do actors achieve success by making thoughtful decisions regarding their careers, such as selecting specific countries or languages to work in, or by strategically choosing the genres or roles they portray in movies? Alternatively, is success primarily determined by inherent qualities and characteristics?


# Proposed additional datasets : #
- [Oscars dataset](https://www.kaggle.com/datasets/unanimad/the-oscar-award)
- IMDb ratings
- Scraped data from Google trends score 

# Methods : #

First, we tried to find insights concerning the longevity of the actors and the number of appearances they have. We identified two main limits of this analysis : it is unequal through time and geographically. 
E plan on using regressions to see the correlation between our variables and success indices, including interactions of relevant variables (eg. age may matter more for women than men). We will look at R squared to see what models explains most of someone’s success.

Supervised ML methods will help us predict success from input features and create an interactive tool where users choose their input and how they view success.

//insert other parts

# Timeline : #

Until the end of P2 : Each team member works on their definition of success

End of november : 
We group our analysis and see whether there are trade-off in success. Do the same features guarantee success along many dimensions? 
Based on our results, work on interactive tools described above

December : Text and writing of the story

//insert Gantt diagram

| Task                        | Start Date | End Date   |
|-----------------------------|------------|------------|
| Until the End of P2         |  -         | P2 Deadline|
| Define Success Criteria     |  -         | P2 Deadline|
| End of November Analysis    | P2 Deadline| End of Nov  |
| Group Analysis              | End of Nov | End of Nov  |
| Develop Interactive Tools   | End of Nov | End of Nov  |
| December Writing            | Dec 1      | Dec 31     |
| Finalize Project             | Dec 31     | Dec 31     |

# Organization within the team : #

  | Nutsa | Anaëlle | Pascal | Quentin | Malo |
|----------|----------|----------|----------|----------|
| Revenues | Awards | Ratings | Trends | Longevity |
| Plot analysis | Row 2, Col 2 | Row 2, Col 3 | Row 2, Col 3 | Row 2, Col 3 |
  

ada-2023-project-datacuisiniers created by GitHub Classroom
