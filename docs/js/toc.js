jQuery.fn.toc = function(depth) {
	return this.each(function() {
		var headers, re, i;
		headers = [];
		re = new RegExp("h([1-" + depth + "])", "i");
		i = 0;
		$("*").each(function() {
			var ms;
			ms = $(this).get(0).tagName.match(re);
			if(ms) {
				$(this).prop("id", "header" + i);
				headers.push([
					parseInt(ms[1]),
					"<a href='#header" + i + "'>" + $(this).html() + "</a>"
				]);
				i++;
			}
		});
		$(this).append(array2ul(headers));
	});
}

function array2ul(a) {
	lines=[];
	lines.push("<ul>");
	for(i = 0; i < a.length; i++) {
		thislevel=a[i][0];
		prelevel = a[i-1] === undefined ? 0 : a[i-1][0];
		nextlevel = a[i+1] === undefined ? 0 : a[i+1][0];
		if(prelevel<thislevel){
			lines.push("<ul>");
		}
		lines.push("<li>");
		lines.push(a[i][1]);
		if(thislevel>=nextlevel){
			temp="</li>";
			for(x=0;x<thislevel-nextlevel;x++){
				temp+="</ul></li>";
			}
			lines.push(temp);
		}
	}
	lines.push("</ul>");
	return lines.join("");
}
