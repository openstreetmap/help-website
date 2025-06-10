+++
type = "question"
title = "Nominatim returning &quot;undefined index: lat&quot;"
description = '''I&#x27;m running Nominatim 2.2.0 on my server, and just finished importing planet data. When I do a reverse geocode lookup from my personal laptop as follows: http://my-ip-address/nominatim/reverse?format=xml&amp;amp;lat=51.507020&amp;amp;lon=-0.100571&amp;amp;zoom=18&amp;amp;addressdetails=1  It works perfectly. But wh...'''
date = "2014-03-12T18:41:00Z"
lastmod = "2014-03-13T07:42:00Z"
weight = 31498
keywords = [ "reversegeocoding", "nominatim" ]
aliases = [ "/questions/31498" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim returning "undefined index: lat"](/questions/31498/nominatim-returning-undefined-index-lat)

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
<span id="post-31498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31498-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm running Nominatim 2.2.0 on my server, and just finished importing planet data. When I do a reverse geocode lookup from my personal laptop as follows:</p>
<pre><code>http://my-ip-address/nominatim/reverse?format=xml&amp;lat=51.507020&amp;lon=-0.100571&amp;zoom=18&amp;addressdetails=1</code></pre>
<p>It works perfectly. But when I run the exact same thing on my server (that's running Nominatim) with curl:</p>
<pre><code>curl http://my-ip-address/nominatim/reverse?format=xml&amp;lat=51.507020&amp;lon=-0.100571&amp;zoom=18&amp;addressdetails=1</code></pre>
<p>or</p>
<pre><code>curl http://localhost/nominatim/reverse?format=xml&amp;lat=51.507020&amp;lon=-0.100571&amp;zoom=18&amp;addressdetails=1</code></pre>
<p>I get "unable to geocode" error. The only difference is that it works when I use my personal laptop (or query remotely) but doesn't work when I do it on a localhost (or query from the same server/computer that's running Nominatim/PostgreSQL).</p>
<p>When I look through my apache log, I get the following:</p>
<pre><code>[Wed Mar 12 11:27:14 2014] [error] [client my-ip-address] PHP Notice:  Undefined index: lat in /postgres/OpenStreetMaps/Nominatim-2.2.0/website/reverse.php on line 57
[Wed Mar 12 11:27:14 2014] [error] [client my-ip-address] PHP Notice:  Undefined index: lon in /postgres/OpenStreetMaps/Nominatim-2.2.0/website/reverse.php on line 57</code></pre>
<p>What could be wrong here? Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '14, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '14, 18:43</strong> </span></p>
</div>
</div>
<div id="comments-container-31498" class="comments-container">
<span id="31499"></span>
<div id="comment-31499" class="comment">
<div id="post-31499-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to be clear - are you using the same "curl" command on your laptop, or are you comparing a request made through a web browser on your laptop with a request made through curl on the server?</p>
</div>
<div id="comment-31499-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 20:01)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="31508"></span>
<div id="comment-31508" class="comment">
<div id="post-31508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>On my laptop, I'm using a normal browser. Just to be sure curl is working correctly on my server, I tried different websites and it seems to be OK.</p>
</div>
<div id="comment-31508-info" class="comment-info">
<span class="comment-age">(12 Mar '14, 21:07)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-31498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31498-form-container" class="comment-form-container">
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

<span id="31516"></span>

<div id="answer-container-31516" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31516-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Figured out the problem! Turns out some parameters were being escaped for whatever reason. Works when I do</p>
<p>curl 'http://my-ip-address/nominatim/reverse?format=xml&amp;lat=51.507020&amp;lon=-0.100571&amp;zoom=18&amp;addressdetails=1'</p>
<p>with the ' ' around the URL</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '14, 23:48</strong></p>
<img src="https://secure.gravatar.com/avatar/61de868d7785f30711497cecbdddf5f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baekacaek&#39;s gravatar image" />
<p><span>baekacaek</span><br />
<span class="score" title="176 reputation points">176</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baekacaek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31516" class="comments-container">
<span id="31519"></span>
<div id="comment-31519" class="comment">
<div id="post-31519-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the character <code>&amp;</code> has a special meaning for the shell.</p>
</div>
<div id="comment-31519-info" class="comment-info">
<span class="comment-age">(13 Mar '14, 07:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31516-form-container" class="comment-form-container">
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

