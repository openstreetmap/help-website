+++
type = "question"
title = "Edit a captured PCAP file to resend it using TCPREPLAY"
description = '''Hi, I have a captured pcap file with a single packet and I would like to edit it and change some value in the user data field (CFLOW). Is there any way I can do it with wireshark assuming it will also update the checksum value of the packet? The edited packet would be sent to the network using tcpre...'''
date = "2011-02-15T00:47:00Z"
lastmod = "2011-02-15T11:48:00Z"
weight = 2339
keywords = [ "cisco" ]
aliases = [ "/questions/2339" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Edit a captured PCAP file to resend it using TCPREPLAY](/questions/2339/edit-a-captured-pcap-file-to-resend-it-using-tcpreplay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2339-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a captured pcap file with a single packet and I would like to edit it and change some value in the user data field (CFLOW). Is there any way I can do it with wireshark assuming it will also update the checksum value of the packet? The edited packet would be sent to the network using tcpreplay..</p></div><div id="question-tags" class="tags-container tags">cisco</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '11, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/178dc260b73e46ae5828f36d5c60f93d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="questions&#39;s gravatar image" /><p>questions<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="questions has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Feb '11, 00:48</p></div></div><div id="comments-container-2339" class="comments-container"></div><div id="comment-tools-2339" class="comment-tools"></div><div class="clear"></div><div id="comment-2339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2353"></span>

<div id="answer-container-2353" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2353-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark won't allow you to edit your pcap file, but can help you get things in order again.</p><p>Open the pcap file in Wireshark and a Hex editor. Use Wireshark to look up the offset of the field you want to change and make that change with the Hex editor, than save it. Now reload the file in Wireshark. That now shows you a wrong checksum, but also the value it should be(!). Use that value to update the checksum field in the hex editor. Rinse, repeat.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '11, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2353" class="comments-container"></div><div id="comment-tools-2353" class="comment-tools"></div><div class="clear"></div><div id="comment-2353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

