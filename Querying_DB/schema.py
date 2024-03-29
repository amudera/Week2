CREATE TABLE `users` (
  `id` INTEGER,
  `name` VARCHAR,
  `email` VARCHAR,
  `city` VARCHAR,
  `state` VARCHAR,
  `last_visit` DATE,
  `page_views` INTEGER,
  PRIMARY KEY (`id`)
);
CREATE TABLE `search_terms` (
  `id` INTEGER,
  `word` VARCHAR,
  PRIMARY KEY (`id`)
);
CREATE TABLE `user_searches` (
  `id` INTEGER,
  `user_id` INTEGER,
  `term_id` INTEGER,
  FOREIGN KEY (`user_id`) REFERENCES users(id),
  FOREIGN KEY (`term_id`) REFERENCES search_terms(id),
  PRIMARY KEY (`id`)
);
sqlite> 