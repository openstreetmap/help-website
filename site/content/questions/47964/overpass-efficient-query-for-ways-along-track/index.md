+++
type = "question"
title = "Overpass: Efficient query for ways along track"
description = '''I want to get all the ways along a track (set of points) for classification. Currently, I create a query by concatenating each point like so: [out:json][timeout:25]; way[&quot;highway&quot;](around:1,48.077600000109015,11.573480996224898);(._;&amp;gt;;);out; way[&quot;highway&quot;](around:1,48.076880000051446,11.573426998...'''
date = "2016-02-05T19:08:00Z"
lastmod = "2016-02-07T13:04:00Z"
weight = 47964
keywords = [ "overpass", "overpass-ql" ]
aliases = [ "/questions/47964" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: Efficient query for ways along track](/questions/47964/overpass-efficient-query-for-ways-along-track)

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
<span id="post-47964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47964-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get all the ways along a track (set of points) for classification. Currently, I create a query by concatenating each point like so:</p>
<pre><code>[out:json][timeout:25];
way[&quot;highway&quot;](around:1,48.077600000109015,11.573480996224898);(._;&gt;;);out;
way[&quot;highway&quot;](around:1,48.076880000051446,11.573426998490564);(._;&gt;;);out;
way[&quot;highway&quot;](around:1,48.0761600000356,11.573377499687094);(._;&gt;;);out;
way[&quot;highway&quot;](around:1,48.0754400000356,11.573332499687094);(._;&gt;;);out;
way[&quot;highway&quot;](around:1,48.0746410000306,11.573278997883973);(._;&gt;;);out;</code></pre>
<p>etc.. However (as I expected) this takes too long for a couple of thousand points. I don't want to increase the timeout.</p>
<p>Is there a more efficient way for this kind of query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '16, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/af773a17bb15268ebadf07fb5751c07f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lcanis&#39;s gravatar image" />
<p><span>lcanis</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lcanis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47964" class="comments-container">
&#10;</div>
<div id="comment-tools-47964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47964-form-container" class="comment-form-container">
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

<span id="47975"></span>

<div id="answer-container-47975" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47975-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I am not wrong, the around parameter works with a real circle ... that clipping is very time consuming for the server, I assume.</p>
<p>So a better way can be that you calculate rectengular bounding boxes around each point, and the you do overpass-api queries by those boxes as parameter, that should be quite faster.</p>
<p>Or download a country extract from raw OSM data from any sourve mentioned at <a href="http://wiki.openstreetmap.org/wiki/Planet.osm">planet.osm</a>, and do some filtering and clipping with your batch calculated mini bounding boxes with tools like <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a>, <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '16, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-47975" class="comments-container">
<span id="47991"></span>
<div id="comment-47991" class="comment">
<div id="post-47991-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. I tried a bounding box around each point first, but the speed increase is not very big. Currently I'm combining the points and their bounding boxes until I reach a given area for the bounding box, thereby reducing the number of combined requests drastically. This is much faster, but still pretty slow: Around 20s for an 80km track. I have since learned about alpha shapes, this could be a way to go but it would make the request more complicated.</p>
<p>I am reluctant to go the raw OSM data route since in the end I would need to practically have the whole planet.osm available locally or on a private server and I was hoping to be lightweight and fast.</p>
</div>
<div id="comment-47991-info" class="comment-info">
<span class="comment-age">(07 Feb '16, 13:04)</span> <span class="comment-user userinfo">lcanis</span>
</div>
</div>
</div>
<div id="comment-tools-47975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47975-form-container" class="comment-form-container">
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

