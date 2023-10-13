package com.example.yandexmaprufat.remote

import com.example.yandexmaprufat.data.Hero
import retrofit2.http.GET

interface RemoteApi {
    @GET("marvel")
    suspend fun getContacts(): List<Hero>
}