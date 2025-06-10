+++
type = "question"
title = "How to correct the details of a place?"
description = '''I live in Palestine, Hampshire, England, and the problem is that this is listed as Palestine in Wiltshire. If I edit the place &quot;Palestine&quot; on the map, it does not list the &quot;Wiltshire&quot; detail so maybe this detail is elsewhere, or I&#x27;m using the wrong editor! Can someone help me to make this correction...'''
date = "2012-01-23T10:02:00Z"
lastmod = "2012-01-23T10:42:00Z"
weight = 10147
keywords = [ "correction", "editing", "place", "details", "nominatim" ]
aliases = [ "/questions/10147" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to correct the details of a place?](/questions/10147/how-to-correct-the-details-of-a-place)

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
<span id="post-10147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10147-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I live in Palestine, Hampshire, England, and the problem is that this is listed as Palestine in Wiltshire. If I edit the place "Palestine" on the map, it does not list the "Wiltshire" detail so maybe this detail is elsewhere, or I'm using the wrong editor! Can someone help me to make this correction please? (In US terms, Palestine is the town and Wiltshire/Hampshire is the county.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-correction" rel="tag" title="see questions tagged &#39;correction&#39;">correction</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-details" rel="tag" title="see questions tagged &#39;details&#39;">details</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jan '12, 10:02</strong></p>
<img src="https://secure.gravatar.com/avatar/9430b2e6b54c8316ecd3b2bc23e22534?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Diggings&#39;s gravatar image" />
<p><span>Diggings</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Diggings has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jan '12, 10:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-10147" class="comments-container">
&#10;</div>
<div id="comment-tools-10147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10147-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="10150"></span>

<div id="answer-container-10150" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10150-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Checking at <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a> it seems that the nominatim search is using the proximity of the county place nodes rather than the administrative boundary relations. I don't think that nominatim is fully up to date at present, and it may be that the administrative boundaries weren't correctly closed at the time it has got up to (the link above says 7th December and the <a href="http://www.openstreetmap.org/browse/relation/76228">Hampshire relation</a> was last amended on 10th December, with a "fix coastline" comment).</p>
<p>So I think the best solution is to wait. It is possible someone might suggest using the is_in:county tag on the Palestine village place node, but with well defined boundary relations this shouldn't be required, and wouldn't be noticed until nominatim catches up to date anyway, by which time it should know that the boundary relations are ok and use those in preference to the place nodes.</p>
<p>I think...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '12, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-10150" class="comments-container">
&#10;</div>
<div id="comment-tools-10150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10150-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10151"></span>

<div id="answer-container-10151" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10151-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is probably a problem caused by place nodes which causes the nominatim to assume that a place belongs to the nearest node. Polygons are really needed for all areas to fix this problem. Try searching these questions for "boundary" get more info.http://<a href="http://help.openstreetmap.org/search/?csrfmiddlewaretoken=ac4b2a2e0dfdb99b0045a7d2abdcef1f&amp;q=boundary&amp;Submit=search&amp;t=question">help.openstreetmap.org/search/?csrfmiddlewaretoken=ac4b2a2e0dfdb99b0045a7d2abdcef1f&amp;q=boundary&amp;Submit=search&amp;t=question</a> and these <a href="http://help.openstreetmap.org/search/?csrfmiddlewaretoken=ac4b2a2e0dfdb99b0045a7d2abdcef1f&amp;q=nominatim&amp;Submit=search&amp;t=question">http://help.openstreetmap.org/search/?csrfmiddlewaretoken=ac4b2a2e0dfdb99b0045a7d2abdcef1f&amp;q=nominatim&amp;Submit=search&amp;t=question</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '12, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jan '12, 10:35</strong> </span></p>
</div>
</div>
<div id="comments-container-10151" class="comments-container">
<span id="10152"></span>
<div id="comment-10152" class="comment">
<div id="post-10152-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As Ed says even when fixed there can be long delay for the nominatim to use the new data I suppose updating the map takes priority, as it should</p>
</div>
<div id="comment-10152-info" class="comment-info">
<span class="comment-age">(23 Jan '12, 10:42)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-10151" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10151-form-container" class="comment-form-container">
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

