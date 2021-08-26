package com.xiaoshuyui.day1

import com.xiaoshuyui.day1.utils.loopTest
import com.xiaoshuyui.day1.utils.loopTest2
import com.xiaoshuyui.day1.utils.loopTest3

fun  main(args:Array<String>){
    println("hello world")

    // loop test1
    var items = listOf<String>("apple","banana","kiwi")
    loopTest(items)

    loopTest2()
    loopTest3()
}