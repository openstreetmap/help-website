+++
type = "question"
title = "Local server geo code service for every received lat long"
description = '''I want to set up both osm map and reverse geo code service locally. I am a bit confuse I know for osm map I need to setup postgres and other related tools. How about the nomatim database is it using the same postgre db ? How can I via my java application run a reverse geo code on this database? '''
date = "2017-06-09T18:35:00Z"
lastmod = "2017-06-10T15:18:00Z"
weight = 56564
keywords = [ "reversegeocoding", "osm", "nominatim" ]
aliases = [ "/questions/56564" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Local server geo code service for every received lat long](/questions/56564/local-server-geo-code-service-for-every-received-lat-long)

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
<span id="post-56564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56564-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to set up both osm map and reverse geo code service locally. I am a bit confuse I know for osm map I need to setup postgres and other related tools. How about the nomatim database is it using the same postgre db ? How can I via my java application run a reverse geo code on this database?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '17, 18:35</strong></p>
<img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" />
<p><span>newbie14</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56564" class="comments-container">
&#10;</div>
<div id="comment-tools-56564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56564-form-container" class="comment-form-container">
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

<span id="56565"></span>

<div id="answer-container-56565" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56565-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim data will go into a separate database (called <code>nominatim</code>) but can be on the same postgres server. That means you have duplicate data with separate update processes on the same server. That's fine though, many companies run both on the same server.</p>
<p>Nominatim comes with a PHP frontend. You'd call <a href="http://localhost:8000/nominatim/reverse.php?lat=...&amp;lon=">http://localhost:8000/nominatim/reverse.php?lat=...&amp;lon=</a> and receive a JSON (or XML) response. Your Java app just calls the URL and doesn't need direct access to the Nominatim database.</p>
<p>Example response: <a href="http://nominatim.openstreetmap.org/reverse.php?lat=45.514&amp;lon=-122.675">http://nominatim.openstreetmap.org/reverse.php?lat=45.514&amp;lon=-122.675</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '17, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-56565" class="comments-container">
<span id="56568"></span>
<div id="comment-56568" class="comment">
<div id="post-56568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a> thank you clear a lot of my doubts. Is nominatim data in the form similar to osm then why can we run the reverse process on osm data itself? I got few more doubt like you see for osm I have been trying a lot to install on centos but it just fails so I deciced to go with ubuntu no choice. Is there a proper guide on how best to install nomatim and does it also work best on ubuntu?</p>
</div>
<div id="comment-56568-info" class="comment-info">
<span class="comment-age">(10 Jun '17, 04:10)</span> <span class="comment-user userinfo">newbie14</span>
</div>
</div>
<span id="56571"></span>
<div id="comment-56571" class="comment">
<div id="post-56571-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nominatim's database is optimized for geocoding. In case of reverse geocoding for example many parent-child relationships (e.g. state-city) are pre-calculated. The install instructions for the stable Nominatim on Ubuntu 16 are on <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">https://wiki.openstreetmap.org/wiki/Nominatim/Installation</a> The scripts in <a href="https://github.com/openstreetmap/Nominatim/tree/master/vagrant">https://github.com/openstreetmap/Nominatim/tree/master/vagrant</a> use the latest (unstable) version I would avoid them for now. If you run into installation problems add an issue on <a href="https://github.com/openstreetmap/Nominatim/issues">https://github.com/openstreetmap/Nominatim/issues</a> with the error message.</p>
</div>
<div id="comment-56571-info" class="comment-info">
<span class="comment-age">(10 Jun '17, 15:18)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-56565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56565-form-container" class="comment-form-container">
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

