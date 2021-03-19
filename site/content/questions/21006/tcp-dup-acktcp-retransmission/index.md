+++
type = "question"
title = "TCP DUP ACK/TCP Retransmission"
description = '''I did some orginal captures on a computer sitting outside our firewall and saw alot of TCP DUP ACK/TCP Retransmission while web browsing. Thought I was having an ISP issue but their testing is indicating no trouble. I thought this message indicated dropped frames. Am I incorrect? I did another captu...'''
date = "2013-05-07T10:46:00Z"
lastmod = "2016-12-05T19:57:00Z"
weight = 21006
keywords = [ "dup-ack" ]
aliases = [ "/questions/21006" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [TCP DUP ACK/TCP Retransmission](/questions/21006/tcp-dup-acktcp-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21006-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I did some orginal captures on a computer sitting outside our firewall and saw alot of TCP DUP ACK/TCP Retransmission while web browsing. Thought I was having an ISP issue but their testing is indicating no trouble. I thought this message indicated dropped frames. Am I incorrect?</p><p>I did another capture between two computers on a 24 port switch, no Internet, no connection other than to each other. One computer coping data from the second and the third doing the capture. I still see this messages.</p><p>This capture is me going to Foxnews</p><p><a href="https://www.cloudshark.org/captures/81fc503552a8">https://www.cloudshark.org/captures/81fc503552a8</a></p><p>Can someone explain is this normal? Thanks</p></div><div id="question-tags" class="tags-container tags">dup-ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '13, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/93eeb9aa0d5b1aed7e7115e4619a0afc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmcmasters&#39;s gravatar image" /><p>dmcmasters<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmcmasters has no accepted answers">0%</span></p></div></div><div id="comments-container-21006" class="comments-container"></div><div id="comment-tools-21006" class="comment-tools"></div><div class="clear"></div><div id="comment-21006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="21010"></span>

<div id="answer-container-21010" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21010-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>TCP has this inherent mechanism of recovery. In tcp stream eq 8 of your trace there was a condition of retransmission generated due to timing but not because of drops. Here is the snippet of your trace.</p><p>Step-1)Server send a packet to client(Let us call it packet-A){Packet.no-150}</p><p>Step-2)Client acknowledged the packet (Let us call it ack-A){Packet.no-192}</p><p>Step-3)Somehow packet-A was retransmitted by Server.The reason might be the delay in receiving ack-A from client and ack timer got out and retransmission timer got kicked in.(Dup of Packet-A){Packet.no-194}</p><p>Step-4)Client generated a duplicate ack for the retransmitted packet.(Dup of ack-A){Packet.no-195}</p><p>It is not always implies to losses whenever you see these retransmissions and duplicate acks.How timers got implemented also plays a role. With that said leaving to expert opinions....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '13, 17:33</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 May '13, 20:13</p></div></div><div id="comments-container-21010" class="comments-container"></div><div id="comment-tools-21010" class="comment-tools"></div><div class="clear"></div><div id="comment-21010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36624"></span>

<div id="answer-container-36624" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36624-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may filter out those DUPs from wireshark's display:</p><pre><code>!_ws.expert.message == &quot;Retransmission (suspected)&quot; &amp;&amp; !_ws.expert.message == &quot;Duplicate ACK (#1)&quot; &amp;&amp; !_ws.expert.message == &quot;Out-Of-Order segment&quot;</code></pre><p>Taken from <a href="http://thevisiblenetwork.com/2014/02/11/filter-duplicate-packets-from-a-capture-file/">http://thevisiblenetwork.com/2014/02/11/filter-duplicate-packets-from-a-capture-file/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '14, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/9e263681488308e5e5d5e548b2f9bc99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cweiske&#39;s gravatar image" /><p>cweiske<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cweiske has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '17, 08:22</p></div></div><div id="comments-container-36624" class="comments-container"><span id="36707"></span><div id="comment-36707" class="comment"><div id="post-36707-score" class="comment-score"></div><div class="comment-text"><p>Couldn't get your filter working. This one worked for me though:</p><p>!tcp.analysis.out_of_order &amp;&amp; ((!tcp.analysis.duplicate_ack_num == 1) || (!tcp.analysis.duplicate_ack_num == 2))</p></div><div id="comment-36707-info" class="comment-info"><span class="comment-age">(29 Sep '14, 13:33)</span> DarrenWright</div></div><span id="36709"></span><div id="comment-36709" class="comment"><div id="post-36709-score" class="comment-score"></div><div class="comment-text"><p>The latest release(s) changed the expert. <em>field names to _ws.expert.</em>. So the filter above will still work when it is corrected using the new syntax:</p><p>!_ws.expert.message == "Retransmission (suspected)" &amp;&amp; !_ws.expert.message == "Duplicate ACK (#1)" &amp;&amp; !_ws.expert.message == "Out-Of-Order segment"</p></div><div id="comment-36709-info" class="comment-info"><span class="comment-age">(29 Sep '14, 14:00)</span> mrEEde</div></div></div><div id="comment-tools-36624" class="comment-tools"></div><div class="clear"></div><div id="comment-36624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57882"></span>

<div id="answer-container-57882" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57882-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I realise that this is a very old question, so the answer is probably too late for the original poster - but may be of interest to anyone finding this post now.</p><p>Packet #149 ACKs everything up to packet #148 data. #150 is the last packet of the burst and isn't ACKed because the receiver sends an ACK only for every two packets (normal behaviour).</p><p>Both sides now timeout after around 200ms.</p><p>The receiver sends a Delayed ACK (#192 - an ACK to #150) and almost at the same time receives #194 (a retransmission of #150 - sent after a Retransmission Timeout at the sender). In response to the unnecessary "spurious" retransmission (#194), the receiver sends a Duplicate-SACK (D-SACK, #195).</p><p>A D-SACK is the use of the SACK mechanism to inform the sender that it has sent duplicate data (#194 = #150). Note the "Left Edge = 23361 &amp; Right Edge = 24062" in the TCP Options/SACK detail. D-SACKs are also Dup-ACKs.</p><p>The next action in this connection Is another GET after around 1 second. This one second delay is purely due to the client.</p><p>We paid a "cost" of 200ms because the server's burst had an odd number of packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '16, 19:57</strong></p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p>Philst<br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philst has 6 accepted answers">27%</span></p></div></div><div id="comments-container-57882" class="comments-container"><span id="57883"></span><div id="comment-57883" class="comment"><div id="post-57883-score" class="comment-score"></div><div class="comment-text"><p>There are other occurrences of the same behaviour in this capture.</p><p>One is: Packets #970, #979, #980 and #981.</p></div><div id="comment-57883-info" class="comment-info"><span class="comment-age">(05 Dec '16, 20:39)</span> Philst</div></div></div><div id="comment-tools-57882" class="comment-tools"></div><div class="clear"></div><div id="comment-57882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

