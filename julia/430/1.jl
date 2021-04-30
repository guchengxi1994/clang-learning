d = Dict("a"=>"aaa","b"=>"bbb")

for (k,v) in d
    println("$k is a $v")
end

struct Person
    age::Int
    name::Any
end

function sayHello(p::Person)
    println("1.jl")
end

p = Person(1000,"小黄鸡")

pp = typeof(p)(2000,"大黄鸡")


sayHello(p)
