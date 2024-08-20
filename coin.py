def calculate_earnings(total_gift_points):
    COINS_PER_DOLLAR = 65
    TIKTOK_PERCENTAGE = 0.66
    INFLUENCER_PERCENTAGE = 1 - TIKTOK_PERCENTAGE
    total_coins = total_gift_points
    total_amount_made = total_coins / COINS_PER_DOLLAR
    tiktok_keeps = total_amount_made * TIKTOK_PERCENTAGE
    influencer_keeps = total_amount_made * INFLUENCER_PERCENTAGE

    return {
        "total_gift_points": total_gift_points,
        "total_coins": total_coins,
        "total_amount_made": total_amount_made,
        "tiktok_keeps": tiktok_keeps,
        "influencer_keeps": influencer_keeps
    }

def main():
    total_gift_points = int(input("Enter the total gift points to calculate: "))
    results = calculate_earnings(total_gift_points)
    print("Here are the results!")
    print(f"Total Gift Points: {results['total_gift_points']} Coins")
    print(f"Total Amount Made: ${results['total_amount_made']:.2f}")
    print(f"TikTok Keeps (66%): -${results['tiktok_keeps']:.2f}")
    print(f"Influencer Keeps: ${results['influencer_keeps']:.2f}")

if __name__ == "__main__":
    main()
