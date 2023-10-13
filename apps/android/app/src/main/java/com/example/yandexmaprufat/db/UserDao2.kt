package com.example.yandexmaprufat.db

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.Query

@Dao
interface UserDao2 {
    @Query("SELECT * FROM user2")
    fun getAll(): List<User2>

//    @Query("SELECT * FROM user WHERE id IN (:userIds)")
//    fun loadAllByIds(userIds: IntArray): List<User>

    @Query(
        "SELECT * FROM user2 WHERE name LIKE :first AND " +
                "message LIKE :last LIMIT 1"
    )
    fun findByName(first: String, last: String): User2

    @Insert
    fun insertAll(vararg users: User2)

    @Delete
    fun delete(user: User2)
}