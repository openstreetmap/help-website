+++
type = "question"
title = "TLS finished packet renamed Encrypted handshake message?"
description = '''Hello, I need your help to confirm or not my analysis. I can&#x27;t see the &quot;finished&quot; packets in all my ssl/tls handshake. This packets is supposed to be send by each sides after the CCS packet as describe in the RFC 2246. The only packet sent immediately after the CCS message is an &quot;Encrypted handshake...'''
date = "2016-11-14T23:18:00Z"
lastmod = "2016-11-15T01:12:00Z"
weight = 57384
keywords = [ "tls", "ssl", "handshake" ]
aliases = [ "/questions/57384" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TLS finished packet renamed Encrypted handshake message?](/questions/57384/tls-finished-packet-renamed-encrypted-handshake-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57384-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I need your help to confirm or not my analysis. I can't see the "finished" packets in all my ssl/tls handshake. This packets is supposed to be send by each sides after the CCS packet as describe in the RFC 2246. The only packet sent immediately after the CCS message is an "Encrypted handshake message". Is it the finished packet?</p><p>For info I am using wireshark v 2.0.2. I have also tried with the latest.</p><p>Thank for your help:)<img src="https://osqa-ask.wireshark.org/upfiles/finished.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tls ssl handshake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '16, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/714579bafff5c0c85fc987d5f1d7b713?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="remyd59&#39;s gravatar image" /><p>remyd59<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="remyd59 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-57384" class="comments-container"></div><div id="comment-tools-57384" class="comment-tools"></div><div class="clear"></div><div id="comment-57384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57385"></span>

<div id="answer-container-57385" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57385-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, the "finished" handshake message comes right after the ChangeCipherSpec. The CCS means that from that point onward, all packets will be encrypted with the negotiated session keys. If you decrypt the SSL traffic, you will see the Finished handshake messages unencrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '16, 01:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-57385" class="comments-container"><span id="57386"></span><div id="comment-57386" class="comment"><div id="post-57386-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your quick feedback.</p></div><div id="comment-57386-info" class="comment-info"><span class="comment-age">(15 Nov '16, 02:08)</span> remyd59</div></div></div><div id="comment-tools-57385" class="comment-tools"></div><div class="clear"></div><div id="comment-57385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

