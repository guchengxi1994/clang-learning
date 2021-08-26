package com.xiaoshuyui.day1.utils

class KtClass1(name: String, city: String) {
    var name: String? = name
        get() = field?.length.toString()
    var city: String? = city
        get() = field?.toUpperCase()

    //    constructor(
//            name:String,city:String
//    ){}

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as KtClass1

        if (name != other.name) return false
        if (city != other.city) return false

        return true
    }

    override fun hashCode(): Int {
        var result = name.hashCode()
        result = 31 * result + city.hashCode()
        return result
    }
}