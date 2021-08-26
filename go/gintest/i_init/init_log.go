package i_init

import (
	"gintest/i_logger"
	"log"
	"os"
)

// 初始化日志
func InitLog() {
	if !i_logger.IsExist("logs/test.log") {
		_, err := os.Create("logs/test.log")
		if err != nil {
			log.Fatalln("fail to create test.log file!")
		}
	}
}
