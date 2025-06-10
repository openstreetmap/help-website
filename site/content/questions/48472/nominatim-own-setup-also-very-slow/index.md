+++
type = "question"
title = "Nominatim own setup also very slow"
description = '''Hi, I setup nominatim in my server. But Its very very slowly processing geocodes. For a single geocode request it takes more than 2 secs. How can i improve speed in nominatim ? Note: I am using NGINX server '''
date = "2016-03-03T04:42:00Z"
lastmod = "2016-06-04T15:07:00Z"
weight = 48472
keywords = [ "maxspeed", "performance", "nominatim", "geocoder", "slow" ]
aliases = [ "/questions/48472" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim own setup also very slow](/questions/48472/nominatim-own-setup-also-very-slow)

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
<span id="post-48472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48472-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I setup nominatim in my server.</p>
<p>But Its very very slowly processing geocodes. For a single geocode request it takes more than 2 secs.</p>
<p>How can i improve speed in nominatim ?</p>
<p>Note: I am using NGINX server</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoder" rel="tag" title="see questions tagged &#39;geocoder&#39;">geocoder</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '16, 04:42</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jun '16, 14:51</strong> </span></p>
</div>
</div>
<div id="comments-container-48472" class="comments-container">
<span id="48475"></span>
<div id="comment-48475" class="comment">
<div id="post-48475-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>what are the characteristics of your server? How much RAM? Do you use SSD or rotating hard drives, and if the latter, at which speed?</p>
</div>
<div id="comment-48475-info" class="comment-info">
<span class="comment-age">(03 Mar '16, 10:28)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="48491"></span>
<div id="comment-48491" class="comment">
<div id="post-48491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/936/dieterdreist"></a><a href="http://help.openstreetmap.org/users/936/dieterdreist">@dieterdreist</a></p>
<p>My server config: 32 core CPU, 128GB RAM &amp; 2TB SSD HD. If i called 1000 geocode queries one by one, it takes around 4000 seconds for finish.</p>
<p>I have another doubt: Is it possible to call bulk geocode queries in a single request ?</p>
</div>
<div id="comment-48491-info" class="comment-info">
<span class="comment-age">(03 Mar '16, 17:33)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="48550"></span>
<div id="comment-48550" class="comment">
<div id="post-48550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can try to ask on the OSM developer mailinglist, see <a href="http://wiki.openstreetmap.org/wiki/Mailing_lists">http://wiki.openstreetmap.org/wiki/Mailing_lists</a> ...</p>
<p>or try to contact user lonvia ... she is quite helpful about nominatim.</p>
</div>
<div id="comment-48550-info" class="comment-info">
<span class="comment-age">(07 Mar '16, 16:49)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="48560"></span>
<div id="comment-48560" class="comment">
<div id="post-48560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would suggest that you analyse what your system is actually doing (munin or similar, postgres logs and so on). Response times as slow as you indicate would tend to point to either:</p>
<ul>
<li>missing indices</li>
<li>other database misconfigurations.</li>
</ul>
</div>
<div id="comment-48560-info" class="comment-info">
<span class="comment-age">(08 Mar '16, 08:32)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48472-form-container" class="comment-form-container">
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

<span id="50015"></span>

<div id="answer-container-50015" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50015-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Postgres is where you need to take a look. With 128 gigs of ram you can cache majority of the data needed for reverse geocoding. placex is the relation that slows down the process the most. Put the table in cache along with geometry index (in later versions reverse geometry index) and that will speed up your queries a lot. Over time, though you may achieve the same result when the cache "warms up" on its own...</p>
<p>OUt of curiousity, what is the project you use Nominatim for?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '16, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/34a9ff282bda047810fdbb874b6671b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Taras%20O&#39;s gravatar image" />
<p><span>Taras O</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Taras O has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50015" class="comments-container">
<span id="50016"></span>
<div id="comment-50016" class="comment">
<div id="post-50016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have similar issue though (see the link below), as all the caching stuff consumes a lot of RAM and I believe 128Gb is an overkill for reverse geo...</p>
<p><a href="https://help.openstreetmap.org/questions/49991/speed-up-nominatimreverse-goecoding-optimize-db-size">https://help.openstreetmap.org/questions/49991/speed-up-nominatimreverse-goecoding-optimize-db-size</a></p>
</div>
<div id="comment-50016-info" class="comment-info">
<span class="comment-age">(04 Jun '16, 15:07)</span> <span class="comment-user userinfo">Taras O</span>
</div>
</div>
</div>
<div id="comment-tools-50015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50015-form-container" class="comment-form-container">
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

