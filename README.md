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

We plan on using regressions to see the correlation between our variables and success indices, including interactions of relevant variables (eg. age may matter more for women than men). We will look at R squared to see what models explains most of someone’s success.

Supervised ML methods will help us predict success from input features and create an interactive tool where users choose their input and how they view success.



### Personna Analysis

A comprehensive method to gauge an actor's performance and success involves assessing the diversity of personas and character types they can convincingly portray. One effective approach for this analysis draws inspiration from the research paper titled "Learning Latent Personas of Film Characters" by David Bamman, Brendan O’Connor, and Noah A. Smit.
The study proposes utilizing the Dirichlet persona model to extract personas from agent verbs, patient verbs, and attributes associated with a character. The Dirichlet model employs soft clustering on words to create topics based on contextual similarity. This soft clustering extends from topics to personas, enabling a subsequent hard clustering from characters to personas.
By associating a specific persona type with a character, it becomes possible to analyze the range of personas embodied by the actor. This analysis involves evaluating the number of persona clusters in which the actor has played a role. Subsequently, correlations can be drawn between the actor's success score and the diversity of personas they have convincingly portrayed. This approach provides a nuanced understanding of an actor's versatility and its potential impact on their overall success in the industry.

### Longevity Analysis

Another possibility to take into account to model an actor’s success can be through its longevity in the movie industry. In fact, we are trying to identify correlations between an actor's movie count, career span, and appearance frequency in films. This analysis addresses potential limitations related to geographical location (country of distribution), gender and historical periods, but we will try to make regression between them after having insights about the datas.

# Timeline : #

| Task                        | Start Date | End Date   |
|-----------------------------|------------|------------|
| Define Success Criteria and first analyses   |  -         | P2 Deadline|
| Continue Analysis of Success incorporating feedback  | P2 Deadline| 24 Nov |
| Grouping of our Analysis    | 24 Nov | 30 Nov  |
| Develop Interactive Tools   | 30 Nov | 15 Dec  |
| Develop the storyline       | 30 Nov     | P3 Deadline    |
| Finalize Project and Webpage    | 15 Dec   | P3 Deadline   |

# Organization within the team : #

| Teammate                        | Analysis | Steps   |
|-----------------------------|------------|------------|
| Nutsa          | Revenues      | 
1) plot analysis
2) insights
3) test      |
| Anaëlle        | Awards        | 
1) awards analysis 
2) insights
3) test     |
| Pascal         | Ratings       | 
1) ratings
2) insights
3) test      |
| Quentin        | Trends        | 
1) Google trends
2) insights
3) test    |
| Malo           | Longevity     | 
1) Preprocessing data for longevity analysis
2) Frequency, career span and number of movies plots
3) Regression and combination between factors |

  

ada-2023-project-datacuisiniers created by GitHub Classroom
