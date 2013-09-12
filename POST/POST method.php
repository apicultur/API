<?php 	

function myfunction($mytext) {
	  	$access_key = "YOUR ACCESS KEY HERE";	
	  
	  
		$url="https://apicultur.io/api/myapi";	

		
		$theUser = '{"texto" : "'.$mytext.'"}';	

  
	  #We set the curl
		$ch = curl_init();

		#We add the Authorization header
		curl_setopt($ch,CURLOPT_HTTPHEADER,array( 'Accept: application/json', 'Content-Type: application/json', 'Authorization: Bearer ' . $access_key ));

	#Pasamos la url de la api con
		
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_POST, TRUE);
		
		curl_setopt($ch, CURLOPT_POSTFIELDS, $theUser);

	#We keep the json returned by our API in the variable $reponse.
		$response = curl_exec($ch);
		
		$http_status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
	
	#We close the cURL resource
		curl_close($ch);	
    
	#If myapi responded with a 200 status, then we decode the json and asign the value to the $obj variable
	#If the status is not 200, then we print an error warning
	switch ($http_status) {
    case '200':
		$obj = json_decode($response);
	 break;
    default:
	  echo "<br/>Error when making the call to myapi" ;
	  echo "<br/>Error:" .$http_status ;
      break;
	}
	
	#We return $obj 
	return $obj;
}
?>
	