+++
type = "question"
title = "Query all roads within AND those exactly on the boundary of an area with overpass"
description = '''I am trying to download all roads for a specific area rel:2800276, including those exactly on the boundary of the area (e.g. way:171480859). However, the query seems slow if I add a few commands (Line 3-4) specifically ask for proximity to the boundary of area like this: [out:json][timeout:3600][max...'''
date = "2022-10-07T07:58:00Z"
lastmod = "2022-10-07T18:55:00Z"
weight = 85827
keywords = [ "overpass" ]
aliases = [ "/questions/85827" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query all roads within AND those exactly on the boundary of an area with overpass](/questions/85827/query-all-roads-within-and-those-exactly-on-the-boundary-of-an-area-with-overpass)

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
<span id="post-85827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85827-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to download all roads for a specific area <a href="https://www.openstreetmap.org/relation/2800276">rel:2800276</a>, including those exactly on the boundary of the area (e.g. way:171480859). However, the query seems slow if I add a few commands (Line 3-4) specifically ask for proximity to the boundary of area like this:</p>
<pre><code>[out:json][timeout:3600][maxsize:1073741824];
area(3602800276)-&gt;.t;
rel(pivot.area.t);
way[&quot;highway&quot;](around:0.0);
(._;way[&quot;highway&quot;](area.t););
(._;&gt;;);
out;</code></pre>
<p>Should I use some other methods to include the roads exactly on the boundary? It looks like by default the area filter just report features with at least one point properly within the area.</p>
<p>** For simplicity, all ways with highway tag are assumed to be roads here.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '22, 07:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ea73c966a34292033938234ef7eb1612?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yikhim&#39;s gravatar image" />
<p><span>yikhim</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yikhim has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85827" class="comments-container">
&#10;</div>
<div id="comment-tools-85827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85827-form-container" class="comment-form-container">
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

<span id="85830"></span>

<div id="answer-container-85830" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85830-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I hope I'm proved incorrect, but I don't think there's a simple way to perform this. To me the <code>is_in</code> command should be able to perform this.</p>
<p>First, the reason your routine is slow is <code>way["highway"](around:0.0);</code> is searching the whole globe for all for <code>highway</code>. It needs to be passed the desired area to search. Your next line is superfluous as it's duplicating the previous.</p>
<p>This routine: The first 'out' is, hopefully, all ways touching the relati9on. Second is all ways within the relation. Third is the relation itself.</p>
<pre><code>rel(2800276)-&gt;.Kwun;
way(around.Kwun:0)[highway=secondary];
out geom;
&#10;.Kwun;map_to_area;
way(area)[highway=secondary];
out geom;
&#10;.Kwun out geom;</code></pre>
<hr />
<p>General Point: you may want to check if the boundary does actually go down the centreline of the road. They rarely do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '22, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '22, 19:08</strong> </span></p>
</div>
</div>
<div id="comments-container-85830" class="comments-container">
&#10;</div>
<div id="comment-tools-85830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85830-form-container" class="comment-form-container">
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

