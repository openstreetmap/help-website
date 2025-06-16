+++
type = "question"
title = "Why protected areas don&#x27;t show up on standard OSM layer?"
description = '''I have been adding few National Parks in our country to the OSM with the appropriate tags but unfortunately I&#x27;m unable to see these areas on openstreetmap.org at the maximum zoom level.The tags that I used for defining National Parks are as follows: boundary=protected_area  protect_class=2 protectio...'''
date = "2016-07-31T09:14:00Z"
lastmod = "2016-08-01T04:02:00Z"
weight = 51180
keywords = [ "not_shown", "protection_class", "nature_reserve", "protected_area", "tagging" ]
aliases = [ "/questions/51180" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why protected areas don't show up on standard OSM layer?](/questions/51180/why-protected-areas-dont-show-up-on-standard-osm-layer)

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
<span id="post-51180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51180-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been adding few National Parks in our country to the OSM with the appropriate tags but unfortunately I'm unable to see these areas on openstreetmap.org at the maximum zoom level.The tags that I used for defining National Parks are as follows:</p>
<p>boundary=protected_area protect_class=2 protection_title=national park</p>
<p>I have seen some people also use the tag leisure=nature_reserve with the above combination, is it the correct approach of tagging such areas? Is there a problem with rendering of these tags on OSM standard layer?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-protection_class" rel="tag" title="see questions tagged &#39;protection_class&#39;">protection_class</span> <span class="post-tag tag-link-nature_reserve" rel="tag" title="see questions tagged &#39;nature_reserve&#39;">nature_reserve</span> <span class="post-tag tag-link-protected_area" rel="tag" title="see questions tagged &#39;protected_area&#39;">protected_area</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '16, 09:14</strong></p>
<img src="https://secure.gravatar.com/avatar/f7da215f2999ecac8d169e32e2c3502e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adib%20Yz&#39;s gravatar image" />
<p><span>Adib Yz</span><br />
<span class="score" title="291 reputation points">291</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adib Yz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '16, 06:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-51180" class="comments-container">
&#10;</div>
<div id="comment-tools-51180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51180-form-container" class="comment-form-container">
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

<span id="51183"></span>

<div id="answer-container-51183" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51183-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-51183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Adib Yz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Regarding of rendering protected boundaries, please, read <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/603">this issue</a>.</p>
<p>Regarding of adding any tags to force rendering, it could be qualified as <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a>.</p>
<p>While <code>leisure=nature_reserve</code> is technically related to <code>boundary=protected_area</code>, the latter one is the most sufficient and recent way of tagging these areas. Keep in mind, that <code>leisure=*</code> key could, in certain cases, lead to misinterpretation, since highest protection class areas are not meant for any recreational activities.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '16, 04:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c7f2443ac02cb3e24f4df768eeb98933?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BushmanK&#39;s gravatar image" />
<p><span>BushmanK</span><br />
<span class="score" title="171 reputation points">171</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BushmanK has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-51183" class="comments-container">
&#10;</div>
<div id="comment-tools-51183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51183-form-container" class="comment-form-container">
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

