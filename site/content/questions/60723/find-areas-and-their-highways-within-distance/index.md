+++
type = "question"
title = "Find areas and their highways within distance"
description = '''The following query provides the names of residential streets within the `distance&#x27; of the lat and lon. (as yet. my current understanding of the QL is too primitive to make the street names visible other than copying and editing the data screen). &amp;lt;query type=&quot;way&quot;  &amp;lt;around lat=&quot;lat_number&quot; lon...'''
date = "2017-11-21T11:28:00Z"
lastmod = "2017-11-21T11:28:00Z"
weight = 60723
keywords = [ "overpass", "residential", "area", "highway", "distance" ]
aliases = [ "/questions/60723" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find areas and their highways within distance](/questions/60723/find-areas-and-their-highways-within-distance)

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
<span id="post-60723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60723-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The following query provides the names of residential streets within the `distance' of the lat and lon. (as yet. my current understanding of the QL is too primitive to make the street names visible other than copying and editing the data screen).</p>
<p>&lt;query type="way"<br />
&lt;around lat="lat_number" lon="lon_number" radius="distance_in_metres"/&gt;<br />
&lt;has-kv k="highway" regv="residential"/&gt;<br />
&lt;/query&gt;<br />
&lt;union&gt;<br />
&lt;item/&gt;<br />
&lt;recurse type="down"/&gt;<br />
&lt;/union&gt;<br />
&lt;print/&gt;</p>
<p>What would be the form of the query which would provide both the street and area in which the street is found.<br />
The area is to be the area one would normally use in an address eg town, village, suburb etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '17, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c5e89b8b037b23165056f8722eb83dd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorylila&#39;s gravatar image" />
<p><span>rorylila</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorylila has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '17, 11:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></br></p>
</div>
</div>
<div id="comments-container-60723" class="comments-container">
&#10;</div>
<div id="comment-tools-60723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60723-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

