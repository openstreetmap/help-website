+++
type = "question"
title = "bounding box values order: (lat,lon,lat,lon) vs. (lat,lat,lon,lon)"
description = '''The order of the values in a bounding box does not seem to be consistent. http://wiki.openstreetmap.org/wiki/Bounding_Box says the order is &quot;left,bottom,right,top&quot;, or &quot;min Longitude , min Latitude , max Longitude , max Latitude&quot;. This seems to be the order given in the box at the top in the search ...'''
date = "2013-01-16T17:19:00Z"
lastmod = "2013-01-17T15:18:00Z"
weight = 19145
keywords = [ "bbox" ]
aliases = [ "/questions/19145" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [bounding box values order: (lat,lon,lat,lon) vs. (lat,lat,lon,lon)](/questions/19145/bounding-box-values-order-latlonlatlon-vs-latlatlonlon)

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
<span id="post-19145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19145-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The order of the values in a bounding box does not seem to be consistent.</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Bounding_Box">http://wiki.openstreetmap.org/wiki/Bounding_Box</a> says the order is "left,bottom,right,top", or "min Longitude , min Latitude , max Longitude , max Latitude". This seems to be the order given in the box at the top in the search that is displayed when doing an HTML query at <a href="http://nominatim.openstreetmaps.org"></a><a href="http://nominatim.openstreetmaps.org">http://nominatim.openstreetmaps.org</a>.</p>
<p>But the ordered returned by an XML or JSON query is "lat1, lat2, lon1, lon2".</p>
<p>Is the wiki wrong or incomplete? Where else are the two different orders used, and which is more canonical?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jan '13, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/507c65170b1d6d484cf28f1a4db5ecb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhalbert&#39;s gravatar image" />
<p><span>dhalbert</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhalbert has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jan '13, 18:36</strong> </span></p>
</div>
</div>
<div id="comments-container-19145" class="comments-container">
&#10;</div>
<div id="comment-tools-19145" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19145-form-container" class="comment-form-container">
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

<span id="19147"></span>

<div id="answer-container-19147" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19147-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dhalbert has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>They <strong>usually</strong> follow the standard format of</p>
</blockquote>
<p>Usually is not the same thing as always. Besides that, there is another incorrect assumption on that wiki-page: There is no rule that the units have to be in degrees.</p>
<p>Every tool is free to define a bounding box in a way that seems best to the maker of that tool.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '13, 19:18</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-19147" class="comments-container">
<span id="19166"></span>
<div id="comment-19166" class="comment">
<div id="post-19166-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sounds like I should augment the wiki entry.</p>
</div>
<div id="comment-19166-info" class="comment-info">
<span class="comment-age">(17 Jan '13, 15:18)</span> <span class="comment-user userinfo">dhalbert</span>
</div>
</div>
</div>
<div id="comment-tools-19147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19147-form-container" class="comment-form-container">
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

