+++
type = "question"
title = "Losing Packets??"
description = '''I&#x27;m getting SEVERAL entries in my packet capture that I beleive indicate lost packets. TCP Dup ACK &amp;amp; TCP Retrasmission to be specific. I see there is a problem here, but can someone walk me step by step through identifying what the cause of this is? I&#x27;m assuming that somewhere within the capture...'''
date = "2013-01-03T14:27:00Z"
lastmod = "2013-01-14T02:26:00Z"
weight = 17420
keywords = [ "dup", "ack", "retransmissions", "tcp" ]
aliases = [ "/questions/17420" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Losing Packets??](/questions/17420/losing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17420-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting SEVERAL entries in my packet capture that I beleive indicate lost packets. TCP Dup ACK &amp; TCP Retrasmission to be specific. I see there is a problem here, but can someone walk me step by step through identifying what the cause of this is? I'm assuming that somewhere within the capture it will tell me the workstation or piece of equipment that is causing this problem??</p></div><div id="question-tags" class="tags-container tags">dup ack retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '13, 14:27</strong></p><img src="https://secure.gravatar.com/avatar/d48f9598408d2d2deeff28d4bc94992c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pstage&#39;s gravatar image" /><p>pstage<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pstage has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jan '13, 00:01</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-17420" class="comments-container"></div><div id="comment-tools-17420" class="comment-tools"></div><div class="clear"></div><div id="comment-17420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="17578"></span>

<div id="answer-container-17578" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17578-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your trace is not indicating lost packets as much as you think - you just got tons of duplicate packets in there, which Wireshark will mark as retransmissions or duplicate ACKs. This is usually caused by spanning multiple source ports or a VLAN. I deduplicated your trace using editcap like this:</p><p><code>editcap -d -D 50 1-4-2013.pcap 1-4-2013-dedup.pcap 179869 packets seen, 82004 packets skipped with duplicate window of 50 packets.</code></p><p>and everyhting looked a lot better. There still are duplicates that editcap won't remove because you captured packets before and after they were routed (you can tell from the TTL and the MAC layer).</p><p>With all those remaining duplicates it's a hard thing to say what really goes on, but I doubt that it is as bad as it seemed to you, especially when you also had the real duplicates still in the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '13, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '13, 12:13</p></div></div><div id="comments-container-17578" class="comments-container"></div><div id="comment-tools-17578" class="comment-tools"></div><div class="clear"></div><div id="comment-17578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17421"></span>

<div id="answer-container-17421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17421-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry. Packet traces will not tell you where the lost is happening. To do that, you have to capture at multiple capture points - not always practical. Are you seeing FAST RETRANSMISSIONS or just RETRANSMISSIONS? Not all packet losses are equal, some are more damaging than others (in terms of performance). If you can post your trace file somewhere, folks may be able to download it an help you analyze it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '13, 17:08</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jan '13, 07:07</p></div></div><div id="comments-container-17421" class="comments-container"><span id="17577"></span><div id="comment-17577" class="comment"><div id="post-17577-score" class="comment-score"></div><div class="comment-text"><p>I'm just seeing retransmissions. That and duplicate ACK messsages #1 to the hundreds. A short sample capture can be downloaded here. <a href="https://www.dropbox.com/sh/a8bub6yryq1v407/MDkooy5E8c">https://www.dropbox.com/sh/a8bub6yryq1v407/MDkooy5E8c</a> Any help would be greatly appreciated!</p></div><div id="comment-17577-info" class="comment-info"><span class="comment-age">(08 Jan '13, 11:03)</span> pstage</div></div></div><div id="comment-tools-17421" class="comment-tools"></div><div class="clear"></div><div id="comment-17421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17657"></span>

<div id="answer-container-17657" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17657-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is an interesting conversation going on between 192.168.1.35 ( sender ) and 192.168.3.54 ( receiver ) where we see a lot of zero window size on the .54 side. Although we don't have the SYN &gt; SYN/ACK it looks like window scaling is not enabled on the .54 machine. The sender sends 65k of data which the sender ACKs with the large number of ACKs that we see whilst reducing the window but increasing the ACK by 2920 bytes which indicates that the receiver is buffering the data but the application is not consuming it. Given that the time taken for each of these events ( zero window, zero window probe and window update ) can be 1.5 -2s then performance for this particular app will be slow. If the app can't handle 65k of date then I'm not sure enabling window scaling will help, the sender would just send more data and the receiver would just buffer the now increased window size worth of data until the app can consume it. In this case it looks like application level delay for this particular conversation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '13, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/56d8eb2da7a48dc0ecedc37a896f68f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tenkrow&#39;s gravatar image" /><p>tenkrow<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tenkrow has no accepted answers">0%</span></p></div></div><div id="comments-container-17657" class="comments-container"><span id="17659"></span><div id="comment-17659" class="comment"><div id="post-17659-score" class="comment-score"></div><div class="comment-text"><p>Of course it could be that the sender only sends in 65k chunks, certainly the PSH biit is set on the last packet indicating the sender has no more data to send and it's always set on the last packet at around 65k, we'd need to see the 3 way handshake to find out if WS is on and what it's at. It's still application level delay.</p></div><div id="comment-17659-info" class="comment-info"><span class="comment-age">(14 Jan '13, 04:37)</span> tenkrow</div></div></div><div id="comment-tools-17657" class="comment-tools"></div><div class="clear"></div><div id="comment-17657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

