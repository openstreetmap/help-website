+++
type = "question"
title = "Traffic (SMB) sent across link at 536 bytes with DF flag set to 1? Why is traffic not sent in bigger chunks?"
description = '''On my wireshark trace I can see that SMB traffic is being sent across wire at 536 bytes with DF flag set to 1. I know the DF flag is set to 1, because Windows 2008 and above cannot deal with packets smaller than this, see this blog post: http://blogs.technet.com/b/nettracer/archive/2010/07/30/why-do...'''
date = "2015-11-08T07:22:00Z"
lastmod = "2015-11-08T07:27:00Z"
weight = 47385
keywords = [ "windows", "mss", "smb", "mtu" ]
aliases = [ "/questions/47385" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Traffic (SMB) sent across link at 536 bytes with DF flag set to 1? Why is traffic not sent in bigger chunks?](/questions/47385/traffic-smb-sent-across-link-at-536-bytes-with-df-flag-set-to-1-why-is-traffic-not-sent-in-bigger-chunks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47385-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On my wireshark trace I can see that SMB traffic is being sent across wire at 536 bytes with DF flag set to 1.</p><p>I know the DF flag is set to 1, because Windows 2008 and above cannot deal with packets smaller than this, see this blog post: <a href="http://blogs.technet.com/b/nettracer/archive/2010/07/30/why-doesn-t-windows-2008-server-send-tcp-segments-smaller-than-536-bytes.aspx">http://blogs.technet.com/b/nettracer/archive/2010/07/30/why-doesn-t-windows-2008-server-send-tcp-segments-smaller-than-536-bytes.aspx</a></p><p>My question is why is the size being negotiated at 536 bytes for SMB when the MTU of the link is 1500?</p><p>In the SYN\ACK requests for traffic, I can see the TCP Option Maximum Segment Size for a lot of communication is 1460 bytes (see here for more info on this: <a href="http://serverfault.com/questions/511299/determing-mss-value-on-windows-server">http://serverfault.com/questions/511299/determing-mss-value-on-windows-server</a>)</p><p>Can this reversion to the lowest MSS be caused by a lower MTU somewhere along the path? What else can explain this? See for example here: <a href="https://msdn.microsoft.com/en-us/library/cc558565(v=bts.10).aspx">https://msdn.microsoft.com/en-us/library/cc558565(v=bts.10).aspx</a> where this reversion to 536 bytes is discussed:</p><blockquote><p>The EnablePMTUBHDetect value governs whether TCP tries to detect black hole routers during the Path MTU (maximum transmission unit) discovery process. Enabling black hole detection increases the maximum number of times TCP retransmits a given segment. If the value of this entry is 1, TCP recognizes when it has transmitted the same segment several times without receiving an acknowledgement. It reduces the maximum segment size (MSS) to 536 bytes, and it sets the Don't-Fragment bit. If, as a result, receipt of the segment is acknowledged, TCP continues this practice in all subsequent transmissions on the connection.</p></blockquote></div><div id="question-tags" class="tags-container tags">windows mss smb mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '15, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/72d6bea28bbbf0536499ac3c76de8948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wshark_man_123&#39;s gravatar image" /><p>wshark_man_123<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wshark_man_123 has no accepted answers">0%</span></p></div></div><div id="comments-container-47385" class="comments-container"></div><div id="comment-tools-47385" class="comment-tools"></div><div class="clear"></div><div id="comment-47385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47386"></span>

<div id="answer-container-47386" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47386-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>DF flag means "Don't Fragment". It's an instruction to routers or switches not do fragment this packet. In another word. the SMB server/client just want to be extra sure that the packets don't get fragmented on the path. It doesn't hurt to be extra cautious, does it? Hope it helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '15, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-47386" class="comments-container"><span id="47387"></span><div id="comment-47387" class="comment"><div id="post-47387-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply.</p><p>I know why the DF flag is set (that was discussed in my question), Windows sets it because, as the blog post I reference mentions, it cannot deal with packets smaller than this.</p><p>My question was WHY is the packet being sent at the minimum possible MSS when the MTU of the link is 1500?</p><p>What is causing the negotiation of a 536 MSS?</p><p>I would expect the traffic for a large SMB transfer to be sent in 1460 byte chunks? Or is this not the case?</p></div><div id="comment-47387-info" class="comment-info"><span class="comment-age">(08 Nov '15, 07:30)</span> wshark_man_123</div></div><span id="47388"></span><div id="comment-47388" class="comment"><div id="post-47388-score" class="comment-score"></div><div class="comment-text"><p>So you are saying the MSS from both SYN and SYNACK packets are 1460 but the max data size in this session is only 536. I guess it could be some configuration on either the client or the server side? I have a pcap on SMB and data in some TCP packets are indeed 1460 (occurred during downloading a big file). I think the issue where your TCP data size is smaller than optimum is not related to the DF bit in IP header. Thx.</p></div><div id="comment-47388-info" class="comment-info"><span class="comment-age">(08 Nov '15, 07:39)</span> pktUser1001</div></div><span id="47390"></span><div id="comment-47390" class="comment"><div id="post-47390-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Yes the DF is there because this is the smallest packet Windows 2008 and above accept, so packets of this size have the DF flag set. See the blog post I referenced that discussed this <a href="http://blogs.technet.com/b/nettracer/archive/2010/07/30/why-doesn-t-windows-2008-server-send-tcp-segments-smaller-than-536-bytes.aspx.">http://blogs.technet.com/b/nettracer/archive/2010/07/30/why-doesn-t-windows-2008-server-send-tcp-segments-smaller-than-536-bytes.aspx.</a></p><p>I have captured some other SMB traffic from different locations and can see 1460 bytes on the wire.</p><p>I am going to play with MTU values and see if there is this odd reversion to 536.</p></div><div id="comment-47390-info" class="comment-info"><span class="comment-age">(08 Nov '15, 07:46)</span> wshark_man_123</div></div><span id="47391"></span><div id="comment-47391" class="comment"><div id="post-47391-score" class="comment-score"></div><div class="comment-text"><p>Good luck to you. Curious to know the root cause. Please keep us posted on what you find out.</p></div><div id="comment-47391-info" class="comment-info"><span class="comment-age">(08 Nov '15, 07:49)</span> pktUser1001</div></div><span id="47396"></span><div id="comment-47396" class="comment"><div id="post-47396-score" class="comment-score"></div><div class="comment-text"><p>Did you take the captures at both ends of the session. Maybe it helps.</p></div><div id="comment-47396-info" class="comment-info"><span class="comment-age">(08 Nov '15, 10:09)</span> Christian_R</div></div><span id="47511"></span><div id="comment-47511" class="comment not_top_scorer"><div id="post-47511-score" class="comment-score"></div><div class="comment-text"><p>The DF is set for all IPv4 datagrams (not used in IPv6 because there is no DF field) to prevent fragmentation so that we can determine the path MTU using ICMP messages.</p><p>What are the operating systems involved ? Are they in same LAN or do you access the target on a remote network?</p><p>You could also use ping to determine the MTU manually to see whether you can send above 567 bytes without causing fragmentation.</p></div><div id="comment-47511-info" class="comment-info"><span class="comment-age">(11 Nov '15, 06:26)</span> adasko</div></div></div><div id="comment-tools-47386" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-47386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

