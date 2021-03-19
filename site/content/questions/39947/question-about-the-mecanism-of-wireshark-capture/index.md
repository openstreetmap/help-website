+++
type = "question"
title = "Question about the mécanism of wireshark capture"
description = '''Hello , Can a frame TCP [SYN ACK] captured (without errors) by wireshark on my eth0, finally, not leave physically, on the network? (remained blocked by the Ethernet card, right before the sending) Thks Thomas'''
date = "2015-02-19T06:45:00Z"
lastmod = "2015-02-19T19:41:00Z"
weight = 39947
keywords = [ "mamaman" ]
aliases = [ "/questions/39947" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Question about the mécanism of wireshark capture](/questions/39947/question-about-the-mecanism-of-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39947-score" class="post-score" title="current number of votes">0</div><span id="post-39947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello ,</p><p>Can a frame TCP [SYN ACK] captured (without errors) by wireshark on my eth0, finally, not leave physically, on the network? (remained blocked by the Ethernet card, right before the sending)</p><p>Thks</p><p>Thomas</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mamaman" rel="tag" title="see questions tagged &#39;mamaman&#39;">mamaman</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '15, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/006b4a73e12f4d00275346a933615585?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThomasAdminLinux&#39;s gravatar image" /><p><span>ThomasAdminL...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThomasAdminLinux has no accepted answers">0%</span></p></div></div><div id="comments-container-39947" class="comments-container"></div><div id="comment-tools-39947" class="comment-tools"></div><div class="clear"></div><div id="comment-39947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39950"></span>

<div id="answer-container-39950" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39950-score" class="post-score" title="current number of votes">0</div><span id="post-39950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In theory, yes, it could. There could be a blocking situation below the capture interface, towards the hardware. Somewhere in the driver, or in the network hardware itself there could be a problem or a bug causing this frame not to appear on the physical layer. How likely this is is depending on the maturity of the silicon and/or software driving the hardware.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '15, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39950" class="comments-container"></div><div id="comment-tools-39950" class="comment-tools"></div><div class="clear"></div><div id="comment-39950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39965"></span>

<div id="answer-container-39965" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39965-score" class="post-score" title="current number of votes">0</div><span id="post-39965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the packet was supposedly sent by your machine, yes, that could happen. Few, if any Ethernet interfaces receive their own transmissions (I don't know of <em>any</em> that do), so transmitted packets are "captured" by the software delivering a copy of the packet to the packet capture mechanism. The packet might be handed to the Ethernet adapter but it might, for example, not be able to transmit it (much more likely if it's half-duplex than if it's full-duplex on a switched Ethernet).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '15, 19:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-39965" class="comments-container"></div><div id="comment-tools-39965" class="comment-tools"></div><div class="clear"></div><div id="comment-39965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

