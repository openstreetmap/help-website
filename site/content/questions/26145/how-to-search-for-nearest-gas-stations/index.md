+++
type = "question"
title = "How to search for nearest gas stations"
description = '''I am completely new to OSM. Sorry if this is a dumb question. My goal is to list the nearest gas stations in order, or all gas stations within a certain area. They don&#x27;t need to be displayed on a map. I have found out that I need to use amenity=fuel, but I&#x27;m not sure how to make the query, or where ...'''
date = "2013-09-05T14:48:00Z"
lastmod = "2013-09-05T17:52:00Z"
weight = 26145
keywords = [ "query", "search", "amenity", "nearest" ]
aliases = [ "/questions/26145" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to search for nearest gas stations](/questions/26145/how-to-search-for-nearest-gas-stations)

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
<span id="post-26145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26145-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am completely new to OSM. Sorry if this is a dumb question.</p>
<p>My goal is to list the nearest gas stations in order, or all gas stations within a certain area. They don't need to be displayed on a map.</p>
<p>I have found out that I need to use amenity=fuel, but I'm not sure how to make the query, or where to run the query.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-nearest" rel="tag" title="see questions tagged &#39;nearest&#39;">nearest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '13, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/1106878994248cf2f1feb27a3f7efc7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pag11123&#39;s gravatar image" />
<p><span>pag11123</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pag11123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26145" class="comments-container">
&#10;</div>
<div id="comment-tools-26145" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26145-form-container" class="comment-form-container">
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

<span id="26146"></span>

<div id="answer-container-26146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26146-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One of the possible solutions is to run an overpass query. The <a href="http://overpass-turbo.eu/s/Yu">http://overpass-turbo.eu/s/Yu</a> one should list all the gas stations within the bounding box that you specify. I'm aware that this is a graphical UI, but you can run the same query from any program language (as it is an http call). The data is can be returned as GeoJSON. All gas stations are specified with the coordinates, so you application can calculate the distance to each one and order them.</p>
<p>More information on overpass can be found here: <a href="http://overpass-api.de/">http://overpass-api.de/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '13, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-26146" class="comments-container">
<span id="26148"></span>
<div id="comment-26148" class="comment">
<div id="post-26148-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Also, if you want a non-interactive version, you might want to consider "normal" Overpass rather than the turbo version, which supports both its own and the old XAPI-style syntax.</p>
</div>
<div id="comment-26148-info" class="comment-info">
<span class="comment-age">(05 Sep '13, 17:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26146-form-container" class="comment-form-container">
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

