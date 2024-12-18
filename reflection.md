# Reflection

Student Name:  Gabriel Lucey
Sudent Email:  gplucey@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

This assignment was not too difficult for me but I did have a little trouble figuring out the selectors to choose for the actual scraping at the end. At first I thought that I needed to do query_selector_all on div.row because when I prtinted it out, it seemed like it had all the inner text that was needed for the scraping. However after looking deeper into the html, looping through the div.row would have only gave me the information for the first category on the menu which was starters and snacks. 

I had to use Github Copilot to explain to me how to extract both the category title as well as each individual item inside each category. I learned that using the (~ *) selector was used to move to the neighboring selector. So by using (~ *) twice I would be able to move over to div.row for the item and use query_selector_all on each item. After this, I used the previous functiosn to split up the data accordingly

The last issue I came across was making sure the file path to read in the csv was correct. After some messing around, I found that the cache folder was not in my code folder. So instead of ./code/cache I changed the path to ./cache and was able to solve this issue.

Overall, this assignment was helpful in refreshing me on how to navigate through html and css selectors and also helped refine my skills in importing local functions from the same folder.