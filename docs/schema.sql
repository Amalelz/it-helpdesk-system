CREATE TABLE users (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  name          VARCHAR(100) NOT NULL,
  email         VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role          ENUM('employee','agent','admin') NOT NULL DEFAULT 'employee',
  is_active     BOOLEAN NOT NULL DEFAULT TRUE,
  created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE categories (
  id   INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE tickets (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  title       VARCHAR(150) NOT NULL,
  description TEXT NOT NULL,
  priority    ENUM('low','medium','high','critical') NOT NULL DEFAULT 'medium',
  status      ENUM('open','in_progress','resolved','closed') NOT NULL DEFAULT 'open',
  category_id INT NULL,
  created_by  INT NOT NULL,
  assigned_to INT NULL,
  created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  resolved_at DATETIME NULL,
  FOREIGN KEY (category_id) REFERENCES categories(id),
  FOREIGN KEY (created_by)  REFERENCES users(id),
  FOREIGN KEY (assigned_to) REFERENCES users(id),
  INDEX idx_tickets_status (status),
  INDEX idx_tickets_priority (priority),
  INDEX idx_tickets_assigned (assigned_to),
  INDEX idx_tickets_creator (created_by),
  INDEX idx_tickets_created (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE comments (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  ticket_id  INT NOT NULL,
  author_id  INT NOT NULL,
  body       TEXT NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  FOREIGN KEY (author_id) REFERENCES users(id),
  INDEX idx_comments_ticket (ticket_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE ticket_history (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  ticket_id  INT NOT NULL,
  actor_id   INT NOT NULL,
  action     ENUM('created','status_changed','assigned','reopened') NOT NULL,
  old_value  VARCHAR(50) NULL,
  new_value  VARCHAR(50) NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
  FOREIGN KEY (actor_id)  REFERENCES users(id),
  INDEX idx_history_ticket (ticket_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;