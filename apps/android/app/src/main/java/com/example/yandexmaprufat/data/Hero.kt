package com.example.yandexmaprufat.data

import com.google.gson.annotations.SerializedName

data class Hero(
    @SerializedName("name") val name : String,
    @SerializedName("realname") val realname : String,
    @SerializedName("team") val team : String,
    @SerializedName("firstappearance") val firstappearance : String,
    @SerializedName("createdby") val createdby : String,
    @SerializedName("publisher") val publisher : String,
    @SerializedName("imageurl") val imageurl : String,
    @SerializedName("bio") val bio : String,
)
