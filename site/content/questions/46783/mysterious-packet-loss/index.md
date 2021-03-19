+++
type = "question"
title = "Mysterious Packet Loss"
description = '''Hey there, I was just playing around with Wireshark on my home network and noticed an awful lot of TCP transmission and other black messages. This connection has been notoriously inconsistant and seemly stops working for web traffic every now and again until I reconnect (VoIP calls work consistantly...'''
date = "2015-10-20T15:51:00Z"
lastmod = "2015-10-22T18:46:00Z"
weight = 46783
keywords = [ "wireshark", "packets", "packetloss" ]
aliases = [ "/questions/46783" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mysterious Packet Loss](/questions/46783/mysterious-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46783-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there, I was just playing around with Wireshark on my home network and noticed an awful lot of TCP transmission and other black messages. This connection has been notoriously inconsistant and seemly stops working for web traffic every now and again until I reconnect (VoIP calls work consistantly however).</p><p>I have attatched some logs below of me trying to access a website:<br />
</p><hr /><p><a href="https://www.cloudshark.org/captures/a366b9205ca8">https://www.cloudshark.org/captures/a366b9205ca8</a> Website loaded before returning an error <a href="https://www.cloudshark.org/captures/e96b45abe3c7">https://www.cloudshark.org/captures/e96b45abe3c7</a> Webite loaded successfully after a long wait</p><hr /><p>I'd appreciate any help as to what is happening here and any possible solutions, Thanks in advanced, Jack.</p></div><div id="question-tags" class="tags-container tags">wireshark packets packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '15, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/f9a2ab1b2c1b3f0990d43a1a8d32868d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jarthur36&#39;s gravatar image" /><p>jarthur36<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jarthur36 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-46783" class="comments-container"><span id="46815"></span><div id="comment-46815" class="comment"><div id="post-46815-score" class="comment-score"></div><div class="comment-text"><p>Yes only TCP seems to be affected by the packet loss. But what... the root cause is...</p><p>Have you checked your Firewall logs?</p></div><div id="comment-46815-info" class="comment-info"><span class="comment-age">(21 Oct '15, 12:29)</span> Christian_R</div></div><span id="46825"></span><div id="comment-46825" class="comment"><div id="post-46825-score" class="comment-score"></div><div class="comment-text"><p>Dropbox &amp; Origin should probably be turned off when you are looking for connectivity problems. Chrome is also spewing packets onto your line in QUIC, probably an addon?? Try starting chrome incognito and testing again. I'm not really very versed in MAC lore, I assume it does things the same but differently. However, dropbox causes quite a few false positives, it just isn't worth worrying about in the first analysis. Also, I have never seen a trace done at home without packet retransmissions etc, that's kinda expected.</p><p>I think Christian has a point. If you look at the trace catastrophic: There are only 7 incoming packet from outside your local network and they are flaky at best and then nothing until 64 seconds. A full stream 19 would have been really useful there :D</p><p>I would assume that A: a Firewall has shut you off for 60 seconds (maybe a response to an incoming packet storm, unlikely though. If it was Windows I'd say turn off ICS/Firewall or your AV solution...) B: Your provider did a line reset, look in the log on your router / firewall (Likely) c: Your provider did not provide very well for 60 seconds (Very Likely)</p><p>No Idea why your voip would work though? unless the TPLink router has 2 connects, one for voip and one for non-voip (I have never heard of one, but this means nothing.) I know that when I lose my provider connection, my phone dies too.</p><p>I can only see udp non tcp traffic to external addresses and I have no idea how the program sending it handles packet loss. It could be screaming out loud and you would not really know about it in the trace. You can see quite a few instances of 1 second between packets in the udp, always around the time TCP stalls, maybe that is packet loss handling?</p></div><div id="comment-46825-info" class="comment-info"><span class="comment-age">(22 Oct '15, 01:46)</span> DarrenWright</div></div><span id="46853"></span><div id="comment-46853" class="comment"><div id="post-46853-score" class="comment-score"></div><div class="comment-text"><p>Well, well seems that I have been yesterday a little bit to hastily. I think the udp traffic is affected, too.</p></div><div id="comment-46853-info" class="comment-info"><span class="comment-age">(22 Oct '15, 13:21)</span> Christian_R</div></div></div><div id="comment-tools-46783" class="comment-tools"></div><div class="clear"></div><div id="comment-46783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46866"></span>

<div id="answer-container-46866" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46866-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please take a look at the file <a href="https://www.cloudshark.org/captures/a366b9205ca8">catastrophicPacketLoss.pcapng</a> and then apply the following display filter (click on the link to see it on cloudshark)</p><blockquote><p><a href="https://www.cloudshark.org/captures/a366b9205ca8?filter=ip.src%20eq%20192.168.1.110">ip.src eq 192.168.1.110</a></p></blockquote><p>You'll see continuous <strong>outgoing</strong> traffic, including DNS queries from 192.168.1.110 -&gt; 192.168.1.1 (TP Link) and also to 8.8.8.8 (Google).</p><p>Now, apply the following filter (click on the link to see it on cloudshark)</p><blockquote><p><a href="https://www.cloudshark.org/captures/a366b9205ca8?filter=ip.dst%20eq%20192.168.1.110">ip.dst eq 192.168.1.110</a></p></blockquote><p>You'll see only a few <strong>incoming</strong> frames. All TCP, no DNS answers and frames only once in a while.</p><p>So, without knowing what's going on, here are some possible explanations:</p><ol><li>There is a bug in your router firmware, which causes the problem</li><li>There is a general problem with the link to your ISP</li><li>your router (TP Link) was somehow overloaded and thus dropped the majority of the traffic</li><li>you have been attacked from the Internet with a DoS/DDoS attack, which flooded your incoming pipe and thus most of the regular response frames (DNS and TCP) were dropped. Only a few made it through (those you see in the capture file). The DoS attack could also have overloaded your router which could have made the problem even worse.</li></ol><blockquote><p>stops working for web traffic every now and again <strong>until I reconnect</strong></p></blockquote><p>Until you reconnect? Interesting! If you reconnect, you will 'reset' the link to the ISP and you will (most certainly) receive a new IP address.</p><p>For me, this makes options 2. and 4. more likely than the others. 2. because a link reset might temporarily fix the problem at the ISP and 4. because if you receive a new IP address, the DoS/DDoS traffic (still going to the old IP address) will no longer end up in your internet pipe.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 18:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Oct '15, 18:47</p></div></div><div id="comments-container-46866" class="comments-container"></div><div id="comment-tools-46866" class="comment-tools"></div><div class="clear"></div><div id="comment-46866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

