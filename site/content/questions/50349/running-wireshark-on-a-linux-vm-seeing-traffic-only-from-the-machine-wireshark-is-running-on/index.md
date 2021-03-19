+++
type = "question"
title = "Running Wireshark on a Linux VM, seeing traffic only from the machine Wireshark is running on..."
description = '''I have a Virtual machine running LINUX (ubuntu 14.04). This machine (server) has a physical port running in promiscuous mode connected to a SPAN (mirror) port on core switch (it is monitoring), and a virtual port setup for management (has IP for connection and data pulling). Whenever I run wireshark...'''
date = "2016-02-19T10:24:00Z"
lastmod = "2016-02-25T11:32:00Z"
weight = 50349
keywords = [ "vmware" ]
aliases = [ "/questions/50349" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Running Wireshark on a Linux VM, seeing traffic only from the machine Wireshark is running on...](/questions/50349/running-wireshark-on-a-linux-vm-seeing-traffic-only-from-the-machine-wireshark-is-running-on)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50349-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Virtual machine running LINUX (ubuntu 14.04). This machine (server) has a physical port running in promiscuous mode connected to a SPAN (mirror) port on core switch (it is monitoring), and a virtual port setup for management (has IP for connection and data pulling). Whenever I run wireshark, I am only seeing traffic that on the Linux server. I am not picking up any traffic on the SPAN port. Why not ?</p></div><div id="question-tags" class="tags-container tags">vmware</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '16, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/7dc1fee5b4e29c4e6cc3d5059312aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msmorten&#39;s gravatar image" /><p>msmorten<br />
<span class="score" title="4 reputation points">4</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msmorten has no accepted answers">0%</span></p></div></div><div id="comments-container-50349" class="comments-container"></div><div id="comment-tools-50349" class="comment-tools"></div><div class="clear"></div><div id="comment-50349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="50350"></span>

<div id="answer-container-50350" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50350-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming by the "vmware" tag that you're running a VMware host. If it's ESXi you'll have to enable promiscuous mode on the vSwitch as described in <a href="https://kb.vmware.com/selfservice/search.do?cmd=displayKC&amp;docType=kc&amp;docTypeID=DT_KB_1_1&amp;externalId=1004099">KB 1004099</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '16, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-50350" class="comments-container"><span id="50351"></span><div id="comment-50351" class="comment"><div id="post-50351-score" class="comment-score"></div><div class="comment-text"><p>This has been done, as far as I know. But I will have my Windows Server admin double check these settings for me. Thanks for the feedback.</p></div><div id="comment-50351-info" class="comment-info"><span class="comment-age">(19 Feb '16, 11:15)</span> msmorten</div></div><span id="50352"></span><div id="comment-50352" class="comment"><div id="post-50352-score" class="comment-score"></div><div class="comment-text"><p>Confirmed with my Server admin that all of these settings are absolutely correct. He is very thorough and showed my these settings are in fact correct, however, when using wireshark, my "host" ip is the IP of the server I have WS running on and not the traffic that is running across the SPAN. I am just so confused as to where what my issue here could be.</p><p>Host: 172.16.4.89 - IP OF THE LINUX BOX I'M on ( and all of my captures are this way) User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0 Accept: <em>/</em></p></div><div id="comment-50352-info" class="comment-info"><span class="comment-age">(19 Feb '16, 11:22)</span> msmorten</div></div></div><div id="comment-tools-50350" class="comment-tools"></div><div class="clear"></div><div id="comment-50350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50355"></span>

<div id="answer-container-50355" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50355-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, after working with "XRDP" and getting a graphical look at wireshark, I found that in this program, it was setup to promiscuous mode for the "ETH0" port. This was for some reason unnecessary based on the fact that the port was properly set to this mode out side of the program. After deselecting this and viewing the captures in a graphical interface, I am seeing more traffic than what destined to my interface.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '16, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/7dc1fee5b4e29c4e6cc3d5059312aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msmorten&#39;s gravatar image" /><p>msmorten<br />
<span class="score" title="4 reputation points">4</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msmorten has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-50355" class="comments-container"><span id="50494"></span><div id="comment-50494" class="comment"><div id="post-50494-score" class="comment-score"></div><div class="comment-text"><p>And after further research, this is still an issue. The Linux VMware server isn't seeing the promiscuous port so wireshark isn't seeing anything but traffic destined to the management port.<br />
</p></div><div id="comment-50494-info" class="comment-info"><span class="comment-age">(24 Feb '16, 17:59)</span> msmorten</div></div><span id="50501"></span><div id="comment-50501" class="comment"><div id="post-50501-score" class="comment-score">1</div><div class="comment-text"><p>What does the <code>ifconfig</code> shell command output on the Ubuntu machine?</p><p>And what does <code>tshark -D</code> output?</p></div><div id="comment-50501-info" class="comment-info"><span class="comment-age">(25 Feb '16, 03:05)</span> sindy</div></div></div><div id="comment-tools-50355" class="comment-tools"></div><div class="clear"></div><div id="comment-50355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50512"></span>

