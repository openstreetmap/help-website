+++
type = "question"
title = "find coordinates with tags in osmium"
description = '''Hello, I have a CSV file with coordinates and I want to find the tags that belong to the coordinates in my osm file. My problem is that the coordinates are not identical to the coordinates in my osm file (for example my csv file has the coordinates lon 1.02 lat 1.02 and the osm file contains the coo...'''
date = "2017-05-31T12:39:00Z"
lastmod = "2017-06-01T06:54:00Z"
weight = 56393
keywords = [ "osmium", "coordinates", "tags" ]
aliases = [ "/questions/56393" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [find coordinates with tags in osmium](/questions/56393/find-coordinates-with-tags-in-osmium)

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
<span id="post-56393-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56393-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56393-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have a CSV file with coordinates and I want to find the tags that belong to the coordinates in my osm file. My problem is that the coordinates are not identical to the coordinates in my osm file (for example my csv file has the coordinates lon 1.02 lat 1.02 and the osm file contains the coordinates lon 1.01 lat 1.01). Does anyone know whether osmium has a "nearest fit" function? Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '17, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/663d0bf2304fc7d48f3237f4f16b989d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M%C3%A4rtin&#39;s gravatar image" />
<p><span>Märtin</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Märtin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56393" class="comments-container">
&#10;</div>
<div id="comment-tools-56393" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56393-form-container" class="comment-form-container">
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

<span id="56397"></span>

<div id="answer-container-56397" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56397-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, Osmium doesn't have a function like that. That is outside its scope. There are plenty of other libraries that do. It depends on what language you want etc. what makes sense for your case. For instance the Shapely Python library seems to be popular and you can combine it with PyOsmium. Another option would be to use PostgreSQL/PostGIS and do this in the database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '17, 06:54</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-56397" class="comments-container">
&#10;</div>
<div id="comment-tools-56397" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56397-form-container" class="comment-form-container">
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

