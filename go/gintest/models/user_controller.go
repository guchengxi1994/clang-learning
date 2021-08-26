package models

func (user User) InsertSingleUser() error {
	result := DB.Debug().Create(&user)
	return result.Error
}
