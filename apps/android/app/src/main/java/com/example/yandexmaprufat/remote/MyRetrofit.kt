package com.example.yandexmaprufat.remote

import android.content.Context
import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.util.concurrent.TimeUnit

class MyRetrofit() {

    val api: RemoteApi

    init {
        val okHttpClient = OkHttpClient.Builder()
            .connectTimeout(1, TimeUnit.MINUTES)
            .readTimeout(30, TimeUnit.SECONDS)
            .writeTimeout(15, TimeUnit.SECONDS)
            .build()

        val retrofit = Retrofit.Builder()
            .baseUrl(URL_TEST)
            .addConverterFactory(GsonConverterFactory.create())
            .client(okHttpClient)
            .build()

        api = retrofit.create(RemoteApi::class.java)
    }

    companion object {
        private var instanceLink: MyRetrofit? = null
        fun getInstance(context: Context): MyRetrofit {
            if (instanceLink == null) instanceLink = MyRetrofit()
            return instanceLink as MyRetrofit
        }

        private const val URL_TEST = "https://simplifiedcoding.net/demos/"
    }
}