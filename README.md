# Reddit Bot Happy Birthday
### Goal
Wishes Reddit users happy birthday based on the account's age.

### Criteria
- Scans through comments sections under any posts on any subreddit. 
- Comments 'Happy Cake-Day [username]!' under a user's comment on the post. (In reddit culture, an account's birthday is often referred to as their 'cake day').
- Also congratualtes user on their account's age. 

### Method & Results
This program calls Reddit's API using Reddit's own python wrapper PRAW. It crawls through the top ten posts on any subreddit (I defaulted r/technology), and subsequtnly crawls though the entire comment section. If it finds a user whose Reddit account was created on the same month and day as the present, then is comments happy birthday to the user. Unexpectedly, Reddit provides users' ages in UNIX format, which is challenging to read and process. I resolved this by converting it to GME format using the datetime library.

I added detailed comments for anyone who would like to change the subreddit of choice easily as well as input their own credentials to wish redditors happy birthday. 
