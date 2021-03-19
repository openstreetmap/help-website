+++
type = "question"
title = "So, is there a place to submit packet captures for the network-smart to dissect?"
description = '''I saw a thread on the Steam Users&#x27; Forum about someone who was getting like, 12 kB/s download speed specifically in his Steam game client. Since he was at the end of his rope, I told him to try capturing with Wireshark and see if anything obvious pops out. He posted packet captures whilst trying to ...'''
date = "2010-11-14T19:27:00Z"
lastmod = "2010-11-14T21:45:00Z"
weight = 943
keywords = [ "capture", "examine", "speed", "steamclient", "community" ]
aliases = [ "/questions/943" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [So, is there a place to submit packet captures for the network-smart to dissect?](/questions/943/so-is-there-a-place-to-submit-packet-captures-for-the-network-smart-to-dissect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-943-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I saw a thread on the Steam Users' Forum about someone who was getting like, 12 kB/s download speed specifically in his Steam game client. Since he was at the end of his rope, I told him to try capturing with Wireshark and see if anything obvious pops out. He posted packet captures whilst trying to download and while not, and I couldn't find anything obvious. Is there a proper place to post packet captures for those who are skilled with networking to poke through and look for problems?</p></div><div id="question-tags" class="tags-container tags">capture examine speed steamclient community</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '10, 19:27</strong></p><img src="https://secure.gravatar.com/avatar/c04f2b4fb0d88dc25e89378b9b0542b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hmmwhatsthisdo&#39;s gravatar image" /><p>hmmwhatsthisdo<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hmmwhatsthisdo has no accepted answers">0%</span></p></div></div><div id="comments-container-943" class="comments-container"></div><div id="comment-tools-943" class="comment-tools"></div><div class="clear"></div><div id="comment-943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="944"></span>

<div id="answer-container-944" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-944-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your friend is comfortable uploading his network data to the web, he can upload it to www.cloudshark.org, from which others can view the data...finding someone versed in the Steam client's protocol(s) is a different matter.</p><p>(I am unaffiliated with CloudShark. No warranty express or implied. Void in Rhode Island. You get the idea.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '10, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Nov '10, 19:34</p></div></div><div id="comments-container-944" class="comments-container"><span id="945"></span><div id="comment-945" class="comment"><div id="post-945-score" class="comment-score"></div><div class="comment-text"><p>He already uploaded the packet data, I'm just looking for somewhere to have people poke through it and see if they notice anything wrong. I didn't want to immediately post it here, because this site appears to be for, well, Wireshark. Posting a thread asking for people to look through something might have been taken the wrong way.</p></div><div id="comment-945-info" class="comment-info"><span class="comment-age">(14 Nov '10, 19:34)</span> hmmwhatsthisdo</div></div><span id="946"></span><div id="comment-946" class="comment"><div id="post-946-score" class="comment-score"></div><div class="comment-text"><p>Where is online (the trace file)? There are a lot of folks here who can take a quick look.</p></div><div id="comment-946-info" class="comment-info"><span class="comment-age">(14 Nov '10, 19:41)</span> hansangb</div></div><span id="947"></span><div id="comment-947" class="comment"><div id="post-947-score" class="comment-score"></div><div class="comment-text"><p>Well, the thread is <a href="http://forums.steampowered.com/forums/showthread.php?t=1581760">here</a>, the packet capture with Steam running (In case you didn't know, Steam is a game client, sort of like iTunes for games) is <a href="http://www.mediafire.com/?mcmxdcndcu0ptqw">here</a>, and the packet capture w/o Steam running is <a href="http://www.mediafire.com/?e5jyezd1uvuuwba">here</a>. From what I can tell, the actual traffic is between 192.168.1.101 and 66.77.49.4, the latter being a Valve content server AFAIK.</p></div><div id="comment-947-info" class="comment-info"><span class="comment-age">(14 Nov '10, 19:48)</span> hmmwhatsthisdo</div></div></div><div id="comment-tools-944" class="comment-tools"></div><div class="clear"></div><div id="comment-944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="949"></span>

<div id="answer-container-949" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-949-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The trace file uploaded shows numerous packets lost in the proces and an interesting "pace" to data sent to your friend's Steam client. It appears the Steam server sends data at a relatively constant 95ms rate with few deviations. In general, not a blazing spew of data...</p><p>In Wireshark, select <code>View &gt; Coloring Rules &gt; Disable the Checksum Errors rule</code>. Now look at <code>Analyze &gt; Expert Info Composite</code> to see the errors (disregard checksum errors) and look at the Warnings and Notes tabs. Duplicate ACKs are requests for the missing packets. Retransmissions and Fast Retransmissions are the well... retransmissions of missing packets. Now assuming the game cannot move forward without those packets, your friend is likely experiencing a slow down as TCP recovers from the lost packets.</p><p>What can your friend do? Well... given that some router along the path to 66.77.49.4 may be dropping the packets, it may be difficult to locate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '10, 21:34</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Nov '10, 21:39</p></div></div><div id="comments-container-949" class="comments-container"><span id="966"></span><div id="comment-966" class="comment"><div id="post-966-score" class="comment-score"></div><div class="comment-text"><p>Should I have him do a tracert to the Valve content server IP and look for say, points where the hop time dramatically increases?</p></div><div id="comment-966-info" class="comment-info"><span class="comment-age">(15 Nov '10, 16:30)</span> hmmwhatsthisdo</div></div><span id="969"></span><div id="comment-969" class="comment"><div id="post-969-score" class="comment-score"></div><div class="comment-text"><p>I had him do a tracert to the content server, results shown <a href="http://img.photobucket.com/albums/v457/Opioid/Tracert.jpg">here.</a></p></div><div id="comment-969-info" class="comment-info"><span class="comment-age">(15 Nov '10, 17:35)</span> hmmwhatsthisdo</div></div></div><div id="comment-tools-949" class="comment-tools"></div><div class="clear"></div><div id="comment-949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="950"></span>

<div id="answer-container-950" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-950-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the "download" capture I see:</p><ol><li>There are two connections each of which is receiving data in a similar fashion. (Two separate downloads ?)</li><li>For the most part the sending (remote) IP on each connection is sending 1 frame just about every 95 millisecs. The (local) receiver is acknowledging almost immediately and is advertising a full size window. (Ie: the receiver is ready and willing to receive more data).</li><li>There's a fair amount of lost packets requiring retransmissions. This just makes things worse but is really a secondary effect compared to the fact that the sender is sending 1 frame every 95 millisecs.</li></ol><p>I've no knowledge about (configuring for) Steam and don't know anything about your setup so I'll just say the following:</p><p>It sure looks like <em>something</em> is going on that is pacing the connection (especially given that it seems that other downloads work AOK). To me it seems pretty unnatural that frames should be received almost always about every 95 millisecs.</p><p>Is it a clue that the same effect is seen from 2 different destination IP's (using the same TCP port 27030) ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '10, 21:45</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-950" class="comments-container"><span id="967"></span><div id="comment-967" class="comment"><div id="post-967-score" class="comment-score"></div><div class="comment-text"><p>The port 27030 definitely means something - the Steam client almost always uses ports in the 270xx range. When I looked up the secondary destination IP (assuming you meant the 4.xx.xx.xx one), it appeared to be an ISP server. The person who's experiencing the problem has contacted their ISP, who told them that they don't interfere with connections, but the ISP support rep may have been misinformed.</p></div><div id="comment-967-info" class="comment-info"><span class="comment-age">(15 Nov '10, 16:39)</span> hmmwhatsthisdo</div></div></div><div id="comment-tools-950" class="comment-tools"></div><div class="clear"></div><div id="comment-950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

