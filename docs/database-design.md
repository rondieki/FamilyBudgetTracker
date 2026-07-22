| Field              | Type     |
| ------------------ | -------- |
| id                 | Auto     |
| email              | Email    |
| first_name         | String   |
| last_name          | String   |
| phone_number       | String   |
| profile_picture    | Image    |
| preferred_currency | String   |
| created_at         | DateTime |

Income
| Field         | Type        |
| ------------- | ----------- |
| id            | Auto        |
| user          | Foreign Key |
| source        | String      |
| amount        | Decimal     |
| date_received | Date        |
| description   | Text        |
| created_at    | DateTime    |

Expense
| Field        | Type        |
| ------------ | ----------- |
| id           | Auto        |
| user         | Foreign Key |
| category     | Foreign Key |
| amount       | Decimal     |
| expense_date | Date        |
| description  | Text        |
| created_at   | DateTime    |

Category
| Field | Type   |
| ----- | ------ |
| id    | Auto   |
| name  | String |
| icon  | String |
| color | String |

Savings goal
| Field          | Type        |
| -------------- | ----------- |
| id             | Auto        |
| user           | Foreign Key |
| goal_name      | String      |
| target_amount  | Decimal     |
| current_amount | Decimal     |
| deadline       | Date        |
| status         | String      |
| created_at     | DateTime    |

Notification
| Field      | Type        |
| ---------- | ----------- |
| id         | Auto        |
| user       | Foreign Key |
| title      | String      |
| message    | Text        |
| is_read    | Boolean     |
| created_at | DateTime    |
