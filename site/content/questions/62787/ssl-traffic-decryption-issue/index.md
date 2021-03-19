+++
type = "question"
title = "SSL traffic decryption issue"
description = '''Hello Sharkers :D Some time we need to investigate SSL traffic on some servers, we do have the SSL certificate for that server but the issue is after trying to decrypt the captured PCAP we are not able to decrypt it. Little bit of research we found that SSL certificate uses Diffi-Helman which couldn...'''
date = "2017-07-14T14:51:00Z"
lastmod = "2017-07-15T09:35:00Z"
weight = 62787
keywords = [ "ssl" ]
aliases = [ "/questions/62787" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL traffic decryption issue](/questions/62787/ssl-traffic-decryption-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62787-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Sharkers :D</p><p>Some time we need to investigate SSL traffic on some servers, we do have the SSL certificate for that server but the issue is after trying to decrypt the captured PCAP we are not able to decrypt it.</p><p>Little bit of research we found that SSL certificate uses Diffi-Helman which couldn't be decrypted with the SSL Cert.</p><p>Since we are the owner of the servers, is there anyway to capture the traffic and decrypt it or even to capture it as HTTP traffic from the server itself?</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '17, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/5e43c2654392b1f09e1104282082684a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rami&#39;s gravatar image" /><p>rami<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rami has no accepted answers">0%</span></p></div></div><div id="comments-container-62787" class="comments-container"></div><div id="comment-tools-62787" class="comment-tools"></div><div class="clear"></div><div id="comment-62787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62805"></span>

<div id="answer-container-62805" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62805-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you own the server, these are your options for SSL/TLS decryption:</p><ul><li>Force use of a cipher suite which uses the RSA key exchange. Disadvantage: loses the forward secrecy property which would be provided by a Diffie-Hellman key exchange.</li><li>Tap the keys from the server process. If you have a webserver using the OpenSSL cryptographic library (e.g. nginx or Apache), then see <a href="https://security.stackexchange.com/q/80158/2630">this post</a> for an approach using a debugger or a interposing library.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '17, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-62805" class="comments-container"></div><div id="comment-tools-62805" class="comment-tools"></div><div class="clear"></div><div id="comment-62805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

