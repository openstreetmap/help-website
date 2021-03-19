+++
type = "question"
title = "TLS handshake appears to fail after Encrypted Handshake Message."
description = '''I have a customer who is trying to establish a TLS connection to my server. They have loaded my certificates and the certificate exchange appears to be working properly. However, their client does not send data after the server has ACKed the clients Encrypted Handshake Message. Link to pcap added. l...'''
date = "2016-09-13T11:35:00Z"
lastmod = "2016-09-13T15:26:00Z"
weight = 55529
keywords = [ "tls", "ssl", "handshake" ]
aliases = [ "/questions/55529" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TLS handshake appears to fail after Encrypted Handshake Message.](/questions/55529/tls-handshake-appears-to-fail-after-encrypted-handshake-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55529-score" class="post-score" title="current number of votes">-1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a customer who is trying to establish a TLS connection to my server. They have loaded my certificates and the certificate exchange appears to be working properly. However, their client does not send data after the server has ACKed the clients Encrypted Handshake Message.</p><p>Link to pcap added. <a href="https://www.cloudshark.org/captures/dac8fabf572a">link text</a> <img src="https://osqa-ask.wireshark.org/upfiles/TLS-Handshake-Screenshot.jpg" alt="alt text" /></p><p>Anyone have any ideas why the client wouldn't be sending application data?</p></div><div id="question-tags" class="tags-container tags">tls ssl handshake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '16, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/61166878288faccd5b649f26d44ff22c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RFB&#39;s gravatar image" /><p>RFB<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RFB has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 14 Sep '16, 09:55</p></div></div><div id="comments-container-55529" class="comments-container"><span id="55537"></span><div id="comment-55537" class="comment"><div id="post-55537-score" class="comment-score"></div><div class="comment-text"><p>For better help you should include a packet capture file, not just a screenshot.</p></div><div id="comment-55537-info" class="comment-info"><span class="comment-age">(13 Sep '16, 15:27)</span> Lekensteyn</div></div><span id="55561"></span><div id="comment-55561" class="comment"><div id="post-55561-score" class="comment-score"></div><div class="comment-text"><p>Added link to pcap in original post.</p></div><div id="comment-55561-info" class="comment-info"><span class="comment-age">(14 Sep '16, 14:30)</span> RFB</div></div><span id="55584"></span><div id="comment-55584" class="comment"><div id="post-55584-score" class="comment-score"></div><div class="comment-text"><p>The pcap strengthens my analysis below, SSLv2 was killed long time ago. Your client should not send a SSLv2-compatible hello message. Btw, the Certificate message contains the hostname of your server which is not anonimized.</p></div><div id="comment-55584-info" class="comment-info"><span class="comment-age">(16 Sep '16, 01:34)</span> Lekensteyn</div></div></div><div id="comment-tools-55529" class="comment-tools"></div><div class="clear"></div><div id="comment-55529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55536"></span>

<div id="answer-container-55536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55536-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at the source address of the TCP RST, you will notice that it matches the IP address of the server (based on the source of the Server Hello).</p><p>There are multiple strange things about your report:</p><ul><li>SSLv2 is reported in the Client Hello.</li><li>Encrypted Handshake Message is reported by the client after the ChangeCipherSpec. I would expect a Finish message here.</li><li>The server did not have the chance to send a ServerHelloDone after the Certificate (see <a href="https://tools.ietf.org/html/rfc5246#page-36">RFC 5246</a> for the expected flow for a full handshake).</li></ul><p>Check:</p><ul><li>Are you using the latest Wireshark version? Currently 2.0.6 or 2.2.0 are considered recent.</li><li>Check the access/error logs of your webserver.</li><li>Check for possible compatibility issues of your client. (Why is it using SSLv2 for example?)</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '16, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-55536" class="comments-container"></div><div id="comment-tools-55536" class="comment-tools"></div><div class="clear"></div><div id="comment-55536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

