+++
type = "question"
title = "Snow Leopard running Fusion has virtual ports invisible to wireshark"
description = '''Win XP SP3 in fusion can surf the net through the mac&#x27;s airport in either bridged or nat mode fine. the mac has a static ip. the windows is set to dhcp. ifconfig on the mac shows en1: inet 192.168.1.43 netmask 0xffffff00 broadcast 192.168.1.255 vmnet1: inet 172.16.193.1 netmask 0xffffff00 broadcast ...'''
date = "2011-07-24T07:30:00Z"
lastmod = "2011-07-27T05:12:00Z"
weight = 5188
keywords = [ "fusion", "mac", "vmware" ]
aliases = [ "/questions/5188" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Snow Leopard running Fusion has virtual ports invisible to wireshark](/questions/5188/snow-leopard-running-fusion-has-virtual-ports-invisible-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5188-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Win XP SP3 in fusion can surf the net through the mac's airport in either bridged or nat mode fine. the mac has a static ip. the windows is set to dhcp.</p><p>ifconfig on the mac shows</p><p>en1: inet 192.168.1.43 netmask 0xffffff00 broadcast 192.168.1.255</p><p>vmnet1: inet 172.16.193.1 netmask 0xffffff00 broadcast 172.16.193.255</p><p>vmnet8: inet 172.16.143.1 netmask 0xffffff00 broadcast 172.16.143.255</p><p>ipconfig on windows shows</p><pre><code>Connection-specific DNS Suffix . : home
IP Address. . . . . . . . . . . . : 192.168.1.42
Subnet Mask . . . . . . . . . . . : 255.255.255.0
Default Gateway . . . . . . . . . : 192.168.1.1</code></pre><p>when the network adapter settings in fusion are changed to NAT and the ipconfig is released and renewed, then ipconfig shows</p><pre><code>Connection-specific DNS Suffix  . : localdomain
IP Address. . . . . . . . . . . . : 172.16.143.132
Subnet Mask . . . . . . . . . . . : 255.255.255.0
Default Gateway . . . . . . . . . : 172.16.143.2</code></pre><p>This shows that the virtual machine is now going through the subnet of vmnet8 Wireshark however does not reveal vmnet8, just en0 and en1-and en1 is getting all the traffic. Why no vmnet8? Why is vmnet8 getting a routable address? shouldn't it be one of those non-routeable 192.xxx.xxx.xxx or 10.xxx.xxx.xxx numbers? And even if windows is bridged and using 192.168.1.42, little snitch on the mac keeps asking if vmnet-natd can talk to the net so i know it's active.</p><p>I can see packets going to the windows ip but it's mixed in with traffic going to the mac (as I'd expect since they are both using the same airport) but it's all going over en1.</p><p>( btw, i dont understand why the gateway in windows is not 172.16.143.1 but rather .2 - after all doesnt the windows box have to talk to vmnet8?)</p></div><div id="question-tags" class="tags-container tags">fusion mac vmware</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '11, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/9e8a91c87607327105bfdf3fc8a7c337?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bwanaaa&#39;s gravatar image" /><p>bwanaaa<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bwanaaa has no accepted answers">0%</span></p></div></div><div id="comments-container-5188" class="comments-container"></div><div id="comment-tools-5188" class="comment-tools"></div><div class="clear"></div><div id="comment-5188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5191"></span>

