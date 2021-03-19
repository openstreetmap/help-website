+++
type = "question"
title = "TCP reassembly: What happens when retransmissions occur?"
description = '''Hello there, I am writing a LUA dissector for an application protocol. The protocol splits data over multiple TCP segments. To reassemble the segments I set pinfo.desegment_len to length of the complete data minus current buffer length. Usually this works very well. However on cases where TCP segmen...'''
date = "2017-02-11T15:43:00Z"
lastmod = "2017-02-11T15:43:00Z"
weight = 59346
keywords = [ "lua", "dissector", "reassembly" ]
aliases = [ "/questions/59346" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP reassembly: What happens when retransmissions occur?](/questions/59346/tcp-reassembly-what-happens-when-retransmissions-occur)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59346-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there,</p><p>I am writing a LUA dissector for an application protocol. The protocol splits data over multiple TCP segments. To reassemble the segments I set pinfo.desegment_len to length of the complete data minus current buffer length. Usually this works very well.</p><p>However on cases where TCP segments are retransmitted (DUP Acks etc.), the TCP data segments are not reassembled. At least my dissector never receives the reassembled tvbuf object.</p><p>Is anyone aware of difficulties in TCP reassembly with out-of-order packets? (Retransmissions, DUP ACks etc?)</p></div><div id="question-tags" class="tags-container tags">lua dissector reassembly</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '17, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/05a89c5522316ab18baf9be9fba5b40d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niklas&#39;s gravatar image" /><p>niklas<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niklas has no accepted answers">0%</span></p></div></div><div id="comments-container-59346" class="comments-container"></div><div id="comment-tools-59346" class="comment-tools"></div><div class="clear"></div><div id="comment-59346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

