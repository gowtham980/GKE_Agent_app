# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A tool for interacting with the Bank of Anthos services."""

import os
import requests
import logging

logging.basicConfig(level=logging.INFO)

def get_balance(account_id: str, token: str) -> str:
    """Get the balance for a given account."""
    hed = {'Authorization': 'Bearer ' + token}
    url = f'http://{os.environ.get("BALANCES_API_ADDR")}/balances/{account_id}'
    logging.info(f"Requesting balance from {url}")
    logging.info(f"Request headers: {hed}")
    try:
        response = requests.get(url, headers=hed, timeout=5)
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Raw response body: {response.text}")
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # The API returns a string of cents. Convert to dollars.
        balance_in_cents = int(response.text)
        balance_in_dollars = balance_in_cents / 100
        formatted_balance = f"${balance_in_dollars:,.2f}"
        logging.info(f"Formatted balance: {formatted_balance}")
        return formatted_balance
        
    except requests.exceptions.RequestException as e:
        logging.error(f"Error getting balance: {e}")
        return f"An error occurred while processing your request: {e}"

def get_transaction_history(account_id: str, token: str) -> list:
    """Gets the transaction history for a given account.

    Args:
        account_id: The account ID to get the transaction history for.
        token: The JWT token for authentication.

    Returns:
        A list of transactions.
    """
    url = f"http://{os.environ.get('HISTORY_API_ADDR')}/transactions/{account_id}"
    headers = {'Authorization': f'Bearer {token}'}
    logging.info(f"Requesting transaction history from {url}")
    logging.info(f"Request headers: {headers}")
    try:
        response = requests.get(url, headers=headers, timeout=5)
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Response body: {response.text}")
        response.raise_for_status()  # Raise an exception for bad status codes
        transactions = response.json()
        for transaction in transactions:
            if 'amount' in transaction:
                transaction['amount'] = transaction['amount'] / 100
        return transactions
    except requests.exceptions.RequestException as e:
        logging.error(f"Error getting transaction history: {e}")
        return f"An error occurred while processing your request: {e}" 