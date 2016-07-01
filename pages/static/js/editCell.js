$(".edit-cell").click(function(){
	var planId = $(this).find('[data-plan-id]').attr('data-plan-id');
	var teacher = $(this).find('[data-teacher]').attr('data-teacher');
	var alter = $(this).find('[data-alter]').attr('data-alter');
	var subject = $(this).find('[data-subject]').attr('data-subject');
	var aud = $(this).find('[data-audience]').attr('data-audience');
	var group = $(this).attr('data-group');
	var pair = $(this).attr('data-pair');
	var day = $(this).attr('data-day');
	var course = $('#course').val();
	lesson.init($(this), planId, teacher, subject, aud, alter, course, day, pair, group);
});

$("#save-lesson").click(function(){
	lesson.refreshFields();
	lesson.saveLesson();
});

$("#delete-lesson").click(function(){
	lesson.deleteLesson();
});

var lesson = {
	planId: null,
    teacher: '',
    subject: '',
    aud: '',
    alter: '',
    course: '',
    day: '',
    pair: '',
    group: '',
    $lessonCell: null,
  
  init: function($lessonCell, planId, teacher, subject, aud, alter, course, day, pair, group) {
  	this.$lessonCell = $lessonCell;
  	this.planId = planId;
  	this.teacher = teacher;
    this.subject = subject;
    this.aud = aud;
    this.alter = alter;
    this.course = course;
    this.day = day;
    this.pair = pair;
    this.group = group;
    this.createModal();
  },

  createModal: function() {
  	if (this.planId) {
	  	$('#edit-teacher').val(this.teacher);
		$('#edit-alter').val(this.alter);
		$('#edit-subject').val(this.subject);
		$('#edit-aud').val(this.aud);
		$('#edit-plan').val(this.planId);
	}
	$('#myModal').modal("show");
  },

  refreshFields: function() {
  	this.teacher = $("#edit-teacher :selected").val();
	this.subject = $("#edit-subject :selected").val();
	this.aud = $("#edit-aud :selected").val();
	this.alter = $("#edit-alter :selected").val();
  },

  deleteLesson: function() {
  	self = this;
  	var planId = $('#edit-plan').val();
	var csrf = $('input[name="csrfmiddlewaretoken"]').val();
  	$.ajax({
      type: "POST",
      url: '/plan/',
      data: { 
        planId: self.planId,
        deletePlan: true
      },
      headers: { 'X-CSRFToken' : csrf},
      success: function () {
      	self.$lessonCell.find('.cell-content').remove();
      },
      error: function (e) {
        debugger;
        alert(e);
      }
    });
    $('#myModal').modal("hide");
  },

  saveLesson: function() {
  	self = this;
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
  	$.ajax({
      type: "POST",
      url: '/plan/',
      data: {
      	planId: self.planId,
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
    $('#myModal').modal("hide");
  }
}
