+++
type = "question"
title = "On Windows7 I can not decode KRB5 AS Response in an active capture"
description = '''I am attempting to capture a security exchange between a device and a provisioning server. Part of the exchange involves requesting and receiving a Kerberos key from a KDC. In the live capture I can see the AS REQ ( key request from the device to the KDC ), but the AS RES (response from the KDC) sho...'''
date = "2011-02-18T16:28:00Z"
lastmod = "2011-03-23T08:57:00Z"
weight = 2421
keywords = [ "windows7", "kerberos" ]
aliases = [ "/questions/2421" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [On Windows7 I can not decode KRB5 AS Response in an active capture](/questions/2421/on-windows7-i-can-not-decode-krb5-as-response-in-an-active-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2421-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to capture a security exchange between a device and a provisioning server. Part of the exchange involves requesting and receiving a Kerberos key from a KDC. In the live capture I can see the AS REQ ( key request from the device to the KDC ), but the AS RES (response from the KDC) show as a UDP packet. The KDC responds on a random port so this may be causing the issue, but previously this was not a problem. I can decode the packet after the trace has run using the dissector, but this will not allow for automated parsing of the capture file.</p><p>This issue only occurs using Windows 7. I'm using the latest release of Wireshark (32 bit) and the associated version of WinPcap.</p><p>Thanks, m</p></div><div id="question-tags" class="tags-container tags">windows7 kerberos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '11, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/6958ddd348a3f0374d82667f9aaf3575?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matclab&#39;s gravatar image" /><p>matclab<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matclab has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 23 Mar '11, 08:59</p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span></p></div></div><div id="comments-container-2421" class="comments-container"><span id="2998"></span><div id="comment-2998" class="comment"><div id="post-2998-score" class="comment-score"></div><div class="comment-text"><p>Latest release? Which specific version of Wireshark are you using? Note that there are latest stable, development and automated releases, so "latest" is a bit ambiguous. I'll assume you were using the latest stable release at the time you posted your query, but there may have been fixes in the other releases that were not in the stable release. You can download the latest stable and development releases from http://www.wireshark.org/download.html, and the latest automated release from https://www.wireshark.org/download/automated/win32/. Maybe one of them will work for you?</p></div><div id="comment-2998-info" class="comment-info"><span class="comment-age">(21 Mar '11, 20:16)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-2421" class="comment-tools"></div><div class="clear"></div><div id="comment-2421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3043"></span>

<div id="answer-container-3043" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3043-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I am surprised that you mention an AS Response coming in over UDP.</p><p>Usually Win 7 sends KRB requests over TCP, and the server sends the responds within the same session. When the client sends the request over UDP the response should be a UDP packet to the source port seen in the request.</p><p>Windows 2000 or XP attempt to obtain the Kerberos ticket via UDP. The server response may be fragmented. The threshold is controlled through the registry parameter: In HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters you find the parameter MaxPacketSize as a DWORD .</p><p>Do you see any Kerberos error messages? Filter for <strong>kerberos.msg.type == 30</strong></p><p>Is there a active device in the network path that could mangle your TCP sessions, like a load balancer, bandwidth enforcer, ACE module etc?</p><p>Can you post a screenshot / text dump of the packets?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Mar '11, 09:12</p></div></div><div id="comments-container-3043" class="comments-container"></div><div id="comment-tools-3043" class="comment-tools"></div><div class="clear"></div><div id="comment-3043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

