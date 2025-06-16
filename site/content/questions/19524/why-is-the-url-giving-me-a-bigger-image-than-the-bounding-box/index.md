+++
type = "question"
title = "Why is the url giving me a bigger image than the bounding box?"
description = '''Hello,  I&#x27;m trying to access OSM through my application. Here is an example of a request I&#x27;m sending: http://pafciu17.dev.openstreetmap.org/?module=map&amp;amp;bbox=-111.97021484375,33.46292927417002,-111.82470703125,33.37333569698748&amp;amp;width=596.0&amp;amp;height=366.0&amp;amp;imgType=jpeg If you notice, the ...'''
date = "2013-02-01T19:04:00Z"
lastmod = "2013-02-01T19:47:00Z"
weight = 19524
keywords = [ "api" ]
aliases = [ "/questions/19524" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is the url giving me a bigger image than the bounding box?](/questions/19524/why-is-the-url-giving-me-a-bigger-image-than-the-bounding-box)

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
<span id="post-19524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19524-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm trying to access OSM through my application. Here is an example of a request I'm sending: <a href="http://pafciu17.dev.openstreetmap.org/?module=map&amp;bbox=-111.97021484375,33.46292927417002,-111.82470703125,33.37333569698748&amp;width=596.0&amp;height=366.0&amp;imgType=jpeg">http://pafciu17.dev.openstreetmap.org/?module=map&amp;bbox=-111.97021484375,33.46292927417002,-111.82470703125,33.37333569698748&amp;width=596.0&amp;height=366.0&amp;imgType=jpeg</a> If you notice, the bounding box that is in the request is smaller than the image that is being returned. I'm not quite sure why this is happening? Is it a pixel issue? I'm trying to get away with using an api that does not require a zoom to be specified, that is why I went with the above api.</p>
<p>Thank you for any help, I appreciate any help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '13, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/148ca0cf9c46ebee577961109b6b4817?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meburris&#39;s gravatar image" />
<p><span>meburris</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meburris has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19524" class="comments-container">
&#10;</div>
<div id="comment-tools-19524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19524-form-container" class="comment-form-container">
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

<span id="19526"></span>

<div id="answer-container-19526" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19526-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That would be <a href="https://wiki.openstreetmap.org/wiki/Static_Maps_API">this API</a>, so be aware that your application is likely to get blocked if it places undue load on the servers as per the warning. From the links on that page it also looks like it is no longer maintained, and the images it produces seem to have an out of date attribution.</p>
<p>It might be worth following the recommendation on the Static Maps API page and trying <a href="http://staticmap.openstreetmap.de/">staticMapLite</a> instead?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '13, 19:44</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-19526" class="comments-container">
<span id="19527"></span>
<div id="comment-19527" class="comment">
<div id="post-19527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok thank you, I will look into that. I was trying to get away with using an api that didn't require a "zoom" or "scale" parameter because we use Pixels per degree and I thought it would be difficult.</p>
</div>
<div id="comment-19527-info" class="comment-info">
<span class="comment-age">(01 Feb '13, 19:47)</span> <span class="comment-user userinfo">meburris</span>
</div>
</div>
</div>
<div id="comment-tools-19526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19526-form-container" class="comment-form-container">
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

