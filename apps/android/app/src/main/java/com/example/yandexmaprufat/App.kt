package com.example.yandexmaprufat

import android.app.Application
import androidx.room.Room
import com.example.yandexmaprufat.db.AppDatabase
import com.example.yandexmaprufat.db.AppDatabase2
import com.yandex.mapkit.MapKitFactory

class App : Application() {
    override fun onCreate() {
        super.onCreate()
        MapKitFactory.setApiKey(BuildConfig.MAPKIT_API_KEY)
//        db = Room.databaseBuilder(applicationContext, AppDatabase::class.java, "Sample.db")
//            //.createFromAsset("my_bd_rufat2.db")
//            //.fallbackToDestructiveMigration()
//            .allowMainThreadQueries()
//            .build()
//
//        db2 = Room.databaseBuilder(applicationContext, AppDatabase2::class.java, "Sample2.db")
//            .allowMainThreadQueries()
//            .build()

    }

    companion object{
        var db : AppDatabase? = null
        var db2 : AppDatabase2? = null
    }
}