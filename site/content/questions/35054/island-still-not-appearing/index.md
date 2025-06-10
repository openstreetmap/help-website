+++
type = "question"
title = "Island still not appearing"
description = '''On this tile set: https://www.openstreetmap.org/#map=17/41.36570/-75.29994 There are 4 islands in this lake. All are experiencing the same issue -- they do not appear on the standard rendering. I&#x27;m trying to fix this -- focusing on Cairns Island in this example. When &quot;map data&quot; is enabled, you can c...'''
date = "2014-07-21T15:31:00Z"
lastmod = "2014-07-21T19:36:00Z"
weight = 35054
keywords = [ "island", "land", "mass" ]
aliases = [ "/questions/35054" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Island still not appearing](/questions/35054/island-still-not-appearing)

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
<span id="post-35054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35054-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On this tile set: <a href="https://www.openstreetmap.org/#map=17/41.36570/-75.29994">https://www.openstreetmap.org/#map=17/41.36570/-75.29994</a></p>
<p>There are 4 islands in this lake. All are experiencing the same issue -- they do not appear on the standard rendering. I'm trying to fix this -- focusing on Cairns Island in this example.</p>
<p>When "map data" is enabled, you can clearly see the land mass that represents the island. I've edited this according to the guidance I've seen here and on the wiki yet I cannot seem to get the land mass to appear on the rendering. I was able to get the "label" to appear (separate from the marker label, which is why there are now two).</p>
<p>Interestingly, the land mass for the island <em>does</em> appear on the Humanitarian layer, but none of the others.</p>
<p>Can someone please point out what is wrong with the way this island is configured? I'm very new to this, so please bear with me...</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span> <span class="post-tag tag-link-land" rel="tag" title="see questions tagged &#39;land&#39;">land</span> <span class="post-tag tag-link-mass" rel="tag" title="see questions tagged &#39;mass&#39;">mass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '14, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/44529d273be75325f61bd2efdd55ef9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robny&#39;s gravatar image" />
<p><span>robny</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jul '14, 21:45</strong> </span></p>
</div>
</div>
<div id="comments-container-35054" class="comments-container">
&#10;</div>
<div id="comment-tools-35054" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35054-form-container" class="comment-form-container">
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

<span id="35056"></span>

<div id="answer-container-35056" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35056-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="robny has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might want to remove natural=water from the <a href="https://www.openstreetmap.org/way/44449351">outer way</a>.</p>
<p>Edit: Sorry for brief answer. Was busy when I typed it. The multipolygon relation is defined as being a reservoir with holes, but with the extra tags on the outer way it is likely that this is <em>also</em> being seen as an area of water without holes, so rendering over the island in this case, depending perhaps on which features are rendered on which layers in particular renderings. Generally water will render on top of land I would think (oceans are handled differently).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '14, 16:33</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jul '14, 16:36</strong> </span></p>
</div>
</div>
<div id="comments-container-35056" class="comments-container">
<span id="35066"></span>
<div id="comment-35066" class="comment">
<div id="post-35066-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for the quick reply. This worked, although I still need to look more deeply into "why" it worked. As you pointed out, I need to better understand the relationship between:</p>
<p><a href="https://www.openstreetmap.org/way/44449351">https://www.openstreetmap.org/way/44449351</a> and: <a href="https://www.openstreetmap.org/relation/326780">https://www.openstreetmap.org/relation/326780</a></p>
<p>Regardless, it seems to be rendering better now -- which is good for all.</p>
</div>
<div id="comment-35066-info" class="comment-info">
<span class="comment-age">(21 Jul '14, 19:36)</span> <span class="comment-user userinfo">robny</span>
</div>
</div>
</div>
<div id="comment-tools-35056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35056-form-container" class="comment-form-container">
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

