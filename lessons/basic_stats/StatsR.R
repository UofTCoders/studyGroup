#Independent-Samples T-test
#Create variables
Women = c(99, 85, 78, 93, 95, 87)
Men = c(72, 75, 70, 68, 70, 80)
#T-test to see if men and women's scores significantly differ
t.test(Women,Men,alternative="two.sided") 

#One-sample t-test to see if women scored significantly lower than 95% on the test
t.test(Women, alternative = "less", mu = 95)

#One-way analysis of variance
#Read sample pain score data into R
pain = c(4, 5, 4, 3, 2, 4, 3, 4, 4, 6, 8, 4, 5, 4, 6, 5, 8, 6, 6, 7, 6, 6, 7, 5, 6, 5, 5)
gender = c("F", "F", "F", "M", "M", "M", "M", "F", "F", "M", "M", "F", "F", "F", "M", "F", "M", "M", "M", "F", "F", "F", "F", "M", "F", "M", "M")
#Code the data according to which drug is associated with the score
drug = c(rep("A",9), rep("B",9), rep("C",9))
#Create data frame with pain scores, coded by which drug the patient took
migraine = data.frame(pain,drug)
#Look at our data frame
migraine
#Run a one-way ANOVA
results = aov(pain ~ drug, data=migraine)
summary(results)

#Post hoc analysis using Tukey's HSD
TukeyHSD(results, conf.level = 0.95)

#Add column full of gender info to migraine dataset
migraine$gender <- c("F", "F", "F", "M", "M", "M", "M", "F", "F", "M", "M", "F", "F", "F", "M", "F", "M", "M", "M", "F", "F", "F", "F", "M", "F", "M", "M")
migraine

#Run two-way ANOVA using gender and drug as factors
results = aov(pain ~ drug*gender, data=migraine)
summary(results)

#Post hoc analysis on two-way ANOVA
TukeyHSD(results, conf.level = 0.95)

#Plot the interaction for our two-way ANOVA
interaction.plot(drug, gender, pain)

#Create bachelor dataset for correlation demo
weeks = c(8,7,6,5,4,4,3,3,3,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
age = c(24,23,25,24,23,22,27,28,23,30,27,30,24,27,29,30,27,29,25,34,27,22,25,28,28,23)
bachelor = data.frame(weeks, age)
bachelor

#Run test of correlation on bachelor data - default method is Pearson correlation
cor.test(bachelor$weeks, bachelor$age)
plot(bachelor$weeks, bachelor$age, xlab="Weeks Before Dumping", ylab="Age of Contestant") 

#Supplemental: Another kind of post hoc test (pairwise t-tests with a bonferroni correction) on the migraine dataset
pairwise.t.test(pain, drug, p.adjust="bonferroni")

#Supplemental: Another way to do a t-test on the migraine dataset
with(migraine, t.test(pain[drug == "A"], pain[drug == "B"]))
