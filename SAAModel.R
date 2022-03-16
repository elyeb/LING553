library(dplyr)
options(scipen = 10)
setwd('~/Desktop/LING553/SpeechAccentArchive/')

ChineseDF <- read.csv('ChineseDF.csv',header = T,stringsAsFactors = F)
EnglishDF <- read.csv('EnglishDF.csv',header = T,stringsAsFactors = F)
FrenchDF <- read.csv('FrenchDF.csv',header = T,stringsAsFactors = F)
ThaiDF <- read.csv('ThaiDF.csv',header = T,stringsAsFactors = F)

EnglishDF$L2_none <- NULL
FrenchDF$L2_none <- NULL
ChineseDF$L2_none <- NULL
ThaiDF$L2_none <- NULL

EnglishDF$no_L2s <- rowSums(EnglishDF[,(which(names(EnglishDF)=="sound_file_no")+1):ncol(EnglishDF)])
FrenchDF$no_L2s <- rowSums(FrenchDF[,(which(names(FrenchDF)=="sound_file_no")+1):ncol(FrenchDF)])
ChineseDF$no_L2s <- rowSums(ChineseDF[,(which(names(ChineseDF)=="sound_file_no")+1):ncol(ChineseDF)])
ThaiDF$no_L2s <- rowSums(ThaiDF[,(which(names(ThaiDF)=="sound_file_no")+1):ncol(ThaiDF)])

#cleaning

ChineseDF$native_language[ChineseDF$native_language=="mandarin  (cnm)"] <- "mandarin  (cmn)"
ThaiDF$native_language[ThaiDF$native_language=="thai  (sou)"] <- "thai  (tha)"

EnglishDF$native_language[EnglishDF$native_language=="english  (eng)"] <- "English"
ChineseDF$native_language[ChineseDF$native_language=="mandarin  (cmn)"] <- "Mandarin"
FrenchDF$native_language[FrenchDF$native_language=="french  (fra)"] <- "French"
ThaiDF$native_language[ThaiDF$native_language=="thai  (tha)"] <- "Thai"


EnglishDF <- EnglishDF %>%
  dplyr::select(big,peas,toy,speakerID,native_language,
                birth_country,age,sex,english_onset_age,
                english_method,english_residence,
                english_residence_length,no_L2s)

FrenchDF <- FrenchDF %>%
  dplyr::select(big,peas,toy,speakerID,native_language,
                birth_country,age,sex,english_onset_age,
                english_method,english_residence,
                english_residence_length,no_L2s)

ChineseDF <- ChineseDF %>%
  dplyr::select(big,peas,toy,speakerID,native_language,
                birth_country,age,sex,english_onset_age,
                english_method,english_residence,
                english_residence_length,no_L2s)

ThaiDF <- ThaiDF %>%
  dplyr::select(big,peas,toy,speakerID,native_language,
                birth_country,age,sex,english_onset_age,
                english_method,english_residence,
                english_residence_length,no_L2s)

DF <- rbind(ChineseDF,EnglishDF,FrenchDF,ThaiDF)
DF <- DF %>%
  filter(!is.na(peas))


DF$years_study <- DF$age-DF$english_onset_age


#Graph box plots

boxplot(DF$peas ~ DF$native_language,
        main='VOT Lengths for "peas"',
        ylab="ms")
boxplot(DF$toy ~ DF$native_language,
        main='VOT Lengths for "toy"',
        ylab="ms")
boxplot(DF$big ~ DF$native_language,
        main='VOT Lengths for "big"',
        ylab="ms")
#        main="Vowel Height by Vowel, Language and Speaker",
#        col=terrain.colors(6),
#        ylab="F1 (Hz)",xaxt = "n")


#Anova
#
summary(aov(peas~native_language,data=DF))
summary(aov(toy~native_language,data=DF))

#Regression analysis

#linear model
#+years_study doesn't make much sense as a variable with all languages, this should probably
#be included language-by-language
m1 <- lm(peas ~ native_language+sex+age,data = DF)
plot(m1$residuals) #reasonably random

print(summary(m1),digits=2)

m2 <- lm(toy ~ native_language+sex+age,data = DF) #,english_residence_length,+years_study
plot(m2$residuals) #reasonably random
print(summary(m2),digits=2)

m3 <- lm(big ~ native_language+sex+age,data = DF) #,english_residence_length,+years_study
plot(m3$residuals) #reasonably random
print(summary(m3),digits=2)
#Language-by-language comparisons

#French, peas   
m4 <- lm(peas ~ age+sex+years_study+english_residence_length+english_method,data = DF[DF$native_language=='French',])
plot(m4$residuals) #reasonably random
print(summary(m4),digits=2)

#French, toy
m5 <- lm(toy ~ age+sex+years_study+no_L2s+english_residence_length+english_method,data = DF[DF$native_language=='French',])
plot(m5$residuals) #reasonably random
print(summary(m5),digits=2)
