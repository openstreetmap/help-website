+++
type = "question"
title = "Systematic TCP retransmission"
description = '''I have 5 same devices connected to the switch. The IPs are constant. Using Wireshark I see a systematic TCP retransmissions within 1 or 2 usec on ports 1 and 5 (only). After swapping Port 1 with 2 for example the retransmission remains the same. It is probably not due to the lose data. What can be t...'''
date = "2016-01-28T00:37:00Z"
lastmod = "2016-02-01T04:18:00Z"
weight = 49571
keywords = [ "tcp_retransmission", "retransmissions", "tcp", "retransmission" ]
aliases = [ "/questions/49571" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Systematic TCP retransmission](/questions/49571/systematic-tcp-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49571-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have 5 same devices connected to the switch. The IPs are constant. Using Wireshark I see a systematic TCP retransmissions within 1 or 2 usec on ports 1 and 5 (only). After swapping Port 1 with 2 for example the retransmission remains the same. It is probably not due to the lose data. What can be the issue?</p></div><div id="question-tags" class="tags-container tags">tcp_retransmission retransmissions tcp retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '16, 00:37</strong></p><img src="https://secure.gravatar.com/avatar/4c126cff500939d384880fa294c41886?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex_Oren&#39;s gravatar image" /><p>Alex_Oren<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex_Oren has no accepted answers">0%</span></p></div></div><div id="comments-container-49571" class="comments-container"><span id="49573"></span><div id="comment-49573" class="comment"><div id="post-49573-score" class="comment-score"></div><div class="comment-text"><p>Maye it is a duplex mismatch. Have you checked that the port and the device have the same link setting ? e.g. Both are set to autoneg?</p></div><div id="comment-49573-info" class="comment-info"><span class="comment-age">(28 Jan '16, 00:59)</span> Christian_R</div></div><span id="49574"></span><div id="comment-49574" class="comment"><div id="post-49574-score" class="comment-score"></div><div class="comment-text"><p>The devices are only half duplex. Initially, the PLC that is sending the commands was full duplex, I changed the setting in the switch for the PLC port to be half duplex as well. No influence on the problem behavior.</p></div><div id="comment-49574-info" class="comment-info"><span class="comment-age">(28 Jan '16, 01:23)</span> Alex_Oren</div></div><span id="49576"></span><div id="comment-49576" class="comment"><div id="post-49576-score" class="comment-score"></div><div class="comment-text"><p>Also the retransmission is very fast within 2 microseconds, so it is not due to any data loss. The time - scale of other commands is milliseconds</p></div><div id="comment-49576-info" class="comment-info"><span class="comment-age">(28 Jan '16, 01:27)</span> Alex_Oren</div></div><span id="49577"></span><div id="comment-49577" class="comment"><div id="post-49577-score" class="comment-score"></div><div class="comment-text"><p>where did you take the trace?</p></div><div id="comment-49577-info" class="comment-info"><span class="comment-age">(28 Jan '16, 01:35)</span> Christian_R</div></div><span id="49578"></span><div id="comment-49578" class="comment"><div id="post-49578-score" class="comment-score"></div><div class="comment-text"><p>A port in the switch was configured for port mirroring of all other ports and Wireshark was connected to this port.</p></div><div id="comment-49578-info" class="comment-info"><span class="comment-age">(28 Jan '16, 01:41)</span> Alex_Oren</div></div><span id="49580"></span><div id="comment-49580" class="comment not_top_scorer"><div id="post-49580-score" class="comment-score"></div><div class="comment-text"><p>Thank you.</p></div><div id="comment-49580-info" class="comment-info"><span class="comment-age">(28 Jan '16, 01:52)</span> Alex_Oren</div></div></div><div id="comment-tools-49571" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-49571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49678"></span>

<div id="answer-container-49678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49678-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like duplicate frames to me, caused by SPANning more than one port (all of them as far as you commented). This means that you'll see packets twice: once when it enters the switch on the source port (and gets copied to the monitor port) and again when it leaves the switch on the destination port.</p><p>You should try deduplicating your capture with editcap.</p><p>See this blog post for details: <a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '16, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-49678" class="comments-container"><span id="49679"></span><div id="comment-49679" class="comment"><div id="post-49679-score" class="comment-score"></div><div class="comment-text"><p>Jasper, In this case the behavior of ports 2,3 and 4 should be the same as 1 and 5? The retransmissions are only on ports 1 and 5</p></div><div id="comment-49679-info" class="comment-info"><span class="comment-age">(01 Feb '16, 04:24)</span> Alex_Oren</div></div><span id="49680"></span><div id="comment-49680" class="comment"><div id="post-49680-score" class="comment-score"></div><div class="comment-text"><p>Depends on what packets are arriving on which ports. Maybe try deduplicating your trace to see if editcap thinks there are duplicates. If it doesn't remove any frames it's something else.</p></div><div id="comment-49680-info" class="comment-info"><span class="comment-age">(01 Feb '16, 04:30)</span> Jasper ♦♦</div></div><span id="49686"></span><div id="comment-49686" class="comment"><div id="post-49686-score" class="comment-score"></div><div class="comment-text"><pre><code> A port in the switch was configured for port mirroring of all other ports </code></pre><p>I think Jasper has pointed out the most probable cause of that behaviour.</p></div><div id="comment-49686-info" class="comment-info"><span class="comment-age">(01 Feb '16, 06:10)</span> Christian_R</div></div><span id="49701"></span><div id="comment-49701" class="comment"><div id="post-49701-score" class="comment-score"></div><div class="comment-text"><p>@Alex_Oren, @Jasper's explanation seems to be the most likely one, but you need to perform additional tests to be sure.</p><p>The reason why the behaviour can only be seen on ports 1 and 5 but not 2, 3, 4 could be a misconfiguration or a bug of the switch, leading to different treatment of traffic on different ports. So to find out, I'd recommend to SPAN only a single port, one of the 1 or 5, and check whether the situation continues or not.</p></div><div id="comment-49701-info" class="comment-info"><span class="comment-age">(01 Feb '16, 14:27)</span> sindy</div></div></div><div id="comment-tools-49678" class="comment-tools"></div><div class="clear"></div><div id="comment-49678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

