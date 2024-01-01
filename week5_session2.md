# Week 5 session 2: The project; modules and testing

## Recording

[Week 5 session
2](https://numfocus-org.zoom.us/rec/share/UyN--58pEYtPK7fAloXHw4Km5lxsPlqi_0WLcYmRKey6r-WCbUCnxBQ6bYsyLZZ9.iX3WF6qd0OIYtovN)

## Schedule and plan

### Details about the project

1. Fill out the script and any needed library code to run
   `scripts/find_outliers.py data` on your data, and return a list of
   outlier volumes for each scan (where there is an outlier);
2. You should add a text file giving a brief summary for each outlier scan,
   why you think the detected scans should be rejected as an outlier, and your
   educated guess as to the cause of the difference between this scan and the
   rest of the scans in the run;
3. You should do this by collaborating in your teams using `git` and Github;

We will rate you on:

* the quality of your outlier detection as assessed by the improvement in the
  statistical testing for the experimental model after removing the outliers;
* the generality of your outlier detection as assessed by the improvement in
  the statistical testing for the experimental model after removing the
  outliers, for another similar dataset;
* the quality of your code;
* the quality and transparency of your process, from your interactions on
  github;
* the quality of your arguments about the scans rejected as outliers.

Your outlier detection script should be *reproducible*.

That means that we, your instructors, should be able to clone your repository,
and then follow simple instructions in order to be able to reproduce your run
of `scripts/find_outliers.py data` and get the same answer.

To make this possible, fill out the `README.md` text file in your repository
to describe a few simple steps that we can take to set up on our own machines
and run your code.  Have a look at the current `README.md` file for a
skeleton.  We should be able to perform these same steps to get the same
output as you from the outlier detection script.

## Modules and testing

* [docstrings](https://textbook.nipraxis.org/docstrings)
* [validating data](https://textbook.nipraxis.org/validating_data)
* [Module directories](https://textbook.nipraxis.org/module_directories.html)
* [On testing](https://textbook.nipraxis.org/on_testing)
