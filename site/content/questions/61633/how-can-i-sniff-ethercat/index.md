+++
type = "question"
title = "How can I sniff EtherCAT ?"
description = '''Hi, OK, first time using Wireshark, and it fell at the first hurdle, hmm. Can some kind person help? I&#x27;m trying to use to sniff an EtherCAT packet. Just to verify, that my understanding of size, is correct. Wireshark says it works with EtherCAT. However, I get error dialogue about Wireshark being un...'''
date = "2017-05-26T00:52:00Z"
lastmod = "2017-05-26T02:09:00Z"
weight = 61633
keywords = [ "promiscuous", "ethercat", "mode" ]
aliases = [ "/questions/61633" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I sniff EtherCAT ?](/questions/61633/how-can-i-sniff-ethercat)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61633-score" class="post-score" title="current number of votes">0</div><span id="post-61633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>OK, first time using Wireshark, and it fell at the first hurdle, hmm. Can some kind person help? I'm trying to use to sniff an EtherCAT packet. Just to verify, that my understanding of size, is correct. Wireshark says it works with EtherCAT.</p><p>However, I get error dialogue about Wireshark being unable to initiate capture session, and 'failed to set hardware filter to promiscuous mode'. And to check <a href="https://wiki.wireshark.org/WinPcap">https://wiki.wireshark.org/WinPcap</a> and <a href="https://wiki.wireshark.org/CaptureSetup.">https://wiki.wireshark.org/CaptureSetup.</a> Nothing relevant there, unfortunately, nor google.</p><p>I have an image of the dialogue, that I can PM if need be. Seems I need 60 points on this forum, to be able to post images.</p><p>I have 2 other network adaptors on the PC, used for regular Ethernet traffic, and Wireshark can sniff those fine. I don't know if it's relevant, but those two are external USB-connected network adaptors (both ASIX AX88179 USB 3.0 to Gigabit Ethernet models). Whereas the adaptor used for EtherCAT, is the PC onboard network adaptor. I have to use the latter for EtherCAT, as it won't work with the external adaptors, reason unknown. None of the 3 network adaptors expose a 'promiscuous mode' setting in their properties. I am familiar with what 'promiscuous mode' is. I have admin rights on the PC.</p><p>The setup I have, is a PC-based and Visual-Studio-2010-hosted Beckhoff-provided TwinCAT3 master project. It communicates with an EtherCAT slave running on an Infineon XMC4300 CPU. This created using the Infineon DAVE4.3.2 IDE, using an Infineon-provided example EtherCAT project. This uses the DAVE ECAT_SSC APP component, and Beckhoff-provided ET9300 Slave Stack Code (SSC) Tool, to configure the values to be provided to the TwinCAT3 master. And all works, fine.</p><p>I've tried starting Wireshark before the master and slave start communicating, as well as after, with the same results.</p><p>I'm not quite sure I understand why Wireshark needs to place the adaptor in promiscuous mode. As I understand, this makes the adaptor accept all packets, not just those with its' IP address. I don't need the adaptor to accept packets which are not addressed to it. I would just like to capture one packet intended for it.</p><p>I've tried each of the following, same results: Turning off the 'Capture packets in promiscuous mode' setting, in Wireshark Edit &gt; Preferences &gt; Capture. Turning off the other 3 options there. Setting the default interface to the onboard network adaptor. Restarting Wireshark. Rebooting PC.</p><p>I suspect, that because the turning off the first option gave same results, the error dialogue indication that inability to set promiscuous mode, is the problem, is infact, a red-herring.</p><p>I'm using the latest Wireshark, Version 2.2.6 (v2.2.6.0-g32dac6a), downloaded and installed this morning, from the Wireshark website.</p><p>Any ideas, anyone ?</p><p>Ah, found the answer! Nothing like explaining the problem, to elicit the solution. It's to select 'Promiscuous Mode (use with Wireshark only)' setting (of course !), in I/O &gt; Devices &gt; mydevice &gt; Adapter settings, in the TwinCAT3 project..</p><p>Many thanks,</p><p>David King</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-ethercat" rel="tag" title="see questions tagged &#39;ethercat&#39;">ethercat</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '17, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/6a8e521520f40114dc5de2e0c7789afc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20King&#39;s gravatar image" /><p><span>David King</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David King has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 May '17, 01:12</strong> </span></p></div></div><div id="comments-container-61633" class="comments-container"><span id="61635"></span><div id="comment-61635" class="comment"><div id="post-61635-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/32933/david-king">@David King</a>,</p><p>Please post your "answer" as an answer and accept it to help others in future.</p></div><div id="comment-61635-info" class="comment-info"><span class="comment-age">(26 May '17, 02:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-61633" class="comment-tools"></div><div class="clear"></div><div id="comment-61633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61637"></span>

<div id="answer-container-61637" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61637-score" class="post-score" title="current number of votes">0</div><span id="post-61637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="grahamb has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ah, found the answer! Nothing like explaining the problem, to elicit the solution. It's to select 'Promiscuous Mode (use with Wireshark only)' setting (of course !), in I/O &gt; Devices &gt; mydevice &gt; Adapter settings, in the TwinCAT3 project..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '17, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/6a8e521520f40114dc5de2e0c7789afc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20King&#39;s gravatar image" /><p><span>David King</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David King has one accepted answer">100%</span></p></div></div><div id="comments-container-61637" class="comments-container"></div><div id="comment-tools-61637" class="comment-tools"></div><div class="clear"></div><div id="comment-61637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

