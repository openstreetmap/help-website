+++
type = "question"
title = "Capturing Voip Correct Procedure"
description = '''OS WindowsXP Home with intel 82566DC-2 network card and it also displays adaptor generic for dialup and VPN -- I&#x27;m on a wireless home network and attempting to capture the calls from a remote machine (2wire router 2701HG-S) I&#x27;m firing up wireshark,selecting the Intel network card and capturing all t...'''
date = "2010-12-14T03:53:00Z"
lastmod = "2010-12-15T06:57:00Z"
weight = 1340
keywords = [ "capture", "troubleshooting", "voip" ]
aliases = [ "/questions/1340" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Voip Correct Procedure](/questions/1340/capturing-voip-correct-procedure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1340-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OS WindowsXP Home with intel 82566DC-2 network card and it also displays adaptor generic for dialup and VPN -- I'm on a wireless home network and attempting to capture the calls from a remote machine (2wire router 2701HG-S) I'm firing up wireshark,selecting the Intel network card and capturing all the traffic, no filters I'm then selecting Voip calls from the Telephony tab I'm not able to capture any traffic Is this the correct procedure. I did a lot of searching on the Internet but I can find basically nothing. I am brand spankin new to wirshark so any assistance would be greatly greatly appreciated</p></div><div id="question-tags" class="tags-container tags">capture troubleshooting voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '10, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/6d9ae90b0c98a3e4f2fc583cf52e3233?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amberdevo&#39;s gravatar image" /><p>amberdevo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amberdevo has no accepted answers">0%</span></p></div></div><div id="comments-container-1340" class="comments-container"><span id="9895"></span><div id="comment-9895" class="comment"><div id="post-9895-score" class="comment-score"></div><div class="comment-text"><p>Was this problem solved? I am having the same problem. When I run wireshark, i see the ip addresses of the phones, with udp and arp. but when i go to Telephony-VOIP calls, there isnt anything. I want to be able to capture the VOIP call and be able to play it back. Can anyone help yrgently please?</p><p>Agnes</p></div><div id="comment-9895-info" class="comment-info"><span class="comment-age">(02 Apr '12, 02:17)</span> AgnesKs</div></div></div><div id="comment-tools-1340" class="comment-tools"></div><div class="clear"></div><div id="comment-1340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1342"></span>

<div id="answer-container-1342" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1342-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the wireshark wiki answers your question best. Have a look at the following pages:</p><ul><li><a href="http://wiki.wireshark.org/CaptureSetup">CaptureSetup</a>: How to setup your network to successfully capture packets</li><li><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">CaptureSetup/Ethernet</a>: Discusses capturing on switched Ethernet networks</li><li><a href="http://wiki.wireshark.org/CaptureSetup/WLAN">CaptureSetup/WLAN</a>: Frequently asked WLAN capture setup info</li></ul><p>These pages will give some insight on how to capture packets and which packets can be seen depending on the place where you are capturing.</p><p>As soon as you have captured the VoIP packets, indeed selectiong "VoIP calls" from the Telephony tab will show you the VoIP calls in your tracefile.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '10, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1342" class="comments-container"></div><div id="comment-tools-1342" class="comment-tools"></div><div class="clear"></div><div id="comment-1342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1358"></span>

<div id="answer-container-1358" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1358-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are capturing everything then you are capturing your VOIP also - it will be in the file. Note that WS cannot identify all VOIP conversations. Look for lots of UDP or RTP packets in the file - theres your VOIP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '10, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/414ce7eff9701dc3a5c2e792f1608ee2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="minorthreat&#39;s gravatar image" /><p>minorthreat<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="minorthreat has no accepted answers">0%</span></p></div></div><div id="comments-container-1358" class="comments-container"><span id="9901"></span><div id="comment-9901" class="comment"><div id="post-9901-score" class="comment-score"></div><div class="comment-text"><p>NB VoIP is a vide term, wireshark Dissects a number of VoIP protocols but some are proprietary like skype and will not show up as a VoIP call.</p></div><div id="comment-9901-info" class="comment-info"><span class="comment-age">(02 Apr '12, 10:18)</span> Anders ♦</div></div></div><div id="comment-tools-1358" class="comment-tools"></div><div class="clear"></div><div id="comment-1358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

