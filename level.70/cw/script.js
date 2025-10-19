function Task(title, desc, state, deadline) {
    this.title = title;      
    this.desc = desc;       
    this.state = state;     
    this.deadline = deadline;
  
    this.complete = function() {
      this.state = "დასრულებულია";
      console.log(this.title + " დასრულდა");
    };
  }
  
  let t1 = new Task("გაკვეთილი", "დავწერო დავალება", "მიმდინარე", "2025-10-13");
  let t2 = new Task("ვარჯიში", "დარბაზი 1 საათით", "გეგმაშია", "2025-10-14");
  let t3 = new Task("წიგნი", "მეორე თავი წავიკითხო", "მიმდინარე", "2025-10-15");
  

  t1.complete();
  t2.complete();
  t3.complete();
  
  
  console.log(t1);
  console.log(t2);
  console.log(t3);