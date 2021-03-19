+++
type = "question"
title = "General troubleshooting methodology - network/transfer slowness"
description = '''I&#x27;m looking for ideas and thoughts on a general troubleshooting methodology for network transfer slowness, using Wireshark, and would like to see what others do when troubleshooting &quot;slow network&quot; issues. For example, a user complains about slow SMB or FTP transfer of large files over the WAN, and a...'''
date = "2016-08-19T08:54:00Z"
lastmod = "2016-08-29T11:15:00Z"
weight = 54985
keywords = [ "troubleshooting", "slowness" ]
aliases = [ "/questions/54985" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [General troubleshooting methodology - network/transfer slowness](/questions/54985/general-troubleshooting-methodology-networktransfer-slowness)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54985-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for ideas and thoughts on a general troubleshooting methodology for network transfer slowness, using Wireshark, and would like to see what others do when troubleshooting "slow network" issues.</p><p>For example, a user complains about slow SMB or FTP transfer of large files over the WAN, and a capture of the transfer is saved to be analyzed.</p><p>Right now, I start by analyzing this way:</p><p>1) Statistics/Conversations - sort by largest Bytes column, and then follow that TCP stream. (If it is a file transfer, generally it is going to be the TCP conversation with the most data transferred)</p><p>1A) Added: Look at the TCP StreamGraphs Time/Sequence (tcptrace) graph, and look for flat sections, showing delays in the transfer.</p><p>1B) Look at 3-way handshake and make note of TCP Window scaling option/RWIN size and TCP SACK options, and note the RTT. 1C) Make use of the Bytes in Flight column, and verify if data transfer is filling or nearing the receiver's advertised window.</p><p>2) Look at average bits/s using the statistics screen for the display filter, and note this. (This averages the transfer speed for the displayed packets, so if you are capturing, and the user is connected to an SMB server, but sitting idle for 5 minutes before copying files, the reported speed in Wireshark will be slower than the actual max speed of data transfer)</p><p>3) Look for packet loss (excessive TCP retransmissions/dup acks)</p><ul><li>Some packet loss is obviously acceptable over a WAN link.</li><li>How do I determine the percent or rate of packet loss?</li><li>In general what percentage packet loss will typically cause a transfer to degrade?</li><li>For small amounts of packet loss, what is an easy way to determine if this is the cause of slowness?</li></ul><p>3a) Here is an example of a tcptrace graph showing 1-2% packet loss on a connection. The packet loss was causing slowness. Notice the bumpy looking graph. If you click the bumpy sections, packet loss was causing the sender to throttle back it's transfer rate, and it was never coming close to filling the Receive Window. <img src="https://osqa-ask.wireshark.org/upfiles/before_fix_-_packet_loss_graph.png" alt="alt text" /></p><p>5) Look for high delta times.</p><p>6) Look for TCP Window Full messages</p><p>Unless there is high packet loss, or obvious client/server processing delay, often times I have a difficult time pinpointing the cause for connections being "slow".</p><p>*** Edit: I found a lot of great videos on packetbomb.com explaining how to read the TCP Graphs, as well as the TCP sections in Laura Chappel's book were really helpful.</p></div><div id="question-tags" class="tags-container tags">troubleshooting slowness</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '16, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/ff0a86a720311c5bec05905c6752c144?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crrimson&#39;s gravatar image" /><p>crrimson<br />
<span class="score" title="15 reputation points">15</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crrimson has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '16, 09:55</p></div></div><div id="comments-container-54985" class="comments-container"></div><div id="comment-tools-54985" class="comment-tools"></div><div class="clear"></div><div id="comment-54985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55174"></span>

<div id="answer-container-55174" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55174-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I too default to Laura as a great resource for methodologies, as Paul mentioned. From your above description, it looks like you already use the method she discusses in the "Wireshark 101" book: 1) Determine who is talking 2) Determine what applications are talking 3) Filter on the conversation(s) of interest 4) Graph the IO to look for drops in throughput 5) Open expert 6) Determine RTT</p><p>In the "Troubleshooting with Wireshark" book, she dedicates the first chapter to discussing a sample troubleshooting methodology that abstracts to a higher level - where you first define the problem - and the work down to the analysis tasks. I think this is important to identify, since as network engrs/analysts/admins it is very easy to jump down a rabbit hole, without clearly assessing the various information at hand and formulating a strategy.</p><p>I shared some thoughts on the methodology topic at this year's SharkFest - <a href="https://sharkfest.wireshark.org/assets/presentations16/23.pdf">https://sharkfest.wireshark.org/assets/presentations16/23.pdf</a></p><p>Looks like you are on a solid path and are asking the right questions...good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '16, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p>BruteForce<br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span></p></div></div><div id="comments-container-55174" class="comments-container"><span id="55176"></span><div id="comment-55176" class="comment"><div id="post-55176-score" class="comment-score"></div><div class="comment-text"><p>Thanks,</p><p>I read your PDF and I appreciate the perspective you share, it looks like you have a good system.</p><p>I own the Wireshark Network Analysis 2nd ed. by Laura, and after looking at the table of contents, I should probably read chapter 29: "Find the Top Causes of Performance Problems"!<br />
</p><p>I may come back and edit my post after reading through that chapter.</p></div><div id="comment-55176-info" class="comment-info"><span class="comment-age">(29 Aug '16, 13:28)</span> crrimson</div></div></div><div id="comment-tools-55174" class="comment-tools"></div><div class="clear"></div><div id="comment-55174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54996"></span>

<div id="answer-container-54996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54996-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>We have a guide to analysis on the TribeLab site - see <a href="http://www.tribelab.com">http://www.tribelab.com</a> then check the Network Analysis Guide and TRANSUM sections.</p><p>Also look out for a series of articles by Gary Kaiser. Laura Chappel also produced a video which I think was called 12345 Guide but I can't find it at the moment.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '16, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span> </br></p></div></div><div id="comments-container-54996" class="comments-container"></div><div id="comment-tools-54996" class="comment-tools"></div><div class="clear"></div><div id="comment-54996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

