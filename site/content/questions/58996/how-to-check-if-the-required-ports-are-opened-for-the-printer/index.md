+++
type = "question"
title = "How to check if the required ports are opened for the printer ?"
description = '''Dear Team,  May I request a favor for my question? I have been implementing Print Management Software in customer site. The problem is the printer could not be added to the Print Management Server . Simply , I used telnet to the device IP and required port 53213 from server and telnet failed. But th...'''
date = "2017-01-23T21:11:00Z"
lastmod = "2017-01-29T23:43:00Z"
weight = 58996
keywords = [ "portsopenedornot" ]
aliases = [ "/questions/58996" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to check if the required ports are opened for the printer ?](/questions/58996/how-to-check-if-the-required-ports-are-opened-for-the-printer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58996-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Team,</p><p>May I request a favor for my question?</p><p>I have been implementing Print Management Software in customer site. The problem is the printer could not be added to the Print Management Server . Simply , I used telnet to the device IP and required port 53213 from server and telnet failed. But the customer complained that they have opened all the ports with any-any setting in firewall and maybe the port of our device is not in the listened stage.</p><p>So may I know if Wireshark can help me check which ports can be reached/which ports cannot be reached while communicating from server to device in the addition of printer to software process.</p><p>Thank you so much in advance for your help.</p><p>Best Regards, Natha</p></div><div id="question-tags" class="tags-container tags">portsopenedornot</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '17, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/8355fc1cda38f20faebdd93c60294b33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Natha&#39;s gravatar image" /><p>Natha<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Natha has no accepted answers">0%</span></p></div></div><div id="comments-container-58996" class="comments-container"><span id="59028"></span><div id="comment-59028" class="comment"><div id="post-59028-score" class="comment-score"></div><div class="comment-text"><p>quick way would be to .... run Wireshark on a PC and then telnet (from same PC) to printer port 53213. Then examine the capture if a RST came back from printer, if yes then the port is closed.</p><p>if not upload that capture to here.</p></div><div id="comment-59028-info" class="comment-info"><span class="comment-age">(24 Jan '17, 13:42)</span> soochi</div></div><span id="59074"></span><div id="comment-59074" class="comment"><div id="post-59074-score" class="comment-score"></div><div class="comment-text"><p>Dear Soochi,</p><p>Thank you for the advice. As it is in customer place, please gimme sometime to go there to try out. I will update the result once testing is done.</p><p>Thanks again and best regards, Natha</p></div><div id="comment-59074-info" class="comment-info"><span class="comment-age">(25 Jan '17, 21:26)</span> Natha</div></div><span id="59093"></span><div id="comment-59093" class="comment"><div id="post-59093-score" class="comment-score"></div><div class="comment-text"><p>Dear Soochi,</p><p>Sorry for my late reply .</p><p>As per your advice, I did telnet and captured the wireshark. But didn't see RST so it seems the port 53213 opened ? But still could not add the device to Print Management software. Kindly see attached . Could you please help me for some more advice ?</p><p>Your understanding for not being able to upload the packet here is much appreciated because customer doesn't allow me to put their data here.</p><p>Thank you so much for your help. Looking forward to your reply .</p><p>Best Regards, Natha</p></div><div id="comment-59093-info" class="comment-info"><span class="comment-age">(26 Jan '17, 22:01)</span> Natha</div></div><span id="59099"></span><div id="comment-59099" class="comment"><div id="post-59099-score" class="comment-score"></div><div class="comment-text"><p>I know this is a wireshark forum, but why don't you just use a tool like nmap to get a list of all the ports open in the server?</p></div><div id="comment-59099-info" class="comment-info"><span class="comment-age">(27 Jan '17, 00:04)</span> csigueros</div></div><span id="59105"></span><div id="comment-59105" class="comment"><div id="post-59105-score" class="comment-score"></div><div class="comment-text"><p>Hello Csigueros,</p><p>Thank you for the advice . nmap could not check device(Copier) port ? Kindly see the following .. 192.128.64.95 is device IP.</p><p>Microsoft Windows [Version 6.3.9600] (c) 2013 Microsoft Corporation. All rights reserved.</p><blockquote><p>nmap -sU -p 53200-53300 192.128.64.95</p></blockquote><p>Starting Nmap 7.40 ( <a href="https://nmap.org">https://nmap.org</a> ) at 2017-01-27 17:54 Myanmar Standard Ti e dnet: Failed to open device eth1 QUITTING!</p><p>Thanks</p></div><div id="comment-59105-info" class="comment-info"><span class="comment-age">(27 Jan '17, 03:27)</span> Natha</div></div><span id="59122"></span><div id="comment-59122" class="comment not_top_scorer"><div id="post-59122-score" class="comment-score"></div><div class="comment-text"><p>If you make the telnet test you can see in most cases an RST in response to the initial SYN, if the port is down. A Firewall can manipulate this handling.</p><p>But if the port is open you should see a full 3 Way handshake (SYN,SYN/ACK,ACK) to the Port 53213.</p><p>So waht exactly do see in the trace?</p></div><div id="comment-59122-info" class="comment-info"><span class="comment-age">(28 Jan '17, 14:35)</span> Christian_R</div></div><span id="59138"></span><div id="comment-59138" class="comment not_top_scorer"><div id="post-59138-score" class="comment-score"></div><div class="comment-text"><p>Hello Christian,</p><p>Thank you for the comment.</p><p>What I see is [SYN,ECN, CWR] to the port 53213. So it means the port not open ?</p><p>Thanks..</p></div><div id="comment-59138-info" class="comment-info"><span class="comment-age">(29 Jan '17, 20:49)</span> Natha</div></div></div><div id="comment-tools-58996" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-58996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59139"></span>

<div id="answer-container-59139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59139-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well normally if you just see the first packet of the handshake (SYN-packet) answered by an RST it means the port is down or blocked by a Firewall.</p><p>If you only the see the first SYN packet, answered by nothing it normally means the packet is lost or blocked by a FW.</p><p>So in your case a FW may block the packets. BUT I think you deal with another problem. It could be that not all devices understand the ECN, CWR Bits in your packet. So please try to disable them on the client side.</p><p>Some clients tries to disable the new RFC feature by itself by retransmit the SYN without these options. But in your case it seems it does not happen. So that is the reason why I suggest to disable this options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '17, 23:43</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '17, 09:02</p></div></div><div id="comments-container-59139" class="comments-container"><span id="59140"></span><div id="comment-59140" class="comment"><div id="post-59140-score" class="comment-score"></div><div class="comment-text"><p>Thank you Christian for the explanation .</p><p>Let me go through with the customer and will update you the result.</p><p>Best Regards, Natha</p></div><div id="comment-59140-info" class="comment-info"><span class="comment-age">(29 Jan '17, 23:55)</span> Natha</div></div></div><div id="comment-tools-59139" class="comment-tools"></div><div class="clear"></div><div id="comment-59139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

