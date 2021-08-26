package i_logger

import (
	"io"
	"os"
	"path"
	"runtime"
	"time"
)

const (
	//LOGPATH  LOGPATH/time.Now().Format(FORMAT)/*.log
	LOGPATH = "../logs/"
	//FORMAT .
	FORMAT = "20060102"
	//LineFeed 换行
	LineFeed = "\r\n"
)

//以天为基准,存日志
var path_ = LOGPATH + time.Now().Format(FORMAT) + "/"

// var LogPath = GetLogfilePath() + "/" + "test.log"

//WriteLog return error
func WriteLog(fileName, msg string) error {
	var (
		err error
		f   *os.File
	)

	// println(GetLogfilePath() + "/" + "logs/" + fileName)

	f, err = os.OpenFile(GetLogfilePath()+"/"+"logs/"+fileName, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		println(err.Error())
	}
	_, err = io.WriteString(f, LineFeed+msg)
	if err != nil {
		println(err.Error())
	}

	defer f.Close()
	return err
}

//CreateDir  文件夹创建
func CreateDir(path string) error {
	err := os.MkdirAll(path, os.ModePerm)
	if err != nil {
		return err
	}
	os.Chmod(path, os.ModePerm)
	return nil
}

//IsExist  判断文件夹/文件是否存在  存在返回 true
func IsExist(f string) bool {
	_, err := os.Stat(f)
	return err == nil || os.IsExist(err)
}

func GetLogfilePath() string {
	_, filename, _, ok := runtime.Caller(1)
	if ok {
		return path.Dir(path.Dir(filename))
	} else {
		return ""
	}
}
