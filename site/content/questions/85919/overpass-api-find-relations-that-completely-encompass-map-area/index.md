+++
type = "question"
title = "Overpass API: find relations that completely encompass map area"
description = '''I have an application that retrieves small areas of map data via the Overpass API to generate custom-rendered maps of interest. However, if the area of interest is completely inside certain relations (e.g. in one case, a multipolygon of natural = heath), this relation is not returned by the bbox que...'''
date = "2022-10-19T19:59:00Z"
lastmod = "2022-10-20T07:57:00Z"
weight = 85919
keywords = [ "overpass", "api", "is_in" ]
aliases = [ "/questions/85919" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: find relations that completely encompass map area](/questions/85919/overpass-api-find-relations-that-completely-encompass-map-area)

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
<span id="post-85919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85919-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an application that retrieves small areas of map data via the Overpass API to generate custom-rendered maps of interest. However, if the area of interest is completely inside certain relations (e.g. in one case, a multipolygon of natural = heath), this relation is not returned by the bbox query and therefore the landuse is not tagged appropriately. I understand that simple areas (closed ways) and <em>named</em> relations can be retrieved using an "is_in" query - but how can I retrieve unnamed relations such as the example above? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-is_in" rel="tag" title="see questions tagged &#39;is_in&#39;">is_in</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '22, 19:59</strong></p>
<img src="https://secure.gravatar.com/avatar/f7649d10621b7be6b2a1bc0858ca9f61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddixon&#39;s gravatar image" />
<p><span>ddixon</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddixon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85919" class="comments-container">
<span id="85922"></span>
<div id="comment-85922" class="comment">
<div id="post-85922-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you post the routine?</p>
</div>
<div id="comment-85922-info" class="comment-info">
<span class="comment-age">(19 Oct '22, 22:20)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="85929"></span>
<div id="comment-85929" class="comment">
<div id="post-85929-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My usual query is:</p>
<pre><code>node(53.113093987353764,-4.054470062255859,53.11925273065562,-4.040318727493286);&lt;;&gt;;</code></pre>
<p>I've also tried to union that with an is_in query (after extracting the nodes from the area):</p>
<pre><code>is_in(53.115,-4.05);</code></pre>
<p>Neither find this relation:</p>
<p><a href="https://www.openstreetmap.org/relation/14644322">https://www.openstreetmap.org/relation/14644322</a></p>
</div>
<div id="comment-85929-info" class="comment-info">
<span class="comment-age">(20 Oct '22, 07:57)</span> <span class="comment-user userinfo">ddixon</span>
</div>
</div>
</div>
<div id="comment-tools-85919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85919-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

