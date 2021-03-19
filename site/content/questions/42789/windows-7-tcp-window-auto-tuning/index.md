+++
type = "question"
title = "Windows 7 TCP Window &quot;Auto-Tuning&quot;"
description = '''As far I know (have just red to be honest :-) ) Windows 7 TCP stack has &quot;Auto-Tuning&quot; functionality which one in particular has following property:     The idea is, a small initial RWIN value is advertised, which is then adjusted on the fly depending on the current line speed and latency. ….//…     ...'''
date = "2015-06-01T03:52:00Z"
lastmod = "2015-06-01T07:19:00Z"
weight = 42789
keywords = [ "windows7", "window", "tcp", "tcpwindowsize" ]
aliases = [ "/questions/42789" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Windows 7 TCP Window "Auto-Tuning"](/questions/42789/windows-7-tcp-window-auto-tuning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42789-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As far I know (have just red to be honest :-) ) Windows 7 TCP stack has "Auto-Tuning" functionality which one in particular has following property:</p><blockquote><blockquote><blockquote><blockquote><p>The idea is, a small initial RWIN value is advertised, which is then adjusted on the fly depending on the current line speed and latency. ….//…</p></blockquote></blockquote></blockquote></blockquote><p>I am very interested in this – cos using 3G connection with increasing latency I got sharp fall of TCP downloads speed, so I perform few tests: TEST 1.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/delay1.jpg" alt="alt text" /></p><p>I performed same test few more time and in most cases I got same results – latency increased during transmission and then sharp fall of TCP downloads speed, cos sender instead of sending more segments has to wait for ACKs from receiver. Window size increase can solve this, I suppose, but as you can see Receive window stay constant – 17680 bytes, what is small for 3G connection. But another day I performed tests again and got another condition – stable high download speed without falls and spikes, I checked Wireshark, and saw following:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/delay2.jpg" alt="alt text" /></p><p>As you can see after delay had increased ( what had resulted in TCP window full message in dump - cos no ACK received during window) receiver adjusted window from 17680 to 243440 bytes! And download speed didnt suffer.</p><p>Can somebody help me to understand why behavior is so different and why? I cant find in what is difference between downloads.</p><p>P.S. Ftp server, Ftp client and mobile network operator are same in all tests.</p><p>P.S2. Here is more, btw filtered to contain only one ftp transfer session and partially - <a href="https://www.cloudshark.org/captures/a04f219f963a">https://www.cloudshark.org/captures/a04f219f963a</a> - steady transfer with adaptive window on fly <a href="https://www.cloudshark.org/captures/a771a2dfa12d">https://www.cloudshark.org/captures/a771a2dfa12d</a> - rough transfer with persistent window</p></div><div id="question-tags" class="tags-container tags">windows7 window tcp tcpwindowsize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '15, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/4f86795c7a782fccae8a0b7bd270d1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mongolio&#39;s gravatar image" /><p>mongolio<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mongolio has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '15, 09:34</p></div></div><div id="comments-container-42789" class="comments-container"></div><div id="comment-tools-42789" class="comment-tools"></div><div class="clear"></div><div id="comment-42789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42796"></span>

<div id="answer-container-42796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42796-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Those screen shots are not really helpful as you cut away the IP addresses, so tracking packet direction is harder than it should be. Also, the three way handshake is important (and missing) to determine options and iRTT. Next time try to include all columns, or better yet, provide a capture file. Sanitize it with TraceWrangler if necessary.</p><p>On a side note: don't try to figure out what Autotuning does - most (all) of us who tried failed. There is no official (or even unofficial) information from Microsoft what their stack is doing, and when. It behaves totally different in various situations. Even things like Antivirus software has an impact. Maybe the receiver had enough memory when it pulled up the window and didn't in the other situation. Everything in modern computers depends on each other, so it's really hard to track behavior like that of the TCP stack.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-42796" class="comments-container"><span id="42805"></span><div id="comment-42805" class="comment"><div id="post-42805-score" class="comment-score"></div><div class="comment-text"><blockquote><p>or better yet, provide a capture file</p></blockquote><p>Just added partial capture files to first post.</p><blockquote><p>On a side note: don't try to figure out what Autotuning does - most (all) of us who tried failed.</p></blockquote><p>It is not my scope to figure out what Autotuning does but I have to find out in which conditions i can have steady download speed. Cos for me all download attempts looks rather similar - same PC, same ftp server, same Node-B, same distance from Node-B, same QoS levels in mobile network, same load on RF channels during tests and so on, but nevertheless in most cases I got poor performance with falls and spikes of traffic.</p></div><div id="comment-42805-info" class="comment-info"><span class="comment-age">(01 Jun '15, 09:53)</span> mongolio</div></div><span id="42806"></span><div id="comment-42806" class="comment"><div id="post-42806-score" class="comment-score">1</div><div class="comment-text"><p>Okay, but determining steady download speed conditions is easy (well, relatively) if you have a capture - just find out what slows you down. There's basically two issues that you'll face: packet loss, and window size too small. For a good analysis you'd need captures taken at the same time both at client and at the server to be able to compare what the situation for each node was.</p><p>Problem is, that it is really hard to tell why a system used a specific window size since we have that funky auto tuning stuff these days. It was a lot easier back when we all ran Windows XP and earlier :-)</p></div><div id="comment-42806-info" class="comment-info"><span class="comment-age">(01 Jun '15, 10:17)</span> Jasper ♦♦</div></div><span id="42830"></span><div id="comment-42830" class="comment"><div id="post-42830-score" class="comment-score"></div><div class="comment-text"><p>Jasper, as I red about Windows (OS) TCP realization it can use latency not only as signal to increase window size, but also as a signal to decrease window size to avoid upcoming congestion. Do you have any assumptions by what means does it derive when latency caused by changing transmission environment (when latency increased but there are no congestion) and when latency increased due to links utilization?</p></div><div id="comment-42830-info" class="comment-info"><span class="comment-age">(02 Jun '15, 09:39)</span> mongolio</div></div><span id="42831"></span><div id="comment-42831" class="comment"><div id="post-42831-score" class="comment-score">1</div><div class="comment-text"><p>No idea; that's in the realm of the mystical magic of the Windows TCP stack. It does what it does, I've given up to try to figure out why :)</p></div><div id="comment-42831-info" class="comment-info"><span class="comment-age">(02 Jun '15, 10:23)</span> Jasper ♦♦</div></div></div><div id="comment-tools-42796" class="comment-tools"></div><div class="clear"></div><div id="comment-42796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

