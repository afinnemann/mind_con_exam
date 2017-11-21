library(tidyverse)
setwd("~/cogsci/Mind and consciousness/exam/python")

files <- list.files(path = "threat_data", full.names = T)

test <- read.csv(files[1], header = T, sep = ";")

da <- tibble(files) %>% 
  mutate(data =  lapply(files, read.csv, sep = ";")) %>% 
  unnest() %>%
  mutate(ID = as.factor(ID)) %>% 
  select(ID,everything())


media_time <- da %>%  group_by(ID) %>% summarise(media_time = mean(media_time, na.rm =T),
                                                 sleep = median(sleep, na.rm = T),
                                                 rating_EB = median(rating_EB, na.rm = T),
                                                 rating_politiken = median(rating_politiken, na.rm = T),
                                                 rating_MX = median(rating_MX, na.rm = T),
                                                 rating_weekend_a = median(rating_weekend_a, na.rm = T),
                                                 pets = median(pets, na.rm =T),
                                                 blue_eyes = median(blue_eyes, na.rm = T),
                                                 countryside = median(countryside, na.rm = T),
                                                 hayfever = median(hayfever, na.rm = T),
                                                 infertility = median(infertility, na.rm = T))

df <- da %>% 
  select(ID, files,t_story, t_story_rating, n_story_rating, topic, rt_response, rt_text, Nationality, block_order, condition, gender, n_story) %>% 
    merge( media_time, by ="ID")

df <- df %>% 
  mutate(pets =as.factor(pets),
         infertility =as.factor(infertility),
         hayfever =as.factor(hayfever),
         blue_eyes =as.factor(blue_eyes),
         sleep =as.factor(sleep))

df <- df %>% 
          mutate(pets = recode(pets, "1" = "threat", "2" = "safe"),
                 infertility = recode(infertility, "1" = "threat", "2" = "safe"),
                 countryside= recode(countryside, "1" = "threat", "2" = "safe"),
                 hayfever = recode(hayfever, "1" = "threat", "2" = "safe"),
                 blue_eyes = recode(blue_eyes, "1" = "threat", "2" = "safe"),
                 sleep = recode(sleep, "1" = "threat", "2" = "safe"),
                 topic = recode(topic, "Blue-eyed" = "blue_eyes", "Hayfever" = "hayfever"))
  


 per_story <-df %>% 
  filter(is.na(condition) & !is.na(topic)) 
  
 test <- per_story %>% 
    group_by(ID, topic) %>% 
    select(pets, infertility, countryside, hayfever, blue_eyes, sleep) %>% 
    gather(key, value, pets:sleep) %>% 
    ungroup %>% 
    select(ID, key, value) %>% 
    unique() 

 colnames(test) = c("ID","topic","threat")
 
 per_long = merge(test, per_story) %>% 
   select(ID,topic,threat,t_story_rating)
 
  
 t_story <-df %>% 
   filter(!is.na(condition)) %>% 
   select(topic, ID, t_story_rating) %>% 
   mutate(value = "threat")
   colnames(t_story) = c("topic","ID", "rating", "threat")
 
 n_story <-df %>% 
   filter(!is.na(condition)) %>% 
   select(topic, ID, n_story_rating) %>% 
   mutate(value =" safe") 
   colnames(n_story) = c("topic","ID", "rating","threat")
 
 t_long <- rbind(t_story, n_story)
 
 colnames(per_long) = c("ID","topic","threat","rating")
 
 full = rbind(per_long, t_long) 
 
 
 long_df <- merge(full, df, by = c("ID","topic")) %>% 
   select(ID, topic, threat, rating) %>% 
   mutate(news_paper = recode(rating, "1" = "MX", "2" = "Politiken", "3" = "EB", "4" = "WA"))
        
 
 newspaper <- per_story %>% 
   group_by(ID) %>% 
   select(ID, rating_EB, rating_politiken, rating_MX, rating_weekend_a) %>% 
   gather(key, value, rating_EB:rating_weekend_a) %>% 
   ungroup %>% 
   select(ID, key, value) %>% 
   unique() %>% 
   mutate(key = as.factor(key),
          key = recode(key, "rating_EB" ="EB", "rating_politiken" = "Politiken",
                            "rating_MX" = "MX", "rating_weekend_a" = "WA"))
 
 colnames(newspaper) = c("ID", "news_paper","competence")

 long_df2 = merge(newspaper, long_df, by = c("ID","news_paper"))  %>% 
   mutate(threat = as.factor(threat),
          threat = recode(threat, "safe" = " safe"))
 
 subset <- df %>% 
   select(ID, topic, Nationality, condition, block_order, gender, media_time,rt_response, rt_text)
 
 long_df3 <- merge(subset, long_df2, by = c("ID","topic")) %>% 
   mutate(type = ifelse(is.na(condition), "person", "contrast"))

  #write.csv(long_df3, "preprocessed_data.csv")
