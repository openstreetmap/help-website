+++
type = "question"
title = "How to capture network message"
description = '''Hello,  I have some digital signage software that can send out a network message (0x02PON0x03) to switch on a TV. I want to be able to control the display without the signage software.  I have tried using netcat to no avail. Is there a method I can use wireshark to monitor and analyze the message se...'''
date = "2011-07-07T13:47:00Z"
lastmod = "2011-07-07T17:09:00Z"
weight = 4946
keywords = [ "ip", "packet" ]
aliases = [ "/questions/4946" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture network message](/questions/4946/how-to-capture-network-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4946-score" class="post-score" title="current number of votes">0</div><span id="post-4946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have some digital signage software that can send out a network message (0x02PON0x03) to switch on a TV. I want to be able to control the display without the signage software.</p><p>I have tried using netcat to no avail. Is there a method I can use wireshark to monitor and analyze the message sent form the signage software so I can duplicate it?</p><p>Any help will be gratefully received.</p><p>Cheers dan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '11, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/3eff599f14431ca6972003fc6fed339a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djhayman&#39;s gravatar image" /><p><span>djhayman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djhayman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jul '11, 17:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-4946" class="comments-container"></div><div id="comment-tools-4946" class="comment-tools"></div><div class="clear"></div><div id="comment-4946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4947"></span>

<div id="answer-container-4947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4947-score" class="post-score" title="current number of votes">1</div><span id="post-4947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, you need to find a way to capture the packet containing the message when it is sent from the original software. This can be done by using a switch with a SPAN port feature or with a hub if you have one. Connect TV and the system with the original software to it, and (if you're not using a hub) configure the switch to copy the data of the software to another port where you connect a PC running Wireshark. Capture wile the software sends the code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '11, 17:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4947" class="comments-container"></div><div id="comment-tools-4947" class="comment-tools"></div><div class="clear"></div><div id="comment-4947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

