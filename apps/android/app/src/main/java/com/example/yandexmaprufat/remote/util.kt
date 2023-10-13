package com.example.yandexmaprufat.remote

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

sealed class Either<out L, out R> {
    companion object {
        inline fun <R> of(action: () -> R): Either<Exception, R> {
            return try {
                Right(action())
            } catch (ex: Exception) {
                Left(ex)
            }
        }
    }
}

data class Right<out R>(val value: R) : Either<Nothing, R>()
data class Left<out L>(val value: L) : Either<L, Nothing>()

suspend fun <T> safeRequest(request: suspend () -> T): Either<Exception, T> =
    Either.of { withContext(Dispatchers.IO) { request() } }