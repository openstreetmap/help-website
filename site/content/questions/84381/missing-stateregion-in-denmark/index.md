+++
type = "question"
title = "Missing state/region in Denmark"
description = '''Hi there, I&#x27;m using Nominatim to draw the Danish states/regions on a map, however one of the regions is missing? The region missing is &quot;Region Hovedstaden&quot;, but it simply does not exist. Who should I get in contact with to fix it? Is it a bug or is the data simply not available on Nominatim?'''
date = "2022-05-06T14:24:00Z"
lastmod = "2022-05-06T16:31:00Z"
weight = 84381
keywords = [ "region", "state", "drawing" ]
aliases = [ "/questions/84381" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing state/region in Denmark](/questions/84381/missing-stateregion-in-denmark)

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
<span id="post-84381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84381-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I'm using Nominatim to draw the Danish states/regions on a map, however one of the regions is missing? The region missing is "Region Hovedstaden", but it simply does not exist.</p>
<p>Who should I get in contact with to fix it? Is it a bug or is the data simply not available on Nominatim?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-region" rel="tag" title="see questions tagged &#39;region&#39;">region</span> <span class="post-tag tag-link-state" rel="tag" title="see questions tagged &#39;state&#39;">state</span> <span class="post-tag tag-link-drawing" rel="tag" title="see questions tagged &#39;drawing&#39;">drawing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '22, 14:24</strong></p>
<img src="https://secure.gravatar.com/avatar/13baebd93712190c686ad3b7b4deec15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WonderingDane&#39;s gravatar image" />
<p><span>WonderingDane</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WonderingDane has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84381" class="comments-container">
<span id="84384"></span>
<div id="comment-84384" class="comment">
<div id="post-84384-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I cannot answer on the nominatim question. But if you are just drawing regions on a map it might be simpler to take the data from the OSM database directly You could use <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass Turbo</a> to filter the desired states/regions and download them.</p>
</div>
<div id="comment-84384-info" class="comment-info">
<span class="comment-age">(06 May '22, 15:12)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-84381" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84381-form-container" class="comment-form-container">
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

<span id="84385"></span>

<div id="answer-container-84385" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84385-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The region definitely exists in OSM <a href="https://www.openstreetmap.org/relation/1320608">https://www.openstreetmap.org/relation/1320608</a> , so it isn't a a data issue per se.</p>
<p>Looking at detail results on nominatim.openstreetmap.org it definitely doesn't seem to be indexed at all, so this is likely an issue for the nominatim maintainers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '22, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '22, 16:36</strong> </span></p>
</div>
</div>
<div id="comments-container-84385" class="comments-container">
&#10;</div>
<div id="comment-tools-84385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84385-form-container" class="comment-form-container">
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

