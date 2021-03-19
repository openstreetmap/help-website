+++
type = "question"
title = "Suspicious packets with all-zero Ethernet header"
description = '''I run wireshark and it captures packets 14% of my all traffic with src 00:00:00:00:00:00 dst 00:00:00:00:00:00  Protocol 0x0000 Length 60 Info Ethernet II please tell me why I&#x27;m getting these Packets.'''
date = "2017-02-12T02:33:00Z"
lastmod = "2017-02-12T22:59:00Z"
weight = 59350
keywords = [ "all-zero", "ethernet", "suspicious" ]
aliases = [ "/questions/59350" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Suspicious packets with all-zero Ethernet header](/questions/59350/suspicious-packets-with-all-zero-ethernet-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59350-score" class="post-score" title="current number of votes">0</div><span id="post-59350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I run wireshark and it captures packets 14% of my all traffic with src 00:00:00:00:00:00 dst 00:00:00:00:00:00 Protocol 0x0000 Length 60 Info Ethernet II please tell me why I'm getting these Packets.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-all-zero" rel="tag" title="see questions tagged &#39;all-zero&#39;">all-zero</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-suspicious" rel="tag" title="see questions tagged &#39;suspicious&#39;">suspicious</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '17, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/1b7c6a2341e9b966d3ed788d5737dc96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Najam&#39;s gravatar image" /><p><span>Najam</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Najam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Feb '17, 11:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-59350" class="comments-container"></div><div id="comment-tools-59350" class="comment-tools"></div><div class="clear"></div><div id="comment-59350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59354"></span>

<div id="answer-container-59354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59354-score" class="post-score" title="current number of votes">1</div><span id="post-59354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Najam</p><p>Welcome to ask.wireshark.org. Obviously the strange Ethernet frames consists of a series of zero bytes. These frame should not be seen for a number of reasons:</p><ul><li>The source MAC address and destination MAC address is the same</li><li>The Ethertype 0x0000 could be interpreted as a frame length of zero</li><li>The switch should learn, that the source port for the frame is also the destination port. Therefore the frame should not be forwarded.</li></ul><p>It is important to find out, if the frames are generated by one individual system, or if they are generated by multiple systems.</p><p><strong>Solution 1: Only one system is causing the frames</strong></p><p>If you have a managed switch I highly recommend to check system log and the status of switch. On a Cisco switch the most helpful command would be <code>show mac address-table</code> For a Cisco switch the output would look similar to this:</p><pre><code>switch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
...
   1    0000.0000.0000    DYNAMIC     Fa0/1
   1    0011.2233.4455    DYNAMIC     Fa0/2
...</code></pre><p>The output should reveal the port, where the network frame entered the network. You might want to replace the network card or update the driver for the system, that is connected to the port.</p><p><strong>Solution 2: Multiple systems are generating the frames</strong></p><p>It could be, that multiple systems generate the frame. Again, a faulty driver would be the most likely root cause. This causes a lot of confusion for the switch: The forwarding engine would assume, that the MAC address 00-00-00-00-00-00 would be jumping from one port to another. This would be logged in the switches log buffer. The log file from the switch could also show a message like <code>%C4K_L2MAN-6-INVALIDSOURCEADDRESSPACKET: (Suppressed x times)Packet received with invalid source MAC address (00:00:00:00:00:00) on port Fa0/1 in vlan x</code></p><p>The switch will always expect, that frames from any MAC address will constantly come in from the same port. Your system 00-11-22-33-44-55 will always be on port Fa 0/2, unless</p><ul><li>The system is moved to a different port (so the old port goes into shut down) OR</li><li>the network topology changes (indicated by a bit in the BPDU frames that implement the spanning tree)</li></ul><p>The whole network can become very unstable, if MAC addresses appear on different ports without a change in the spanning tree.</p><p><strong>Solution 3: Faulty network equipment</strong></p><p>Of course, it is also possible, that the switch generates the frames without reason. Please connect the suspicious computer to a different switch and verify, if the frames still show up.</p><p><strong>Solution 4: Problem in the virtualization software</strong></p><p>There seems to be a bug in certain VMware installations, that cause these frames. Please check this thread from 2008 in the <a href="https://communities.vmware.com/thread/52174?start=15&amp;tstart=0">VMware community</a></p><p>Good hunting</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '17, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-59354" class="comments-container"><span id="59360"></span><div id="comment-59360" class="comment"><div id="post-59360-score" class="comment-score"></div><div class="comment-text"><p>Your answer helps me a lot thank you very much.</p></div><div id="comment-59360-info" class="comment-info"><span class="comment-age">(12 Feb '17, 22:59)</span> <span class="comment-user userinfo">Najam</span></div></div></div><div id="comment-tools-59354" class="comment-tools"></div><div class="clear"></div><div id="comment-59354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

