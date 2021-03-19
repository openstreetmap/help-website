+++
type = "question"
title = "SSL Decrypt works on my station but not those captured elsewhere on others"
description = '''I&#x27;ve successfully set up ssl decrypt to work on my systems sessions with an ssl server by getting the private key. Works! I have traces of other stations traffic that I need to analyze. I can&#x27;t get those other stations traffic to decode. What&#x27;s the unknown I&#x27;m missing?  Thanks! '''
date = "2013-12-12T11:56:00Z"
lastmod = "2013-12-13T03:11:00Z"
weight = 28063
keywords = [ "ssl" ]
aliases = [ "/questions/28063" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decrypt works on my station but not those captured elsewhere on others](/questions/28063/ssl-decrypt-works-on-my-station-but-not-those-captured-elsewhere-on-others)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28063-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've successfully set up ssl decrypt to work on my systems sessions with an ssl server by getting the private key. Works!</p><p>I have traces of other stations traffic that I need to analyze. I can't get those other stations traffic to decode. What's the unknown I'm missing?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '13, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/0a57afcbb8cd956e0f42b1bd1a2c3783?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetman007&#39;s gravatar image" /><p>packetman007<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetman007 has no accepted answers">0%</span></p></div></div><div id="comments-container-28063" class="comments-container"></div><div id="comment-tools-28063" class="comment-tools"></div><div class="clear"></div><div id="comment-28063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28071"></span>

<div id="answer-container-28071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28071-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>For SSL decryption to work, there are three main conditions that need to be fulfilled:</p><ol><li>You must have the private key matching the certificate used in the session. And it needs to be in the proper format for wireshark to read. As I assume the other stations go to the same server, this condition is fulfilled.</li><li>You need to have the full SSL handshake in the tracefile (so including the Certificate and the ClientKeyExchange messages). When you see ServerHello immediately followed by a ChangeCipherspec, then you have a reused SSL session and you can not decrypt it in Wireshark (unless the full handhshake is in the same tracefile).</li><li>The client and server must have chosen a non-diffie-hellman key exchange. When DH is used, the master secret is encrypted with dynamically setup keys instead of the public key from the certificate and can therefor not be decrypted by wireshark. And without the cleartext master secret for the session, wireshark can not decrypt the session. A DH key exchange can be recognized by an extra "ServerKeyExchange" message in the SSL handshake.</li></ol><p>What do your SSL handshakes look like?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-28071" class="comments-container"></div><div id="comment-tools-28071" class="comment-tools"></div><div class="clear"></div><div id="comment-28071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

