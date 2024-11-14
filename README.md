# Invoice API

## Overview
This project is a Django REST Framework (DRF) API for managing invoices and their details. It supports creating, updating, and retrieving invoices with nested invoice details.

## Features
- **Nested Serializer**: Uses nested serializers to handle related data (Invoice and InvoiceDetail).
- **Endpoints**:
  - `POST /api/invoices/`: Create a new invoice along with its details.
  - `PUT /api/invoices/<invoice_number>/`: Update an existing invoice and replace old details with new ones.
  
  ** Here i also created for GET operation to get all the invoices or specific one.
  - `GET /api/invoices/`: Retrieve all invoices.
  - `GET /api/invoices/<invoice_number>/`: Retrieve a specific invoice by `invoice_number`.

## Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.8+
- Git

### Installation

1. **Clone the Repository**:

   ```bash
   git clone <your-repository-url>
   cd invoice_project
