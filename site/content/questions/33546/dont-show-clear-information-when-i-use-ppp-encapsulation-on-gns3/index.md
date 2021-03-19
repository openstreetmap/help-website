+++
type = "question"
title = "Don&#x27;t show clear information when I use PPP encapsulation on GNS3"
description = '''Hello everybody  I&#x27;m working with GNS3 and PPP encapsulation I put the simple example the PPP encapsulation.  This is the desing of the network  This is the basic configuration is: R1 Router(config)#int s0/0 Router(config-if)#ip address 190.0.0.1 255.255.255.0  Router(config-if)#encapsulation ppp Ro...'''
date = "2014-06-08T07:53:00Z"
lastmod = "2014-06-08T18:19:00Z"
weight = 33546
keywords = [ "gns3", "ppp", "encapsulation" ]
aliases = [ "/questions/33546" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Don't show clear information when I use PPP encapsulation on GNS3](/questions/33546/dont-show-clear-information-when-i-use-ppp-encapsulation-on-gns3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33546-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody</p><p>I'm working with <a href="http://www.gns3.net">GNS3</a> and PPP encapsulation I put the simple example the PPP encapsulation.</p><p>This is the desing of the network</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ppp_fail.png" alt="alt text" /></p><p>This is the basic configuration is:</p><p><strong>R1</strong></p><pre><code>Router(config)#int s0/0
Router(config-if)#ip address 190.0.0.1 255.255.255.0  
Router(config-if)#encapsulation ppp
Router(config-if)#no sh 
Router(config-if)#exit</code></pre><p><strong>R2</strong></p><pre><code>Router(config)#int s0/0
Router(config-if)#ip address 190.0.0.2 255.255.255.0
Router(config-if)#encapsulation ppp
Router(config-if)#no sh
Router(config-if)#exit</code></pre><p>So when I try to capture the information with Wireshark I get the following information.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Pantallazo.png" alt="alt text" /></p><p>This is the specifications of my platform:</p><pre><code>Linux socialmedia 3.14-1-amd64 #1 SMP Debian 3.14.4-1 (2014-05-13) x86_64 GNU/Linux</code></pre><p>Running the command <strong>wireshark -v</strong></p><pre><code>wireshark 1.10.7 (v1.10.7-0-g6b931a1 from master-1.10)

Compiled (64-bit) with GTK+ 3.12.2, with Cairo 1.12.16, with Pango 1.36.3, with
GLib 2.40.0, with libpcap, with libz 1.2.8, with POSIX capabilities (Linux),
with libnl 3, with SMI 0.4.8, with c-ares 1.10.0, with Lua 5.2, without Python,
with GnuTLS 3.2.14, with Gcrypt 1.5.3, with MIT Kerberos, with GeoIP, with
PortAudio V19-devel (built Feb 15 2014 23:28:00), without AirPcap.

Running on Linux 3.14-1-amd64, with locale es_CO.UTF-8, with libpcap version
1.5.3, with libz 1.2.8, GnuTLS 3.2.15, Gcrypt 1.5.3.
AMD C-60 APU with Radeon(tm) HD Graphics

Built using gcc 4.8.3.</code></pre><p>I can see nothing. Someone could tell me why does this happen and how to fix it?</p><p>According with this: <a href="http://wiki.wireshark.org/CaptureSetup/PPP,">http://wiki.wireshark.org/CaptureSetup/PPP,</a> it's possible but I don't kwow how.</p></div><div id="question-tags" class="tags-container tags">gns3 ppp encapsulation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '14, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/c90b45a5bde3f27dcffe26ef54760faf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cristianchaparroa&#39;s gravatar image" /><p>cristianchap...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cristianchaparroa has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '14, 18:42</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></img></div></div><div id="comments-container-33546" class="comments-container"><span id="33559"></span><div id="comment-33559" class="comment"><div id="post-33559-score" class="comment-score"></div><div class="comment-text"><p>So what are machines R1 and R2, and is the Linux box on which you ran Wireshark one of those two machines or some third machine plugged into the connection between R1 and R2?</p></div><div id="comment-33559-info" class="comment-info"><span class="comment-age">(08 Jun '14, 17:58)</span> Guy Harris ♦♦</div></div><span id="33560"></span><div id="comment-33560" class="comment"><div id="post-33560-score" class="comment-score"></div><div class="comment-text"><p>I don't understand your question. R1 and R2 are routers, and I use vpcs, virtual machines to connect to it. Remember it is a LAB with GNS3. I run GNS3 on Linux machine.</p></div><div id="comment-33560-info" class="comment-info"><span class="comment-age">(08 Jun '14, 18:06)</span> cristianchap...</div></div><span id="33562"></span><div id="comment-33562" class="comment"><div id="post-33562-score" class="comment-score"></div><div class="comment-text"><p>Just to clarify Guy, GNS3 is virualization software that allows you to run Cisco/Juniper routers, and even clients/servers (Virtual Box hosts), in one big virtual network sandbox.</p><p>Within that environment, GNS3 supports exporting packets between the virtual systems into Wireshark. The problem here is that he's using GNS3's default L2 protocol for serial interfaces (HDLC) for generating the packet capture so Wireshark will decode it that way, while he's manually configured PPP on the routers themselves.</p></div><div id="comment-33562-info" class="comment-info"><span class="comment-age">(08 Jun '14, 18:25)</span> Quadratic</div></div></div><div id="comment-tools-33546" class="comment-tools"></div><div class="clear"></div><div id="comment-33546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33561"></span>

<div id="answer-container-33561" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33561-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your problem is that you're using GNS3's default L2 protocol for packet captures (HDLC) instead of specifying PPP. When you right-click to "Start Capture" on an interface in GNS3, click the drop-down and specify PPP specifically.</p><p>Wireshark needs to be given a context (what L2 protocol is in use) in order to know how to decode the packets correctly. GNS3 doesn't know what L2 protocol you're going to configure on that router's serial interface, so it default to HDLC and gives you the option to specify the L2 encapsulation to use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '14, 18:19</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '14, 18:27</p></div></div><div id="comments-container-33561" class="comments-container"><span id="33563"></span><div id="comment-33563" class="comment"><div id="post-33563-score" class="comment-score"></div><div class="comment-text"><p>That awkward I am, thanks for your answer.</p></div><div id="comment-33563-info" class="comment-info"><span class="comment-age">(08 Jun '14, 18:37)</span> cristianchap...</div></div><span id="33564"></span><div id="comment-33564" class="comment"><div id="post-33564-score" class="comment-score"></div><div class="comment-text"><p>No problem. :)</p></div><div id="comment-33564-info" class="comment-info"><span class="comment-age">(08 Jun '14, 20:14)</span> Quadratic</div></div></div><div id="comment-tools-33561" class="comment-tools"></div><div class="clear"></div><div id="comment-33561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

