+++
type = "question"
title = "tcp reset by the server due to 2 consecutive SYNs"
description = '''Hi, I have a sequence of tcp connection establishment as follows:  client sends a syn to server client do not hear a response within 2.996seconds client initiates a second syn to server server acknowledges for the syn. not sure if its for the first syn or second syn. but looking at the timestamp its...'''
date = "2012-12-27T13:07:00Z"
lastmod = "2013-01-02T05:38:00Z"
weight = 17280
keywords = [ "consecutive", "two", "syns" ]
aliases = [ "/questions/17280" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tcp reset by the server due to 2 consecutive SYNs](/questions/17280/tcp-reset-by-the-server-due-to-2-consecutive-syns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17280-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a sequence of tcp connection establishment as follows:</p><ol><li>client sends a syn to server</li><li>client do not hear a response within 2.996seconds</li><li>client initiates a second syn to server</li><li>server acknowledges for the syn. not sure if its for the first syn or second syn. but looking at the timestamp its matching with the second syn</li><li>client receives a RST,ACK.</li></ol><p>I am not sure why i receive a TCP reset. Is there a problem in client or server ? is the server recognizing it as a syn flood ? destination is a VIP (might be a loadbalancer cum firewall). I am actually an application's guy with very limited knowledge on tcp/networking stuff. Could you pls help me out here as i have no clue of whether its an issue with client or server.</p><p>SYN goes with flags SYN, ECN, CWR for both SYNs.</p><p>Thanks, resolver</p></div><div id="question-tags" class="tags-container tags">consecutive two syns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '12, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/1fde3199bc6f991fdda6ed413c404050?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="synresolver&#39;s gravatar image" /><p>synresolver<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="synresolver has no accepted answers">0%</span></p></div></div><div id="comments-container-17280" class="comments-container"><span id="17283"></span><div id="comment-17283" class="comment"><div id="post-17283-score" class="comment-score">1</div><div class="comment-text"><p>can you post a capture file somewhere? It's hard to do any troubleshooting based on a text description of what you (believe to) have seen ;-)</p></div><div id="comment-17283-info" class="comment-info"><span class="comment-age">(27 Dec '12, 14:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-17280" class="comment-tools"></div><div class="clear"></div><div id="comment-17280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17295"></span>

<div id="answer-container-17295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17295-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>SYN goes with flags SYN, <strong>ECN</strong>, CWR for both SYNs.</p></blockquote><p>from <a href="http://tools.ietf.org/html/rfc3360">RFC 3360</a>:</p><pre><code>   
   Unfortunately, a number of firewalls and load-balancers in the
   current Internet send a reset in response to a TCP SYN packet that
   use flags from the Reserved field in the TCP header.  Section 3 below
   discusses the specific example of firewalls that send resets in
   response to TCP SYN packets from ECN-capable hosts.</code></pre><p>well, that was in 2002. Anyway, as you mentioned a loadbalancer and/or a firewall, I would try to check that with the device admins in charge.</p><p>Can you disable the use of ECN on your client (just for a test)?</p><blockquote><p><code>http://en.wikipedia.org/wiki/Explicit_Congestion_Notification#ECN_support_in_TCP_by_hosts</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '12, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Dec '12, 23:19</p></div></div><div id="comments-container-17295" class="comments-container"><span id="17302"></span><div id="comment-17302" class="comment"><div id="post-17302-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks a lot for your response. I will disable the ECN and test it.</p><p>Is there a way that i can post the pcap file to you. if you dont mind pls share your email id. Following is the sequence for one of the resets.</p><pre><code>No.       Time         Source      Destination           Protocol Length Info

11931 6218.308766      SrcHst        DstHost           TCP      74     13358 &gt; https [SYN, ECN, CWR] Seq=0 Win=5840 Len=0 MSS=1460 SACK_PERM=1 TSval=145993636 TSecr=0 WS=256

11972 6221.305267      SrcHst        DstHost           TCP      74     13358 &gt; https [SYN, ECN, CWR] Seq=0 Win=5840 Len=0 MSS=1460 SACK_PERM=1 TSval=145994386 TSecr=0 WS=256

11973 6221.328336      DstHost       SrcHst            TCP      60     https &gt; 13358 [ACK] Seq=1 Ack=1 Win=12288 Len=0

11974 6225.741699       DstHost       SrcHst            TCP      60     https &gt; 13358 [RST, ACK] Seq=1 Ack=1 Win=12288 Len=0
</code></pre><p>I will go through the links you have shared. What are the consequences of disabling the ECN at the device level ?</p><p>Not able to post the above details via "add new comment" button hence posting in the Your answer text area. if you would like to move to my comment in any way pls do so.</p><p>Thanks a lot again.</p></div><div id="comment-17302-info" class="comment-info"><span class="comment-age">(28 Dec '12, 02:27)</span> synresolver</div></div><span id="17303"></span><div id="comment-17303" class="comment"><div id="post-17303-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Thanks a lot for your response. I will disable the ECN and test it.</p></blockquote><p>O.K. what is your client OS?</p><blockquote><p>Is there a way that i can post the pcap file to you. if you dont mind pls share your email id. Following is the sequence for one of the resets.</p></blockquote><p>If you can upload it somewhere (google docs, one-click filehoster) I would prefer that. Otherwise you can find my e-mail address in my profile (just click on my name).</p><blockquote><p>I will go through the links you have shared. What are the consequences of disabling the ECN at the device level ?</p></blockquote><p>If ECN causes the problem, then the 'consequence' would be that it works ;-)</p><p>The 'bad' consequences are minimal (or none), if your network connection is otherwise stable (not too much packet loss).</p></div><div id="comment-17303-info" class="comment-info"><span class="comment-age">(28 Dec '12, 03:01)</span> Kurt Knochner ♦</div></div><span id="17304"></span><div id="comment-17304" class="comment"><div id="post-17304-score" class="comment-score"></div><div class="comment-text"><p>You can post capture files to <a href="http://www.cloudshark.org">www.cloudshark.org</a>, but beware that you don't publicly share capture files with sensitive data in it (you can change IP addresses with <a href="http://bittwist.sourceforge.net/">bittwist</a> or <a href="http://tcpreplay.synfin.net/wiki/tcprewrite">tcprewrite</a>).</p></div><div id="comment-17304-info" class="comment-info"><span class="comment-age">(28 Dec '12, 03:01)</span> SYN-bit ♦♦</div></div><span id="17380"></span><div id="comment-17380" class="comment"><div id="post-17380-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Sorry for delayed response due to the holdiays. I have sent you the pcap file. If you filter with ip.addr == 20.20.20.20 &amp;&amp; tcp.port == 53810 you can see the SYN, ECN, CWR are being set but at the IP level the differentiated services flag states that its not ECN-Capable support. So, not sure if this is completely because of ECN flag.</p><p>OS - is IBM's DataPower XI 50 server.</p><p>For the other successful tcp connections, i can see these so network team is ruling out this is the root cause, hence we are not able to disable the ECN and test.</p><p>synbit- thanks for suggesting the tools and i modified the capture files to certain extent so that the data is being scrambled.</p><p>thanks again.</p></div><div id="comment-17380-info" class="comment-info"><span class="comment-age">(02 Jan '13, 05:24)</span> synresolver</div></div><span id="17384"></span><div id="comment-17384" class="comment"><div id="post-17384-score" class="comment-score"></div><div class="comment-text"><p>O.K. I checked the pcap file you sent me via email. Please apply the following filter:</p><blockquote><p><code>tcp.flags.syn eq 1 and (tcp.stream eq 16 or tcp.stream eq 632)</code><br />
</p></blockquote><p>As you can see, there are HTTPS connections that do work with ECN (and CWR) set. Stream #16 works, whereas stream #632 (similar connection parameters) does <strong>not work</strong>.</p><p>Then please apply this filter:</p><blockquote><p><code>ip.addr eq 20.20.20.20 and ((tcp.flags.syn eq 1 and  tcp.flags.ecn eq 1) or tcp.flags.reset eq 1)</code><br />
</p></blockquote><p>As you can see, most (similar) connections do work, just a few show that 'silly' behavior.</p><p>So, I don't think that ECN (and CWR) is the problem. Now I believe it might be a bug/problem with the device between 10.10.10.10 and 20.20.20.20 (if there is one) or the server 20.20.20.20 itself. However, with just a capture from 10.10.10.10, it is hard to make any assumption.</p><p><strong>Recommendation</strong>: Please try to capture at two points in parallel. One at 10.10.10.10 and one one 20.20.20.20 (if that is the sever), or <strong>after</strong> 20.20.20.20 if that is the firewall/loadbalancer you mentioned.</p><p>BTW: do you know what type of firewall/loadbalancer is in use?</p></div><div id="comment-17384-info" class="comment-info"><span class="comment-age">(02 Jan '13, 06:26)</span> Kurt Knochner ♦</div></div><span id="17396"></span><div id="comment-17396" class="comment not_top_scorer"><div id="post-17396-score" class="comment-score"></div><div class="comment-text"><blockquote><p><strong>server acknowledges for the syn</strong>. not sure if its for the first syn or second syn. but looking at the timestamp its matching with the second syn</p></blockquote><p>That's not quite correct, which also make me believe it's a bug as mentioned above.</p><p>I think I can post the following output, as its totally anonymous.</p><pre><code>   No.     Time        Source                Destination           Protocol Length Info
   7113 3677.285242 10.10.10.10           20.20.20.20           TCP      74     53810 &gt; https [SYN, ECN, CWR] Seq=0 Win=5840 Len=0 MSS=1460 SACK_PERM=1 TSval=145592423 TSecr=0 WS=256

   7151 3680.281717 10.10.10.10           20.20.20.20           TCP      74     53810 &gt; https [SYN, ECN, CWR] Seq=0 Win=5840 Len=0 MSS=1460 SACK_PERM=1 TSval=145593173 TSecr=0 WS=256

   7152 3680.312861 20.20.20.20           10.10.10.10           TCP      60     https &gt; 53810 [ACK] Seq=1 Ack=1 Win=12288 Len=0

   7153 3684.553901 20.20.20.20           10.10.10.10           TCP      60     https &gt; 53810 [RST, ACK] Seq=1 Ack=1 Win=12288 Len=0</code></pre><p>As you can see:</p><blockquote><p>Frame #7113: 10.10.10.10 -&gt; 20.20.20.20 SYN,ECN,CWR<br />
