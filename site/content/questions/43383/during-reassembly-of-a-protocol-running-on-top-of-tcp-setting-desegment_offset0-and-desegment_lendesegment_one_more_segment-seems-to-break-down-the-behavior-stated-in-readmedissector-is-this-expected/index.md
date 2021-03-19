+++
type = "question"
title = "During reassembly of a protocol running on top of TCP, setting desegment_offset=0 and desegment_len=DESEGMENT_ONE_MORE_SEGMENT seems to break down the behavior stated in README.dissector. Is this expected?"
description = '''I am writing a dissector for a custom protocol running on TCP. A single TCP packet can contain multiple PDUs for this protocol, and PDUs can be split between TCP packets. It is difficult to distinguish between cases where a protocol requires more data from the TCP stream to continue dissection, and ...'''
date = "2015-06-19T12:17:00Z"
lastmod = "2015-06-19T12:17:00Z"
weight = 43383
keywords = [ "reassembly", "dissector", "desegment", "tcp" ]
aliases = [ "/questions/43383" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [During reassembly of a protocol running on top of TCP, setting desegment\_offset=0 and desegment\_len=DESEGMENT\_ONE\_MORE\_SEGMENT seems to break down the behavior stated in README.dissector. Is this expected?](/questions/43383/during-reassembly-of-a-protocol-running-on-top-of-tcp-setting-desegment_offset0-and-desegment_lendesegment_one_more_segment-seems-to-break-down-the-behavior-stated-in-readmedissector-is-this-expected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43383-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a dissector for a custom protocol running on TCP. A single TCP packet can contain multiple PDUs for this protocol, and PDUs can be split between TCP packets. It is difficult to distinguish between cases where a protocol requires more data from the TCP stream to continue dissection, and when there is bad data in the protocol. I am trying to solve that by grabbing up to N packets (by setting desegment offset=0; desegment len=DESEGMENT ONE MORE SEGMENT;return; to get the next packet each time) if my dissector can't make sense of what is in the current buffer. Once it's over N packets, I assume that the first packet is bad and drop it from the buffer by setting desegment offset = length of first packet; desegment len = DESEGMENT ONE MORE SEGMENT; return;.</p><p>According to README.dissector, this should give me the tvb starting from the second packet up to packet N+1. However, I get a tvb starting from the original first packet (that was supposed to be dropped from the buffer), up to N+1.</p><p>Does anyone know why this behavior is happening, and what can be done to make it work like described in the README.dissector?</p></div><div id="question-tags" class="tags-container tags">reassembly dissector desegment tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '15, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/64fb35b42054028a8ada9479b24d6d25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oleks&#39;s gravatar image" /><p>oleks<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oleks has no accepted answers">0%</span></p></div></div><div id="comments-container-43383" class="comments-container"></div><div id="comment-tools-43383" class="comment-tools"></div><div class="clear"></div><div id="comment-43383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

