package com.example.yandexmaprufat.db

import android.util.Log
import com.example.yandexmaprufat.App

class TestLogDb {
    fun testLogDb(){
        App.db2?.userDao2()
            ?.insertAll(User2(name = "222222222", message = "2222222222   42334=========%%%"))
        App.db2?.userDao2()
            ?.insertAll(User2(name = "222222222", message = "2222222222   42334=========%%%"))

        App.db?.userDao()?.getAll()?.forEach {
            Log.d("TAGt", "l =  $it")
        }

        App.db2?.userDao2()?.getAll()?.forEach {
            Log.d("TAGt", "l2 =  $it")
        }
    }
}