+++
type = "question"
title = "Is fitBounds available in osmdroid?"
description = '''My map will have two markers for routing purpose, now how could i automatically zoom out to the center between those two markers? Is there any alternative approach to fitBounds in osmdroid(or is there fitBounds itself!!)? Thanks in advance :)'''
date = "2016-06-07T14:14:00Z"
lastmod = "2016-06-07T16:58:00Z"
weight = 50069
keywords = [ "development", "android", "osmdroid", "fitbounds" ]
aliases = [ "/questions/50069" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is fitBounds available in osmdroid?](/questions/50069/is-fitbounds-available-in-osmdroid)

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
<span id="post-50069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50069-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My map will have two markers for routing purpose, now how could i automatically zoom out to the center between those two markers? Is there any alternative approach to fitBounds in osmdroid(or is there fitBounds itself!!)?</p>
<p>Thanks in advance :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-fitbounds" rel="tag" title="see questions tagged &#39;fitbounds&#39;">fitbounds</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '16, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/dfcf9d391ca68ff816e8f9f8ec9f3fc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20Gowtham&#39;s gravatar image" />
<p><span>Arun Gowtham</span><br />
<span class="score" title="0 reputation points">0</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun Gowtham has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '16, 20:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-50069" class="comments-container">
&#10;</div>
<div id="comment-tools-50069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50069-form-container" class="comment-form-container">
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

<span id="50075"></span>

<div id="answer-container-50075" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50075-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a <a href="http://stackoverflow.com/a/24122164/1340631">solution on Stack Overflow</a>. Basically you have to compute a bounding box by iterating over your markers and calculating min/max lat and lon. Then just call <code>zoomToBoundingBox()</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '16, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-50075" class="comments-container">
&#10;</div>
<div id="comment-tools-50075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50075-form-container" class="comment-form-container">
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

