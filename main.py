from src.data_loader import DataLoader
from src.preprocessors.customer_preprocessor import CustomerPreprocessor
from src.preprocessors.credit_preprocessor import CreditPreprocessor
from src.preprocessors.transaction_preprocessor import TransactionPreprocessor
from src.data_saver import save_raw, save_processed
from src.data_exporter import DataExporter


def main():
    print("\n=== AtliQo Credit Card Data Pipeline Started ===\n")
    loader = DataLoader()
    exporter = DataExporter()

    customers = loader.load_table("customers")
    credit_profiles = loader.load_table("credit_profiles")
    transactions = loader.load_table("transactions")

    print("All tables loaded successfully.")

    save_raw(customers, "customers_raw.csv")
    save_raw(credit_profiles, "credit_profiles_raw.csv")
    save_raw(transactions, "transactions_raw.csv")

    print("All RAW datasets saved.")

    processor = CustomerPreprocessor()
    customers = processor.preprocess(customers)

    print(f"Customer preprocessing complete. shape{customers.shape}")

    credit_processor = CreditPreprocessor()
    credit_profiles = credit_processor.preprocess(credit_profiles)

    print(f"Credit profile preprocessing complete. shape{credit_profiles.shape}")

    transaction_processor = TransactionPreprocessor()
    transactions = transaction_processor.preprocess(transactions)

    print(f"Transaction preprocessing complete. Shape: {transactions.shape}")

    save_processed(customers, "customers_processed.csv")
    save_processed(credit_profiles, "credit_profiles_processed.csv")
    save_processed(transactions, "transactions_processed.csv")

    exporter.export_table(customers, "customers_processed")
    exporter.export_table(credit_profiles, "credit_profiles_processed")
    exporter.export_table(transactions, "transactions_processed")
    print("All processed tables exported to MySQL.")
    print("=== Pipeline Completed Successfully ===\n")

if __name__ == "__main__":
    main()
