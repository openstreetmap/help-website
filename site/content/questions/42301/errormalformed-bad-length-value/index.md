+++
type = "question"
title = "[closed] Error/Malformed: Bad length value"
description = '''Hello,  I am trying to send UDP packets using socket programming in python. In my python code, i am packing the send information as  For UDP: udp_send = struct.pack(&#x27;!HHHH&#x27;, udpsourceport, udpdestport, udplen, udpchecksum) where calculated udplen = 380 and udpchecksum = 0. For IP: ip_send = struct.p...'''
date = "2015-05-11T06:52:00Z"
lastmod = "2015-05-11T06:52:00Z"
weight = 42301
keywords = [ "python", "udp", "ipv4", "malformed", "socket" ]
aliases = [ "/questions/42301" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Error/Malformed: Bad length value](/questions/42301/errormalformed-bad-length-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42301-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am trying to send UDP packets using socket programming in python. In my python code, i am packing the send information as</p><p><strong>For UDP:</strong></p><p>udp_send = struct.pack('!HHHH', udpsourceport, udpdestport, udplen, udpchecksum) where calculated udplen = 380 and udpchecksum = 0.</p><p><strong>For IP:</strong></p><p>ip_send = struct.pack('!BBHHHBBH4s4s', versionIHL, 0, totalLength, ID, flags, 225, 17, 0, sourceAddress, destinationAddress) where calculated totallength = 400</p><p>When i check this output in wireshark i get the output with IP total length = 60 and udp error as <img src="https://osqa-ask.wireshark.org/upfiles/ipv4.PNG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_xnitumm.PNG" alt="alt text" /></p><p>Is it the correct way to send a udp packet ? Are there any changes to be done in Windows or in Wireshark ? Please help me to solve this problem. :-(</p></div><div id="question-tags" class="tags-container tags">python udp ipv4 malformed socket</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '15, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/85652400f627dbc4dbd4d0d09e03ecee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Praju&#39;s gravatar image" /><p>Praju<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Praju has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>closed 11 May '15, 07:27</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></img></div></div><div id="comments-container-42301" class="comments-container"><span id="42303"></span><div id="comment-42303" class="comment"><div id="post-42303-score" class="comment-score"></div><div class="comment-text"><p>Not really a Wireshark question. You'll hopefully find more appropriate help on a Python programming focused site.</p></div><div id="comment-42303-info" class="comment-info"><span class="comment-age">(11 May '15, 07:27)</span> grahamb ♦</div></div><span id="42305"></span><div id="comment-42305" class="comment"><div id="post-42305-score" class="comment-score"></div><div class="comment-text"><p>This is related to Wireshark. I tried to change the total length of IP in my program but it doesnt show any changes in Wireshark. Are there any changes that need to be done in Wireshark ?</p></div><div id="comment-42305-info" class="comment-info"><span class="comment-age">(11 May '15, 07:32)</span> Praju</div></div><span id="42306"></span><div id="comment-42306" class="comment"><div id="post-42306-score" class="comment-score"></div><div class="comment-text"><p>Wireshark just reports what's captured. There are no other reports of Wireshark misreporting UDP packet length, if you look at the Wireshark Expert Info, it tells you what's wrong, the UDP header says there are more bytes in the packet (380) than the IP header says (60). The length in the IP header should be the IP Header (20) + all payload bytes.</p></div><div id="comment-42306-info" class="comment-info"><span class="comment-age">(11 May '15, 07:49)</span> grahamb ♦</div></div></div><div id="comment-tools-42301" class="comment-tools"></div><div class="clear"></div><div id="comment-42301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by grahamb 11 May '15, 07:27

</div>

</div>

</div>

