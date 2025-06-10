+++
type = "question"
title = "How to map rooftop pools?"
description = '''I have a building polygon: building=yes leisure=water_park and a swimming pool that is located on top of the building: leisure=swimming_pool What is the proper way to tag a rooftop pool so that it renders correctly? As it is now, the pool is not rendered on the map. I&#x27;ve tried layer=1 on the pool, w...'''
date = "2016-12-31T00:37:00Z"
lastmod = "2016-12-31T10:41:00Z"
weight = 53772
keywords = [ "building", "water_park", "swimmingpool", "roof" ]
aliases = [ "/questions/53772" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to map rooftop pools?](/questions/53772/how-to-map-rooftop-pools)

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
<span id="post-53772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53772-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a building polygon: building=yes leisure=water_park</p>
<p>and a swimming pool that is located on top of the building: leisure=swimming_pool</p>
<p>What is the proper way to tag a rooftop pool so that it renders correctly? As it is now, the pool is not rendered on the map. I've tried layer=1 on the pool, with no success.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-water_park" rel="tag" title="see questions tagged &#39;water_park&#39;">water_park</span> <span class="post-tag tag-link-swimmingpool" rel="tag" title="see questions tagged &#39;swimmingpool&#39;">swimmingpool</span> <span class="post-tag tag-link-roof" rel="tag" title="see questions tagged &#39;roof&#39;">roof</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Dec '16, 00:37</strong></p>
<img src="https://secure.gravatar.com/avatar/95ff57b6d571cffa00600d67c0e0b81b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wcwalker&#39;s gravatar image" />
<p><span>wcwalker</span><br />
<span class="score" title="81 reputation points">81</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wcwalker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53772" class="comments-container">
&#10;</div>
<div id="comment-tools-53772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53772-form-container" class="comment-form-container">
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

<span id="53773"></span>

<div id="answer-container-53773" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53773-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-53773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wcwalker has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding layer=1 assuming the building is at 0 is quite OK and likely the best way to map the pool currently (I would have suggested adding an <a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">indoor</a> level tag too).</p>
<p>However you should not necessarily expect the standard map style to actually render the pool on top of the building at the current time. There are numerous, sometimes conflicting, requirements wrt layering for the style and not all of them can be met within the resource constraints the project has.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Dec '16, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Dec '16, 10:42</strong> </span></p>
</div>
</div>
<div id="comments-container-53773" class="comments-container">
&#10;</div>
<div id="comment-tools-53773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53773-form-container" class="comment-form-container">
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

