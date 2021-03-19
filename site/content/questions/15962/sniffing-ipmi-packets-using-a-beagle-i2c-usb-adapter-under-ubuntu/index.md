+++
type = "question"
title = "Sniffing IPMI packets using a Beagle i2c USB adapter under Ubuntu"
description = '''Hello everybody, I&#x27;m trying to read IPMI packets transmitted by two devices under Ubuntu Environment. I have physical access to the i2c bus to which I connect using a Beagle i2c usb adapter by TotalPhase. The i2c monitor application is correctly configured (usb udev). What I want to do now is to mak...'''
date = "2012-11-16T05:05:00Z"
lastmod = "2012-11-18T03:34:00Z"
weight = 15962
keywords = [ "beagle", "ipmi", "i2c", "wireshark", "bus" ]
aliases = [ "/questions/15962" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Sniffing IPMI packets using a Beagle i2c USB adapter under Ubuntu](/questions/15962/sniffing-ipmi-packets-using-a-beagle-i2c-usb-adapter-under-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15962-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody,</p><p>I'm trying to read IPMI packets transmitted by two devices under Ubuntu Environment. I have physical access to the i2c bus to which I connect using a Beagle i2c usb adapter by <a href="http://www.totalphase.com/products/beagle_ism">TotalPhase</a>. The i2c monitor application is correctly configured (usb udev). What I want to do now is to make Wireshark communicating with the Beagle to read IPMI commands on the bus. Running a 'lsusb' command on the terminal I get the USB number which is the 5. When I start a capture on this port, no packet is detected.</p><p>Can you help me finding a solution?</p><p>Thank you very much in advance for any hint and/or idea on what else I could try in order to understand where the problem comes from.</p></div><div id="question-tags" class="tags-container tags">beagle ipmi i2c wireshark bus</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '12, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/e2b74c2c5818f2dc9e2436b235e2762e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matte87&#39;s gravatar image" /><p>matte87<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matte87 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Nov '12, 08:48</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-15962" class="comments-container"></div><div id="comment-tools-15962" class="comment-tools"></div><div class="clear"></div><div id="comment-15962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15972"></span>

<div id="answer-container-15972" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15972-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand correctly you have a Beagle, a monitor application from TotalPhase and Wireshark to look at the link between the Beagle and this monitor application.</p><p>Now you'll have to use the monitor application to instruct the Beagle to capture the I2C comms and send them back over the USB interface. It's this communication you can capture using Wireshark.</p><p>Unless the Beagle has an RPCAP interface it won't take instructions from Wireshark directly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '12, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-15972" class="comments-container"><span id="15973"></span><div id="comment-15973" class="comment"><div id="post-15973-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for your reply.</p><p>Actually I can't figure out how to instruct the beagle to capture and send back i2c comms to the usb interface. It seems to react only to its monitor. If there is a way to do this, it would be real-time monitoring, what I would like to do.</p><p>However, I found the link <a href="http://wiki.wireshark.org/IPMB_protocol">http://wiki.wireshark.org/IPMB_protocol</a> which explains how to campure IPMI commands. Unfortunatly, it seems that the only way is to use the 'i2c_analyzer' (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1970)">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1970)</a> to capture i2c comms and then import then into wireshark after the creation of the pcap file using 'text2pcap'. When I try to open the associated pcap file with wireshark the Protocol is 'unknown' and no packets are read...I have the same problem with the examples capture file as well. (the IPMI is correctly checked on Analyze/Enabled Protocols).</p><p>Thank you very much for any your advice.</p></div><div id="comment-15973-info" class="comment-info"><span class="comment-age">(16 Nov '12, 09:26)</span> matte87</div></div></div><div id="comment-tools-15972" class="comment-tools"></div><div class="clear"></div><div id="comment-15972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16003"></span>

<div id="answer-container-16003" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16003-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>I tried to make some progress for my goal. I took a look to all the files reported into the Bug repository and it seems that the installation of the IPMB plugin is necessary.</p><p>Therefore, my first question is why do I need to add this plugin if wireshark already comes out with a ipmb dissector?</p><p>Anyway, I tried to add this plugin and I faced a more common problem..</p><p>In order to install the plugin I followed the README.plugin procedure. Since the plugin souce files are given, I just make the suggested modifications to the <a href="http://Makefile.am">Makefile.am</a>, <a href="http://Cmaketlist.txt">Cmaketlist.txt</a> etc...</p><p>and then I execute:</p><p>./autogen.sh ./configure make</p><p>The compiling process correctly starts but after a while I get this error concerning the the plugin directory:</p><p>make[3]: Leaving directory <code>/home/userme/wireshark-1.8.3/plugins/gryphon'  Making all in ipmb  make[3]: Entering directory</code>/home/userme/wireshark-1.8.3/plugins/ipmb' make[3]: <strong><em>No rule to make target <code>all'.  Stop.  make[3]: Leaving directory</code>/home/userme/wireshark-1.8.3/plugins/ipmb' make[2]:</em></strong> [all-recursive] Error 1 make[2]: Leaving directory <code>/home/userme/wireshark-1.8.3/plugins'  make[1]: *** [all-recursive] Error 1  make[1]: Leaving directory</code>/home/userme/wireshark-1.8.3' make: *** [all] Error 2</p><p>I'm using Ubuntu 10.04 LTS (2.6.32-45-generic) wireshark 1.8.3 Python 2.6.5 Perl, v5.10.1 GNU sed version 4.2.1 flex 2.5.35 bison (GNU Bison) 2.4.1 autoconf 2.13 automake 1.9.6</p><p>I hope that someone will help me to found a solution..</p><p>Thank you very much.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '12, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/e2b74c2c5818f2dc9e2436b235e2762e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matte87&#39;s gravatar image" /><p>matte87<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matte87 has no accepted answers">0%</span></p></div></div><div id="comments-container-16003" class="comments-container"></div><div id="comment-tools-16003" class="comment-tools"></div><div class="clear"></div><div id="comment-16003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

