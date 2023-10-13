package com.example.yandexmaprufat.ui

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.yandexmaprufat.data.LatestNewsUiState
import com.example.yandexmaprufat.remote.Left
import com.example.yandexmaprufat.remote.MyRetrofit
import com.example.yandexmaprufat.remote.Right
import com.example.yandexmaprufat.remote.safeRequest
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class MainViewModel : ViewModel() {
    private val _uiState: MutableStateFlow<LatestNewsUiState> =
        MutableStateFlow(LatestNewsUiState.Success(emptyList()))
    val uiState: StateFlow<LatestNewsUiState> = _uiState

    init {
        viewModelScope.launch {
//            launch {
//                delay(2000)
//                _uiState.value = LatestNewsUiState.Success(listOf(1, 2, 3))
//                delay(2000)
//                _uiState.value = LatestNewsUiState.Error(Throwable("ошибка 123334"))
//                _uiState.value = LatestNewsUiState.Success(listOf())
//
//            }
            launch {
                val api = MyRetrofit().api

                when (val r = safeRequest { api.getContacts() }) {
                    is Left -> {_uiState.value = LatestNewsUiState.Error(r.value)}
                    is Right -> {
                        //_uiState.value = LatestNewsUiState.Success(r.value)
                        Log.d("TAGt", "r =${r.value}")
                    }
                }
            }
        }
    }
}