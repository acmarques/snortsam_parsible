--
-- Creates table to store snortsam event information
--
create table quarantines(
  sig_id INT NOT NULL,
  ip_src VARCHAR(20) NOT NULL,
  ip_dst VARCHAR(20) NOT NULL,
  sensor VARCHAR(50) NOT NULL,
  port INT NOT NULL DEFAULT 0,
  duration INT NOT NULL,
  created_at INT NOT NULL,
  UNIQUE(ip_src, ip_dst, sensor, port)
);