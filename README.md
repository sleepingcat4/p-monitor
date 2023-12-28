### Introduction

A few months back, I had been bored and was considering the possibility “How could someone know when I was online? On my computer. I thought it could be a fun way to challenge my software designing capabilities, though the concept sounds simple yet the moving components and services that might require for it to be successful isn’t that straightforward. 

Considering, I wasn’t keen on spending any cash/pay for services to make the process simple. After 2 months of back-forth on different ideas, I finally found a simple solution. 

#### Solve!

A complicated but first solution will be: Writing a C++/C# program that runs on both my computer locally and another individual who is interested in tracking my online presence. It starts automatically on the startup of Windows. 

It’s a good solution, unfortunately I didn’t have concrete programming knowledge to tinker with Windows API and bypassing firewall and C# in general to perform that. I went through a lot of libraries and .Net bindings yet it looked too complicated and now learning a new language and its libraries will be time-consuming. Which is why, I wanted to find a yet simpler solution. 

Now, a possibility I had to consider, third-party might not be interested in running a script on their laptop because for obvious security reasons. 

#### There comes my solution:

I utilised the GitHub API and wrote a python script that analyses my keyboard and mouse activity and after each hour, if it detects mouse/keyboard activity, it performs a commit on a GitHub repository on my account. 

Another program running a third-party virtual machine, uses my GitHub personal access token to retrieve “last commit” metadata and shows when I was online by showing the last commit time and date.

Later it converts the commit time and data into EST, GMT and Shanghai time zone using a python library and shows it in a HTML table. 

Note: the script runs automatically in the background. 

### How to use it?

Quite a simple set-up. But, I won’t share the source code (including the WEB-UI) for security reasons but I am providing the script that performs the commit automatically.
