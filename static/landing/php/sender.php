<?php
/*
 **************************************
 *									  *
 * Config here                        *
 *									  *
 **************************************
 */

$to = 'lucio.bosco@gmail.com';
$siteName = "Elitrec";

/*
 *************************************************************
 *									                         *
 *      Don't Change below code, if you don't know php.      *
 *									                         *
 *************************************************************
 */

$name = $_POST['fname'];
$mail = $_POST['email'];
$subject = $_POST['subj'];
$message = $_POST['mssg'];

if (isset($name) && isset($mail) && isset($message)) {
	

	$mailSub = $siteName . ' [Contacto] - '.$subject;

	$body = 'Nombre: ' . $name . "\n\n";
	$body .= 'Email: ' . $mail . "\n\n";
	$body .= 'Asunto: ' . $subject . "\n\n";
	$body .= 'Mensaje: ' . $message;

	$header = 'From: ' . $mail . "\r\n";
	$header .= 'Reply-To:  ' . $mail . "\r\n";
	$header .= 'X-Mailer: PHP/' . phpversion();

	echo mail($to, $mailSub, $body, $header);
}else{
	echo '0';
}
?>