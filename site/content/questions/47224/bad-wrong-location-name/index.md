+++
type = "question"
title = "Bad / wrong location name"
description = '''Hi! I&#x27;ve recently installed an OSM file of Nominatim 2.4 in a new Server, but it shows an error message at the end of the instalation. Here is some of the end lines in setup.log file &quot;/utils/setup.log&quot;: Done 9688999 in 280842 @ 34.499821 per second - Rank 26 ETA (seconds): 127908.812500 Done 9688999...'''
date = "2015-12-18T23:04:00Z"
lastmod = "2015-12-18T23:53:00Z"
weight = 47224
keywords = [ "reversegeocoding", "bad", "wrongname", "wrong" ]
aliases = [ "/questions/47224" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Bad / wrong location name](/questions/47224/bad-wrong-location-name)

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
<span id="post-47224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47224-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I've recently installed an OSM file of Nominatim 2.4 in a new Server, but it shows an error message at the end of the instalation. Here is some of the end lines in setup.log file "/utils/setup.log":</p>
<pre><code>Done 9688999 in 280842 @ 34.499821 per second - Rank 26 ETA (seconds): 127908.812500
Done 9688999 in 280842 @ 34.499821 per second - Rank 26 ETA (seconds): 127908.812500
Done 9688999 in 280843 @ 34.499699 per second - Rank 26 ETA (seconds): 127909.265625
Done 9688999 in 280844 @ 34.499577 per second - Rank 26 ETA (seconds): 127909.710938
Done 9688999 in 280844 @ 34.499577 per second - Rank 26 ETA (seconds): 127909.710938
&#10;index_placex: UPDATE failed: ERROR:  could not read block 20133 in file &quot;base/2205538/2719940&quot;: Error de entrada/salida
CONTEXT:  SQL statement &quot;DELETE FROM location_road_2 where place_id = in_place_id&quot;
PL/pgSQL function deleteroad(integer,bigint) line 1197 at SQL statement
PL/pgSQL function placex_update() line 77 at assignment
Done 9688999 in 280845 @ 34.499454 per second - Rank 26 ETA (seconds): 127910.164062
ERROR: Error executing external command: /home/nominatim/Nominatim/nominatim/nominatim -i -d nominatim -P 5432 -t 1 -r 26
Error executing external command: /home/nominatim/Nominatim/nominatim/nominatim -i -d nominatim -P 5432 -t 1 -r 26</code></pre>
<p>The instalation finsed and it's a complete continent (NorthAmerica)... So, when I try to find a place, the Address request from Nominatim is wrong.</p>
<p>This is an example with the next lat/long data in the new server: "25.539999","-103.427098"</p>
<pre><code>URL: http://192.168.1.207/nominatim/reverse?format=json&amp;addressdetails=0&amp;zoom=18&amp;lat=25.539999&amp;lon=-103.427098</code></pre>
<p>Returns:</p>
<pre><code>&quot;Central de Abastos, Torreón, Coahuila de Zaragoza, 27010, México&quot;
&#10;{&quot;place_id&quot;:&quot;21325872&quot;,&quot;licence&quot;:&quot;Data © OpenStreetMap contributors, ODbL 1.0. http:\/\/www.openstreetmap.org\/copyright&quot;,&quot;osm_type&quot;:&quot;way&quot;,&quot;osm_id&quot;:&quot;116771106&quot;,&quot;lat&quot;:&quot;25.5542692&quot;,&quot;lon&quot;:&quot;-103.425345760978&quot;,&quot;display_name&quot;:&quot;Central de Abastos, Torreón, Coahuila de Zaragoza, 27010, México&quot;}</code></pre>
<p>And searching the place in my old server, it should be showing some thing like this:</p>
<pre><code>URL: http://192.168.1.178/nominatim/reverse?format=json&amp;addressdetails=0&amp;zoom=18&amp;lat=25.539999&amp;lon=-103.427098
&#10;&quot;Av. Matamoros, Torreón, Coahuila de Zaragoza, 27010, México&quot;
&#10;{&quot;place_id&quot;:&quot;275172&quot;,&quot;licence&quot;:&quot;Data \u00a9 OpenStreetMap contributors, ODbL 1.0. http:\/\/www.openstreetmap.org\/copyright&quot;,&quot;osm_type&quot;:&quot;way&quot;,&quot;osm_id&quot;:&quot;50857796&quot;,&quot;lat&quot;:&quot;25.5400986&quot;,&quot;lon&quot;:&quot;-103.4204802&quot;,&quot;display_name&quot;:&quot;Av. Matamoros, Torre\u00f3n, Coahuila de Zaragoza, 27010, M\u00e9xico&quot;}</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-bad" rel="tag" title="see questions tagged &#39;bad&#39;">bad</span> <span class="post-tag tag-link-wrongname" rel="tag" title="see questions tagged &#39;wrongname&#39;">wrongname</span> <span class="post-tag tag-link-wrong" rel="tag" title="see questions tagged &#39;wrong&#39;">wrong</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '15, 23:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad1381f8d4450095fae2b1b678f90957?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nahum%20Larriva&#39;s gravatar image" />
<p><span>Nahum Larriva</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nahum Larriva has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47224" class="comments-container">
&#10;</div>
<div id="comment-tools-47224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47224-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47225"></span>

<div id="answer-container-47225" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47225-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nahum Larriva has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your disk is faulty. Type <code>dmesg</code> to confirm (or run SMART checks). You will have to replace the disk and run the import again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '15, 23:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47225" class="comments-container">
<span id="47226"></span>
<div id="comment-47226" class="comment">
<div id="post-47226-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, i´m gonna run a chek disk and tell you the resoults.</p>
</div>
<div id="comment-47226-info" class="comment-info">
<span class="comment-age">(18 Dec '15, 23:53)</span> <span class="comment-user userinfo">Nahum Larriva</span>
</div>
</div>
</div>
<div id="comment-tools-47225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47225-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

