## Projet datacuisiniers : How to quantify the actors success ? ##

# Abstract : #
Using the CMU Movie Summary Corpus dataset, we want to dive into the drivers of an actor's success. Since the aspiration to become an actor is a dream for many, uncovering the factors or combinations of factors that contribute to an actor's accomplishment can provide valuable insights.

However, quantifying an actor's success is inherently subjective, because there are numerous ways to assess it. Some seek peer recognition through awards, others prioritize financial gains, positive ratings, public attendance, or long-lasting careers. Given these diverse goals we consider, the factors driving success may differ.

Through our analysis, we aim to offer a nuanced understanding of what drives an actor’s accomplishments. Ultimately, we want to quantify the success of actors in our dataset and  allow our readers to identify the attributes maximizing a specified success metrics.

Check our [website](https://ninonutsa.github.io/ada-project-datacuisiniers/) for our datastory!

# Research questions : #
- What are the different ways to be successful and are they correlated?
- What drives these different dimensions of success?
- How much do personal characteristics matter (age, gender, height, etc)?
- How much do movie characteristics matter (genre, country, etc)?
- Do actors achieve success by making thoughtful decisions regarding their careers, such as diversifying the countries or languages to work in, or by strategically choosing the genres or personas they portray in movies?


# Proposed additional datasets : #
- [Oscars dataset](https://www.kaggle.com/datasets/unanimad/the-oscar-award)
- [IMDb ratings](https://developer.imdb.com/non-commercial-datasets/)
- Scraped data from [Google trends score](https://trends.google.com/trends/)  

# Methods : #


### Personna Analysis

A comprehensive method to gauge an actor's performance and success involves assessing the diversity of personas and character types they can convincingly portray. One effective approach for this analysis draws inspiration from the research paper titled "Learning Latent Personas of Film Characters" by David Bamman, Brendan O’Connor, and Noah A. Smit.
The study proposes utilizing the Dirichlet persona model to extract personas from agent verbs, patient verbs, and attributes associated with a character. The Dirichlet model employs soft clustering on words to create topics based on contextual similarity. This soft clustering extends from topics to personas, enabling a subsequent hard clustering from characters to personas.
By associating a specific persona type with a character, it becomes possible to analyze the range of personas embodied by the actor. This analysis involves evaluating the number of persona clusters in which the actor has played a role. Subsequently, correlations can be drawn between the actor's success score and the diversity of personas they have convincingly portrayed. This approach provides a nuanced understanding of an actor's versatility and its potential impact on their overall success in the industry.

### Ratings Analysis

The performance of an actor can greatly differ from a movie to another and it can be easily seen through the movie's ratings. Even though a rating is attributed to the movie in its globality, it can also reflect how well the actors played to some extent and we want to find out how much the movies' ratings can tell about an actor. The analysis will take into account limitations concerning the number of votes for ratings, the number of movies in which an actor has played and other parameters that can skew the data in order to quantify the success and combine the insights with the other perspectives.

### Longevity Analysis

Another possibility to take into account to model an actor’s success can be through its longevity in the movie industry. In fact, we are trying to identify correlations between an actor's movie count, career span, and appearance frequency in films. This analysis addresses potential limitations related to geographical location (country of distribution), gender and historical periods, but we will try to combine these factors to model longevity success.

### Awards analysis
To proxy peers' rcognition, we will use awards, in particular Oscars, as a success outcome. Supervised ML methods will help us predict success from features included in the dataset and highlight the important ones for getting an Oscar.

### Revenues analysis
We plan on using regressions to see the correlation between our variables and the success index of cumulated revenues. It represents all the revenues generated by movies the actor participated in, assuming that even though it is not a perfect indicator, it is proportional to the actual revenues an actor made. We will include interactions of relevant variables (eg. age may matter more for women than men).

### Google Trends Score Analysis

Success for an actor can also be seen as the fact that people are talking about him or her a lot. One way of estimating this is to see whether an actor's name is highly searched on the Internet. This can be done using the Google Trends service. One of the main difficulties with this approach is managing to extract data from Google for a hundred thousand actors. This method also suffers from certain biases. For example, an actor's name may be highly searched on the Internet for reasons unrelated to his or her acting career. As the film industry has existed since long before the Google search service was introduced, older actors find themselves disavowed by this assessment. It should also be pointed out that Google is not the only browser, so people who use other ones are under-represented in this rating.

# Timeline : #

| Task                        | Start Date | End Date   |
|-----------------------------|------------|------------|
| Define Success Criteria and first analyses   |  -         | P2 Deadline|
| Continue Analysis of Success incorporating feedback  | P2 Deadline| 8 Dec |
| Grouping of our Analysis    | 30 Nov | 8 Dec  |
| Develop Interactive Tools   | 8 Dec | 15 Dec  |
| Develop the storyline       | 30 Nov     | P3 Deadline    |
| Finalize Project and Webpage    | 15 Dec   | P3 Deadline   |

# Organization within the team : #

| Teammate | Analysis                                       | Steps                                                |
|----------|-------------------------------------------------|------------------------------------------------------|
| Nino | Plot analysis: Persona Analysis  | 1) From ccprocessed dependencies in Standford CoreNLP dataset extract the agent verbs, patient verbs, and attributes as described in the paper<br> 2) Generate couples of {(agent verbs, patient verbs, attributes), word lemma}<br> 3) apply Dirichlet model for clustering|
| Nino | Leading character classification  | 1) Analyse the frequency of the character name appearance in the plot summary<br> 2) Merge with the Characters dataset<br> 3) Separate main characters from secondary character test |
| Anaëlle | Revenues | 1) Creating cumulated movie revenues by actor <br> 2) Assessing the causal effect of movie and actor characteristics on cumulated revenues using regressions  <br> 3) Identifying and understanding the contributing features |
| Anaëlle | Awards | 1) Including datasets on Oscars <br> 2) Using supervised ML to predict awards reception <br>  |
| Pascal | Ratings | 1) Preprocessing datasets for ratings analysis<br> 2) Compute ratings for actors<br>3) Initial plots for analysis<br> |
| Quentin | TrendsGoogle | 1) Scraping of Google Trends data<br> 2) Calculate trends score<br> 3) Initial plots for analysis |
| Malo | Longevity | 1) Preprocessing data for longevity analysis<br> 2) Frequency, career span and number of movies plots<br> 3) Regression and combination between factors |

  

ada-2023-project-datacuisiniers created by GitHub Classroom
