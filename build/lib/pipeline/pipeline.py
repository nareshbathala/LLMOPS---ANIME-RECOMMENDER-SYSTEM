from src.vector_store import VectorStoreBuilder
from src.recommender import AnimieRecommender
from config.config import GROQ_API_KEY,MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline")

            vector_build = VectorStoreBuilder(csv_path="",persist_dir= persist_dir)

            retriever = vector_build.load_vector_store().as_retriever()

            self.recomender = AnimieRecommender(retriever, GROQ_API_KEY, MODEL_NAME)

            logger.info("Pipeline Initialize Successful")
        
        except Exception as e:
            logger.error(f"Failed to Initialize the pipeline {str(e)}")
            raise CustomException("Error during pipeline Exeception",e)
        

    def recommend(self,query:str):
        try:
            logger.info(f"Received a query {query}")

            recommendation =  self.recomender.get_recommendation(query)

            logger.info("Recommendations generated successfully")

            return Exception
        
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation",e)