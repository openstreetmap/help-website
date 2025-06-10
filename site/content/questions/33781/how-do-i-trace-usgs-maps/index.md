+++
type = "question"
title = "How do I trace USGS maps?"
description = '''I would like to trace islands around my area (57,-135) and the best background data is the USGS topo maps. However, whenever I zoom in it disappears. I tried using the JOSM editor, but its imagery also disappears. Is there something I&#x27;m doing wrong? Or is there another way to get around this? Does U...'''
date = "2014-06-07T20:51:00Z"
lastmod = "2014-06-08T08:27:00Z"
weight = 33781
keywords = [ "topo", "coastline", "usgs" ]
aliases = [ "/questions/33781" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I trace USGS maps?](/questions/33781/how-do-i-trace-usgs-maps)

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
<span id="post-33781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33781-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to trace islands around my area (57,-135) and the best background data is the USGS topo maps. However, whenever I zoom in it disappears. I tried using the JOSM editor, but its imagery also disappears. Is there something I'm doing wrong?</p>
<p>Or is there another way to get around this? Does USGS have topo / coastline data I could import? I've tried finding data through the USGS but I cannot find anything useful.</p>
<p>Thanks for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-topo" rel="tag" title="see questions tagged &#39;topo&#39;">topo</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span> <span class="post-tag tag-link-usgs" rel="tag" title="see questions tagged &#39;usgs&#39;">usgs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '14, 20:51</strong></p>
<img src="https://secure.gravatar.com/avatar/efa2bd232d1bfd0540fe303e6cba5f64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jfact0ry&#39;s gravatar image" />
<p><span>Jfact0ry</span><br />
<span class="score" title="366 reputation points">366</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jfact0ry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33781" class="comments-container">
<span id="33782"></span>
<div id="comment-33782" class="comment">
<div id="post-33782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are not alone and you are doing nothing wrong. I have the same issue in JOSM. Depending on the area you're looking at the MSR Topos, which AFAIK contain identical information as the USGS maps, sometimes allow higher zoom levels. For as useful as the USGS topos are it's a shame they are so badly limited in their display.</p>
<p>I'm hoping someone will come along to answer your question more helpfully than I can.</p>
</div>
<div id="comment-33782-info" class="comment-info">
<span class="comment-age">(07 Jun '14, 20:59)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-33781" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33781-form-container" class="comment-form-container">
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

<span id="33788"></span>

<div id="answer-container-33788" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33788-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Could you please clarify which source you are using. For example if you are using the OSM-US proxy service and which proxied service?</p>
<p>The issue is likely caused by a combination of higher zoom tiles not being available and the max zoom parameter in JOSM for the source being wrong. JOSM and most other editors will "overzoom" imagery but for that it needs to knows the correct max zoom level is. Naturally "overzooming" will only help to a certain point, best if the imagery source actually has tiles to max zoom level the source can reasonably support from a resolution point of view.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '14, 08:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-33788" class="comments-container">
&#10;</div>
<div id="comment-tools-33788" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33788-form-container" class="comment-form-container">
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

