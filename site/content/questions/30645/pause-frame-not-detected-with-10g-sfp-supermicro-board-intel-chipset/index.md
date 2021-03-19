+++
type = "question"
title = "Pause frame not detected with 10G SFP+ SuperMicro Board (INTEL chipset)"
description = '''Hello, When I send a pause frame on my 10G SFP+ SuperMicro Board (INTEL chipset), I cannot see the pause frame detected on wireshark. The Linux driver is ixgbe. When I send a pause frame on my 10G CX4 board, I CAN See the pause frame detected on wireshark. Can you tell me why I cannot see the pause ...'''
date = "2014-03-10T06:00:00Z"
lastmod = "2014-03-10T10:34:00Z"
weight = 30645
keywords = [ "pause" ]
aliases = [ "/questions/30645" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Pause frame not detected with 10G SFP+ SuperMicro Board (INTEL chipset)](/questions/30645/pause-frame-not-detected-with-10g-sfp-supermicro-board-intel-chipset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30645-score" class="post-score" title="current number of votes">0</div><span id="post-30645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>When I send a pause frame on my 10G SFP+ SuperMicro Board (INTEL chipset), I cannot see the pause frame detected on wireshark. The Linux driver is ixgbe.</p><p>When I send a pause frame on my 10G CX4 board, I CAN See the pause frame detected on wireshark.</p><p>Can you tell me why I cannot see the pause frame with the 10G SFP+ SuperMicro Board on wireshark.</p><p>Thank you for help. Serge</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pause" rel="tag" title="see questions tagged &#39;pause&#39;">pause</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '14, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/89b753c8ddca3e9415953ab5725d6a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="serge&#39;s gravatar image" /><p><span>serge</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="serge has no accepted answers">0%</span></p></div></div><div id="comments-container-30645" class="comments-container"></div><div id="comment-tools-30645" class="comment-tools"></div><div class="clear"></div><div id="comment-30645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30658"></span>

<div id="answer-container-30658" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30658-score" class="post-score" title="current number of votes">0</div><span id="post-30658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you know if the pause frame even comes up through from the hardware? It might as well be handled in the chipset. Check the relevant documentation of that item.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '14, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-30658" class="comments-container"><span id="30659"></span><div id="comment-30659" class="comment"><div id="post-30659-score" class="comment-score"></div><div class="comment-text"><p>Hello Jaap,</p><p>Yes the frame is coming to the board. If I just change the Opcode : 8808 by 0888 for example, the frame is detected on Wireshark as a undefined frame.</p><p>Thanks for help. Serge</p></div><div id="comment-30659-info" class="comment-info"><span class="comment-age">(10 Mar '14, 10:34)</span> <span class="comment-user userinfo">serge</span></div></div></div><div id="comment-tools-30658" class="comment-tools"></div><div class="clear"></div><div id="comment-30658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

