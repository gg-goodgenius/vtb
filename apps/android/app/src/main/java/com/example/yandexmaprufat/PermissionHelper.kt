package com.example.yandexmaprufat

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.provider.Settings
import android.util.Log
import androidx.appcompat.app.AlertDialog
import androidx.core.app.ActivityCompat


const val PERMISSION_REQUEST_LOCATION = 1000

fun Activity.requestPermission() {
    if (ActivityCompat.shouldShowRequestPermissionRationale(
            this,
            android.Manifest.permission.ACCESS_FINE_LOCATION
        )
    ) {
        showRationalDialog(this)
    } else {
        val res = ActivityCompat.requestPermissions(
            this,
            arrayOf(
                android.Manifest.permission.ACCESS_FINE_LOCATION,
                android.Manifest.permission.ACCESS_COARSE_LOCATION
            ),
            PERMISSION_REQUEST_LOCATION
        )
    }
}

fun Activity.isPermissionGranted(): Boolean {
    return ActivityCompat.checkSelfPermission(
        this,
        android.Manifest.permission.ACCESS_FINE_LOCATION
    ) == PackageManager.PERMISSION_GRANTED &&
            ActivityCompat.checkSelfPermission(
                this,
                android.Manifest.permission.ACCESS_COARSE_LOCATION
            ) == PackageManager.PERMISSION_GRANTED
}

private fun showRationalDialog(activity: Activity) {
    AlertDialog.Builder(activity).apply {
        setTitle(R.string.permission_rational_dialog_title)
        setMessage(R.string.permission_rational_dialog_message)
        setPositiveButton(R.string.permission_rational_dialog_positive_button_text) { _, _ ->
            ActivityCompat.requestPermissions(
                activity, arrayOf(
                    android.Manifest.permission.ACCESS_FINE_LOCATION,
                    android.Manifest.permission.ACCESS_COARSE_LOCATION
                ),
                PERMISSION_REQUEST_LOCATION
            )
        }
        setNegativeButton(R.string.permission_rational_dialog_negative_button_text) { dialog, _ ->
            dialog.dismiss()
        }
    }.run {
        create()
        show()
    }
}

private fun showSettingsDialog(activity: Activity){
    AlertDialog.Builder(activity).apply {
        setTitle(R.string.settings_dialog_title)
        setMessage(R.string.settings_dialog_message)
        setPositiveButton(R.string.settings_dialog_positive_button_text) { _, _ ->
            startAppSettings(activity)
        }
        setNegativeButton(R.string.settings_dialog_negative_button_text){ dialog, _ ->
            dialog.dismiss()
        }
    }.run {
        create()
        show()
    }
}

private fun startAppSettings(context: Context) {
    val intent = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS)
    val uri: Uri = Uri.fromParts("package", context.packageName, null)
    intent.data = uri
    context.startActivity(intent)
}

fun Activity.onRequestPermissionsResultCheck(
    requestCode: Int,
    grantResults: IntArray
){
    when (requestCode) {
        PERMISSION_REQUEST_LOCATION -> if (grantResults.size >= 2 &&
            grantResults[0] != PackageManager.PERMISSION_GRANTED &&
            grantResults[1] != PackageManager.PERMISSION_GRANTED
        ) {
            showSettingsDialog(this)
        }
        else -> Unit
    }
}