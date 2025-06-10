+++
type = "question"
title = "If I want to calculate total way length, is this query a good way to do it?"
description = '''Hi,  If I wanted to calculate the total length of highway ways in OSM, would this query be a good way to achieve that if I have an osmosis (snapshot schema) database with linestring extension? select tags-&amp;gt;&#x27;highway&#x27;, sum(st_length(linestring::geography)) from ways where tags?&#x27;highway&#x27; group by ta...'''
date = "2014-10-31T23:18:00Z"
lastmod = "2014-11-01T06:39:00Z"
weight = 38203
keywords = [ "length", "statistics", "postgis" ]
aliases = [ "/questions/38203" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [If I want to calculate total way length, is this query a good way to do it?](/questions/38203/if-i-want-to-calculate-total-way-length-is-this-query-a-good-way-to-do-it)

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
<span id="post-38203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38203-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>If I wanted to calculate the total length of <code>highway</code> ways in OSM, would this query be a good way to achieve that if I have an osmosis (snapshot schema) database with linestring extension?</p>
<p><code>select tags-&gt;'highway', sum(st_length(linestring::geography)) from ways where tags?'highway' group by tags-&gt;'highway' order by sum desc;</code></p>
<p>Here are the top results for a small (Utah, USA) database:</p>
<p><code>?column? | sum -----------------------+------------------ residential | 77732401.8750182 track | 53492052.9473808 service | 6386628.52935351 tertiary | 4980880.41582732 unclassified | 4854814.04812725 secondary | 4620784.71714738 primary | 4097059.7290093 path | 3771029.8775133 motorway | 3259385.13873852 footway | 1672679.77904645</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '14, 23:18</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '14, 23:21</strong> </span></p>
</div>
</div>
<div id="comments-container-38203" class="comments-container">
<span id="38211"></span>
<div id="comment-38211" class="comment">
<div id="post-38211-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This thread may be an interesting read:</p>
<p><a href="http://gis.stackexchange.com/questions/63762/why-is-sum-of-st-length-of-segments-20-too-big">http://gis.stackexchange.com/questions/63762/why-is-sum-of-st-length-of-segments-20-too-big</a></p>
</div>
<div id="comment-38211-info" class="comment-info">
<span class="comment-age">(01 Nov '14, 06:39)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-38203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38203-form-container" class="comment-form-container">
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

<span id="38208"></span>

<div id="answer-container-38208" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38208-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It certainly does look like it's working ;) If the reason you're doing this is that you want to compare with existing statistics, remember that your query will count the total way length in OSM, whereas official statistics will occasionally throw together both carriageways of a dual-carriageway road, yielding a smaller total length.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '14, 00:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-38208" class="comments-container">
&#10;</div>
<div id="comment-tools-38208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38208-form-container" class="comment-form-container">
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

