package com.example.yandexmaprufat.util

import android.app.Activity
import androidx.appcompat.app.AlertDialog
import com.example.yandexmaprufat.R

fun Activity.showErrorDialog(text: String?) {
    AlertDialog.Builder(this).apply {
        setTitle(R.string.error_title_text)
        setMessage(text.orEmpty())
        setNeutralButton(R.string.error_button_text) { dialog, _ ->
            dialog.dismiss()
        }
    }.run {
        create()
        show()
    }
}