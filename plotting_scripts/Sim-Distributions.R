# Preamble: set the path to the directory that the checkedout git repo is in - need to do this in order to load the data
logFilesPath <- "/home/rowem/Documents/Git/Drought-Analysis/data/logs/similarity/"
gitRepoPath <- "/home/rowem/Documents/Git/Drought-Analysis/"

options(digits=10)

z = 2.576

#TODO split up the processing into separate segments for the different files
# 2011_lch_dist.csv
file_name = "2011_lch_dist.csv"
simFile <- paste(logFilesPath, file_name, sep="")
type <- gsub("_dist.csv", "", file_name)    
sim_dist <- read.table(simFile, sep=",", header=F, stringsAsFactors=F)
nums <- sapply(sim_dist, is.numeric)
nums_sim_dist <- sim_dist[, nums]
nums_sim_dist <- nums_sim_dist[nums_sim_dist < 3]
# std_nums_sim_dist <- scale(nums_sim_dist)
print(mean(nums_sim_dist))
print(sd(nums_sim_dist))
print(pdf(paste(gitRepoPath, "plotting_scripts/plots/", type, "-sim-dist.pdf", sep=""), height=5, width=5))
print(par(mfrow=c(1,1), mar=c(4.5,4.5,1.5,1), oma=c(0.5,0.5,0.5,0.5)))
hist(nums_sim_dist,       
      col="darkgreen", xlab="Distance", ylab="Density", lwd=1, cex=1.5, cex.axis=1.5, cex.lab=1.5, main=type, xlim=c(0,3))     
abline(v=mean(nums_sim_dist), col="darkred", lwd=2)
abline(v=(mean(nums_sim_dist) - z * sd(nums_sim_dist)), col="darkred", lty=2, lwd=2)
print(dev.off())

# 2012_lch_dist.csv
file_name = "2012_lch_dist.csv"
simFile <- paste(logFilesPath, file_name, sep="")
type <- gsub("_dist.csv", "", file_name)    
sim_dist <- read.table(simFile, sep=",", header=F, stringsAsFactors=F)
nums <- sapply(sim_dist, is.numeric)
nums_sim_dist <- sim_dist[, nums]
nums_sim_dist <- nums_sim_dist[nums_sim_dist < 3]
# std_nums_sim_dist <- scale(nums_sim_dist)
print(mean(nums_sim_dist))
print(sd(nums_sim_dist))
print(pdf(paste(gitRepoPath, "plotting_scripts/plots/", type, "-sim-dist.pdf", sep=""), height=5, width=5))
print(par(mfrow=c(1,1), mar=c(4.5,4.5,1.5,1), oma=c(0.5,0.5,0.5,0.5)))
hist(nums_sim_dist,       
     col="darkgreen", xlab="Distance", ylab="Density", lwd=1, cex=1.5, cex.axis=1.5, cex.lab=1.5, main=type, xlim=c(0,3))     
abline(v=mean(nums_sim_dist), col="darkred", lwd=2)
abline(v=(mean(nums_sim_dist) - z * sd(nums_sim_dist)), col="darkred", lty=2, lwd=2)
print(dev.off())

