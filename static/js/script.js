// Generated by CoffeeScript 1.7.1
(function() {
  $('.dep-code-container').toggle();

  $('a.dep-name').on('click', function(e) {
    e.preventDefault();
    return $(this).siblings().siblings('.dep-code-container').fadeToggle();
  });

}).call(this);
