# scraper_wiki
Scraping project for a large amount of businesses social media + google searches for SEO 

The main idea of this project is to scrape as much information as possible about a single business, replicate the steps for any business and make it scalable.

Example below


Input:
1. single business
2. list of businesses
3. area to crawl from
4. list of areas to crawl from

Lets go with 1.

We have a website of a single business www.xyz.com

Step one

Scraping
- Check Site for SEO and any errors
- Business name
- Email
- Phone contact
- Facebook
- Instagram
- Linkedin
- Twitter
- Industry
Keeping that data in csv file

Step two
Socials

- Check followers/likes
- Check for any additional information or just for reverification purposes such as phone email or other socials
- Check interactions for the last 20 posts(like,share,comment) and spit out the engagement ratio
- Check if the business runs any ads + ads history
- Compare a post interactions between ads and no ads post

Step Three
- Google search the business
- Check rating
- Check amount of ratings
- Check SEO

Step Four
- Check directly involved people in the management of the business
- Get their socials
- Make a list of possible issues with the business

Step Five
- Identify business
- Compare the social situation with the competition
- Write algorithm to rate the business on how likely are they to become a customer
