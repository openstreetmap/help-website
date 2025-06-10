+++
type = "question"
title = "How can I count numbers of natural=waters filtered by a country?"
description = '''I&#x27;m interested to find out how many waterbodies there are in each countries. I have checked out http://taginfo.openstreetmap.org/tags/natural=water but can&#x27;t figure out how to filter this stats by country. How can this be done?'''
date = "2016-10-26T12:40:00Z"
lastmod = "2016-10-29T14:03:00Z"
weight = 52691
keywords = [ "stats" ]
aliases = [ "/questions/52691" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I count numbers of natural=waters filtered by a country?](/questions/52691/how-can-i-count-numbers-of-naturalwaters-filtered-by-a-country)

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
<span id="post-52691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52691-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm interested to find out how many waterbodies there are in each countries. I have checked out <a href="http://taginfo.openstreetmap.org/tags/natural=water">http://taginfo.openstreetmap.org/tags/natural=water</a> but can't figure out how to filter this stats by country. How can this be done?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stats" rel="tag" title="see questions tagged &#39;stats&#39;">stats</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '16, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/f6f7ab85f0551b83758a39eaabff1965?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fishbrain&#39;s gravatar image" />
<p><span>Fishbrain</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fishbrain has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52691" class="comments-container">
&#10;</div>
<div id="comment-tools-52691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52691-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="52692"></span>

<div id="answer-container-52692" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52692-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot do that kind of analyses with taginfo. Some countries have there own local taginfo server (e.g. UK and Italy), in which case you can see it on that server for that country.</p>
<p>A solution would be to download the OSM data and use a program such as QGIS to split the waterbodies per country and count them. QGIS has a possibility to invoke an Overpass Query to obtain only waterbodies. You need to download the country boundaries as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '16, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-52692" class="comments-container">
&#10;</div>
<div id="comment-tools-52692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52692-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52728"></span>

<div id="answer-container-52728" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52728-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download the extract for the country of your choice and write a small C++ program which uses the Osmium library. I suggest to modify the osmium_road_length example program (currently it calculates the length of a road and adds the value to a variable).</p>
<p>The necessary modifications:</p>
<ul>
<li>RoadLengthHandler::length should be int and renamed to waterbodys_count</li>
<li>You should query the natural instead of the highway tag at line 57</li>
<li>"if (highway)" (line 58) should be changed to "if (highway &amp;&amp; !strcmp(highway, "water"))"</li>
<li>Replace "length += osmium::geom::haversine::distance(way.nodes());" by "++waterbodys_count;"</li>
<li>change the final output at line 90 (If you understand the points above, this will be easy)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '16, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/d2a3b905e2632430b47dd9b8de3d8ba0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nakaner&#39;s gravatar image" />
<p><span>Nakaner</span><br />
<span class="score" title="610 reputation points">610</span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nakaner has 3 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-52728" class="comments-container">
&#10;</div>
<div id="comment-tools-52728" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52728-form-container" class="comment-form-container">
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

