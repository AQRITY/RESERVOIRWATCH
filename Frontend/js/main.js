$(window).load(function () {
  // executes when complete page is fully loaded, including all frames, objects and images
});

function callButtonGraph(river, type, button) {
  var riverFolder = '';
  riverFolder = river == 'hemavathi' ? 'Hemavathi' : riverFolder;
  riverFolder = river == 'harangi' ? 'Harangi' : riverFolder;
  riverFolder = river == 'kabini' ? 'Kabini' : riverFolder;
  riverFolder = river == 'krs' ? 'KRS' : riverFolder;

  var buttonType = '';
  buttonType = button == 'level' ? 'level.csv' : buttonType;
  buttonType = button == 'storage' ? type + '_storage.csv' : buttonType;
  buttonType = button == 'inflow' ? type + '_inflow.csv' : buttonType;
  buttonType = button == 'outflow' ? type + '_outflow.csv' : buttonType;
  buttonType = button == 'rainfall' ? 'rainfall.csv' : buttonType;
  buttonType = button == 'soilmoisture' ? 'soilmoisture.csv' : buttonType;
  buttonType =
    button == 'evapotranspiration' ? 'evapotranspiration.csv' : buttonType;

  var graphId = 0;
  graphId = river == 'hemavathi' ? 55 : graphId;
  graphId = river == 'harangi' ? 56 : graphId;
  graphId = river == 'kabini' ? 58 : graphId;
  graphId = river == 'krs' ? 57 : graphId;

  g3 = new Dygraph(
    document.getElementById(river + '-levelgraphdiv'),
    'Reservoirs-Data/' + riverFolder + '/' + buttonType,
    {
      rollPeriod: 1,
    }
  );
}

$(document).ready(function () {
  $('.extrasectionforinflow').css('display', 'none');

  $('.buttonsection ul.observed li').click(function () {
    var varible = $(this).text();
    console.log($(this), '--this');

    if (['Storage', 'Inflow'].includes(varible.trim())) {
      $('.buttonsection ul li').removeClass('buttonactive');
      $('.buttonsection ul li').removeClass('greenactive');
      $(this).addClass('greenactive');
    } else {
      $('.buttonsection ul li').removeClass('greenactive');
      $('.buttonsection ul li').removeClass('buttonactive');
      $(this).addClass('buttonactive');
    }

    //   $('.buttonsection ul li').removeClass('buttonactive');
    //   $(this).addClass('buttonactive');

    console.log(varible + ' function called');
    if (['Storage', 'Inflow'].includes(varible.trim())) {
      $('.extrasectionforinflow').css('display', 'flex');
    } else {
      $('.extrasectionforinflow').css('display', 'none');
    }
  });
});

$(document).ready(function () {
  $('.buttonsection ul.simulated li').click(function () {
    var varible = $(this).text();
    $('.buttonsection ul li').removeClass('buttonactive');

    $(this).addClass('buttonactive');
    console.log(varible + ' function called');

    $('.extrasectionforinflow').css('display', 'none');
  });
});

function callForecast(reservoirsName) {
  var a = $('#' + reservoirsName + ' input[name=predictedDays]:checked').val();
  var b = $('#' + reservoirsName + ' input[name=predictedDate]').val();

  console.log(b, a);
}

$(document).ready(function () {
  $('.datedayforcast').click(function () {
    console.log('forecast called');
  });
});

//onclick function
$(document).ready(function () {
  $('.onclickbtn').click(function () {
    $('.showDiv').hide();
    var varible = $(this).attr('id');
    $('.' + varible).show();
  });
});

//onclick function
$(document).ready(function () {
  $('.onclickbtn').click(function () {
    $('.showDivone').hide();
    var varible = $(this).attr('id');
    $('.' + varible).show();
  });
});

$(document).ready(function () {
  $('.onclickbtntwo').click(function () {
    $('.showDivtwo').hide();
    var varible = $(this).attr('id');
    $('.' + varible).show();
    $('.body_starts').hide();
    if (varible == 56) {
      graphPath = 'Reservoirs-Data/Harangi/level.csv';
      graphId = 'harangi';
    } else if (varible == 57) {
      graphPath = 'Reservoirs-Data/KRS/level.csv';
      graphId = 'krs';
    } else if (varible == 58) {
      graphPath = 'Reservoirs-Data/Kabini/level.csv';
      graphId = 'kabini';
    } else if (varible == 55) {
      graphPath = 'Reservoirs-Data/Hemavathi/level.csv';
      graphId = 'hemavathi';
    }
    g3 = new Dygraph(
      document.getElementById(graphId + '-levelgraphdiv'),
      graphPath,
      {
        rollPeriod: 1,
      }
    );
  });
});

