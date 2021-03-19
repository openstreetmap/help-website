+++
type = "question"
title = "window sizing always at 65k with .116 sending?  Does only the ack from dst only show scale size?"
description = '''Hello, Current transfer test over 10gigabit is around 7.3mbit/s; not so good.  I see my syn and syn ack set rwin multiplier to 11 in the beginning. The ack&#x27;s from .171 show good win values; but my intial send is always at 65336 (default for tcp_wmem). is this normal?  Anything indicative of a window...'''
date = "2013-08-23T18:52:00Z"
lastmod = "2013-08-24T22:46:00Z"
weight = 23989
keywords = [ "windows", "scaling" ]
aliases = [ "/questions/23989" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [window sizing always at 65k with .116 sending? Does only the ack from dst only show scale size?](/questions/23989/window-sizing-always-at-65k-with-116-sending-does-only-the-ack-from-dst-only-show-scale-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23989-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/oo_issue_vzw.JPG" alt="alt text" />Hello,</p><p>Current transfer test over 10gigabit is around 7.3mbit/s; not so good.<br />
</p><p>I see my syn and syn ack set rwin multiplier to 11 in the beginning.</p><p>The ack's from .171 show good win values; but my intial send is always at 65336 (default for tcp_wmem). is this normal?<br />
</p><p>Anything indicative of a window scaling problem for the dismal performance?</p></div><div id="question-tags" class="tags-container tags">windows scaling</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '13, 18:52</strong></p><img src="https://secure.gravatar.com/avatar/d76fa281adbb90a4765395cdd615a6c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zerobane&#39;s gravatar image" /><p>zerobane<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zerobane has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 24 Aug '13, 10:12</p></div></div><div id="comments-container-23989" class="comments-container"><span id="23991"></span><div id="comment-23991" class="comment"><div id="post-23991-score" class="comment-score"></div><div class="comment-text"><p><a href="https://docs.google.com/file/d/0B-wHgm2sKSdWS1kxcFhra2hGNUU/edit?usp=sharing">https://docs.google.com/file/d/0B-wHgm2sKSdWS1kxcFhra2hGNUU/edit?usp=sharing</a></p></div><div id="comment-23991-info" class="comment-info"><span class="comment-age">(23 Aug '13, 18:57)</span> zerobane</div></div></div><div id="comment-tools-23989" class="comment-tools"></div><div class="clear"></div><div id="comment-23989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="23992"></span>

<div id="answer-container-23992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23992-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In this conversation the .116 is only sending data, so there is no need to change the window size (the window size in the packets from .116 tell .171 how much data can be sent without waiting for an ACK, but .171 is not sending data, so no need to increase the buffer size).</p><p>The window size sent by .171 is indeed growing from the initial 64K. This only happens a bit later in the trace file as it is not needed in the <a href="http://en.wikipedia.org/wiki/Slow-start">slowstart fase</a> of the TCP connection. In the slowstart fase, the congestion window is exponentially grown, once the congestion window gets larger than the window size, the window size will be increased as well. It would be interesting to see the whole transfer, as it should grow to the configured maximum value.</p><p>The culprit in your capture file is the round trip time of 75 ms, have a look at the <a href="http://en.wikipedia.org/wiki/Bandwidth-delay_product">bandwidth delay product</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23992" class="comments-container"></div><div id="comment-tools-23992" class="comment-tools"></div><div class="clear"></div><div id="comment-23992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23995"></span>

<div id="answer-container-23995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23995-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Current transfer test over 10gigabit is around 7.3mbit/s; not so good."</p><p>This is a transfer over a WAN connection, as the RTT of ~75ms and inbound TTL 56 indicate. So I doubt that you will have a 10G bandwidth all the way and I think you need to set your expectations a little lower. ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-23995" class="comments-container"><span id="23998"></span><div id="comment-23998" class="comment"><div id="post-23998-score" class="comment-score"></div><div class="comment-text"><p>Thanks for reply / info guys,</p><p>This is on a long distance private network; but fairly heavy congestion / busy.</p><p>Yes; 64KB win size gets me around 7.8mbit/s; hoping to get at least 50mbit/s (what it was before the upgrade to 10gbit ironically)</p><p>Attached a larger pcap; entire transfer dump was 500mb using netcat/dd.</p><p>I see the window size from the acks increase to about 400,000 then it resets; both the window size and byes in flight seem to drop down.</p><p>My max window size on each side is set to 64MB (in sysctl)</p></div><div id="comment-23998-info" class="comment-info"><span class="comment-age">(24 Aug '13, 06:21)</span> zerobane</div></div><span id="23999"></span><div id="comment-23999" class="comment"><div id="post-23999-score" class="comment-score"></div><div class="comment-text"><p><a href="https://docs.google.com/file/d/0B-wHgm2sKSdWZ0V3NWMtX2Y2dzQ/edit?usp=sharing">https://docs.google.com/file/d/0B-wHgm2sKSdWZ0V3NWMtX2Y2dzQ/edit?usp=sharing</a></p><p>larger pcap (500 lines)</p></div><div id="comment-23999-info" class="comment-info"><span class="comment-age">(24 Aug '13, 06:22)</span> zerobane</div></div><span id="24000"></span><div id="comment-24000" class="comment"><div id="post-24000-score" class="comment-score"></div><div class="comment-text"><p>Is it reasonable to have bytes in flight and BDP at 85Megs on a large scale WAN?</p><p>If not; whats a good expectation / setting?</p><p>Could traffic shaping be causing the bytes in flight / RWIN to be limited to 400,000 bytes?<br />
</p><p>My background in networking is strictly limited to internal appliance/solution in which there is 1 to 10 switches that I have complete control over.</p></div><div id="comment-24000-info" class="comment-info"><span class="comment-age">(24 Aug '13, 09:59)</span> zerobane</div></div></div><div id="comment-tools-23995" class="comment-tools"></div><div class="clear"></div><div id="comment-23995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24014"></span>

<div id="answer-container-24014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24014-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ul><li>"Is it reasonable to have bytes in flight and BDP at 85Megs on a large scale WAN?"</li></ul><p>No, this is not reasonable. With a 75 ms RTT and a 50Mb/s capacity you need 468750 bytes to fill the pipe. However yor trace shows that we start losing packets in the network when we approach 400000 bytes_in_flight and congestion avoidance algorithm at the sender will drop the congestion_window.</p><ul><li>If not; whats a good expectation / setting?</li></ul><p>That is a good question, ask 3 experts and you get 9 suggestions! <a href="http://fasterdata.es.net/host-tuning/background/#t1">here is a good read</a> and <a href="http://www.psc.edu/index.php/networking/641-tcp-tune#Linux">another one</a> ;-) And here is <em>my suggestion</em> for <em>this scenario</em> : I'd stay below 350000 bytes to avoid packet loss. Sometimes 'less is more'.</p><ul><li>Could traffic shaping be causing the bytes in flight / RWIN to be limited to 400,000 bytes?</li></ul><p>I doubt that traffic shaping is in place here. To me this looks more like a result of segmentation offload that is in place now and maybe wasn't on your old NIC card and is now generating a higher (too high) packet rate</p><p>Good luck in your tuning effort and please post your results!</p><p>Ah, and maybe changing your algorithm might optimize this also:</p><pre><code>sysctl net.ipv4.tcp_available_congestion_control

sysctl net.ipv4.tcp_congestion_control</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 22:46</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Aug '13, 22:51</p></div></div><div id="comments-container-24014" class="comments-container"></div><div id="comment-tools-24014" class="comment-tools"></div><div class="clear"></div><div id="comment-24014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

