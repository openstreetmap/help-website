+++
type = "question"
title = "Using Wireshark to detect isp throttling"
description = '''A little preface. Recently I switched my isp to the fastest one available here (advertised speed is &quot;up to 300 Mb/s&quot; both ways). While at the speedtest.net I can easily get impressive numbers like 800 Mb/s down &amp;amp; 900 Mb/s up it&#x27;s not that great when it comes to the real world usage. I noticed a ...'''
date = "2015-05-11T15:46:00Z"
lastmod = "2015-05-12T06:21:00Z"
weight = 42321
keywords = [ "packetloss", "rwin", "throttling" ]
aliases = [ "/questions/42321" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using Wireshark to detect isp throttling](/questions/42321/using-wireshark-to-detect-isp-throttling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42321-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A little preface. Recently I switched my isp to the fastest one available here (advertised speed is "up to 300 Mb/s" both ways). While at the speedtest.net I can easily get impressive numbers like 800 Mb/s down &amp; 900 Mb/s up it's not that great when it comes to the real world usage. I noticed a strange/peculiar pattern: when downloading from p2p networks throughput may be floating around 50 MB/s (over 400 Mbit/s) provided there's enough fast sources (regardless of their geographical location). "Enough" means roughly the following: while every single connection seems to be capped at ~1 MB/s if there are 50 sources I get ~50 MB/s. However fast this may sound there's one big downside: single connection can never be as fast. I was able to squeeze 10-13 MB/s while downloading from my 1 Gb/s VPS (most of the time it's 4-5 MB/s). So I was trying to figure it out, and after a lot of googling and tinkering with TCP, registry settings (Windows 8.1 here) with little to no effect I decided it would be more insightful and efficient to monitor my connection with some sniffing tool.</p><p>So I captured my ftp downloading session. Originally I thought my situation must have something to do with RWIN, but TCP <em>StreamGraph</em> &gt; <em>Window Scaling Graph</em> showed me straight horizontal line at 1048576 (all ACK packets from my side have this size listed).</p><p>As the side note: when I go to <em>Statistics</em> &gt; <em>IO graph</em> and plot <strong>tcp.window_size</strong> filter I get different result: with tick interval being 0.01s line becomes very jagged, drops to 0 constantly, teeth go up to 100000~250000 bytes/s (at the start and at the end they are higher than in the middle); with tick interval being 1s it's still not straight, rising and falling edges go up to 6000000 bytes/s with the middle being sank up to ~3000000 bytes/s. So why the difference and which one is correct?</p><p>Another bad thing I noticed was many <em>DUP ACK</em> (some dupes go up to ridiculous numbers like ~#200), <em>Out-Of-Order</em> and <em>Previous Segment not Captured</em> messages, like every 100-200 packets. So I presume it testifies to some serious packet loss during transfer. So could it be that this is my isp is trying to throttle my fast single connections? And may be there are additional things Wireshark could help me to spot before I give them a call and call out this nonsense?</p></div><div id="question-tags" class="tags-container tags">packetloss rwin throttling</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '15, 15:46</strong></p><img src="https://secure.gravatar.com/avatar/09bc377c22204a9ee52ac3f717a10fa1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joo&#39;s gravatar image" /><p>Joo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joo has no accepted answers">0%</span></p></div></div><div id="comments-container-42321" class="comments-container"><span id="42323"></span><div id="comment-42323" class="comment"><div id="post-42323-score" class="comment-score">1</div><div class="comment-text"><p>Have you tried Glasnost?</p></div><div id="comment-42323-info" class="comment-info"><span class="comment-age">(12 May '15, 02:04)</span> Roland</div></div><span id="42349"></span><div id="comment-42349" class="comment"><div id="post-42349-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the suggestion. I did, however it haven't detected any traffic shaping. though I was unable to complete <em>SSH</em> and <em>Flash Video</em> tests, also it complained about some measurements were affected by noise during several runs.</p></div><div id="comment-42349-info" class="comment-info"><span class="comment-age">(12 May '15, 17:12)</span> Joo</div></div></div><div id="comment-tools-42321" class="comment-tools"></div><div class="clear"></div><div id="comment-42321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42329"></span>

<div id="answer-container-42329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42329-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't (reliably) detect ISP throttling with a capture file taken at the client only, because you will never know who/what is causing packet loss (retransmissions in the capture file). The only reliable option is to run a test with a server you own (like on rented in the cloud).</p><p>See here for some ideas:</p><blockquote><p><a href="https://www.eff.org/de/testyourisp">https://www.eff.org/de/testyourisp</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '15, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 May '15, 06:23</p></div></div><div id="comments-container-42329" class="comments-container"><span id="42350"></span><div id="comment-42350" class="comment"><div id="post-42350-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the link. Unfortunately I was unable to make Switzerland work on my home PC. I did some tests listed at <a href="http://www.measurementlab.net/">http://www.measurementlab.net/</a> (half of them do not work either), didn't really provide any additional info.</p><p>As far as I understand, specific protocol traffic shaping should affect overall throughput with this protocol, not just a single connection. Oh, well, I should probably call their support.</p></div><div id="comment-42350-info" class="comment-info"><span class="comment-age">(12 May '15, 17:12)</span> Joo</div></div><span id="42357"></span><div id="comment-42357" class="comment"><div id="post-42357-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Oh, well, I should probably call their support.</p></blockquote><p>good idea. I had cases, where they simply forgot/overlooked a setting on their router, that was not intended to be there for that customer.</p></div><div id="comment-42357-info" class="comment-info"><span class="comment-age">(13 May '15, 05:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-42329" class="comment-tools"></div><div class="clear"></div><div id="comment-42329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

