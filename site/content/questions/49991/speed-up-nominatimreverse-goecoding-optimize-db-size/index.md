+++
type = "question"
title = "Speed up Nominatim/reverse goecoding, optimize DB size?"
description = '''Hello, I&#x27;ve been trying to improve reverse geocoding queries speed and during the action I&#x27;ve noticed that many tables are not used in the process. So, hence are the 2 questions: 1) What tables can be safely removed/truncated to minimize disk usage? Of course, it would be great to have possibility t...'''
date = "2016-06-03T14:41:00Z"
lastmod = "2018-11-13T21:39:00Z"
weight = 49991
keywords = [ "nominatim", "performance", "reversegeocoding", "index", "disk_usage" ]
aliases = [ "/questions/49991" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Speed up Nominatim/reverse goecoding, optimize DB size?](/questions/49991/speed-up-nominatimreverse-goecoding-optimize-db-size)

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
<span id="post-49991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49991-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I've been trying to improve reverse geocoding queries speed and during the action I've noticed that many tables are not used in the process. So, hence are the 2 questions:</p>
<p>1) What tables can be safely removed/truncated to minimize disk usage? Of course, it would be great to have possibility to keep the DB up to date (even if i need to truncate aforementioned tables from time to time)</p>
<p>2) Is there any way to speed up Nominatim queries? From what I can see so far:</p>
<ul>
<li><p>loading indices/tables into system cache (either by pg_prewarm or pgfincore or a separate tool)</p></li>
<li><p>disable logging of the queries to new_query_log table, i haven't found the config parameter though (hacking PHP code is surely a dirty way). If someone could advise where to find exhaustive list of the configuration options for OSM/Nominatim that'd be great.</p></li>
<li><p>add more indices? I noticed there was a new index added relatively not long ago that includes only geometry records that needed for reverse geocoding, this way reducing size of the index by a few gigabytes.</p></li>
<li><p>use persistent connections to postgres (reduces system time).</p></li>
<li><p>any other ideas???</p></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-disk_usage" rel="tag" title="see questions tagged &#39;disk_usage&#39;">disk_usage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jun '16, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/34a9ff282bda047810fdbb874b6671b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Taras%20O&#39;s gravatar image" />
<p><span>Taras O</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Taras O has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '16, 14:42</strong> </span></p>
</div>
</div>
<div id="comments-container-49991" class="comments-container">
<span id="55578"></span>
<div id="comment-55578" class="comment">
<div id="post-55578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello <a href="https://help.openstreetmap.org/users/12381/taras-o">@Taras</a>, Can you describe more detail about loading indices/table into system cache ?</p>
<p>In my case, I need geocoder in my country only and its data is rather small so I think if I can cache main table into memory It will improve performance a lot but I can't find any guidelines about this</p>
</div>
<div id="comment-55578-info" class="comment-info">
<span class="comment-age">(12 Apr '17, 09:49)</span> <span class="comment-user userinfo">Bui Khanh</span>
</div>
</div>
<span id="55583"></span>
<div id="comment-55583" class="comment">
<div id="post-55583-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please do not ask or expand questions in answers, either use comments or edit your original question.</p>
</div>
<div id="comment-55583-info" class="comment-info">
<span class="comment-age">(12 Apr '17, 15:03)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="66771"></span>
<div id="comment-66771" class="comment">
<div id="post-66771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13585/bui-khanh"></a><a href="https://help.openstreetmap.org/users/13585/bui-khanh">@Bui Khanh</a>, yes, basically when you access a file it gets into system cache (or rather part of it that was read), the idea is to determine what files you need (depends on your use case) and put them into cache. For me the tables were:</p>
<p>idx_place_id</p>
<p>idx_placex_geometry</p>
<p>idx_place_addressline_place_id</p>
<p>placex</p>
<p>So, for me finding the tables and reading the files once made the trick. I used pg_relation_filepath() function to determine the files and then used vmtouch tool to put them in memory. I hope this helps!</p>
</div>
<div id="comment-66771-info" class="comment-info">
<span class="comment-age">(13 Nov '18, 21:39)</span> <span class="comment-user userinfo">Taras O</span>
</div>
</div>
</div>
<div id="comment-tools-49991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49991-form-container" class="comment-form-container">
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

<span id="50502"></span>

<div id="answer-container-50502" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50502-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, if you want to disable logging to new_query_log<br />
you have to set const_log_db to false,<br />
File: Nominatim/settings/settings.php String: @define('CONST_Log_DB', <strong>true</strong>); =&gt; @define('CONST_Log_DB', <strong>false</strong>);</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '16, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d6d37d20b56ee02918091fdea0529865?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20Sirs&#39;s gravatar image" />
<p><span>Mike Sirs</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike Sirs has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '16, 11:39</strong> </span></p>
</div>
</div>
<div id="comments-container-50502" class="comments-container">
<span id="66772"></span>
<div id="comment-66772" class="comment">
<div id="post-66772-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-66772-info" class="comment-info">
<span class="comment-age">(13 Nov '18, 21:39)</span> <span class="comment-user userinfo">Taras O</span>
</div>
</div>
</div>
<div id="comment-tools-50502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50502-form-container" class="comment-form-container">
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

