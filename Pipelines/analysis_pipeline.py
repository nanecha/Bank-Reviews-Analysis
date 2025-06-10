# analysis_pipeline.py
import pandas as pd
from sentiment_analysis import SentimentAnalyzer, ThematicAnalyzer

class AnalysisPipeline:
    def __init__(self):
        self.sentiment_analyzer = SentimentAnalyzer()
        self.thematic_analyzer = ThematicAnalyzer()
    
    def run_pipeline(self, input_path: str, output_path: str):
        # Load preprocessed data
        df = pd.read_csv(input_path)
        df["review_id"] = df.index
        
        # Sentiment Analysis
        print("Running sentiment analysis...")
        sentiment_results = df["processed_text"].apply(
            lambda x: self.sentiment_analyzer.analyze_sentiment(x)
        ).apply(pd.Series)
        df = pd.concat([df, sentiment_results], axis=1)
        
        # Thematic Analysis
        print("Running thematic analysis...")
        keywords = self.thematic_analyzer.extract_keywords(df["processed_text"].tolist())
        themes = self.thematic_analyzer.cluster_themes(df)
        
        # Save results
        df["themes"] = df["review_id"].map(themes)
        df.to_csv(output_path, index=False)
        return df

    def generate_report(self, df: pd.DataFrame):
        # Sentiment by bank and rating
        report = df.groupby(["bank", "rating"])["score"].mean().unstack()
        print("\nSentiment Analysis Report:")
        print(report)
        
        # Theme frequency
        theme_counts = df.explode("themes").groupby(["bank", "themes"]).size().unstack()
        print("\nTheme Frequency Report:")
        print(theme_counts)