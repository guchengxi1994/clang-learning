package models

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var (
	DB    *gorm.DB
	DbErr error
)

func init() {
	InitMySqlDatabase()
}

// 初始化 mysql 数据库
func InitMySqlDatabase() {

	var err error
	dsn := "root:123456@tcp(127.0.0.1:3306)/testdb?charset=utf8mb4&parseTime=True&loc=Local"
	DB, err = gorm.Open(mysql.Open(dsn), &gorm.Config{})

	if err != nil {
		println(err.Error())
	}

	DB.AutoMigrate(&User{})
}
