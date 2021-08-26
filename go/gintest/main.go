package main

import (
	"gintest/handler"
	"gintest/i_init"
	"gintest/i_logger"
	"gintest/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

var s string

var ExecRunningPath = i_logger.GetLogfilePath()

func main() {

	i_init.InitLog()

	println(i_logger.GetLogfilePath())

	r := gin.Default()
	r.Use(handler.ExceptionRecover)
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.GET("/test", func(c *gin.Context) {
		var slice = []int{1, 2, 3, 4, 5, 6}
		println(slice[6])
		c.JSON(http.StatusOK, gin.H{
			"message": "test",
		})
	})

	r.GET("/createuser", func(c *gin.Context) {
		user := new(models.User)
		// models.User{Username: "法外狂徒张三", Age: 120, Sex: 0}
		user.Age = 120
		user.Username = "法外狂徒张三"
		user.Sex = 0
		user.InsertSingleUser()
	})

	r.Run()
}
