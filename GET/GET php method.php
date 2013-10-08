<?php

function myfunction($word){
		#API Key
		$access_key = "YOUR ACCESS TOKEN HERE";		

		#URL de la API
		$url="http://apicultur.io/api/myapi".$word;	

	#Start cURL
	$ch = curl_init();

	#We add the Authorization header
	curl_setopt($ch,CURLOPT_HTTPHEADER,array( 'Accept: application/json', 'Authorization: Bearer ' . $access_key ));

	#We pass the url of the API 
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

	#We create the variable $response where the API response will be kept
	$response = curl_exec($ch);

	$http_status = curl_getinfo($ch, CURLINFO_HTTP_CODE);

	#We close the cURL 
	curl_close($ch);	
    
	#If myapi responded with a 200 status, then we decode the json and asign the value to the $obj variable
	#If the status is not 200, then we print an error warningswitch ($http_status) {
    case '200':
		$obj = json_decode($respuesta);
	  break;
    default:
	  echo "<br/>Error when making the call to myapi.".$word;
	  echo "<br/>Error:" .$http_status ;
      break;
	}

	#We return $obj 	
	return $obj;
	}
	
?>	
