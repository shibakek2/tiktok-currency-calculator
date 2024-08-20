# Gift Points Calculator

This Python script calculates the amount of coins and earnings based on the total gift points. It provides a breakdown of the total amount made, TikTok's share, and the influencer's share.

## How to Use

1. Clone the repository:
    ```sh
    git clone https://github.com/shibakek2/tiktok-currency-calculator
    cd gift-points-calculator
    ```

2. Run the script:
    ```sh
    python coin.py
    ```

3. Enter the total gift points when prompted.

## Example
```sh
Enter the total gift points to calculate: 100
Here are the results!
Total Gift Points: 100 Coins
Total Amount Made: $1.54
TikTok Keeps (66%): -$1.02
Influencer Keeps: $0.52
```


## Code Overview

### `calculate_earnings(total_gift_points)`

This function takes the total gift points as input and returns a dictionary with the following keys:
- `total_gift_points`: The input total gift points.
- `total_coins`: The total coins, which is equal to the total gift points.
- `total_amount_made`: The total amount made in dollars.
- `tiktok_keeps`: The amount TikTok keeps (66% of the total amount made).
- `influencer_keeps`: The amount the influencer keeps (34% of the total amount made).

### `main()`

This function prompts the user to enter the total gift points, calls `calculate_earnings`, and prints the results.

## License

This project is licensed under the MIT License
