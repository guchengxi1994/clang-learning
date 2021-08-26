package com.xiaoshuyui.day1.utils

fun loopTest(arg: List<String>) {
    for (item in arg) {
        println(item)
    }
}

fun loopTest2() {
    for (i in 1..10) {
        if (i % 3 == 0) {
            println(i)
        }
    }
}

fun loopTest3() {
    loop@ for (i in 1..100) {
        if (i * i > 100) {
            println(i)
            break@loop
        }
    }
}