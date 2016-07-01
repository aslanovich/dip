$("#btnGenerateModule").click(function(){
  var teacher = $("#teacher :selected").val();
  var subject = $("#subject :selected").val();
  var aud = $("#aud :selected").val();
  var alter = $("#alter :selected").val();
  var course = $("#course").val();
  form.init(teacher, subject, aud, alter, course); 
});

var form = {
    teacher: '',
    subject: '',
    aud: '',
    alter: '',
    course: '',
    day: '',
    pair: '',
    group: '',
    $fields: null,
  
  init: function(teacher, subject, aud, alter, course) {
  	this.teacher = teacher;
    this.subject = subject;
    this.aud = aud;
    this.alter = alter;
    this.course = course;
    this.$fields = $("#result-form .field");
    this.createBlock();
	console.log(form);
  },
  
  createBlock: function() {
  	self = this;
  	this.$fields.each(function (index) {
    	var field = $(this).data("field");
      var value = self[field];
      
      if (field == 'alter') {
        value = self.getStringAlter(value);
      }
      $(this).text(value);
    });
	// debugger;
  },

  getStringAlter: function(value) {
    switch(value) {
      case '0':
        return '';
      case '1':
        return '(+)';
      case '2':
        return '(-)';
    }
  },
  
  addPlanDetails: function(pair, day, group) {
    this.pair = pair;
    this.day = day;
    this.group = group;
	console.log(form);
  },

  send: function() {
  	self = this;
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
  	$.ajax({
      type: "POST",
      url: '/plan/',
      data: { 
        teacher: self.teacher,
        subject: self.subject,
        audience: self.aud,
        alter: self.alter,
        course: self.course,
        group: self.group,
        day: self.day,
        pair: self.pair
      },
      headers: { 'X-CSRFToken' : csrf},
      success: function () {
      	//alert("success");
      },
      error: function (e) {
        debugger;
        alert(e);
      }
    });
  }
}
