+++
type = "question"
title = "Sea/Ocean Polygons help, please!"
description = '''Can anyone please advise the code I need to receive polys back for the sea/ocean in a bounding rect? Naively, I expected the below to return all water elements, but I understand seas and oceans work differently: [out:json]; (nwr[&quot;natural&quot;~&quot;water&quot;] (53.264064,-4.657101,53.319909,-4.577605); ); out me...'''
date = "2020-06-12T10:23:00Z"
lastmod = "2020-06-12T11:10:00Z"
weight = 75303
keywords = [ "sea", "ocean" ]
aliases = [ "/questions/75303" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Sea/Ocean Polygons help, please!](/questions/75303/seaocean-polygons-help-please)

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
<span id="post-75303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75303-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can anyone please advise the code I need to receive polys back for the sea/ocean in a bounding rect?</p>
<p>Naively, I expected the below to return all water elements, but I understand seas and oceans work differently:</p>
<p>[out:json]; (nwr["natural"~"water"] (53.264064,-4.657101,53.319909,-4.577605); ); out meta; &gt;; out skel qt;</p>
<p>Naturally, I've tried swapping out natural for place and water for sea - but still no luck.</p>
<p>Appreciate any help in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sea" rel="tag" title="see questions tagged &#39;sea&#39;">sea</span> <span class="post-tag tag-link-ocean" rel="tag" title="see questions tagged &#39;ocean&#39;">ocean</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '20, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/09f53b06dcac1cb83c71c601571cf449?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jusdespommes&#39;s gravatar image" />
<p><span>jusdespommes</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jusdespommes has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jun '20, 10:23</strong> </span></p>
</div>
</div>
<div id="comments-container-75303" class="comments-container">
&#10;</div>
<div id="comment-tools-75303" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75303-form-container" class="comment-form-container">
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

<span id="75304"></span>

<div id="answer-container-75304" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75304-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can only retrieve coastline (<code>natural=coastline</code>) from Overpass, not ready-made water polygons. OpenStreetMap does not store the sea as polygons but as coastline segments. See <a href="https://wiki.openstreetmap.org/wiki/Tag:natural%3Dcoastline">https://wiki.openstreetmap.org/wiki/Tag:natural%3Dcoastline</a> for details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '20, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-75304" class="comments-container">
&#10;</div>
<div id="comment-tools-75304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75304-form-container" class="comment-form-container">
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

