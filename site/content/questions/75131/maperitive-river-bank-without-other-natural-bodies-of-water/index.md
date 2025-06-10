+++
type = "question"
title = "Maperitive - River Bank without other natural bodies of water"
description = '''Using the Maperitive I am modifying a ruleset to meet my requirements.  The place I am stuck is wanting to fill in an area of the river. Its a larger area. I don&#x27;t however want the other bodies that are around it that are not marked river. Is there a way to exclude the other bodies or specify that I...'''
date = "2020-06-04T06:17:00Z"
lastmod = "2020-06-04T15:36:00Z"
weight = 75131
keywords = [ "water", "maperitive" ]
aliases = [ "/questions/75131" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maperitive - River Bank without other natural bodies of water](/questions/75131/maperitive-river-bank-without-other-natural-bodies-of-water)

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
<span id="post-75131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75131-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using the Maperitive I am modifying a ruleset to meet my requirements.</p>
<p>The place I am stuck is wanting to fill in an area of the river. Its a larger area. I don't however want the other bodies that are around it that are not marked river. Is there a way to exclude the other bodies or specify that I only want the natural bodie if it is a river?</p>
<p>Here is what I have in the rule<img src="https://help.openstreetmap.org/upfiles/2020-06-04_00_14_00-Maperitive_(v2.4.3).png" alt="alt text" /></p>
<pre><code>    areas
    water : natural=water OR waterway=riverbank</code></pre>
<p>Here is an examle of the area I want and don't want. This is Nashville TN.<br />
Here are the tags on the river. <img src="https://help.openstreetmap.org/upfiles/2020-06-04_00_25_05-OpenStreetMap_ACn438b.png" alt="alt text" /></p>
<p>And here are the tags on the Pond <img src="https://help.openstreetmap.org/upfiles/2020-06-04_00_24_21-OpenStreetMap.png" alt="alt text" /></p>
<p>Thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '20, 06:17</strong></p>
<img src="https://secure.gravatar.com/avatar/6264d568d3522860f4cd24b54f0ffe53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thumper369&#39;s gravatar image" />
<p><span>Thumper369</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thumper369 has no accepted answers">0%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '20, 06:28</strong> </span></p>
</div>
</div>
<div id="comments-container-75131" class="comments-container">
&#10;</div>
<div id="comment-tools-75131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75131-form-container" class="comment-form-container">
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

<span id="75145"></span>

<div id="answer-container-75145" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75145-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ok, Figured it out thismorning. In the areas section of the rules.</p>
<p>Old value: areas water : natural=water OR waterway=riverbank</p>
<p>New values: areas water : water=river OR waterway=riverbank</p>
<p>Results: <img src="https://help.openstreetmap.org/upfiles/2020-06-04_09_34_50-Maperitive_(v2.4.3).png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '20, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/6264d568d3522860f4cd24b54f0ffe53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thumper369&#39;s gravatar image" />
<p><span>Thumper369</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thumper369 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-75145" class="comments-container">
&#10;</div>
<div id="comment-tools-75145" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75145-form-container" class="comment-form-container">
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

