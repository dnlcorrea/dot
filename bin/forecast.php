#!/usr/bin/php

<?php

$json = json_decode(file_get_contents('/home/daniel/.cache/forecast.json', 'r'));

for($i=0; $i<12; $i++) {
	$item = $json->list[$i];

	print date('d h:i', $item->dt).' ';

	print number_format($item->main->temp)."º";

	print ($i+1) % 3 === 0
		? "\n"
		: "   ";
}

