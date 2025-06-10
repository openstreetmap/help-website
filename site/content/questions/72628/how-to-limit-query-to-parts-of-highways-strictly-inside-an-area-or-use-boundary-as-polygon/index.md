+++
type = "question"
title = "How to limit query to parts of highways strictly inside an area or use boundary as polygon"
description = '''I want to perform some analyses on the cycleways in my town. To do this I exported the cycleways using the following overpass query: [out:json]; area[name=&quot;Segrate&quot;]; way[&quot;highway&quot;=&quot;cycleway&quot;](area); (._;&amp;gt;;); out;  I noticed that some of the returned cycleways are outside of the town, which is ve...'''
date = "2020-01-22T21:29:00Z"
lastmod = "2020-01-22T21:29:00Z"
weight = 72628
keywords = [ "overpass", "boundary", "area" ]
aliases = [ "/questions/72628" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to limit query to parts of highways strictly inside an area or use boundary as polygon](/questions/72628/how-to-limit-query-to-parts-of-highways-strictly-inside-an-area-or-use-boundary-as-polygon)

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
<span id="post-72628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72628-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to perform some analyses on the cycleways in my town. To do this I exported the cycleways using the following overpass query:</p>
<pre><code>[out:json];
area[name=&quot;Segrate&quot;];
way[&quot;highway&quot;=&quot;cycleway&quot;](area);
(._;&gt;;);
out;</code></pre>
<p>I noticed that some of the returned cycleways are <strong>outside</strong> of the town, which is very clear if you run <a href="http://overpass-turbo.eu/s/Q0Z">this query, in which I also draw the town boundaries</a>.</p>
<p>It appears that if the cycleway has a part inside the area and one outside, also the outer part is included in the query response.</p>
<ul>
<li>Is there a way to limit the response of the query regarding a area, to the parts of the highways strictly inside that area?</li>
<li>Alternatively, how can I use the boundaries as a polygon to limit the returned highways at the nodes that are inside?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '20, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/45814029815083fa610e054e4c079a3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="livmilan&#39;s gravatar image" />
<p><span>livmilan</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="livmilan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '20, 21:30</strong> </span></p>
</div>
</div>
<div id="comments-container-72628" class="comments-container">
&#10;</div>
<div id="comment-tools-72628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72628-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

