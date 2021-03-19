+++
type = "question"
title = "Trouble getting capture to dissect TLS Handshake in Ubuntu"
description = '''I&#x27;m trying to look at the TLS handshake messages for a session, and I am getting different results when I open the capture in Wireshark 2.2.5 in Windows 10 vs Ubuntu 16.04. In Windows it identifies the protocol as TLSv1.2 and shows the Client Hello and Server Hello messages. In Ubuntu it just shows ...'''
date = "2017-04-10T16:36:00Z"
lastmod = "2017-04-12T14:12:00Z"
weight = 60722
keywords = [ "tls", "ubuntu" ]
aliases = [ "/questions/60722" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Trouble getting capture to dissect TLS Handshake in Ubuntu](/questions/60722/trouble-getting-capture-to-dissect-tls-handshake-in-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60722-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to look at the TLS handshake messages for a session, and I am getting different results when I open the capture in Wireshark 2.2.5 in Windows 10 vs Ubuntu 16.04. In Windows it identifies the protocol as TLSv1.2 and shows the Client Hello and Server Hello messages. In Ubuntu it just shows the Client Hello, and then the rest of the messages are left uninterpreted as just SSL.<br />
</p><p>I installed Wireshark from <a href="http://ppa.launchpad.net/wireshark-dev/stable/ubuntu">http://ppa.launchpad.net/wireshark-dev/stable/ubuntu</a></p><p>What am I missing in my Linux install that would let it interpret the Server Hello message?</p><p>Thank you so much! Screenshots of the capture are below.</p><p>Capture From Windows 10: <img src="https://osqa-ask.wireshark.org/upfiles/CaptureInWindows_w8kgvKS.png" alt="Windows Capture" /></p><p>Capture from Ubuntu 16.04 <img src="https://osqa-ask.wireshark.org/upfiles/CaptureInUbuntu2_FfrtDOV.png" alt="Ubuntu Capture" /></p></div><div id="question-tags" class="tags-container tags">tls ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '17, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/ff8b2177f8c51bfeb30fecef96efd673?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DevinCallahan&#39;s gravatar image" /><p>DevinCallahan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DevinCallahan has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-60722" class="comments-container"><span id="60727"></span><div id="comment-60727" class="comment"><div id="post-60727-score" class="comment-score"></div><div class="comment-text"><p>On Ubuntu it seems like reassembly is not working, is it the same Wireshark version on both systems? if so compare your preference settings.</p></div><div id="comment-60727-info" class="comment-info"><span class="comment-age">(11 Apr '17, 01:54)</span> Anders ♦</div></div></div><div id="comment-tools-60722" class="comment-tools"></div><div class="clear"></div><div id="comment-60722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60785"></span>

<div id="answer-container-60785" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60785-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Given that the protocol is just "SSL" (rather than a more specific version like "TLSv1.2") and given that some packets are reported as "Continuation Data", I think that you have disabled TCP reassembly.</p><p>To enable TCP reassembly, right-click on the TCP layer, select <em>Protocol Preferences</em> and check the <em>Allow subdissector to reassemble TCP streams</em> option.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Spectacle.cl1841.png" alt="screenshot" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></img></div></div><div id="comments-container-60785" class="comments-container"><span id="60786"></span><div id="comment-60786" class="comment"><div id="post-60786-score" class="comment-score"></div><div class="comment-text"><p>That was it! Thank you so much!</p></div><div id="comment-60786-info" class="comment-info"><span class="comment-age">(12 Apr '17, 14:16)</span> DevinCallahan</div></div></div><div id="comment-tools-60785" class="comment-tools"></div><div class="clear"></div><div id="comment-60785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

