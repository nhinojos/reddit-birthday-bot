# DReddit Bot Happy Birthday
### Goal
Wishes reddit accounts happy birthday based on the age of the account.

### Criteria
- Scans through comments sections under any posts on any subreddit. 
- Comments 'Happy Cake-Day [username]!' under a user's comment on the post. (In reddit culture, an account's birthday is often called their 'cake day').
- Also congratualtes user on their account's age. 

### Method & Results
This program calls Reddit's API using reddit's own python wrapper PRAW. It crawls through the top ten posts any subreddit (I chose r/technology), and subsequtnly crawls though the entire comment section. If it finds a user whose reddit account was created on the same month and day as the time this program is ran, then is wishes happy birthday as a comment on their comment. Unexpectedly, reddit provides users' ages in UNIX format, which is challenging to read and process. I resolved this by converting it to GME time using the datetime library.

I added detailed comments for anyone to change the subreddit of choice easily, or, input their own account credentials to wish redditors happy birthday. 
