package com.example.yandexmaprufat.util

import android.content.Context
import android.content.SharedPreferences
import androidx.core.content.edit

class SharedPreferencesProvider(context: Context) {
    private var sharedPreferences: SharedPreferences =
        context.getSharedPreferences(SP_SETTINGS, Context.MODE_PRIVATE)

    fun savePreferencesString(key: String, value: String?) {
        sharedPreferences.edit { putString(key, value) }
    }

    fun getPreferencesString(key: String, defValue: String): String? =
        sharedPreferences.getString(key, defValue)

    companion object {
        private var instanceLink: SharedPreferencesProvider? = null
        fun getInstance(context: Context) : SharedPreferencesProvider {
            if (instanceLink == null) instanceLink = SharedPreferencesProvider(context)
            return instanceLink as SharedPreferencesProvider
        }

        private const val SP_SETTINGS = "app_data"
    }
}