+++
type = "question"
title = "How do I correct an administrative boundary in the Nominatim?"
description = '''If I search on &quot;Grayling, MI&quot; in OpenStreetMap.org, the first result that pops up from the OpenStreetMap Nominatim is: &quot;Administrative Boundary Grayling, Oscoda County, Michigan, United States of America&quot; That is incorrect. The correct listing should be: &quot;Administrative Boundary Grayling, Crawford C...'''
date = "2012-06-27T15:25:00Z"
lastmod = "2012-06-27T21:19:00Z"
weight = 13858
keywords = [ "nominatim" ]
aliases = [ "/questions/13858" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I correct an administrative boundary in the Nominatim?](/questions/13858/how-do-i-correct-an-administrative-boundary-in-the-nominatim)

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
<span id="post-13858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13858-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I search on "Grayling, MI" in OpenStreetMap.org, the first result that pops up from the OpenStreetMap Nominatim is: "Administrative Boundary Grayling, Oscoda County, Michigan, United States of America"</p>
<p>That is incorrect. The correct listing should be: "Administrative Boundary Grayling, Crawford County, Michigan, United States of America"</p>
<p>I can see the data listed in the Nominatim page at <a href="http://nominatim.openstreetmap.org/details.php?place_id=128836176">http://nominatim.openstreetmap.org/details.php?place_id=128836176</a> but I don't see any options for updating the data.</p>
<p>How can I correct the bad data in the Nominatim?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '12, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/6a7176992911c9fb542a181011bf10cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ArDub&#39;s gravatar image" />
<p><span>ArDub</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ArDub has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '12, 15:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-13858" class="comments-container">
&#10;</div>
<div id="comment-tools-13858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13858-form-container" class="comment-form-container">
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

<span id="13863"></span>

<div id="answer-container-13863" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13863-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There seems to be an error in the data. If you follow the link in the detals view you can find the Oscoda County relation. As you see this have the wrong name.</p>
<p>If you select any of the boundary ways in an editor, you can select the relation and change its name. Nominatim will update its database from the main OSM database.</p>
<p>If you want you can message the user that added the data and ask him to go through the rest of the data if he have done simelar mistakes elsewhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '12, 21:19</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13863" class="comments-container">
&#10;</div>
<div id="comment-tools-13863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13863-form-container" class="comment-form-container">
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

