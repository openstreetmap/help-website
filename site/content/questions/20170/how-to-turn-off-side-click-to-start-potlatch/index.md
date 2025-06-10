+++
type = "question"
title = "How to turn off &quot;side-click&quot; to start Potlatch?"
description = '''This is a weirdly specific question, sorry. I&#x27;m running an Ubuntu system on an iMac, so I have a mouse that has buttons on the side, and if you squeeze them to side-click, that&#x27;s sending a particular kind of mouse event (specifically, xev says it&#x27;s registering as button 8, if you can believe it). It...'''
date = "2013-02-23T00:04:00Z"
lastmod = "2013-02-23T08:19:00Z"
weight = 20170
keywords = [ "potlatch", "mac", "mouse", "click" ]
aliases = [ "/questions/20170" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to turn off "side-click" to start Potlatch?](/questions/20170/how-to-turn-off-side-click-to-start-potlatch)

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
<span id="post-20170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is a weirdly specific question, sorry. I'm running an Ubuntu system on an iMac, so I have a mouse that has buttons on the side, and if you squeeze them to side-click, that's sending a particular kind of mouse event (specifically, xev says it's registering as button <em>8</em>, if you can believe it). It doesn't do anything in most places. But when I'm in the regular map layer of OSM, if I side-click, it starts up Potlatch, just as if I'd clicked "Edit".</p>
<p>The problem is, this happens very often unintentionally, and I'd really rather just turn it off. Is there any way to do that? Ubuntu doesn't seem to have any controls to handle this weird button, and neither does OSM or Potlatch that I can see.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch" rel="tag" title="see questions tagged &#39;potlatch&#39;">potlatch</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-mouse" rel="tag" title="see questions tagged &#39;mouse&#39;">mouse</span> <span class="post-tag tag-link-click" rel="tag" title="see questions tagged &#39;click&#39;">click</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '13, 00:04</strong></p>
<img src="https://secure.gravatar.com/avatar/4a4c8a91603aa21e05f5a441d5c13f26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blahedo&#39;s gravatar image" />
<p><span>blahedo</span><br />
<span class="score" title="736 reputation points">736</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blahedo has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-20170" class="comments-container">
&#10;</div>
<div id="comment-tools-20170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20170-form-container" class="comment-form-container">
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

<span id="20172"></span>

<div id="answer-container-20172" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20172-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not an Ubuntu expert, but <a href="http://blog.burlock.org/ubuntu/196-disabling-the-mouse-scroll-wheel-left-and-right-click-for-ubuntu-1010">this guide</a> (admittedly for 10.04) suggests you might find a .conf file where you can set ButtonMapping - I'm guessing you'd replace an 8 by a 0 to disable it (assuming you don't need to use it in other applications).</p>
<p>If you do need it to work in other applications then we probably also need to know the browser you are using and version of Ubuntu and the browser, and even then this might possibly be slightly off-topic for these forums.</p>
<p>I recently had problems with my mouse (in Opera on Windows) doing forward or back if I managed to press both left and right buttons at the same time (forward or back depending which was pressed first). This was an Opera feature I have since disabled.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '13, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-20172" class="comments-container">
&#10;</div>
<div id="comment-tools-20172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20172-form-container" class="comment-form-container">
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

