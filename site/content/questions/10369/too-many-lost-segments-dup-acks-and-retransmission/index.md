+++
type = "question"
title = "Too many lost segments, Dup Acks and retransmission"
description = '''Hi all, I am building a new network and I started monitoring the network using Wireshark. All the switches are Cisco SG300 52 ports switch with FW 1.0.0.27. I configured port mirroring on one of the switches so as to view communications between servers on that switch. I found that there are too many...'''
date = "2012-04-20T22:58:00Z"
lastmod = "2012-04-21T02:29:00Z"
weight = 10369
keywords = [ "segment", "lost", "tcp", "previous" ]
aliases = [ "/questions/10369" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Too many lost segments, Dup Acks and retransmission](/questions/10369/too-many-lost-segments-dup-acks-and-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10369-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://" alt="alt text" />Hi all,</p><p>I am building a new network and I started monitoring the network using Wireshark. All the switches are Cisco SG300 52 ports switch with FW 1.0.0.27. I configured port mirroring on one of the switches so as to view communications between servers on that switch. I found that there are too many lost segments that are causing Dup Acks and fast retransmit. I checked the Speed and Duplex settings on the switch ports and the servers but they all seemed fine. Speed and Duplex are set to Auto negotiate on all ports. Flow control is disabled on the switch. The servers NICs are left as default and I believe they are all set to autonegotiate.Jumbo frames are disabled on all the ports of the switch. After seeing that I decided to isolate that switch from the network and troubleshoot. I double checked speed and duplex settings, flow control settings, edge port settings.I tried to play around by changing the settings but I still got almost 40% of packets with errors in some cases.</p><p>I just don't get it. It's not between particular machines. It is happening for several machines sitting on that switch.</p><p>Could that be a bad RAM or something on the switch?What other settings can I check on the switch or the computers connected to it? Any help would be much appreciated.</p><p>Thanks.</p><p>Vishal</p><p><img src="http://" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">segment lost tcp previous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '12, 22:58</strong></p><img src="https://secure.gravatar.com/avatar/43591378d04b0dc33c5978a99bee1d76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vishal90216&#39;s gravatar image" /><p>vishal90216<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vishal90216 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-10369" class="comments-container"></div><div id="comment-tools-10369" class="comment-tools"></div><div class="clear"></div><div id="comment-10369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10372"></span>

<div id="answer-container-10372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10372-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I bet you mirrored more than one port on your switch, which will usually result in something between a few and a ton of duplicate packets being recorded in your trace. Those will show up as Dup Acks, Retransmissions and other funny things. You could check if you're suffering from duplicates by comparing retransmissions to the original packets - they're identical bit by bit, while a real retransmission would at least have a different IP ID (unless the OS is using always the same ID for paranoid reasons).</p><p>My advice would be to use the command line tool editcap (it is installed together with Wireshark) to remove the duplicates before trying to analyze anything with Wireshark. You could do something like this:</p><p><strong>editcap -d yourstrangecapturefile.pcap deduplicatedfile.pcap</strong></p><p>This will create a new file ("deduplicatedfile.pcap") that will be cleaned of any duplicates found in "yourstrangecapturefile.pcap". You might have to play around with the additional -D and -w parameters to get better results if some duplicates survive the procedure with default parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '12, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-10372" class="comments-container"></div><div id="comment-tools-10372" class="comment-tools"></div><div class="clear"></div><div id="comment-10372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

