+++
type = "question"
title = "A building over pedestrian area."
description = '''I am modifying a building (Tochigi Prefectural Cultural Center (100583549)) that is over a pedestrian area. The building has overhangs and a skybridge over the pedestrian area (https://flic.kr/p/2mRcVhw ). I thought adding a tag layer=1 to the building would render the entire building as seen from a...'''
date = "2021-12-17T02:37:00Z"
lastmod = "2021-12-17T10:05:00Z"
weight = 82858
keywords = [ "building", "layer", "overhang" ]
aliases = [ "/questions/82858" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [A building over pedestrian area.](/questions/82858/a-building-over-pedestrian-area)

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
<span id="post-82858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82858-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am modifying a building (Tochigi Prefectural Cultural Center (100583549)) that is over a pedestrian area. The building has overhangs and a skybridge over the pedestrian area (<a href="https://flic.kr/p/2mRcVhw">https://flic.kr/p/2mRcVhw</a> ). I thought adding a tag layer=1 to the building would render the entire building as seen from above. But the result was the opposite. The entire pedestrian area is rendered including the area under the building in the standard map. Is this correct?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-overhang" rel="tag" title="see questions tagged &#39;overhang&#39;">overhang</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '21, 02:37</strong></p>
<img src="https://secure.gravatar.com/avatar/08f7ac2db31d66e3efdd3a33fe0e7e22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yasobara&#39;s gravatar image" />
<p><span>yasobara</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yasobara has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Dec '21, 02:47</strong> </span></p>
</div>
</div>
<div id="comments-container-82858" class="comments-container">
<span id="82862"></span>
<div id="comment-82862" class="comment">
<div id="post-82862-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><code>highway=pedestrian</code> + <code>area=yes</code> is wrong here. <code>=pedestrian</code> means a pedestrianized street, with four-wheeled motorized vehicles physically able to travel on it. iD's "pedestrian area" preset name is misleading. This should be <code>highway=footway</code> + <code>area=yes</code>, which will still render.</p>
</div>
<div id="comment-82862-info" class="comment-info">
<span class="comment-age">(17 Dec '21, 10:01)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-82858" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82858-form-container" class="comment-form-container">
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

<span id="82859"></span>

<div id="answer-container-82859" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82859-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, It seems to be a quirk of the standard OSM layer, in all other layers (from the right sidebar) the building is rendered over the pedestrian area. However there are a few nodes of the layer=1 building that are joined to other areas. Personally I would unjoin the building from adjacent areas but doing this seems not to affect the standard layer of render.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '21, 08:02</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-82859" class="comments-container">
&#10;</div>
<div id="comment-tools-82859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82859-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82863"></span>

<div id="answer-container-82863" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82863-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is expected. It will always render above anything, including buildings. I don't remember there's rendering for <code>highway=*</code> + <code>covered=yes</code> + <code>covered=yes</code>. <code>layer=*</code> was only made for linear features. For 3D parts, use <code>building:min_level=*</code>, which will be rendered by 3D renderers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '21, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-82863" class="comments-container">
&#10;</div>
<div id="comment-tools-82863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82863-form-container" class="comment-form-container">
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

