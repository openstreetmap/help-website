+++
type = "question"
title = "Is this a correct connection buildup?"
description = '''Hi all, I setup the LwIP Stack on a microcontroller, buildup a connection to a PC, transmit some data and close the connection. Please see the screenshot below. The first connection seems to be correct (Frame 6 has the PSH and ACK flag) but when I reset the controller and try to buildup a connection...'''
date = "2012-10-05T05:04:00Z"
lastmod = "2012-10-05T05:04:00Z"
weight = 14730
keywords = [ "connection" ]
aliases = [ "/questions/14730" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is this a correct connection buildup?](/questions/14730/is-this-a-correct-connection-buildup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14730-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I setup the LwIP Stack on a microcontroller, buildup a connection to a PC, transmit some data and close the connection. Please see the screenshot below. The first connection seems to be correct (Frame 6 has the PSH and ACK flag) but when I reset the controller and try to buildup a connection in the same way as the first one I receive previous segment not captured. So is this still a correct connection buildup?</p><p><a href="http://tinypic.com/r/r8f1fm/6">Wireshark screenshot</a></p></div><div id="question-tags" class="tags-container tags">connection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '12, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/1a8f429484fa071196373e8e190f1bc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vic&#39;s gravatar image" /><p>Vic<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vic has no accepted answers">0%</span></p></div></div><div id="comments-container-14730" class="comments-container"><span id="14744"></span><div id="comment-14744" class="comment"><div id="post-14744-score" class="comment-score"></div><div class="comment-text"><p>Put the capture on <a href="http://www.cloudshark.org/">CloudShark</a>, so when can see/research it more easily.</p></div><div id="comment-14744-info" class="comment-info"><span class="comment-age">(06 Oct '12, 05:47)</span> Jaap ♦</div></div><span id="14767"></span><div id="comment-14767" class="comment"><div id="post-14767-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply. I uploaded the capture. Please see <a href="http://www.cloudshark.org/captures/f5459e28de9f">http://www.cloudshark.org/captures/f5459e28de9f</a></p></div><div id="comment-14767-info" class="comment-info"><span class="comment-age">(08 Oct '12, 00:54)</span> Vic</div></div><span id="14774"></span><div id="comment-14774" class="comment"><div id="post-14774-score" class="comment-score">1</div><div class="comment-text"><p>There's port reuse here, but Wireshark doesn't really pick up upon it. The warning seems to come from a (perceived) jump in sequence numbering.</p></div><div id="comment-14774-info" class="comment-info"><span class="comment-age">(08 Oct '12, 07:49)</span> Jaap ♦</div></div><span id="14807"></span><div id="comment-14807" class="comment"><div id="post-14807-score" class="comment-score"></div><div class="comment-text"><p>So the connection is correct buildup and closed? Just for my understanding, sorry I'm really new to the ethernet stuff.</p></div><div id="comment-14807-info" class="comment-info"><span class="comment-age">(09 Oct '12, 01:29)</span> Vic</div></div></div><div id="comment-tools-14730" class="comment-tools"></div><div class="clear"></div><div id="comment-14730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

