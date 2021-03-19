+++
type = "question"
title = "Adding VLAN Tag on Wireshark capture"
description = '''Hi all, I have basic Wireshark capture (HTTP, CAP format) I would like to put VLAN Tag label on this capture, I mean I want to have the original capture with encapsulate of VLAN ID. For this purpose I having Cisco SW Layer 2 and Layer 3 if needed and two PCs , I am using “bittwist” software to injec...'''
date = "2012-05-10T00:06:00Z"
lastmod = "2012-05-10T16:01:00Z"
weight = 10868
keywords = [ "adding", "vlan", "bittwist", "tagging", "wireshark" ]
aliases = [ "/questions/10868" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Adding VLAN Tag on Wireshark capture](/questions/10868/adding-vlan-tag-on-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10868-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I have basic Wireshark capture (HTTP, CAP format) I would like to put VLAN Tag label on this capture, I mean I want to have the original capture with encapsulate of VLAN ID. For this purpose I having Cisco SW Layer 2 and Layer 3 if needed and two PCs , I am using “bittwist” software to inject the XXX.CAP capture to the SW. I also tried to do span port (Monitoring port) at Layer 2 SW but I didn’t success to see VLAN tag at the destination port (I add the column of dot1q at the Wireshark Software)<br />
</p><p>Anyone can figure how to do it ?</p></div><div id="question-tags" class="tags-container tags">adding vlan bittwist tagging wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '12, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/0cd56c61152785b5e3b6153e49dc62ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ariel%20Goldenberg&#39;s gravatar image" /><p>Ariel Golden...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ariel Goldenberg has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-10868" class="comments-container"></div><div id="comment-tools-10868" class="comment-tools"></div><div class="clear"></div><div id="comment-10868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10869"></span>

<div id="answer-container-10869" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10869-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming that your CAP file (that you're injecting using bittwist) has in fact VLAN tags. If you're setting up a span port you need to tell the switch to keep the VLAN information intact, because Cisco switches remove the VLAN tag when spanning. You should set up your monitor session with the "encapsulation dot1q" parameter when defining it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '12, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10869" class="comments-container"><span id="10872"></span><div id="comment-10872" class="comment"><div id="post-10872-score" class="comment-score"></div><div class="comment-text"><p>Wow thanks for your quick response, I don’t know if the CAP file was in VLAN tag, I did exactly what you suggest with the span port (LACP). Look at the configuration file , I’m using Cisco SW 2940 Ver. 12.1(22).</p><p><a href="http://www.fileflyer.com/view/vc7RpBW">http://www.fileflyer.com/view/vc7RpBW</a></p></div><div id="comment-10872-info" class="comment-info"><span class="comment-age">(10 May '12, 00:57)</span> Ariel Golden...</div></div><span id="10874"></span><div id="comment-10874" class="comment"><div id="post-10874-score" class="comment-score"></div><div class="comment-text"><p>Looks like I would need a code to unlock the file... strange service to host a file. Maybe you can just post your monitor command sequence - that could speed things up.</p><p>Anyway, the CAP file you're injecting using bittwist should contain VLAN tags, which you can easily verify by looking at the file in Wireshark - if it has VLAN tags, it will show them :-) Then, after you made sure the file has VLAN tags you can do the injection, and your monitor port should show the packets with tags if your SPAN session is configured correctly.</p></div><div id="comment-10874-info" class="comment-info"><span class="comment-age">(10 May '12, 01:09)</span> Jasper ♦♦</div></div><span id="10890"></span><div id="comment-10890" class="comment"><div id="post-10890-score" class="comment-score"></div><div class="comment-text"><p>The file witout VLAN Tag (Only regular HTTP),</p><p>monitor session 1 source interface Fa0/1 monitor session 1 destination interface Fa0/8 encapsulation dot1q ingress vlan 100</p><p>Here another link for this file <a href="http://www.2shared.com/document/eNpVe4-a/Configuration.html">http://www.2shared.com/document/eNpVe4-a/Configuration.html</a></p><p>Thanks</p></div><div id="comment-10890-info" class="comment-info"><span class="comment-age">(10 May '12, 02:29)</span> Ariel Golden...</div></div><span id="10891"></span><div id="comment-10891" class="comment"><div id="post-10891-score" class="comment-score">1</div><div class="comment-text"><p>The monitor session configuration looks okay - if you want to add VLAN tags by injecting it on a trunk and then capture the tagged packets the monitor session should just do that. Of course your NIC that you capture with must be able to accept VLAN tagged frames (and not drop them, as some do).</p><p>But if you just want add VLAN tags to your file you could do that with tcprewrite, for example:</p><p><strong>tcprewrite --enet-vlan=add --enet-vlan-tag=40 --enet-vlan-cfi=1 --enet-vlan-pri=4 --infile=input.pcap --outfile=output.pcap</strong></p><p>See <a href="http://tcpreplay.synfin.net/wiki/tcprewrite">http://tcpreplay.synfin.net/wiki/tcprewrite</a></p></div><div id="comment-10891-info" class="comment-info"><span class="comment-age">(10 May '12, 02:38)</span> Jasper ♦♦</div></div><span id="10892"></span><div id="comment-10892" class="comment"><div id="post-10892-score" class="comment-score"></div><div class="comment-text"><p>Let me try with tcpwrite ...</p></div><div id="comment-10892-info" class="comment-info"><span class="comment-age">(10 May '12, 02:46)</span> Ariel Golden...</div></div><span id="10893"></span><div id="comment-10893" class="comment not_top_scorer"><div id="post-10893-score" class="comment-score"></div><div class="comment-text"><p>can you send me the download link .... Should I need to use Linux or there is Windows Compatible version?</p></div><div id="comment-10893-info" class="comment-info"><span class="comment-age">(10 May '12, 02:52)</span> Ariel Golden...</div></div><span id="10894"></span><div id="comment-10894" class="comment not_top_scorer"><div id="post-10894-score" class="comment-score"></div><div class="comment-text"><p>Downloads are at <a href="http://tcpreplay.synfin.net/wiki/Download">http://tcpreplay.synfin.net/wiki/Download</a> - but I think they're all source code only, so you'd have to compile it first. There probably are binaries in the various Linux distribution package management systems, but I haven't checked lately. On Debian/Ubuntu you could do an "apt-cache search tcprewrite" which should tell you if there is a package.</p><p>I always used the linux version myself, so I can't tell you if the Windows version is any good.</p></div><div id="comment-10894-info" class="comment-info"><span class="comment-age">(10 May '12, 03:05)</span> Jasper ♦♦</div></div><span id="10896"></span><div id="comment-10896" class="comment not_top_scorer"><div id="post-10896-score" class="comment-score"></div><div class="comment-text"><p>There is no Windows release of tcpreplay ?</p></div><div id="comment-10896-info" class="comment-info"><span class="comment-age">(10 May '12, 04:49)</span> Ariel Golden...</div></div><span id="10898"></span><div id="comment-10898" class="comment not_top_scorer"><div id="post-10898-score" class="comment-score"></div><div class="comment-text"><p>Well, there is a source you could compile, but then again that is not something we're used to do on Windows... so unless you can compile it or find someone to do that for you there is binary release afaik.</p></div><div id="comment-10898-info" class="comment-info"><span class="comment-age">(10 May '12, 07:44)</span> Jasper ♦♦</div></div><span id="10964"></span><div id="comment-10964" class="comment not_top_scorer"><div id="post-10964-score" class="comment-score"></div><div class="comment-text"><p>I couldn’t success to install it on Linux, I don’t have experience with LINUX , Can I have this application “tcp replay” “tcpwrite” to WINDOWS platform ?</p></div><div id="comment-10964-info" class="comment-info"><span class="comment-age">(13 May '12, 04:50)</span> Ariel Golden...</div></div></div><div id="comment-tools-10869" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-10869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10908"></span>

<div id="answer-container-10908" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10908-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you checked whether your NIC strips the vlan tags before Wireshark gets hold of the packets? Have a look at <a href="http://wiki.wireshark.org/CaptureSetup/VLAN">http://wiki.wireshark.org/CaptureSetup/VLAN</a> for instructions for configuring several NICs to <em>not</em> strip the vlan tags.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '12, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10908" class="comments-container"><span id="10963"></span><div id="comment-10963" class="comment"><div id="post-10963-score" class="comment-score"></div><div class="comment-text"><p>I want to be clear , I'm having Capture (Without VLAN TAG). I want to have this Capture with VLAN tagging (VLAN 100 for example)</p><p>The scenario I having is: I play this capture from my PC with bittwist to Cisco SW (port1) and configure monitor port from port 1 to destination port 8 , I connect at port 8 PC with Wireshark and I want to recorder this Capture with VLAN Tag.</p></div><div id="comment-10963-info" class="comment-info"><span class="comment-age">(13 May '12, 04:48)</span> Ariel Golden...</div></div></div><div id="comment-tools-10908" class="comment-tools"></div><div class="clear"></div><div id="comment-10908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

