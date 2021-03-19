+++
type = "question"
title = "Server sends a strange ACK during three-way handshake"
description = '''The service in question is FTP_DL with proxy between client and server. The problem is that proxy sends 2 SYNs with different sequence numbers over the same port and from same IP address. To the first SYN server responds with SYN,ACKs, but to the second it responds with ACK with unexpected seq/ack v...'''
date = "2011-10-12T09:00:00Z"
lastmod = "2011-10-12T09:00:00Z"
weight = 6871
keywords = [ "ack", "syn", "tcp", "sequence" ]
aliases = [ "/questions/6871" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Server sends a strange ACK during three-way handshake](/questions/6871/server-sends-a-strange-ack-during-three-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6871-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The service in question is <strong>FTP_DL with proxy</strong> between client and server. The problem is that proxy sends 2 SYNs with different sequence numbers over the same port and from same IP address. To the first SYN server responds with SYN,ACKs, but to the second it responds with ACK with unexpected seq/ack values. After receiving unexpected ACK, proxy RSTs the connection. <strong>Can anyone tell me, why does the server send such ACK?</strong></p><p>Here are the details:</p><p>Client sends a SYN (sequence number = c1ef8b59) in order to establish the TCP connection with proxy. Proxy sends a SYN (seq=fa23e9d9) to the server in order to establish a TCP connection with the server. Server responds with multiple SYN,ACKs (seq=9ad421d5, ack=fa23e9da). None of the SYN,ACKs arrive to the client because proxy RSTs the connection to client.</p><p>After RST client sends a new SYN (seq=c1ef8b59 - same as the last time). Proxy sends a new SYN to server over the same port with the same IP, but different sequence number = 5625cb85. The server responds with ACK (seq=9ad421d6, ack=fa23e9da). Proxy sends RST (seq=fa23e9da, ack= broken TCP, <em>ack field is non zero while ACK flag is not set</em>).</p><p>Thnx</p></div><div id="question-tags" class="tags-container tags">ack syn tcp sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '11, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/7820f7b9638e63d42e5c6fb4de7262d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brklp&#39;s gravatar image" /><p>brklp<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brklp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 21:28</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-6871" class="comments-container"></div><div id="comment-tools-6871" class="comment-tools"></div><div class="clear"></div><div id="comment-6871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

