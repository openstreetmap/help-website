+++
type = "question"
title = "Finding all blocks in a city"
description = '''Hey everyone! New user to just started to played around with OSM, using Postgis with an OSM extract of the USA. I was wondering if it were possible to find every block in a city and their start+end coordinates? I was thinking of identifying every intersection and their connecting roads and then find...'''
date = "2017-01-27T09:52:00Z"
lastmod = "2017-01-27T15:39:00Z"
weight = 54324
keywords = [ "intersection", "blocks", "road" ]
aliases = [ "/questions/54324" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Finding all blocks in a city](/questions/54324/finding-all-blocks-in-a-city)

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
<span id="post-54324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54324-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey everyone! New user to just started to played around with OSM, using Postgis with an OSM extract of the USA. I was wondering if it were possible to find every block in a city and their start+end coordinates? I was thinking of identifying every intersection and their connecting roads and then find out where the road leads until the next intersection, then take the lat+long of the intersecting points.Can anyone help with some general plan to get me started on the right direction?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-blocks" rel="tag" title="see questions tagged &#39;blocks&#39;">blocks</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '17, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/b0e23e6d1b403f99f26b125293bf6f83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flames403&#39;s gravatar image" />
<p><span>flames403</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flames403 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54324" class="comments-container">
<span id="54335"></span>
<div id="comment-54335" class="comment">
<div id="post-54335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not a direct answer to your question, but what you describe is exactly what Census blocks are. (see <a href="https://www.census.gov/geo/maps-data/data/tiger-line.html">https://www.census.gov/geo/maps-data/data/tiger-line.html</a> for details of all the TIGER data) The 2010 blocks probably won't be as accurate as OSM data, but would be much easier not having to create your own if they meet your needs.</p>
</div>
<div id="comment-54335-info" class="comment-info">
<span class="comment-age">(27 Jan '17, 14:56)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="54336"></span>
<div id="comment-54336" class="comment">
<div id="post-54336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey neuhausr. Would I be able to get the long and lats for start and end of the streets though? I want to be able to say intersec1 lat/long goes to intersec2 lat/long and those are the start and end points to one street block. Then do that for a while city and have every block defined as a pair of long/lats</p>
</div>
<div id="comment-54336-info" class="comment-info">
<span class="comment-age">(27 Jan '17, 15:39)</span> <span class="comment-user userinfo">flames403</span>
</div>
</div>
</div>
<div id="comment-tools-54324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54324-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

