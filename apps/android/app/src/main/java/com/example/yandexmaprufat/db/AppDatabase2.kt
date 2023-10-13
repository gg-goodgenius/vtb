package com.example.yandexmaprufat.db

import androidx.room.Database
import androidx.room.RoomDatabase

@Database(
    entities = [
        User2::class,
    ], version = 1
)
abstract class AppDatabase2 : RoomDatabase() {
    abstract fun userDao2(): UserDao2
}