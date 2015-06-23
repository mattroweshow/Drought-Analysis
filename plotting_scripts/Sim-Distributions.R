q# Preamble: set the path to the directory that the checkedout git repo is in - need to do this in order to load the data
gitRepoPath <- "/home/rowem/Documents/Git/Drought-Analysis/"

# list the synset distribution files
simFiles <- list.files(path = paste(gitRepoPath, "data/logs/similarity/", sep=""))
options(digits=10)

for (simFile in simFiles) {
  
  # Get the name of the filter by stripping out the trailing content
  type <- gsub("_dist.csv", "", simFile)    
  print(type)

  # Read in each year's synset distribution
  sim_dist <- read.table(paste(gitRepoPath,"data/logs/similarity/", simFile, sep=""), sep=",", header=F, stringsAsFactors=F)
  data_m <- as.matrix(as.character(sim_dist))
  
  # Plot the distribution of synsets  
  print(pdf(paste(gitRepoPath, "plotting_scripts/plots/", type, "-sim-dist.pdf", sep=""), height=5, width=5))
  print(par(mfrow=c(1,1), mar=c(4.5,4.5,1.5,1), oma=c(0.5,0.5,0.5,0.5)))
  plot(density(data_m),       
        col="darkgreen", 
        xlab="Similarity", 
        ylab="Density", 
        lwd=1, cex=1.5, 
        cex.axis=1.5, cex.lab=1.5, 
        main=type)     
  print(dev.off())
}
