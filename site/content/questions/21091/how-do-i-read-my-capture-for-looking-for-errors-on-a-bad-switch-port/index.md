+++
type = "question"
title = "How do i read my capture for looking for errors on a bad switch port"
description = '''Hello, After configuring Port mirroring on a HP Procurve switch I was able to have my Wireshark program installed on a Windows 7 box connected to the Procurve on port 10 setup to monitor a PC in port 11 which is getting thousands of Rx errors on the port 11 interface as I see on the HP Web GUI Port ...'''
date = "2013-05-10T21:08:00Z"
lastmod = "2013-05-11T03:59:00Z"
weight = 21091
keywords = [ "reading", "logs" ]
aliases = [ "/questions/21091" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do i read my capture for looking for errors on a bad switch port](/questions/21091/how-do-i-read-my-capture-for-looking-for-errors-on-a-bad-switch-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21091-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>After configuring Port mirroring on a HP Procurve switch I was able to have my Wireshark program installed on a Windows 7 box connected to the Procurve on port 10 setup to monitor a PC in port 11 which is getting thousands of Rx errors on the port 11 interface as I see on the HP Web GUI Port counters for the HP switch. I did capture for about 5 minutes and now I have not idea what I am looking for to find out why that port 11 is logging thousands of Rx errors. What do I need to look for to figure out why that port has so many errors. The PC connected to that port 11 is Windows 7 as well. Thanks,</p><p>Jimmy (first time Wireshark user)</p></div><div id="question-tags" class="tags-container tags">reading logs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '13, 21:08</strong></p><img src="https://secure.gravatar.com/avatar/d2425ae4e36594cafdb08bd31b66424f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="forums712&#39;s gravatar image" /><p>forums712<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="forums712 has no accepted answers">0%</span></p></div></div><div id="comments-container-21091" class="comments-container"></div><div id="comment-tools-21091" class="comment-tools"></div><div class="clear"></div><div id="comment-21091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21093"></span>

<div id="answer-container-21093" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21093-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't capture damaged frames on a mirror port, as the switch will drop those frames. Even if you use a TAP in front of the switch, you probably won't see those frames as your network card (or the driver) will drop them.</p><p>For more information on that topic, I recommend an article of @Jasper in his blog: <a href="http://blog.packet-foo.com/2013/05/capturing-damaged-frames/">http://blog.packet-foo.com/2013/05/capturing-damaged-frames/</a></p><p>So, here are your options (in the order of appearance):</p><ul><li>Enable <strong>debug logging</strong> on the switch. Maybe the log tells you why there are so many RX errors. If the switch does not provide a debug log, send a complaint to the CEO of the vendor or buy a different product next time ;-)</li><li>Change the switch port. Maybe that one port is broken</li><li>Replace the cable</li><li>Boot the PC with a Linux CDROM (Knoppix) and do some tests. Maybe it's just a Windows driver problem</li><li>Replace the NIC of your PC. Maybe that interface is broken</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '13, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 May '13, 06:50</p></div></div><div id="comments-container-21093" class="comments-container"></div><div id="comment-tools-21093" class="comment-tools"></div><div class="clear"></div><div id="comment-21093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21094"></span>

<div id="answer-container-21094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21094-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Jimmy, most likely, the HP switch will not mirror any packets that have errors. So the port mirror configuration will not help you in finding the cause of the Rx Errors. Is there more information the Procurve can give you? Most managed switches have some more detailed counters for different kinds of Rx Errors.</p><p>There are a couple of things you might want to check:</p><ul><li>Are the duplex settings on the PC and the switchport (11) the same? If they have a mismatch, you will see lots of errors</li><li>Are the errors still increasing on the port (11) when you connect another device?</li><li>Do you still see errors when moving the PC to another port?</li></ul><p>As for things you can see with wireshark, when there are Rx errors, there is presumably packet loss. So when doing a large file transfer over TCP, you will see retransmissions. Based on what you see in wireshark, you can determine whether the missing packets are inbound or outbound and whether they are get lost on the leg between the PC and the switch or between the switch and the rest of the network.</p><p>If you really want to catch the bad packets, you will have to use a TAP between the PC and the switchport and then capture the traffic with a network card that is able to pass frames with a bad FCS to the OS (most normal NICs won't do that).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '13, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21094" class="comments-container"><span id="21135"></span><div id="comment-21135" class="comment"><div id="post-21135-score" class="comment-score"></div><div class="comment-text"><p>ok thanks SYN-Bit. So if i do a large file transfer and capture the packets with Wireshark, i still dont know what i am looking for. Sorry, but this is the first time i am using a tool like this. So, on other words what am i looking for as far as "Protocol, Length, and in the Info"? Thanks,</p><p>Jimmy K</p></div><div id="comment-21135-info" class="comment-info"><span class="comment-age">(14 May '13, 08:55)</span> forums712</div></div><span id="21139"></span><div id="comment-21139" class="comment"><div id="post-21139-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So, on other words what am i looking for as far as "Protocol, Length, and in the Info"?</p></blockquote><p>to detect what exactly?</p></div><div id="comment-21139-info" class="comment-info"><span class="comment-age">(14 May '13, 09:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-21094" class="comment-tools"></div><div class="clear"></div><div id="comment-21094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

