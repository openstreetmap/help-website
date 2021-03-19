+++
type = "question"
title = "traces from multiple interface"
description = '''Hello, Using wreshark for windows at multiple interfaces:  Is it possible to show the interfcae the packet was captured from in a column? How? Capture Intercae naming: Is it possible to show the at OS-level given and self speeking interface names in place of the cryptic and none self speeking driver...'''
date = "2014-03-10T02:26:00Z"
lastmod = "2014-03-10T11:38:00Z"
weight = 30636
keywords = [ "naming", "multiple-interfaces" ]
aliases = [ "/questions/30636" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [traces from multiple interface](/questions/30636/traces-from-multiple-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30636-score" class="post-score" title="current number of votes">0</div><span id="post-30636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Using wreshark for windows at multiple interfaces:</p><ol><li>Is it possible to show the interfcae the packet was captured from in a column? How?</li><li>Capture Intercae naming: Is it possible to show the at OS-level given and self speeking interface names in place of the cryptic and none self speeking driver name?</li></ol><p>thx for responses, Steffen</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-naming" rel="tag" title="see questions tagged &#39;naming&#39;">naming</span> <span class="post-tag tag-link-multiple-interfaces" rel="tag" title="see questions tagged &#39;multiple-interfaces&#39;">multiple-interfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '14, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/bee49869be792a7d6aee203210f9892e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Discovery&#39;s gravatar image" /><p><span>Discovery</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Discovery has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Mar '14, 02:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-30636" class="comments-container"></div><div id="comment-tools-30636" class="comment-tools"></div><div class="clear"></div><div id="comment-30636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30637"></span>

<div id="answer-container-30637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30637-score" class="post-score" title="current number of votes">3</div><span id="post-30637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1) yes. Add a custom column "frame.interface_id". Easiest way to do this is to select a packet in the packet list, find the line "interface id" in the first collapsed section, and right click on it. Then select "Apply as Column".</p><p>2) you can set interface names in the preferences. Go to the "Capture" page, and select the "Edit" Button next to "Interfaces". Use the "Comment" field to set a name that will be shown in the interface list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '14, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30637" class="comments-container"><span id="30639"></span><div id="comment-30639" class="comment"><div id="post-30639-score" class="comment-score"></div><div class="comment-text"><p>thx, very nice answers, everything is correct and working</p></div><div id="comment-30639-info" class="comment-info"><span class="comment-age">(10 Mar '14, 03:53)</span> <span class="comment-user userinfo">Discovery</span></div></div><span id="30660"></span><div id="comment-30660" class="comment"><div id="post-30660-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-30660-info" class="comment-info"><span class="comment-age">(10 Mar '14, 11:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-30637" class="comment-tools"></div><div class="clear"></div><div id="comment-30637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

