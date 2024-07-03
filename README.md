# Guiding sentiment analysis with hierarchical text clustering: Analyzing the German X/Twitter conversation on face masks in the 2020 COVID-19 pandemic

**Abstract**: Social media are a critical component of the information ecosystem during public health crises. Understanding the public discourse is essential for effective communication and misinformation mitigation. Computational methods can aid these efforts through online social listening. We combined hierarchical text clustering and sentiment analysis to examine the face mask-wearing discourse in Germany during the COVID-19 pandemic using a dataset of 353,420 German X (formerly Twitter) posts from 2020. For sentiment analysis, we annotated a subsample of the data to train a neural network for classifying the sentiments of posts (neutral, negative, or positive). In combination with clustering, this approach uncovered sentiment patterns of different topics and their subtopics, reflecting the online public response to mask mandates in Germany. We show that our approach can be used to examine long-term narratives and sentiment dynamics and to identify specific topics that explain peaks of interest in the social media discourse.

***Link to paper will be added soon!***

# Overview
This repository contains code we used for our paper, specifically for
- [the hierarchical clustering pipeline](hierarchical_clustering/README.md),
- [the link to the trained sentiment classifier on Hugging Face](https://huggingface.co/slvnwhrl/gbert-face-mask-sentiment),
- [and the interactive visualization of topic hierarchy](treemap_visualization/README.md).

While we cannot share the raw X (formerly Twitter) data used in our work, we want to make our research as transparent as possible and enable other researchers to try the presented approach on their data. If you have any questions, do not hesitate to contact us.
