+++
type = "question"
title = "How to search by name in .osm.pbf/.shp.zip/.osm.bz2"
description = '''Hello, i want to get locations(latitude, longitude) of around 1kk addresses. I tried Nominatim in python lib geopy but it will take too much time for processing all addresses. Than i tried osmium with osb.pbf data dumps, but it can`t make search by address, it just iterare over nodes, ways, areas al...'''
date = "2021-01-20T11:52:00Z"
lastmod = "2021-01-20T12:19:00Z"
weight = 78425
keywords = [ "osm.pbf", "geopy", "nominatim" ]
aliases = [ "/questions/78425" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to search by name in .osm.pbf/.shp.zip/.osm.bz2](/questions/78425/how-to-search-by-name-in-osmpbfshpziposmbz2)

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
<span id="post-78425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78425-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, i want to get locations(latitude, longitude) of around 1kk addresses. I tried Nominatim in python lib geopy but it will take too much time for processing all addresses. Than i tried osmium with osb.pbf data dumps, but it can`t make search by address, it just iterare over nodes, ways, areas also it take too much time while handling nodes. So my question is there a tool/way to make search by location name like Nominatim in geopy which works with local data dump? I know hard way to do this. It requires importing data dump in local postgress sql database and build and run Nominatim server. Is there easer way?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.pbf" rel="tag" title="see questions tagged &#39;osm.pbf&#39;">osm.pbf</span> <span class="post-tag tag-link-geopy" rel="tag" title="see questions tagged &#39;geopy&#39;">geopy</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jan '21, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/aa737c655e149fa6f283918ac07f64d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maruo95&#39;s gravatar image" />
<p><span>maruo95</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maruo95 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78425" class="comments-container">
<span id="78427"></span>
<div id="comment-78427" class="comment">
<div id="post-78427-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your requirements are not clear. Sometimes you ask about search by name, sometimes you want search by address. These are two completely different things. Which one do you need?</p>
</div>
<div id="comment-78427-info" class="comment-info">
<span class="comment-age">(20 Jan '21, 12:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78425-form-container" class="comment-form-container">
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

<span id="78426"></span>

<div id="answer-container-78426" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78426-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-78426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="maruo95 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No.</p>
<p>The reason for that is that addresses are not stored in OSM ready-to-use. It requires computation to build the address of a place. Also, in case a precise match cannot be found, to find the "nearest" match. Nominatim does these things for you. If you don't use Nominatim then you have to write code that does these things, which will make that way more difficult than using Nominatim. Therefore, there is no easier way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '21, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78426" class="comments-container">
&#10;</div>
<div id="comment-tools-78426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78426-form-container" class="comment-form-container">
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

