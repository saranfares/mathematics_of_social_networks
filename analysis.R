# change directory to the place where the data is (setwd to current directory of script... use session-> set working dir)

# packages
require(igraph)
require("rjson")

# row label data (user names): restaurant_row_labels_matrix.txt
row_names <- read.csv("data/restaurant_row_labels_matrix.txt", header=FALSE)
row_names <- as.matrix(row_names)
row_names <- t(row_names)

# column label data (restaurant names): restaurant_col_labels_matrix.txt
column_names <- read.csv("data/restaurant_col_labels_matrix.txt", header=FALSE)
column_names <- as.matrix(column_names)
column_names <- t(column_names)

# user x restaurant adj matrix: restaurant_matrix.csv
graph_data <- as.matrix(read.csv("data/restaurant_matrix.csv",row.names=row_names, col.names=column_names, header=FALSE))


# read in the cleaned json of user data in order to be able to get metadata on the users when necessary 
user <- fromJSON(paste(readLines("data/user_clean.json"),collapse=""))
user_df <- as.data.frame(user)


#agent x agent network - zero out diagonals
agent.net <- graph_data %*% t(graph_data)
diag(agent.net) <- NA

# convert the matrices into graphs
agent.g <- graph.adjacency(agent.net, mode="undirected",
                           weighted=NULL, diag=FALSE)



# TOP RANKED USERS (PPL)
## Betweenness
btwn.person <- betweenness(agent.g)
ind <- order(-btwn.person)
btwn.person[ind][1:20]
vals_to_find <- names(btwn.person[ind][1:20])
found <- user_df[user_df$user_id %in% vals_to_find,]
vals_to_find
mean(btwn.person[ind][1:20])

## Closeness
close.person <- closeness(agent.g)
ind <- order(-close.person)
close.person[ind][1:20]
vals_to_find <- names(close.person[ind][1:20])
found <- user_df[user_df$user_id %in% vals_to_find,]
vals_to_find
mean(close.person[ind][1:20])

## Eigenvector
eig.person <- evcent(agent.g)
ind <- order(-eig.person$vector)
eig.person$vector[ind][1:20]
vals_to_find <- names(eig.person$vector[ind][1:20])
found <- user_df[user_df$user_id %in% vals_to_find,]
vals_to_find
mean(eig.person$vector[ind][1:20])

## Degree
deg.person <- centr_degree(agent.g)
names(deg.person$res) <- V(agent.g)$name
ind <- order(-deg.person$res)
deg.person$res[ind][1:20]
vals_to_find <- names(deg.person$res[ind][1:20])
found <- user_df[user_df$user_id %in% vals_to_find,]
vals_to_find
mean(deg.person$res[ind][1:20])
found <- user_df[user_df$user_id %in% vals_to_find,]
found

# free up some memory 
user <- NULL
user_df$friends <- NULL
user_df$elite <-NULL


# read in the cleaned json of business data in order to be able to get metadata on the businesses when necessary
business <- fromJSON(paste(readLines("data/business_clean.json"),collapse=""))
business$categories <- NULL
business_df <- as.data.frame(business)


#group x group network - zero out diagonals
org.net<- t(graph_data) %*% graph_data
diag(org.net) <- NA

# convert the matrix into a graph
organization.g <- graph.adjacency(org.net,
                                  mode="undirected", diag=FALSE)


########### TOP RANKED BUSINESSES!!!! (restaurants)
## Betweenness
btwn.org <- betweenness(organization.g)
ind <- order(-btwn.org)
btwn.org[ind][1:20]
vals_to_find <- names(btwn.org[ind][1:20])
found <- business_df[business_df$business_id %in% vals_to_find,]
found
mean(btwn.org[ind][1:20])

## Closeness
close.org <- closeness(organization.g)
ind <- order(-close.org)
close.org[ind][1:20]
vals_to_find <- names(close.org[ind][1:20])
found <- business_df[business_df$business_id %in% vals_to_find,]
vals_to_find
mean(close.org[ind][1:20])

## Eigenvector
eig.org <- evcent(organization.g)
ind <- order(-eig.org$vector)
eig.org$vector[ind][1:20]
vals_to_find <- names(eig.org$vector[ind][1:20])
found <- business_df[business_df$business_id %in% vals_to_find,]
vals_to_find
mean(eig.org$vector[ind][1:20])


## Degree
deg.org <- centr_degree(organization.g)
names(deg.org$res) <- V(organization.g)$name
ind <- order(-deg.org$res)
deg.org$res[ind][1:20]
vals_to_find <- names(deg.org$res[ind][1:20])
found <- business_df[business_df$business_id %in% vals_to_find,]
vals_to_find
mean(deg.org$res[ind][1:20])

# free up some memory 
business <- NULL
business_df <- NULL


######## further analysis...
# first, run clustering on the org netowrk-- aka the restaurants
# to allow for a visualization of whether they all come from similar places or not in the clusters (they should)


# ONLY PLOT AFTER CLUSTERING and removing non important nodes-- dataset is WAY too big otherwise
plot(agent.g, vertex.size=2, vertex.label=NA, main="inferred user network")

