# ♻️ Waste Management & Recycling Platform

## Overview
This is a **waste management and recycling platform** built with Django.  
The platform connects **waste generators** (households, businesses) with **waste recyclers** by allowing waste to be posted, viewed, and traded.  
It also creates **awareness** on proper waste management practices and includes a **messaging system** for user-to-user communication.

---

## ✨ Features
- 🔑 **User Authentication & Roles**  
  - Waste Generators → Can post waste for sale.  
  - Recyclers → Can view and purchase waste, but **cannot post**.  
  - Role-specific dashboards.  

- 📦 **Waste Marketplace**  
  - Create, list, and view waste posts.  
  - Filter by waste type and availability.  

- 💬 **Messaging System**  
  - Send direct messages to other users.  
  - General messaging option for awareness.  
  - Inbox for received messages.  

- 📚 **Awareness & Tips Section**  
  - Provides real-time waste management tips.  
  - Educational content to encourage sustainable practices.  

- 👤 **Profile Management**  
  - Users can update their email, role, and other details.  

---

## 🛠️ Tech Stack
- **Backend**: Django 5, Django ORM, Python 3.x  
- **Frontend**: Django Templates, Bootstrap 5  
- **Database**: SQLite (default) → can be swapped with PostgreSQL/MySQL in production  
- **Other Tools**: Django Messages Framework, Crispy Forms (if enabled), Bootstrap Icons  

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Levyslater/waste-management-app.git
cd waste-management-app
