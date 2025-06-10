+++
type = "question"
title = "Internal Nominatim returning a different city than that returned by the public Nominatim"
description = '''Hi, our team is hosting Nominatim(app version 3.6.0) internally with the latest North America OSM data downloaded from http://download.geofabrik.de/ and TIGER data set of 2019. We recently noticed that the reverse-geocoding result of a specific coordinate from our Nominatim is a bit different from t...'''
date = "2021-03-29T21:46:00Z"
lastmod = "2021-03-29T21:46:00Z"
weight = 79439
keywords = [ "tiger", "city", "reversegeocoding", "nominatim" ]
aliases = [ "/questions/79439" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Internal Nominatim returning a different city than that returned by the public Nominatim](/questions/79439/internal-nominatim-returning-a-different-city-than-that-returned-by-the-public-nominatim)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79439-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, our team is hosting Nominatim(app version 3.6.0) internally with the latest North America OSM data downloaded from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> and TIGER data set of 2019. We recently noticed that the reverse-geocoding result of a specific coordinate from our Nominatim is a bit different from that of the public Nominatim.</p>
<p><strong>Coordinate of interest:</strong> (lat: 33.88741050822116, lon:-118.26697164758119)</p>
<p><strong>What public Nominatim returns:</strong></p>
<p>URL: <a href="https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=33.8874564&amp;lon=-118.2669698&amp;zoom=18&amp;addressdetails=1#">https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=33.8874564&amp;lon=-118.2669698&amp;zoom=18&amp;addressdetails=1#</a></p>
<pre><code>{
   &quot;place_id&quot;:264864471,
   &quot;licence&quot;:&quot;Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright&quot;,
   &quot;osm_type&quot;:&quot;way&quot;,
   &quot;osm_id&quot;:466977226,
   &quot;lat&quot;:&quot;33.88741050822116&quot;,
   &quot;lon&quot;:&quot;-118.26697164758119&quot;,
   &quot;display_name&quot;:&quot;546, East Airline Way, West Rancho Dominguez, Los Angeles County, California, 90248, United States&quot;,
   &quot;address&quot;:{
      &quot;house_number&quot;:&quot;546&quot;,
      &quot;road&quot;:&quot;East Airline Way&quot;,
      &quot;hamlet&quot;:&quot;West Rancho Dominguez&quot;,
      &quot;county&quot;:&quot;Los Angeles County&quot;,
      &quot;state&quot;:&quot;California&quot;,
      &quot;postcode&quot;:&quot;90248&quot;,
      &quot;country&quot;:&quot;United States&quot;,
      &quot;country_code&quot;:&quot;us&quot;
   },
   &quot;boundingbox&quot;:[
      &quot;33.887360508221&quot;,
      &quot;33.887460508221&quot;,
      &quot;-118.26702164758&quot;,
      &quot;-118.26692164758&quot;
   ]
}</code></pre>
<p><strong>What our internal Nominatim returns:</strong></p>
<p>Command we ran:</p>
<pre><code>curl &#39;http://localhost:8080/reverse?format=json&amp;lat=33.8874564&amp;lon=-118.2669698&amp;zoom=18&amp;addressdetails=1&#39; -H &#39;pragma: no-cache&#39;   -H &#39;cache-control: no-cache&#39;   -H &#39;sec-ch-ua: &quot;Google Chrome&quot;;v=&quot;89&quot;, &quot;Chromium&quot;;v=&quot;89&quot;, &quot;;Not A Brand&quot;;v=&quot;99&quot;&#39;   -H &#39;sec-ch-ua-mobile: ?0&#39;   -H &#39;upgrade-insecure-requests: 1&#39;   -H &#39;user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36&#39;   -H &#39;accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9&#39;   -H &#39;sec-fetch-site: none&#39;   -H &#39;sec-fetch-mode: navigate&#39;   -H &#39;sec-fetch-user: ?1&#39;   -H &#39;sec-fetch-dest: document&#39;   -H &#39;accept-language: en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,es-MX;q=0.6,es;q=0.5&#39;   --compressed
&#10; {
   &quot;place_id&quot;:68635125,
   &quot;licence&quot;:&quot;Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright&quot;,
   &quot;osm_type&quot;:&quot;way&quot;,
   &quot;osm_id&quot;:466977226,
   &quot;lat&quot;:&quot;33.88741050822116&quot;,
   &quot;lon&quot;:&quot;-118.26697164758119&quot;,
   &quot;display_name&quot;:&quot;546, East Airline Way, West Rancho Dominguez, El Monte, Los Angeles County, California, 90248, United States of America&quot;,
   &quot;address&quot;:{
      &quot;house_number&quot;:&quot;546&quot;,
      &quot;road&quot;:&quot;East Airline Way&quot;,
      &quot;hamlet&quot;:&quot;West Rancho Dominguez&quot;,
      &quot;city&quot;:&quot;El Monte&quot;,
      &quot;county&quot;:&quot;Los Angeles County&quot;,
      &quot;state&quot;:&quot;California&quot;,
      &quot;postcode&quot;:&quot;90248&quot;,
      &quot;country&quot;:&quot;United States of America&quot;,
      &quot;country_code&quot;:&quot;us&quot;
   },
   &quot;boundingbox&quot;:[
      &quot;33.887360508221&quot;,
      &quot;33.887460508221&quot;,
      &quot;-118.26702164758&quot;,
      &quot;-118.26692164758&quot;
   ]
}</code></pre>
<p>The only difference is that our Nominatim returns <code>"city":"El Monte"</code> while the public one doesn't, however when visually checking this specific coordinate we found that it's actually pretty far from <code>El Monte city</code>, so in this case, the public Nominatim works correctly by not including <code>"city":"El Monte"</code> in the result.</p>
<p>We are curious about what could cause such a difference between the results, since our internal Nominatim is using the latest released version(3.6.0) and the latest OSM data(the only difference I could think of is that we're using TIGER data set of 2019, I'm not sure if the public Nominatim is actually using TIGER data set), we'd like to get some help from the community:) Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '21, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/93297ac8f7966d189c78d26c1443d949?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyzhang93&#39;s gravatar image" />
<p><span>tyzhang93</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyzhang93 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79439" class="comments-container">
&#10;</div>
<div id="comment-tools-79439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79439-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

