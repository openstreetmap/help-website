+++
type = "question"
title = "Change svg size by definition in .mss files"
description = '''During carto style definition I would like to enlarge some svg&#x27;s icons depends on zoom level. I&#x27;m wondering if it&#x27;s possible to override some SVG file attributes in .mss files? In example I would like to override width and height value defined already in SVG file. Or scale up svg for specific scale....'''
date = "2021-03-23T10:30:00Z"
lastmod = "2021-03-23T14:12:00Z"
weight = 79363
keywords = [ "style", "carto", "mapnik" ]
aliases = [ "/questions/79363" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Change svg size by definition in .mss files](/questions/79363/change-svg-size-by-definition-in-mss-files)

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
<span id="post-79363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79363-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>During carto style definition I would like to enlarge some svg's icons depends on <code>zoom</code> level. I'm wondering if it's possible to override some SVG file attributes in <code>.mss</code> files? In example I would like to override <code>width</code> and <code>height</code> value defined already in SVG file. Or scale up svg for specific scale.<br />
For example: <code>[highway = 'motorway_link'] { [zoom &gt;= 16 ] { marker-scale: 2; } marker-fill: @motorway-oneway-arrow-color; }</code></p>
<p>or</p>
<p><code>[highway = 'motorway_link'] { [zoom &gt;= 16 ] { marker-width: 15; marker-height: 15; } marker-fill: @motorway-oneway-arrow-color; }</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '21, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/735ed8c1abf1a1f7b907b78d9594303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engopy&#39;s gravatar image" />
<p><span>engopy</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engopy has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-79363" class="comments-container">
&#10;</div>
<div id="comment-tools-79363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79363-form-container" class="comment-form-container">
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

<span id="79364"></span>

<div id="answer-container-79364" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79364-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="engopy has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please look at the Mapnik documentation, there are some marker-related functions like <em>marker-transform</em>:</p>
<p><a href="https://cartocss.readthedocs.io/en/latest/mapnik_api.html#markers">https://cartocss.readthedocs.io/en/latest/mapnik_api.html#markers</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '21, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-79364" class="comments-container">
<span id="79365"></span>
<div id="comment-79365" class="comment">
<div id="post-79365-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I wasn't aware there are so many possible configurations for SVG. actually: <code>marker-width: marker-height:</code> does what I needed Thanks</p>
</div>
<div id="comment-79365-info" class="comment-info">
<span class="comment-age">(23 Mar '21, 14:04)</span> <span class="comment-user userinfo">engopy</span>
</div>
</div>
<span id="79366"></span>
<div id="comment-79366" class="comment">
<div id="post-79366-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Exactly what you have ordered... :-)</p>
</div>
<div id="comment-79366-info" class="comment-info">
<span class="comment-age">(23 Mar '21, 14:12)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
</div>
<div id="comment-tools-79364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79364-form-container" class="comment-form-container">
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

