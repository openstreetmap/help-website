+++
type = "question"
title = "Can wireshark decrypted abbreviated TLS/SSL handshakes?"
description = '''In my particular case, there seem to be multiple abbreviated handshakes performed after the initial session creating full handshake, and these use multiple additional ports. Decryption is failing, and I am seeing &quot;mac failed&quot; errors in the ssl debug log. I&#x27;m wondering if this is caused by the abbrev...'''
date = "2013-06-11T03:14:00Z"
lastmod = "2013-06-11T04:07:00Z"
weight = 21911
keywords = [ "ssl", "abbreviated", "handshake" ]
aliases = [ "/questions/21911" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can wireshark decrypted abbreviated TLS/SSL handshakes?](/questions/21911/can-wireshark-decrypted-abbreviated-tlsssl-handshakes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21911-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my particular case, there seem to be multiple abbreviated handshakes performed after the initial session creating full handshake, and these use multiple additional ports. Decryption is failing, and I am seeing "mac failed" errors in the ssl debug log. I'm wondering if this is caused by the abbreviated handshakes? I can't really post the pcap as there's some sensitive info. in there.</p></div><div id="question-tags" class="tags-container tags">ssl abbreviated handshake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '13, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/40920813c79c306646f94e993af244da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AdamZSI&#39;s gravatar image" /><p>AdamZSI<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AdamZSI has no accepted answers">0%</span></p></div></div><div id="comments-container-21911" class="comments-container"></div><div id="comment-tools-21911" class="comment-tools"></div><div class="clear"></div><div id="comment-21911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21920"></span>

<div id="answer-container-21920" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21920-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the initial full SSL handshake is also in the tracefile and the sessions are indexed by a SSL SessionID, you should be able to decrypt the resumed sessions (with abbreviated handshakes) too. AFAIK, Wireshark does not (yet) support decryption of sessions that used a TLS session ticket to resume the session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21920" class="comments-container"><span id="21921"></span><div id="comment-21921" class="comment"><div id="post-21921-score" class="comment-score"></div><div class="comment-text"><p>Thank you, that's as I understood but good to get confirmation. I'll accept that as the answer, but as a quick follow up, what are the likely/possible reasons for "mac failed" errors? It seems like SOME http is decrypted successfully, but others not (I have a lot of "Continuation or non-HTTP traffic" and a lot of "Ignored or Unknown Record"). Any pointers?</p></div><div id="comment-21921-info" class="comment-info"><span class="comment-age">(11 Jun '13, 04:11)</span> AdamZSI</div></div><span id="21926"></span><div id="comment-21926" class="comment"><div id="post-21926-score" class="comment-score">1</div><div class="comment-text"><p>Do you have retransmissions or out-of-order packets in the sessions where decryption fails?</p></div><div id="comment-21926-info" class="comment-info"><span class="comment-age">(11 Jun '13, 08:23)</span> SYN-bit ♦♦</div></div><span id="21954"></span><div id="comment-21954" class="comment"><div id="post-21954-score" class="comment-score"></div><div class="comment-text"><p>Yes there are a fair number of [TCP Retransmission] and [TCP previous segment not captured] and [TCP Out of order]. Some from client, some from server. I think they're all after the abbreviated handshakes. Also getting some [TCP Dup Ack], don't know if that matters</p></div><div id="comment-21954-info" class="comment-info"><span class="comment-age">(11 Jun '13, 22:00)</span> AdamZSI</div></div></div><div id="comment-tools-21920" class="comment-tools"></div><div class="clear"></div><div id="comment-21920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

