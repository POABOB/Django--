$(function()
{
	error = false;

	$('#email').blur(function()
	{
		if($('#email').val().length == 0)
		{
			$('.error_email').html("<span>請輸入email!</span><br>").show();
			error_email = false;
		}
		else
		{
			$('.error_email').hide();
			error_email = true;
		}
	});

	$('#password').blur(function()
	{
		if($('#password').val().length == 0)
		{
			$('.error_password').html("<span>請輸入密碼!</span><br>").show();
			error_password = false;
		}
		else
		{
			$('.error_password').hide();
			error_password = true;
		}
	});

	if({{error}} == 1)
		{
			$('.error').html('<span>Email或密碼錯誤!</span><br>').show();
		}

});

		