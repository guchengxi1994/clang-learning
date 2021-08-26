#[allow(dead_code)]
pub struct Rect{
   pub width:u32,
   pub height:u32,
}

#[allow(dead_code)]
pub fn  get_area(rect:&mut Rect)->u32{
    rect.height = 200;
    return rect.height*rect.width;
}

fn main() {

    let mut a = String::from("aaaaaaaaaaaaaaa");
    let mut c = &mut a;
  
    c = &mut String::from("sasasas");
  
    println!("{}",c);
  }