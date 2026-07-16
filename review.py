class Review:
    def __init__(self, text, rating):
        self.text = text 
        self.rating = int(rating)

    def is_positive(self):
        return self.rating >= 3


reviews = []


def main():

        try:
            with open("review.txt", "r", encoding="utf-8") as file:
                    for line in file:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            text, rating = line.rsplit(",", 1)
                            rating = int(rating.strip())

                            if rating < 1 or rating > 5:
                                raise ValueError("Rating out of range")

                            review = Review(text.strip(), rating)
                            reviews.append(review)

                        except ValueError as e:
                            print(f"Skipped invalid line: {line} | Reason: {e}")
        except FileNotFoundError:
                print("File not found, please check the file path.")

        
        your_review = input("enter your review (text,rating) or 'exit' :")
        if your_review.lower() == "exit":
            print("Exiting review system.")
            return
        try:
            text, rating = your_review.split(",")
            
            rating = int(rating)
            if rating < 1 or rating > 5:
                print("Rating must be between 1 and 5")
                
            
            with open("review_afterfilter.txt", "a", encoding="utf-8") as file:
                file.write(f"{text.strip()},{rating}\n")
            reviews.append(Review(text.strip(), rating))
        except ValueError:
            print("Wrong format! Use: text,rating")


        positive = [r for r in reviews if r.is_positive()]
        negative = [r for r in reviews if not r.is_positive()]

        positive.sort(key=lambda r: r.rating, reverse=True)
        negative.sort(key=lambda r: r.rating)

        average = sum(r.rating for r in reviews) / len(reviews) if reviews else 0

        positive_percent = (len(positive) / len(reviews) * 100) if reviews else 0
        negative_percent = (len(negative) / len(reviews) * 100) if reviews else 0

        top_reviews = positive[:3]
        worst_reviews = negative[:3]


        with open("review_afterfilter.txt", "w", encoding="utf-8") as file:
            file.write(f"Average Rating: {average:.2f}\n")
            file.write(f"Positive Reviews: {positive_percent:.2f}%\n")
            file.write(f"Negative Reviews: {negative_percent:.2f}%\n")
            file.write(f"Total Reviews: {len(reviews)}\n")
            file.write('='*50 + '\n')

            file.write("\nTop 3 Reviews:\n")
            for r in top_reviews:
                file.write(f"{r.text} ({r.rating})\n")

            file.write("\nWorst 3 Reviews:\n")
            for r in worst_reviews:
                file.write(f"{r.text} ({r.rating})\n")

            file.write("="*50 + '\n')

            file.write("\n---(Review Analysis)---\n")
            file.write("\nPositive Reviews:\n")
            for review in positive:
                file.write(f"{review.text},{review.rating}\n")

            file.write('-'*50 + '\n')
            file.write("\nNegative Reviews:\n")
            for review in negative:
                file.write(f"{review.text},{review.rating}\n")


if __name__ == "__main__":  
    main()