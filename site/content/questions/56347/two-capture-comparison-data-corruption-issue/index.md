+++
type = "question"
title = "Two capture comparison | Data corruption issue"
description = '''Hello, I have an issue in the network. Files are getting sometimes corrupted while being copied using SMB over WAN link. I did a packet capture on both ends and now need a tool to compare packets/segments payload/body/data to find which exact packet is being corrupted/changed.  Is there any tool whi...'''
date = "2016-10-13T12:26:00Z"
lastmod = "2016-10-13T12:45:00Z"
weight = 56347
keywords = [ "comparison" ]
aliases = [ "/questions/56347" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Two capture comparison | Data corruption issue](/questions/56347/two-capture-comparison-data-corruption-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56347-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have an issue in the network. Files are getting sometimes corrupted while being copied using SMB over WAN link. I did a packet capture on both ends and now need a tool to compare packets/segments payload/body/data to find which exact packet is being corrupted/changed.</p><p>Is there any tool which will allow to compare the payloads of sent and received packets? Checking checksums on the receiver is not welcomed because I think the packets are being corrupted in the network and their checksums are being calculated after that. Thanks.</p><p>Handshake.</p></div><div id="question-tags" class="tags-container tags">comparison</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '16, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/d693072a1921dc46b6a19a4d82f64ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="handshake&#39;s gravatar image" /><p>handshake<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="handshake has no accepted answers">0%</span></p></div></div><div id="comments-container-56347" class="comments-container"></div><div id="comment-tools-56347" class="comment-tools"></div><div class="clear"></div><div id="comment-56347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56350"></span>

<div id="answer-container-56350" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56350-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm sure better tools exist, but you may use <code>tshark</code> with an appropriate filter to dump just the <code>tcp.seq</code> and <code>tcp.checksum</code> of the necessary direction of the SMB session in question from both captures to text files and then use <code>diff</code> to compare the text files. The TCP checksum of the corrupt packet as it has arrived to the destination will probably be correct but it will be different from the one at the source.</p><p><code>tshark -r &lt;file_name&gt; -Y "tcp.stream == n and ip.dst == m.m.m.m" -T fields -e tcp.seq -e tcp.checksum</code></p><p>This assumes that no packets have been lost and retransmitted, though. If they have, you would have to use <code>sort -u</code> before running the <code>diff</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '16, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56350" class="comments-container"></div><div id="comment-tools-56350" class="comment-tools"></div><div class="clear"></div><div id="comment-56350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

