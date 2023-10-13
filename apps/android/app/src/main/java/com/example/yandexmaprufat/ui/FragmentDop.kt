package com.example.yandexmaprufat.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import com.example.yandexmaprufat.R
import com.example.yandexmaprufat.databinding.FragmentDopBinding

class FragmentDop : Fragment() {
    private lateinit var viewModel: DopViewModel
    private lateinit var binding: FragmentDopBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        viewModel = ViewModelProvider(this)[DopViewModel::class.java]
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        return inflater.inflate(R.layout.fragment_dop, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        FragmentDopBinding.inflate(layoutInflater)
        binding = FragmentDopBinding.bind(view)
        binding.message.text = "12321321321"
        binding.buttonBack.setOnClickListener {
            fragmentManager?.popBackStack()
        }
    }

    companion object {
        fun newInstance() = FragmentDop()
    }

}