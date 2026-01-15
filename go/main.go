package main

import (
	"caffeine/db"
	"database/sql"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/widget"
)

var database *sql.DB

func main() {
	database = db.Open("app.db")
	defer database.Close()
	db.SeedTestUsers(database)

	users := getAllUsersText(database)

	a := app.New()
	w := a.NewWindow("Hello World")

	w.SetContent(widget.NewLabel(users))
	w.ShowAndRun()
}

func getAllUsersText(d *sql.DB) string {
	rows, _ := d.Query(`SELECT id, name, email FROM users`)
	defer rows.Close()

	text := ""
	for rows.Next() {
		var id int
		var name, email string
		rows.Scan(&id, &name, &email)
		text += name + " - " + email + "\n"
	}

	return text
}
