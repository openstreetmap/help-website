+++
type = "question"
title = "Frame Check Sequence  Incorrect during  Port fowarding to Virtual Machine"
description = '''I am trying to go from my web address aseanenglish.info to a virtual machine. I have Ubuntu 16.04 as a guest in Virtual Box. I have set up port forwarding on my router so that traffic on ports 1935 and 5080 get directed to this virtual machine. I have also tried setting up port forwarding from the r...'''
date = "2016-09-27T06:54:00Z"
lastmod = "2016-09-29T03:15:00Z"
weight = 55908
keywords = [ "frame", "check" ]
aliases = [ "/questions/55908" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Frame Check Sequence Incorrect during Port fowarding to Virtual Machine](/questions/55908/frame-check-sequence-incorrect-during-port-fowarding-to-virtual-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55908-score" class="post-score" title="current number of votes">0</div><span id="post-55908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to go from my web address aseanenglish.info to a virtual machine.</p><p>I have Ubuntu 16.04 as a guest in Virtual Box.</p><p>I have set up port forwarding on my router so that traffic on ports 1935 and 5080 get directed to this virtual machine.</p><p>I have also tried setting up port forwarding from the router to the host and configuring port forwarding in Virtual Box so that my guest virtual machine sees the traffic on 1935 and 5080.</p><p>I receive the Frame Check Sequence Incorrect error in my capture on the host computer.</p><p>But what does it mean and what causes it ?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_DV48cCH.PNG" alt="Wireshark from Windows Host" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-check" rel="tag" title="see questions tagged &#39;check&#39;">check</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '16, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/6542e6eefb50912d4c7d9d15d38bd81c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kam2700&#39;s gravatar image" /><p><span>kam2700</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kam2700 has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Sep '16, 06:56</strong> </span></p></div></div><div id="comments-container-55908" class="comments-container"></div><div id="comment-tools-55908" class="comment-tools"></div><div class="clear"></div><div id="comment-55908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="55982"></span>

<div id="answer-container-55982" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55982-score" class="post-score" title="current number of votes">0</div><span id="post-55982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kam2700 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It turns out the problem was when port forwarding from the router I had to enable <strong>TCP/UDP</strong> then it worked.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '16, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/6542e6eefb50912d4c7d9d15d38bd81c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kam2700&#39;s gravatar image" /><p><span>kam2700</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kam2700 has one accepted answer">100%</span></p></div></div><div id="comments-container-55982" class="comments-container"></div><div id="comment-tools-55982" class="comment-tools"></div><div class="clear"></div><div id="comment-55982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55910"></span>

<div id="answer-container-55910" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55910-score" class="post-score" title="current number of votes">0</div><span id="post-55910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think this is a capture problem - I've seen packets like this when capturing VMs on the host, and they're not really being sent to the network. No idea what causes those.</p><p>What I would recommend is to capture the traffic with a device that isn't involved in the communication (dedicated capture laptop/PC) via TAP or SPAN port. Otherwise your readings are incorrect.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '16, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-55910" class="comments-container"></div><div id="comment-tools-55910" class="comment-tools"></div><div class="clear"></div><div id="comment-55910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55912"></span>

<div id="answer-container-55912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55912-score" class="post-score" title="current number of votes">0</div><span id="post-55912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Big chance the capture engine gets confused by real vs virtualised network interface capabilities, and likely assumes the FCS is there while it's not. Try modifying the Ethernet dissector preferences (disable: Assume packets has FCS and Validate the Ethernet checksum if possible).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '16, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55912" class="comments-container"></div><div id="comment-tools-55912" class="comment-tools"></div><div class="clear"></div><div id="comment-55912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

