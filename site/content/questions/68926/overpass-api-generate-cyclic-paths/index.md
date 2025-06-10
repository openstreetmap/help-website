+++
type = "question"
title = "Overpass API: generate cyclic paths"
description = '''I&#x27;m developing a simulation which should emulate the movement of cars on a road, emitting GPS coordinates for different cars in a certain bounding box. Therefore, i&#x27;d like to use OverpassQL to generate some &quot;random&quot; (i suppose i will just choose a random starting point myself, since as far as i know...'''
date = "2019-04-24T17:49:00Z"
lastmod = "2019-04-24T17:49:00Z"
weight = 68926
keywords = [ "overpass", "overpass-ql", "overpass-api" ]
aliases = [ "/questions/68926" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: generate cyclic paths](/questions/68926/overpass-api-generate-cyclic-paths)

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
<span id="post-68926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68926-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm developing a simulation which should emulate the movement of cars on a road, emitting GPS coordinates for different cars in a certain bounding box. Therefore, i'd like to use OverpassQL to generate some "random" (i suppose i will just choose a random starting point myself, since as far as i know OverpassQL does not implement any RNG), if possible cyclic paths for cars to "drive" along repeatedly. Another possibility would be just a path that starts at one border of the bounding box and ends at the other. I suppose i could just recurse along adjacent ways at their corresponding ends, but how do i make this cyclic, i.e. ending at the starting point?</p>
<p>I am a total beginner at OverpassQL and the options seem overwhelming. Can anyone help me out?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '19, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a794b3f5ba76e34823fb7518a0ab62d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbaier1&#39;s gravatar image" />
<p><span>sbaier1</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbaier1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '19, 17:50</strong> </span></p>
</div>
</div>
<div id="comments-container-68926" class="comments-container">
&#10;</div>
<div id="comment-tools-68926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68926-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

