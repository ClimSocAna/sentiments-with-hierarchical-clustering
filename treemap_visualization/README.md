This directory contains code in the form of a jupyter notebook [treemap.ipynb](treemap.ipynb)
to reproduce the hierarchical clustering pipeline described in the paper.

> [!TIP]
> If you only want to have a look at the interactive version of the figure presented in the paper (Figure 2), you can
> also use the standalone HTML file [treemap.html](treemap.html). *Note that GitHub prevents the HTML from rendering, so you have to download the > file and then render it with your browser.*
> <br><br>Additional information such as the keywords are available
> through text hovering. In the paper, we have labeled and described specific clusters manually and these information is also
> avialble through hovering. The treemap itself is only annotated with unique identifiers that result from the original clustering
> tree (tree_level/cluster_id).

> [!IMPORTANT]
> **Installation:** We provide a `conda` configuration file to install the required packages
> ```
> conda env create -f environment.yml
> conda activate treemap-visualization
>```
> If you have alread installed the environment for the [hierarchical_clustering](../hierarchical_clustering),
> you only need to install `plotly` with
> ```
> conda install conda-forge::plotly
> ```
> Make sure to run the notebook from this folder to load the necessary files correctly.
