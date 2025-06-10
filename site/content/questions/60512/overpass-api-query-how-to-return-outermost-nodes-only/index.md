+++
type = "question"
title = "Overpass API query: How to return outermost nodes only?"
description = '''I&#x27;m working on a bit of an isoline/catchment issue for some set locations.  I need to get an idea of where the road extents are within a given radius or bounding box eg: 5km, 10km, 50km of the facility. I can do this with queries like the one below But I don&#x27;t need all 70,000 points (5mb), I just ne...'''
date = "2017-11-08T22:36:00Z"
lastmod = "2017-11-08T22:36:00Z"
weight = 60512
keywords = [ "overpassapi", "overpass" ]
aliases = [ "/questions/60512" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API query: How to return outermost nodes only?](/questions/60512/overpass-api-query-how-to-return-outermost-nodes-only)

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
<span id="post-60512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60512-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on a bit of an isoline/catchment issue for some set locations.</p>
<p>I need to get an idea of where the road extents are within a given radius or bounding box</p>
<p>eg: 5km, 10km, 50km of the facility.</p>
<p>I can do this with queries like the one below But I don't need all 70,000 points (5mb), I just need to know the outer reachable ring. This is more of an issue on the coast where I basically need to know the closest road to the beach.</p>
<p><a href="http://overpass-turbo.eu/s/sRf">http://overpass-turbo.eu/s/sRf</a></p>
<p>[bbox:-37.964903,144.682029,-37.764903,144.882029]; way[highway~"^(unclassified|residential|living_street|service|motorway|trunk|primary|secondary|tertiary|(motorway|trunk|primary|secondary)_link)$"]-&gt;.road1; node(w.road1); out;</p>
<p>Any suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '17, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/b8aa7704e87131c7e31196e2ca47c323?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lobsang&#39;s gravatar image" />
<p><span>lobsang</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lobsang has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60512" class="comments-container">
&#10;</div>
<div id="comment-tools-60512" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60512-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

