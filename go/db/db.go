package db

import (
	"database/sql"
	"log"
	"os"
	"path/filepath"

	_ "github.com/mattn/go-sqlite3"
)

func Open(path string) *sql.DB {
	home, _ := os.UserHomeDir()
	dir := filepath.Join(home, "Library", "Application Support", "CaffeineApp")
	os.MkdirAll(dir, 0755)
	dbPath := filepath.Join(dir, "app.db")
	db, _ := sql.Open("sqlite3", dbPath)
	log.Println("Using DB at: ", dbPath)
	initTables(db)
	return db
}

func initTables(db *sql.DB) {
	db.Exec(`
        CREATE TABLE IF NOT EXISTS flavours (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            email  TEXT NOT NULL UNIQUE
        );
    `)
}

func SeedTestUsers(d *sql.DB) {
	d.Exec(`INSERT INTO users (name, email) VALUES (?, ?)`, "Alice", "alice@example.com")
	d.Exec(`INSERT INTO users (name, email) VALUES (?, ?)`, "Bob", "bob@example.com")
	d.Exec(`INSERT INTO users (name, email) VALUES (?, ?)`, "Charlie", "charlie@example.com")
}

func seedDataIfEmpty(d *sql.DB) {
	var count int
	d.QueryRow(`SELECT COUNT(*) FROM flavours`).Scan(&count)
	if count > 0 {
		return
	}

	d.Exec(``)
}
