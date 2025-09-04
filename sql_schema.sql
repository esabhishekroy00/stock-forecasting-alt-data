-- sql_schema.sql
CREATE TABLE stocks (
    ticker VARCHAR(10),
    date DATE,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume BIGINT,
    PRIMARY KEY (ticker, date)
);

CREATE TABLE sentiment (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10),
    date DATE,
    source VARCHAR(50),  -- e.g., twitter/reddit/news
    text TEXT,
    sentiment_score FLOAT
);
