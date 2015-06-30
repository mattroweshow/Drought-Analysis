q# Preamble: set the path to the directory that the checkedout git repo is in - need to do this in order to load the data
gitRepoPath <- "/home/rowem/Documents/Git/Drought-Analysis/"

# list the synset distribution files
synsetFiles <- list.files(path = paste(gitRepoPath, "data/logs/synsets/", sep=""))
options(digits=10)

for (synsetFile in synsetFiles) {
  
  # Get the name of the filter by stripping out the trailing content
  year <- gsub("_synset_dist.csv", "", synsetFile)    
  print(year)

  # Read in each year's synset distribution
  synsets_dist <- read.table(paste(gitRepoPath,"data/logs/synsets/", synsetFile, sep=""), sep=",", header=F, stringsAsFactors=F)
  data_m <- data.matrix(synsets_dist)
  
  # Plot the distribution of synsets  
  print(pdf(paste(gitRepoPath, "plotting_scripts/plots/", year, "-synsets-dist.pdf", sep=""), height=5, width=5))
  print(par(mfrow=c(1,1), mar=c(4.5,4.5,1.5,1), oma=c(0.5,0.5,0.5,0.5)))
  hist(data_m,       
       breaks=100,
        col="darkgreen", 
        xlab="#Synsets", 
        ylab="Density", 
        lwd=1, cex=1.5, 
        cex.axis=1.5, cex.lab=1.5, 
        main=year)     
  print(dev.off())
}
