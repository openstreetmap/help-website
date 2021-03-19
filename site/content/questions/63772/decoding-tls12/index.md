+++
type = "question"
title = "Decoding tls1.2"
description = '''I am not seeing any decoded application data.  I am running wireshark 2.4 on the web server box, I have the private key in .pem format I have the server private key listed in the RSA keys list I have the port specified as start_tls and the protocol as http. The traffic comes in on https://servername...'''
date = "2017-10-09T13:03:00Z"
lastmod = "2017-10-14T10:52:00Z"
weight = 63772
keywords = [ "ssl", "tlsv1.2" ]
aliases = [ "/questions/63772" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Decoding tls1.2](/questions/63772/decoding-tls12)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63772-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am not seeing any decoded application data.</p><p>I am running wireshark 2.4 on the web server box, I have the private key in .pem format</p><p>I have the server private key listed in the RSA keys list</p><p>I have the port specified as start_tls and the protocol as http.</p><p>The traffic comes in on <a href="https://servername:4993">https://servername:4993</a></p><p>Is there anything else I need to specify in the rsa keys list or ???</p><p>thanks ron</p></div><div id="question-tags" class="tags-container tags">ssl tlsv1.2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '17, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/f562b6f68b80628bc62bc5acb4af3cd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ronrrm&#39;s gravatar image" /><p>ronrrm<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ronrrm has no accepted answers">0%</span></p></div></div><div id="comments-container-63772" class="comments-container"></div><div id="comment-tools-63772" class="comment-tools"></div><div class="clear"></div><div id="comment-63772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63900"></span>

<div id="answer-container-63900" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63900-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The port number in the RSA keys dialog is actually ignored since Wireshark 2.2, at least for matching the private key file.</p><p>You probably run into a TLS session which uses a (EC)DHE cipher suite instead of one based on the RSA key exchange. Such sessions cannot be decrypted using the RSA private key file, look for the keylog file (SSLKEYLOGFILE) approach instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '17, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-63900" class="comments-container"></div><div id="comment-tools-63900" class="comment-tools"></div><div class="clear"></div><div id="comment-63900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63785"></span>

<div id="answer-container-63785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63785-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Presuming that the traffic is simply https on port 4993, try replacing the start_tls entry with 4993.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '17, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63785" class="comments-container"><span id="63796"></span><div id="comment-63796" class="comment"><div id="post-63796-score" class="comment-score"></div><div class="comment-text"><p>Did that, same results. Tried 443, 4993, start_tls...Same results</p></div><div id="comment-63796-info" class="comment-info"><span class="comment-age">(10 Oct '17, 15:52)</span> ronrrm</div></div><span id="63801"></span><div id="comment-63801" class="comment"><div id="post-63801-score" class="comment-score"></div><div class="comment-text"><p>We need to see the contents of the SSL debug log. In the SSL preferences configure a debug log file and then amend your question with the contents of the log file.</p></div><div id="comment-63801-info" class="comment-info"><span class="comment-age">(11 Oct '17, 01:46)</span> grahamb ♦</div></div></div><div id="comment-tools-63785" class="comment-tools"></div><div class="clear"></div><div id="comment-63785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

