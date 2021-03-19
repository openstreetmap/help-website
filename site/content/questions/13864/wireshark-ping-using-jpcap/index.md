+++
type = "question"
title = "Wireshark : Ping using Jpcap"
description = '''Hello All, I made a basic program in java using Jpcap to ping a machine. However the problem is whenever I ping using Win 7 command prompt, it returns a ping reply. However using Jpcap, it doesn&#x27;t send a reply to my ping request. However I came across a strange situation. On the other machine, which...'''
date = "2012-08-24T02:58:00Z"
lastmod = "2012-08-24T04:13:00Z"
weight = 13864
keywords = [ "icmp", "jpcap", "ping", "wireshark" ]
aliases = [ "/questions/13864" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark : Ping using Jpcap](/questions/13864/wireshark-ping-using-jpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13864-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I made a basic program in java using Jpcap to ping a machine. However the problem is whenever I ping using Win 7 command prompt, it returns a ping reply. However using Jpcap, it doesn't send a reply to my ping request. However I came across a strange situation. On the other machine, which I am pinging, If I open a Wireshark console and monitor the packets, it shows a ICMP request and sends a reply then. However this is not working again if I close the wireshark !!</p><p>What is the problem here ?? Is it with some Win 7 firewall or some other issues ?</p><p>I have attached the code below :</p><pre><code>JpcapSender sender=JpcapSender.openDevice(devices[index]);

ICMPPacket p=new ICMPPacket();
p.type=ICMPPacket.ICMP_ECHO;
p.seq=1000;
p.id=999;
p.orig_timestamp=123;
p.trans_timestamp=456;
p.recv_timestamp=789;
p.setIPv4Parameter(0,false,false,false,0,false,false,false,0,1010101,100,IPPacket.IPPROTO_ICMP, InetAddress.getByName(&quot;192.168.101.18&quot;),InetAddress.getByName(&quot;192.168.101.4&quot;));
p.data=&quot;data&quot;.getBytes();

EthernetPacket ether=new EthernetPacket();
ether.frametype=EthernetPacket.ETHERTYPE_IP;
ether.src_mac=new byte[]{(byte)00,(byte)26,(byte)18,(byte)00,(byte)25,(byte)65};    
ether.dst_mac=new byte[]{(byte)90,(byte)230,(byte)186,(byte)60,(byte)205,(byte)90};
p.datalink=ether;

//for(int i=0;i&lt;10;i++)
    sender.sendPacket(p);</code></pre><p>}</p></div><div id="question-tags" class="tags-container tags">icmp jpcap ping wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '12, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/02159717bcbbad739340426573e3468a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Somnath%20Paul&#39;s gravatar image" /><p>Somnath Paul<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Somnath Paul has no accepted answers">0%</span></p></div></div><div id="comments-container-13864" class="comments-container"></div><div id="comment-tools-13864" class="comment-tools"></div><div class="clear"></div><div id="comment-13864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13867"></span>

<div id="answer-container-13867" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13867-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This question is not really related to Wireshark. I suggest:</p><ul><li>to try the ICMP sample from the Jpcap site: <a href="http://netresearch.ics.uci.edu/kfujii/Jpcap/doc/samples.html">http://netresearch.ics.uci.edu/kfujii/Jpcap/doc/samples.html</a></li><li>to ask the Jpcap community for help: <a href="https://groups.google.com/forum/?fromgroups#!forum/jpcap">https://groups.google.com/forum/?fromgroups#!forum/jpcap</a></li></ul><blockquote><p>If I open a Wireshark console and monitor the packets, it shows a ICMP request and sends a reply then. However this is not working again if I close the wireshark !!</p></blockquote><p>IF this happens on the client (where your Jpcap code runs), I guess that you just loaded the WinPcap driver when you started Wireshark and that's the reason why it then works. In that case it's a WinPcap issue and you need to figure out why the Winpcap driver is not running per default.</p><blockquote><p><code>http://www.winpcap.org/misc/faq.htm</code><br />
</p></blockquote><p>You should also add some error detection code, to detect these kind of situations, when Jpcap is not able to receive/send packets.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '12, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Aug '12, 04:24</p></div></div><div id="comments-container-13867" class="comments-container"></div><div id="comment-tools-13867" class="comment-tools"></div><div class="clear"></div><div id="comment-13867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

