+++
type = "question"
title = "Can a tile server and reverse geocoding server use the same database?"
description = '''I used this tutorial to setup an OSM tile server in Ubuntu 20.04, and that is currently working. I am now following this tutorial to setup a nominatim reverse geocoding server on the same machine. But the database names seems to be different, but I should not have 2 databases with the same data I do...'''
date = "2021-08-25T10:42:00Z"
lastmod = "2021-08-25T12:24:00Z"
weight = 81470
keywords = [ "geocoding_server", "nominatim", "postgres", "tileserver" ]
aliases = [ "/questions/81470" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can a tile server and reverse geocoding server use the same database?](/questions/81470/can-a-tile-server-and-reverse-geocoding-server-use-the-same-database)

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
<span id="post-81470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81470-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I used <a href="https://www.linuxbabe.com/ubuntu/openstreetmap-tile-server-ubuntu-20-04-osm">this</a> tutorial to setup an OSM tile server in Ubuntu 20.04, and that is currently working.</p>
<p>I am now following <a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-20/">this</a> tutorial to setup a nominatim reverse geocoding server on the same machine.</p>
<p>But the database names seems to be different, but I should not have 2 databases with the same data I downloaded from <a href="https://download.geofabrik.de/">GeoFabrik</a>, right?</p>
<p>So is it somehow possible to run a tile server and reverse geocoding server using the same instance and the same data on the database? Or is there a rule of thumb which states that you should never run both servers/services on the same machine/database?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding_server" rel="tag" title="see questions tagged &#39;geocoding_server&#39;">geocoding_server</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postgres" rel="tag" title="see questions tagged &#39;postgres&#39;">postgres</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '21, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/04175cc004ecad1e262fad8e94f86d62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoenMlt&#39;s gravatar image" />
<p><span>KoenMlt</span><br />
<span class="score" title="42 reputation points">42</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoenMlt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81470" class="comments-container">
&#10;</div>
<div id="comment-tools-81470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81470-form-container" class="comment-form-container">
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

<span id="81472"></span>

<div id="answer-container-81472" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81472-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-81472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="KoenMlt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tile server and nominating don't use the same database schema, so you can't use the same database for both.</p>
<p>Depending on the load of your server, hosting both on the same machine could work. You don't want to import both databases at the same time though.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '21, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-81472" class="comments-container">
<span id="81473"></span>
<div id="comment-81473" class="comment">
<div id="post-81473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Makes sense, thank you for your answer!</p>
</div>
<div id="comment-81473-info" class="comment-info">
<span class="comment-age">(25 Aug '21, 12:24)</span> <span class="comment-user userinfo">KoenMlt</span>
</div>
</div>
</div>
<div id="comment-tools-81472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81472-form-container" class="comment-form-container">
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

