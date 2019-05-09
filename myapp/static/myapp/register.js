$(function()
{
	var error_email = false;

	$('#email').blur(function()
	{
		check_email();
	});

	function check_email()
	{
		var len = $('#email').val().length;

		if(len == 0)
		{
			$('#email').next().html("請輸入email!").show();
			error_email = false;
		}
		else
		{
			$.get('/user/check_email/?email='+$('#email').val(), function(data)
			{
				if(data.count == 1)
				{
					$('#email').next().html("Email已被註冊!").show();
					error_email = true;
				}
				else
				{
					$('#email').next().hide();
					error_email = false;
				}
			});
		}

	}

});
