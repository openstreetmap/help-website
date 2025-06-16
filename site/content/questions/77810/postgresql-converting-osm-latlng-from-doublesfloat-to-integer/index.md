+++
type = "question"
title = "postgresql converting  osm latlng from doubles/float  to integer"
description = '''hi i am putting osm data into postgres using osmosis the command i use is : osmosis --read-xml file=&quot;/home/ubuntu/osmosis/bin/eu_filterxrx.osm&quot; --write-apidb host=&quot;localhost&quot; database=&quot;osm_test-1&quot; user=&quot;shafi&quot; password=&quot;lhoft&quot; validateSchemaVersion=&quot;no&quot; writing it to an apidb. Doing this makes conve...'''
date = "2020-11-30T17:03:00Z"
lastmod = "2020-11-30T18:24:00Z"
weight = 77810
keywords = [ "postgresql", "osm", "postgres", "osmosis", "help" ]
aliases = [ "/questions/77810" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [postgresql converting osm latlng from doubles/float to integer](/questions/77810/postgresql-converting-osm-latlng-from-doublesfloat-to-integer)

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
<span id="post-77810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77810-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi i am putting osm data into postgres using osmosis the command i use is :</p>
<p>osmosis --read-xml file="/home/ubuntu/osmosis/bin/eu_filterxrx.osm" --write-apidb host="localhost" database="osm_test-1" user="shafi" password="lhoft" validateSchemaVersion="no"</p>
<p>writing it to an apidb. Doing this makes converts my latitude and longitudes to integers for some reason</p>
<p>orignal data looks like this:</p>
<p><img src="/upfiles/latlngOSM.jpeg" alt="osm data viewed in notepad++" /> as you can see lat and long are both decimals above. but once i put the data into postgres and i view it using pgadmin the lat and lon are no longer deicmals they are now integers making them useless. how do i stop it doing that,</p>
<p>Thanks in Advance</p>
<p><img src="/upfiles/Capture_ga6jcJk.PNG" alt="data once it is inside DB" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '20, 17:03</strong></p>
<img src="https://secure.gravatar.com/avatar/87f23f2f0056b2d7d6ed1760463ea1c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shafi-as&#39;s gravatar image" />
<p><span>shafi-as</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shafi-as has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-77810" class="comments-container">
&#10;</div>
<div id="comment-tools-77810" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77810-form-container" class="comment-form-container">
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

<span id="77812"></span>

<div id="answer-container-77812" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77812-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have explicitly asked for an "apidb" database. The "apidb" schema is optimised for processing by the "openstreetmap-website" software and nothing else. The openstreetmap-website code expects the latitudes and longitudes to be written exactly like they are here.</p>
<p>If you want to do <em>anything else</em> with the OSM data than using it with the openstreetmap-website code, then <em>do not use the apidb schema</em>. Import the data with osm2pgsql instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '20, 17:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-77812" class="comments-container">
<span id="77815"></span>
<div id="comment-77815" class="comment">
<div id="post-77815-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i need to use the apidb schema as i have cloned the osm webpage and im viewing this data in josm on my own private server, osm2pgsql doesnt allow me to do that from what i have heard.</p>
</div>
<div id="comment-77815-info" class="comment-info">
<span class="comment-age">(30 Nov '20, 18:21)</span> <span class="comment-user userinfo">shafi-as</span>
</div>
</div>
<span id="77816"></span>
<div id="comment-77816" class="comment">
<div id="post-77816-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>True, but if you view the data in JOSM then everything is fine, as the openstreetmap-website (or cgimap) code that sits between JOSM and the database will convert these coordinates for you.</p>
</div>
<div id="comment-77816-info" class="comment-info">
<span class="comment-age">(30 Nov '20, 18:24)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77812" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77812-form-container" class="comment-form-container">
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

