-- Create 1,000,000 users
WITH RECURSIVE cnt(x) AS (
  SELECT 1
  UNION ALL
  SELECT x + 1 FROM cnt WHERE x <= 1000000
)
INSERT INTO leaderboard_user (username, join_date)
SELECT 'user_' || x, datetime('now')
FROM cnt;


-- Create 50,000 random game sessions
WITH RECURSIVE gen(n) AS (
  SELECT 1
  UNION ALL
  SELECT n + 1 FROM gen WHERE n <= 50000
)
INSERT INTO leaderboard_gamesession (user_id, score, game_mode, timestamp)
SELECT
  abs(random() % 1000000) + 1,                    -- user_id (1–1M)
  abs(random() % 10000) + 1,                      -- score (1–10000)
  CASE abs(random() % 2) WHEN 0 THEN 'solo' ELSE 'team' END,
  datetime('now', '-' || abs(random() % 365) || ' days')
FROM gen;



-- Populate leaderboard with total score and rank
INSERT INTO leaderboard_leaderboard (user_id, total_score, rank)
SELECT
  user_id,
  SUM(score) as total_score,
  RANK() OVER (ORDER BY SUM(score) DESC)
FROM leaderboard_gamesession
GROUP BY user_id;

