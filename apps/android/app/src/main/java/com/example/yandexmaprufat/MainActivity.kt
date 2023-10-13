package com.example.yandexmaprufat

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.yandexmaprufat.ui.Fragment1


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        if (savedInstanceState == null) {
            supportFragmentManager.beginTransaction()
                .replace(R.id.container, Fragment1.newInstance())
                .commitNow()
        }
    }
}