Frame #7151: 10.10.10.10 -&gt; 20.20.20.20 SYN,ECN,CWR<br />
</p></blockquote><p>then</p><blockquote><p>Frame #7152: 20.20.20.20 -&gt; 10.10.10.10 <strong>only</strong> ACK, no SYN/ACK. So this is not a valid reply.<br />
Frame #7153: 20.20.20.20 -&gt; 10.10.10.10 RST<br />
</p></blockquote><p>very strange and possibly a bug in the firmware of the firewall/loadbalancer (or server). See my previous comment.</p></div><div id="comment-17396-info" class="comment-info"><span class="comment-age">(02 Jan '13, 13:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-17295" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-17295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17382"></span>

<div id="answer-container-17382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17382-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>is there a way to adjust your tcp settings so that it doesn't send the second SYN until more time has passed? If it's consistently taking ~2 seconds to respond to SYN, wait 3 before you retransmit, etc... likewise, you might be able to use HPing or SCAPY to send a single SYN packet on it's own and just see what happens. If you still get no reply or an RST, then it's an issue at/past whatever loadbalancer/firewall is in place. I've only rarely used those programs, so I can't remember the relevent commands, but there's plenty of info online.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '13, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/8c8bb4331d25d8ed8241358cecc41b39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="W-George&#39;s gravatar image" /><p>W-George<br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="W-George has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-17382" class="comments-container"><span id="17391"></span><div id="comment-17391" class="comment"><div id="post-17391-score" class="comment-score"></div><div class="comment-text"><p>Hi George, I dont see a provision to edit this. The retry was almost 3secs i.e. 2.996 seconds. I will need to check with IBM if there is any issue in the firmware. Before that i wanted to make sure thats the reason.</p><p>Thanks</p></div><div id="comment-17391-info" class="comment-info"><span class="comment-age">(02 Jan '13, 08:25)</span> synresolver</div></div></div><div id="comment-tools-17382" class="comment-tools"></div><div class="clear"></div><div id="comment-17382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

