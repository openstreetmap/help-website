+++
type = "question"
title = "TCP connection"
description = '''Hi, I have a problem in establishing a tcp connection with a device(client) and PC(server) I will list important places in the wireshark to make it comfortable for you. start - connection established till 106 - full of retransmission. then window size of tcp if full. so data starts sending again.. a...'''
date = "2013-09-17T21:37:00Z"
lastmod = "2013-09-18T00:34:00Z"
weight = 24878
keywords = [ "labview", "tcp", "wireshark" ]
aliases = [ "/questions/24878" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP connection](/questions/24878/tcp-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24878-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a problem in establishing a tcp connection with a device(client) and PC(server) I will list important places in the wireshark to make it comfortable for you.</p><p>start - connection established till 106 - full of retransmission. then window size of tcp if full. so data starts sending again..</p><p>after this, there is no problem.(no retransmissions)</p><p>at 1032 - exit is sent from PC. It closes connection in labview and device also responds for it.(this stops the labview as well)</p><p>the device is programmed to always look for connection. so it send arp request even after that.</p><p>at 1050 - labview started. but still connection is not establishing.. PC is sending 'ack" instead of "syn ack" as a reply to "syn" from device..</p><p>this continues..</p><p>at 1103 - a "rst" is given from PC.. after this connection establishes.. then retransmission for some time.. then proper communication...</p><p>my questions are "what decides when rst signal sent by PC?", "why connection establishes after 'rst' ?" , "during retransmission there was seperate "ack" from PC. when not after that?" ," why transmits well after window gets full ?</p></div><div id="question-tags" class="tags-container tags">labview tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '13, 21:37</strong></p><img src="https://secure.gravatar.com/avatar/14ae6741f009eb9551c897744110e25f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raja%20Balaji&#39;s gravatar image" /><p>Raja Balaji<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raja Balaji has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Sep '13, 02:09</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-24878" class="comments-container"><span id="24879"></span><div id="comment-24879" class="comment"><div id="post-24879-score" class="comment-score"></div><div class="comment-text"><p>Sorry, but that kind of description is not really good enough to really help you. A packet trace would be much better, especially since nobody here knows your application like you do and (at least I) can't exactly follow what is happening. For example:</p><p>What do you mean by</p><ul><li><p>"exit is sent from PC"?</p></li><li><p>"device is programmed to look for connection", and what does an ARP request have to do with that?</p></li></ul><p>If you can, put a sample trace on Cloudshark.</p></div><div id="comment-24879-info" class="comment-info"><span class="comment-age">(17 Sep '13, 22:22)</span> Jasper ♦♦</div></div><span id="24880"></span><div id="comment-24880" class="comment"><div id="post-24880-score" class="comment-score"></div><div class="comment-text"><p>I am having a device which I have programmed to work as a tcp client (enc28j60+ arduino controller)</p><p>from the PC, I use a programming software called labview to "listen for a tcp connection, read some data packets, write some data packets and close a tcp connection".</p><p>based on what data I sent from this software, I get a data from the device. when "exit" is sent from labview, I have programmed it such a way that connection is closed and the labview program also stops.</p><p>when I again try to start the labview code, the connection is not getting established at once. It takes some 2 minutes to connect again. I want to know why this happens and is there a way out to prevent it?</p><p><a href="http://forums.ni.com/t5/LabVIEW/how-tcp-listen-works/td-p/2553567/page/2">click here</a> you can find the wireshark log in this link. I could not upload an attachment here.(3rd conversation in the page)</p></div><div id="comment-24880-info" class="comment-info"><span class="comment-age">(17 Sep '13, 22:42)</span> Raja Balaji</div></div></div><div id="comment-tools-24878" class="comment-tools"></div><div class="clear"></div><div id="comment-24878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24883"></span>

<div id="answer-container-24883" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24883-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>click here you can find the wireshark log in this link. I could not upload an attachment here.(3rd conversation in the page)</p></blockquote><p>The problem seems to be that your application is using the same source port for new connections. As the time between the new connections is only a few seconds, the socket on the server may still exists (not closed) in your Labview application and thus the server (Labview tool) sends an ACK for the new SYN instead of a SYN-ACK.</p><p>After the server resets the connection in frame #1103, a new connection can be established, as the server now accepts connections with that source port as <strong>new</strong> connections.</p><p>Solution: Don't use the same source port for new connections too fast, or troubleshoot the timing values in your Labview application.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '13, 00:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Sep '13, 02:09</p></div></div><div id="comments-container-24883" class="comments-container"><span id="24889"></span><div id="comment-24889" class="comment"><div id="post-24889-score" class="comment-score"></div><div class="comment-text"><p>ok thanks.. if not in labview, where can I change it.. (any other option available in PC to change the timing?)<br />
</p><p>why do you there is re-transmissions initially?? why did it stop after the window size of tcp gets full??</p><p>have I established the tcp connection correctly??</p><p>(doubt: once I get data from server, should the client separately send an ack signal or can I make the ack flag high in the data packet and send it directly)<br />
</p></div><div id="comment-24889-info" class="comment-info"><span class="comment-age">(18 Sep '13, 02:10)</span> Raja Balaji</div></div><span id="24891"></span><div id="comment-24891" class="comment"><div id="post-24891-score" class="comment-score"></div><div class="comment-text"><p>I have no idea how Labview handles TCP, so this might be a question for the Labview forum.</p><p>However, instead of trying to change any timeout values, do the right thing and don't use the same source port several times in your client.</p><blockquote><p>why do you there is re-transmissions initially?? why did it stop after the window size of tcp gets full??</p></blockquote><p>Well, there are some other problems in the TCP connection. I will come back on them later.</p><p>In the meantime, as a first step, please fix the source port problem.</p></div><div id="comment-24891-info" class="comment-info"><span class="comment-age">(18 Sep '13, 02:21)</span> Kurt Knochner ♦</div></div><span id="24898"></span><div id="comment-24898" class="comment"><div id="post-24898-score" class="comment-score"></div><div class="comment-text"><p>Some problems:</p><ol><li><p>Your client advertises a Window size of 66 bytes and a MSS of 64 bytes. Is there any special reason for this?</p></li><li><p>Your server advertizes a window size of 66 bytes. Is there any special reason for this?</p></li></ol><p>These rather small window sizes will certainly call for trouble.</p></div><div id="comment-24898-info" class="comment-info"><span class="comment-age">(18 Sep '13, 03:20)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24883" class="comment-tools"></div><div class="clear"></div><div id="comment-24883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

