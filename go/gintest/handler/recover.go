package handler

import (
	"gintest/i_logger"
	"log"
	"net/http"
	"runtime/debug"
	"time"

	"github.com/gin-gonic/gin"
)

// 统一的异常处理
func ExceptionRecover(c *gin.Context) {
	defer func() {
		if r := recover(); r != nil {
			log.Printf("panic: %v\n", r)

			go i_logger.WriteLog("test.log", errorToString(r))

			debug.PrintStack()
			c.JSON(http.StatusOK, gin.H{
				"code": "1",
				"msg":  "只是一个错误信息",
				"data": nil,
			})
			//终止后续接口调用，不加的话recover到异常后，还会继续执行接口里后续代码
			c.Abort()
		}
	}()
	//加载完 defer recover，继续后续接口调用
	c.Next()
}

// recover错误，转string
func errorToString(r interface{}) string {
	switch v := r.(type) {
	case error:
		return time.Now().Format("2006-01-02 15:04:05 MST Mon") + "  [ERROR]:" + v.Error()
	default:
		return time.Now().Format("2006-01-02 15:04:05 MST Mon") + "  [ERROR]:" + r.(string)
	}
}
