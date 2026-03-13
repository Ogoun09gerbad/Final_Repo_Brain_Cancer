
import pandas as pd
from sklearn.metrics import accuracy_score
import os

def update_leaderboard(repo_path, user_name='New_Participant'):
    sol_path = os.path.join(repo_path, 'solution.csv')
    sub_path = os.path.join(repo_path, 'submission.csv')

    if not os.path.exists(sol_path) or not os.path.exists(sub_path):
        print('Missing required CSV files.')
        return

    solution = pd.read_csv(sol_path)
    submission = pd.read_csv(sub_path)
    merged = solution.merge(submission, on='ImageId', suffixes=('_true', '_pred'))
    score = accuracy_score(merged['Expected_true'], merged['Expected_pred'])

    new_entry = pd.DataFrame({
        'User': [user_name],
        'Score (Accuracy)': [score],
        'Date': [pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')]
    })

    lb_path = os.path.join(repo_path, 'leaderboard.csv')
    if os.path.exists(lb_path):
        leaderboard_df = pd.read_csv(lb_path)
        leaderboard_df = pd.concat([leaderboard_df, new_entry], ignore_index=True)
    else:
        leaderboard_df = new_entry

    leaderboard_df.sort_values(by='Score (Accuracy)', ascending=False, inplace=True)
    leaderboard_df.to_csv(lb_path, index=False)
    print('Leaderboard updated successfully.')
    return leaderboard_df