<div id="answer-container-5191" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5191-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all lets get the idea of "non-routable" addresses straight. The ranges 10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16 are reserved for private use. This means they are not routed on the Internet, but they are perfectly routable in private networks (like your VM fusion setup). See also <a href="http://www.ietf.org/rfc/rfc1918.txt">RFC 1918</a> for more information on these IP ranges.</p><p>The addresses assigned to vmnet1 and vmnet8 are within these private address ranges. The reason your XP guest has 172.16.143.2 as gateway and not 172.16.143.1, is that the NAT deamon used by VMware Fusion has it's own address (.2), that's just the way VMware has implemented it.</p><p>Unfortunately the vmnet interfaces are not visible to libpcap (which is used by Wireshark to capture packets), so you can't use Wireshark to capture on these (virtual) interfaces. However, VMware has provided the tool "vmnet-sniffer", which makes it possible to capture on these interfaces. See <a href="http://communities.vmware.com/thread/177416">http://communities.vmware.com/thread/177416</a> for more info on using "vmnet-sniffer".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '11, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5191" class="comments-container"><span id="5194"></span><div id="comment-5194" class="comment"><div id="post-5194-score" class="comment-score"></div><div class="comment-text"><p>thank you for that. dunno why i forgot bout 172.xxx.xxx.xxx.</p><p>i tried the vmnet-sniffer</p><p>dumbuser$ vmnet-sniffer -e vmnet8 -w testdump</p><p>and it gave a blank line-no prompt or anything so i assumed the process was capturing. i did stuff but then did not know how to stop the capture. I hit ctrl C but no capture file was saved. I guess this is a vmware question from here. But just to let you know, i tried the same experiment with parallels 6, and wireshark can see those virtual adapters , vNIC0 and vNIC1. But guess what, no traffic is seen on them when wireshark is running on the host.</p></div><div id="comment-5194-info" class="comment-info"><span class="comment-age">(24 Jul '11, 13:41)</span> bwanaaa</div></div><span id="5196"></span><div id="comment-5196" class="comment"><div id="post-5196-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment", please see the FAQ for details)</p></div><div id="comment-5196-info" class="comment-info"><span class="comment-age">(24 Jul '11, 15:44)</span> SYN-bit ♦♦</div></div><span id="5203"></span><div id="comment-5203" class="comment"><div id="post-5203-score" class="comment-score"></div><div class="comment-text"><p>I just tried the vmnet-sniffer command on my own MacbookPro with Fusion and it does work as expected. Did you use"sudo"?</p></div><div id="comment-5203-info" class="comment-info"><span class="comment-age">(24 Jul '11, 23:57)</span> SYN-bit ♦♦</div></div><span id="5251"></span><div id="comment-5251" class="comment"><div id="post-5251-score" class="comment-score"></div><div class="comment-text"><p>yes i can get it to start but how do you stop it, save the fle, and gracefully exit from terminal?</p></div><div id="comment-5251-info" class="comment-info"><span class="comment-age">(26 Jul '11, 04:59)</span> bwanaaa</div></div><span id="5254"></span><div id="comment-5254" class="comment"><div id="post-5254-score" class="comment-score"></div><div class="comment-text"><p>The "-w &lt;file&gt;" option makes the output go to file in libpcap format so that you can read the file in Wireshark.</p><p>There are no options to stop the capture automatically, so manually pressing "&lt;ctrl&gt;+C" is the right way to go.</p><p>After that, you can close the terminal window and open the file in Wireshark.</p></div><div id="comment-5254-info" class="comment-info"><span class="comment-age">(26 Jul '11, 05:51)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-5191" class="comment-tools"></div><div class="clear"></div><div id="comment-5191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5307"></span>

<div id="answer-container-5307" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5307-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>tnx. i learned that the w option doesnt work on a mac, rather one needs to do</p><p>sudo vmnet-sniffer -e vmnet8 &gt;outputfile.pcap</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '11, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/9e8a91c87607327105bfdf3fc8a7c337?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bwanaaa&#39;s gravatar image" /><p>bwanaaa<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bwanaaa has no accepted answers">0%</span></p></div></div><div id="comments-container-5307" class="comments-container"><span id="5324"></span><div id="comment-5324" class="comment"><div id="post-5324-score" class="comment-score"></div><div class="comment-text"><p>That must be something on "your" Mac then, cause VMware fusion is a Mac Application, also the -w option does indeed work on "my" Mac.</p><p>Maybe you could check the VMware forums or create a case with VMware?</p></div><div id="comment-5324-info" class="comment-info"><span class="comment-age">(27 Jul '11, 11:01)</span> SYN-bit ♦♦</div></div><span id="5330"></span><div id="comment-5330" class="comment"><div id="post-5330-score" class="comment-score"></div><div class="comment-text"><p>that was what the vmware moderator suggested actually.</p><p>and this does not work when in the vmware directory sudo vmnet-sniffer -e vmnet8 &gt;./tmp/outputfile.pcap permission denied</p><p>but this does work sudo vmnet-sniffer -e vmnet8 &gt;/tmp/outputfile.pcap</p><p>but that's a vmware question too.</p></div><div id="comment-5330-info" class="comment-info"><span class="comment-age">(27 Jul '11, 15:13)</span> bwanaaa</div></div></div><div id="comment-tools-5307" class="comment-tools"></div><div class="clear"></div><div id="comment-5307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

