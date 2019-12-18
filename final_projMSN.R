# change directory to the place where the data is
library("rjson")
library("dplyr")

# read in the four json files we will be working with
business <- fromJSON(paste(readLines("data/business_clean.json"),collapse=""))
business$categories <- NULL

business_df <- as.data.frame(business)
business_df$review_count <- as.numeric(business_df$review_count)
business_df$stars <- as.numeric(business_df$stars)

business_df$state

ave(business_df$stars)

user <- fromJSON(paste(readLines("data/user_clean.json"),collapse=""))
user_df <- as.data.frame(user)

review <- fromJSON(paste(readLines("data/review_clean.json"),collapse=""))
review_df <- as.data.frame(review)

# preview what is in each file
head(business_df)
head(user_df)
head(review_df)

user_df_wo_friends <- user_df

# get rid of unecessary data for now... it makes everything slow..
user_df_wo_friends$friends <- NULL
user_df_wo_friends$name <- NULL
user_df_wo_friends$elite <- NULL
user_df_wo_friends$compliment_cool <- NULL
user_df_wo_friends$compliment_hot <- NULL
user_df_wo_friends$compliment_more <- NULL
user_df_wo_friends$compliment_profile <- NULL
user_df_wo_friends$compliment_cute <- NULL
user_df_wo_friends$compliment_list <- NULL
user_df_wo_friends$compliment_plain <- NULL
user_df_wo_friends$compliment_note <- NULL
user_df_wo_friends$compliment_funny <- NULL
user_df_wo_friends$compliment_writer <- NULL
user_df_wo_friends$compliment_photos <- NULL

user_df_clean <- user_df_wo_friends

business_df$name <- NULL


##### These are our dataframes
head(user_df_clean)
head(review_df)
head(business_df)




##### now, lets transform them into a usable matrix
# links will be created based on restaurants reviewed...
# business_df will not be necessary until later on (for analysis purposes)
# as we will only be using restaurants that have been reviewed (as demonstrated by their existence within review_df)

# step 1: run through the dataset and construct an edgelist
require(igraph)
require(networkD3)
library(dplyr)



num_reviews <- nrow(review_df)
num_reviews


# join the three dfs together
merged_df <- merge(x = review_df, y = business_df, by = "business_id", all = TRUE)
merged_with_users_df <- merge(x = merged_df, y = user_df_clean, by = "user_id", all = TRUE)

# access the lists we need for our edgelist
business_ids <- merged_with_users_df$business_id
user_ids <- merged_with_users_df$user_id
citys <- merged_with_users_df$city

# create our edgelist
edgelist_place_w_person <- data.frame(user_id=user_ids, business_id=business_ids, city=citys)
head(edgelist_place_w_person)
nrow(edgelist_place_w_person)

complete_records <- na.omit(edgelist_place_w_person) 
head(complete_records)
nrow(complete_records)



citys <- complete_records$city

# subset the graph by city 
top_3_citys <- sort(summary(citys),decreasing=TRUE)[1:100]
top_3_citys
top_3_citys <- names(top_3_citys)
top_city <- c("Hudson")
second_city <- c("Pickering")
third_city <- c("Homestead") 

top_city_df <- complete_records[complete_records$city %in% top_city,]
second_city_df <- complete_records[complete_records$city %in% second_city,]
third_city_df <- complete_records[complete_records$city %in% third_city,]

top_city_m <- as.matrix(top_city_df)
second_city_m <- as.matrix(second_city_df)
third_city_m <- as.matrix(third_city_df)

####################################################################
# !!!! TOP CITY !!!!!WORK ON FIRST CITY: VEGAS !!!! TOP CITY !!!!!
####################################################################
edges <- top_city_df[,1:2]
edges$user_id <- as.vector(edges$user_id)
edges$business_id <- as.vector(edges$business_id)

# create a graph
top_city_graph <- graph.empty(directed = F)
node.out <- unique(edges$business_id) 
node.in <- unique(edges$user_id) 

top_city_graph <- add.vertices(top_city_graph,nv=length(node.out),attr=list(name=node.out),type=rep(FALSE,length(node.out)))
top_city_graph <- add.vertices(top_city_graph,nv=length(node.in),attr=list(name=node.in),type=rep(TRUE,length(node.in)))

edges_list <- c(edges[1,1], edges[1, 2])
nrow(edges)
for (idx in 2:nrow(edges))
{
  new_l <- c(edges[idx,"business_id"],edges[idx,"user_id"])
  edges_list <- c(edges_list, new_l)
}


top_city_graph <- add.edges(top_city_graph, edges_list)
top_city_graph

plot(top_city_graph, vertex.size=10, vertex.label=NA, main="inferred social network")

adj_matrix <- get.adjacency(top_city_graph)

head(adj_matrix)

###### now that we have leaders in the network, lets analyze them in comparison with some averages within the dataset

# get the average num of years "yelping_since"
# get the average of average_stars
# get the average review_count



