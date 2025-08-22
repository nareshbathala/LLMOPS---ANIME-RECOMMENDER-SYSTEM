from src.data_loader import AnimieDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException


load_dotenv()
logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to Build Pipeline")

        loader =  AnimieDataLoader("data/anime_with_synopsis.csv","data/anime_updated.csv")
        processed_csv = loader.load_and_process()
        logger.info("Data Loaded and Processed")

        vector_store_builder = VectorStoreBuilder(processed_csv)
        vector_store_builder.build_and_save_vectors()

        logger.info("Vector Store built Successfully")

        logger.info("Pipeline built Successfully..")

    except Exception as e:
            logger.error(f"Failed to execute pipeline {str(e)}")
            raise CustomException("Error when execute the build pipeline",e)


if __name__ == '__main__':
     main()
     