+++
type = "question"
title = "VPN connection"
description = '''Hi, I have Wireshark monitoring a TAP-Win32 Adapter connection installed with Cyberghost but the traffic doesn&#x27;t show up as encrypted. Is this normal? And how do I check if traffic is encrypted through VPN. This happens with ProXPN also. Many thanks'''
date = "2010-12-12T23:55:00Z"
lastmod = "2010-12-13T05:30:00Z"
weight = 1324
keywords = [ "connection", "vpn" ]
aliases = [ "/questions/1324" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VPN connection](/questions/1324/vpn-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1324-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have Wireshark monitoring a TAP-Win32 Adapter connection installed with Cyberghost but the traffic doesn't show up as encrypted. Is this normal? And how do I check if traffic is encrypted through VPN. This happens with ProXPN also.</p><p>Many thanks</p></div><div id="question-tags" class="tags-container tags">connection vpn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '10, 23:55</strong></p><img src="https://secure.gravatar.com/avatar/d2b2981122cbe6dc05d3af8332fe1548?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fh67&#39;s gravatar image" /><p>fh67<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fh67 has no accepted answers">0%</span></p></div></div><div id="comments-container-1324" class="comments-container"></div><div id="comment-tools-1324" class="comment-tools"></div><div class="clear"></div><div id="comment-1324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1325"></span>

<div id="answer-container-1325" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1325-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that is normal. If you capture on a virtual adapter that is used for a VPN connection you will see unencrypted packets in and out. The encryption happens when the virtual TAP adapter passes the data over to your physical network card. To see the encrypted traffic you need to capture on your "real" network card (wired or wireless) and you should see lots of encrypted packets.</p><p>In fact you can go and capture both with two Wireshark instances at the same time and then see how the unencrypted packets on the TAP adapter correlate to the physical adapter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '10, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Dec '10, 05:31</p></div></div><div id="comments-container-1325" class="comments-container"></div><div id="comment-tools-1325" class="comment-tools"></div><div class="clear"></div><div id="comment-1325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