//remove class

$('.adding').removeClass('riverlines');

$('.rivershowbtn').click(function () {
  $('.adding').toggleClass('riverlines');
});

let logo = document.getElementById('logo');
let leftNav = document.getElementById('left_Navigation');
let main_content = document.getElementById('main_content');
let word = document.getElementById('word');
let word1 = document.getElementById('word1');
let word2 = document.getElementById('word2');
let word3 = document.getElementById('word3');
let word4 = document.getElementById('word4');
let word5 = document.getElementById('word5');
let wordlogo = document.getElementById('wordlogo');

main_content.style.width = '100%';

$('.open').hover(function () {
  if (leftNav.style.width == '250px') {
    setTimeout(function () {
      // leftNav.style.transition = '.2s';
      leftNav.style.width = '65px';
      main_content.style.width = '100%';
      word.style.display = 'none';
      word1.style.display = 'none';
      word2.style.display = 'none';
      word3.style.display = 'none';
      word4.style.display = 'none';
      word5.style.display = 'none';
      wordlogo.style.display = 'none';
    }, 3000);
  } else {
    // leftNav.style.transition = '.2s';
    // leftNav.style.transitionDelay = '.0s';
    leftNav.style.width = '250px';
    main_content.style.width = '85%';
    word.style.display = 'inherit';
    word1.style.display = 'inherit';
    word2.style.display = 'inherit';
    word3.style.display = 'inherit';
    word4.style.display = 'inherit';
    word5.style.display = 'inherit';
    wordlogo.style.display = 'initial';
  }
});
logo.hover = function () {};

$('.circle_percent').each(function () {
  var $this = $(this),
    $dataV = $this.data('percent'),
    $dataDeg = $dataV * 3.6,
    $round = $this.find('.round_per');
  $round.css('transform', 'rotate(' + parseInt($dataDeg + 180) + 'deg)');
  $this.append(
    '<div class="circle_inbox"><span class="percent_text"></span></div>'
  );
  $this.prop('Counter', 0).animate(
    { Counter: $dataV },
    {
      duration: 2000,
      easing: 'swing',
      step: function (now) {
        $this.find('.percent_text').text(Math.ceil(now) + '%');
      },
    }
  );
  if ($dataV >= 51) {
    $round.css('transform', 'rotate(' + 360 + 'deg)');
    setTimeout(function () {
      $this.addClass('percent_more');
    }, 1000);
    setTimeout(function () {
      $round.css('transform', 'rotate(' + parseInt($dataDeg + 180) + 'deg)');
    }, 1000);
  }
});

function makesvg(percentage, inner_text = '') {
  var abs_percentage = Math.abs(percentage).toString();
  var percentage_str = percentage.toString();
  var classes = '';

  if (percentage < 0) {
    classes = 'danger-stroke circle-chart__circle--negative';
  } else if (percentage > 0 && percentage <= 30) {
    classes = 'warning-stroke';
  } else {
    classes = 'success-stroke';
  }

  var svg =
    '<svg class="circle-chart" viewbox="0 0 33.83098862 33.83098862" xmlns="http://www.w3.org/2000/svg">' +
    '<circle class="circle-chart__background" cx="16.9" cy="16.9" r="15.9" />' +
    '<circle class="circle-chart__circle ' +
    classes +
    '"' +
    'stroke-dasharray="' +
    abs_percentage +
    ',100"    cx="16.9" cy="16.9" r="15.9" />' +
    '<g class="circle-chart__info">' +
    '   <text class="circle-chart__percent" x="17.9" y="15.5">' +
    percentage_str +
    '%</text>';

  if (inner_text) {
    svg +=
      '<text class="circle-chart__subline" x="16.91549431" y="22">' +
      inner_text +
      '</text>';
  }

  svg += ' </g></svg>';

  return svg;
}

(function ($) {
  $.fn.circlechart = function () {
    this.each(function () {
      var percentage = $(this).data('percentage');
      var inner_text = $(this).text();
      $(this).html(makesvg(percentage, inner_text));
    });
    return this;
  };
})(jQuery);

$(function () {
  $('.circlechart').circlechart();
});

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function currentSlide(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName('mySlides');
  var dots = document.getElementsByClassName('dot');
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(' active', '');
  }
  slides[slideIndex - 1].style.display = 'block';
  dots[slideIndex - 1].className += ' active';
}
