+++
type = "question"
title = "Capture DHCP traffic on the DHCP server side"
description = '''I’m pretty new to Wireshark and trying to TS an issue and want to prove that a PXE DHCP request isn’t being received by the Microsoft DHCP server. I thought it would be a case of:  Start a capture on the DHCP server Kick off the boot process on the client, watch the PXE boot and note the mac address...'''
date = "2013-09-18T17:37:00Z"
lastmod = "2013-09-18T20:14:00Z"
weight = 24930
keywords = [ "dhcp", "server", "capture" ]
aliases = [ "/questions/24930" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture DHCP traffic on the DHCP server side](/questions/24930/capture-dhcp-traffic-on-the-dhcp-server-side)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24930-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I’m pretty new to Wireshark and trying to TS an issue and want to prove that a PXE DHCP request isn’t being received by the Microsoft DHCP server. I thought it would be a case of:</p><ol><li>Start a capture on the DHCP server</li><li>Kick off the boot process on the client, watch the PXE boot and note the mac address</li><li>Stop the capture on the DHCP server and filter (eth.src.==xx.xx.xx.xx.xx.xx)</li><li>If nothing shows then my point is proved.</li></ol><p>Problem is, I’ve performed this on a client that is successfully obtaining an address and to see a positive result I repeated the process above but do not see any packets. I can see plenty of DHCP traffic. I’m just wondering of the source mac address will be the Cisco switch routing the request via the helper.</p><p>Any ideas how one can achieve what I’m trying to do?</p><p>Thanks..</p></div><div id="question-tags" class="tags-container tags">dhcp server capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '13, 17:37</strong></p><img src="https://secure.gravatar.com/avatar/e3430a5f65a15daed41a38faf727f46f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="plentymech&#39;s gravatar image" /><p>plentymech<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="plentymech has one accepted answer">100%</span></p></div></div><div id="comments-container-24930" class="comments-container"></div><div id="comment-tools-24930" class="comment-tools"></div><div class="clear"></div><div id="comment-24930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24934"></span>

<div id="answer-container-24934" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24934-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I worked out the process myself now. I was doing it right but just played with the filters a little more and all was revealed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '13, 20:14</strong></p><img src="https://secure.gravatar.com/avatar/e3430a5f65a15daed41a38faf727f46f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="plentymech&#39;s gravatar image" /><p>plentymech<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="plentymech has one accepted answer">100%</span></p></div></div><div id="comments-container-24934" class="comments-container"></div><div id="comment-tools-24934" class="comment-tools"></div><div class="clear"></div><div id="comment-24934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