<div id="answer-container-50512" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>COOL.I make these posts after a meeting and have become frustrated. Get back to my desk after thinking about it and find out that the problem is normally me. So after doing a "ifconfig" I only see "ETH0" and "lo". BUT if I do and "ifconfig -a" I see an unassigned port..."eth1"... There is my interface that needs to be configured that was setup and assigned to my VM environment as promiscuous by my Windows system admin. After setting up the interface in /etc/network/interfaces with the proper commands to get the interface setup as "promiscuous", I am able to use wireshark to get information from my SPAN port. I could have also run the commands.</p><p><strong>ifconfig eth1 up ifconfig eth1 promisc</strong></p><p>to temporarily get it up, but I wanted the interface to come back after a reboot or whatever. I also added the above commands to /etc/rc.local so that the interface will stay up... ( I think that's why those commands are there) lol. .. Any way, I was able to get the interface up and running once I located it. I just never knew it was there because it never showed up under a normal <strong>ifconfig</strong></p><p>THE COMMANDS BELOW ARE LIKE A TIME LINE OF HOW I WENT ABOUT SETTING UP THE INTERFACE.</p><h1 id="ifconfig"><strong>ifconfig</strong></h1><p>eth0 Link encap:Ethernet HWaddr 00:0c:29:5c:81:e0 inet addr:172.16.4.89 Bcast:172.16.4.255 Mask:255.255.255.0 inet6 addr: fe80::20c:29ff:fe5c:81e0/64 Scope:Link UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1 RX packets:33338134 errors:0 dropped:0 overruns:0 frame:0 TX packets:228793969 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:1000 RX bytes:2497495424 (2.4 GB) TX bytes:523594338379 (523.5 GB)</p><p>lo Link encap:Local Loopback inet addr:127.0.0.1 Mask:255.0.0.0 inet6 addr: ::1/128 Scope:Host UP LOOPBACK RUNNING MTU:65536 Metric:1 RX packets:560399756 errors:0 dropped:0 overruns:0 frame:0 TX packets:560399756 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:0 RX bytes:1479271113780 (1.4 TB) TX bytes:1479271113780 (1.4 TB)</p><p>:/# <strong>ifconfig -a</strong> eth0 Link encap:Ethernet HWaddr 00:0c:29:5c:81:e0 inet addr:172.16.4.89 Bcast:172.16.4.255 Mask:255.255.255.0 inet6 addr: fe80::20c:29ff:fe5c:81e0/64 Scope:Link UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1 RX packets:33738969 errors:0 dropped:0 overruns:0 frame:0 TX packets:228895529 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:1000 RX bytes:2573209836 (2.5 GB) TX bytes:523620839695 (523.6 GB)</p><p><strong>eth1 Link encap:Ethernet HWaddr 00:0c:29:5c:81:ea BROADCAST MULTICAST MTU:1500 Metric:1 RX packets:0 errors:0 dropped:0 overruns:0 frame:0 TX packets:0 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:1000 RX bytes:0 (0.0 B) TX bytes:0 (0.0 B)</strong></p><p>lo Link encap:Local Loopback inet addr:127.0.0.1 Mask:255.0.0.0 inet6 addr: ::1/128 Scope:Host UP LOOPBACK RUNNING MTU:65536 Metric:1 RX packets:560565049 errors:0 dropped:0 overruns:0 frame:0 TX packets:560565049 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:0 RX bytes:1479443551265 (1.4 TB) TX bytes:1479443551265 (1.4 TB)</p><p><strong>ifconfig</strong> eth1 Link encap:Ethernet HWaddr 00:0c:29:5c:81:ea inet6 addr: fe80::20c:29ff:fe5c:81ea/64 Scope:Link UP BROADCAST RUNNING <strong>PROMISC</strong> MULTICAST MTU:1500 Metric:1 RX packets:168274261 errors:0 dropped:16365 overruns:0 frame:0 TX packets:16 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:1000 <strong>RX bytes:155986089864 (155.9 GB) TX bytes:1296 (1.2 KB)</strong></p><p><strong>netstat -i</strong> Kernel Interface table Iface MTU Met RX-OK RX-ERR RX-DRP RX-OVR TX-OK TX-ERR TX-DRP TX-OVR Flg eth0 1500 0 3267113 0 0 0 19271185 0 0 0 BMRU <strong>eth1</strong> 1500 0 168474659 0 16365 0 16 0 0 0 <strong>BMPRU</strong> lo 65536 0 36303118 0 0 0 36303118 0 0 0 LRU</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '16, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/7dc1fee5b4e29c4e6cc3d5059312aac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msmorten&#39;s gravatar image" /><p>msmorten<br />
<span class="score" title="4 reputation points">4</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msmorten has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-50512" class="comments-container"></div><div id="comment-tools-50512" class="comment-tools"></div><div class="clear"></div><div id="comment-50512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

