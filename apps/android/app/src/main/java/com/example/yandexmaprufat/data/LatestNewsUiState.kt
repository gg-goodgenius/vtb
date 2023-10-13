package com.example.yandexmaprufat.data

sealed class LatestNewsUiState {
    data class Success(val news: List<Int>): LatestNewsUiState()
    data class Error(val exception: Throwable): LatestNewsUiState()
}