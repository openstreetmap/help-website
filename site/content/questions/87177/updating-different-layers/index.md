+++
type = "question"
title = "Updating different layers"
description = '''As a newbie, I am going as slowly as I can to understand how OSM works in practice. I have made 2 changes (of the few thousand planned) to get an idea of the quirks of the system. I can see one of my updates on CycleOSM but not the Standard map. I am assuming from this earlier thread that all change...'''
date = "2023-04-26T15:04:00Z"
lastmod = "2023-04-26T21:35:00Z"
weight = 87177
keywords = [ "layers", "changes", "update" ]
aliases = [ "/questions/87177" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Updating different layers](/questions/87177/updating-different-layers)

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
<span id="post-87177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87177-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As a newbie, I am going as slowly as I can to understand how OSM works in practice. I have made 2 changes (of the few thousand planned) to get an idea of the quirks of the system.</p>
<p>I can see one of my updates on CycleOSM but not the Standard map. I am assuming from this earlier thread that all changes should be made on the Standard map which will then cascade to the other layer versions.</p>
<p>My second change (on the Standard Map) has not shown after a few hours now. My presumption if someone will confirm, is that as I asked for it to be checked, it will not show until it is actually checked?</p>
<p><a href="https://help.openstreetmap.org/questions/56241/why-is-the-standard-updated-but-cycle-transport-and-humanitarian-still-show-old-data">https://help.openstreetmap.org/questions/56241/why-is-the-standard-updated-but-cycle-transport-and-humanitarian-still-show-old-data</a></p>
<p>Looking forward to contributing more data but want to ensure I don't cause work for others later.</p>
<p>Great project which I have used a few times now so time to give back.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '23, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f40e05217be4ca4139ef971a740c1371?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Angus%20Gill&#39;s gravatar image" />
<p><span>Angus Gill</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Angus Gill has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87177" class="comments-container">
&#10;</div>
<div id="comment-tools-87177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87177-form-container" class="comment-form-container">
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

<span id="87178"></span>

<div id="answer-container-87178" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87178-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-87178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Angus Gill has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are not making changes to any specific layer, you are making changes to the underlying data which is common to all maps generated from OSM data (some maps will use additional 3rd party data, but that is a bit out of scope here).</p>
<p>Now why there is a difference in the display of what you changed between CycleOSM and the standard style can be due to a lot of things, from different choices on which data to render, to simple caching issues in your browser.</p>
<p>As a rule the "standard" layer is the quickest to update, so I suspect the issue is due to rendering differences, but without more information you are not going to get a definitive answer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '23, 16:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Apr '23, 16:21</strong> </span></p>
</div>
</div>
<div id="comments-container-87178" class="comments-container">
<span id="87179"></span>
<div id="comment-87179" class="comment">
<div id="post-87179-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Assuming your OSM user name is the same as here I can verify that both your edits are visible on both maps for me (the Apartamentos De Montaña Mendiola only on the most zoomed in layer in CyclOSM for now). So I presume there was just some time lag between the edits and the rendering or you have still old tiles cached.</p>
<p>The check option does not delay rendering.</p>
</div>
<div id="comment-87179-info" class="comment-info">
<span class="comment-age">(26 Apr '23, 21:35)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-87178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87178-form-container" class="comment-form-container">
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

