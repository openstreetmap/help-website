+++
type = "question"
title = "Suspicious ARP activity?"
description = '''I&#x27;m kind of new to the world of monitoring network activity and I&#x27;m seeing something in my logs that concerns me a little. One computer, and only one, seems to be sending ARP requests to every single possible IP address (&quot;Who has 192.168.1.1, Who has 192.168.1.2... etc.). No other machine on this ne...'''
date = "2012-01-22T16:13:00Z"
lastmod = "2012-01-23T00:09:00Z"
weight = 8547
keywords = [ "arp", "ip", "virus", "ping" ]
aliases = [ "/questions/8547" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Suspicious ARP activity?](/questions/8547/suspicious-arp-activity)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8547-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm kind of new to the world of monitoring network activity and I'm seeing something in my logs that concerns me a little.</p><p>One computer, and only one, seems to be sending ARP requests to every single possible IP address ("Who has 192.168.1.1, Who has 192.168.1.2... etc.).</p><p>No other machine on this network is doing this. As I cannot fathom any legitimate reason any machine ought to be pinging every possible address, I'm thinking this machine probably has a virus looking to do mischief.</p><p>Thoughts?</p></div><div id="question-tags" class="tags-container tags">arp ip virus ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '12, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/e70c4ece5d334c65ea0d3bc54d3705f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Riversiderepeat&#39;s gravatar image" /><p>Riversiderepeat<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Riversiderepeat has no accepted answers">0%</span></p></div></div><div id="comments-container-8547" class="comments-container"></div><div id="comment-tools-8547" class="comment-tools"></div><div class="clear"></div><div id="comment-8547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8551"></span>

<div id="answer-container-8551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8551-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you see ARP packets for a full network range you might have some sort of ping sweep in your network, where a system tries to find out which other IPs are there. There are some legitimate reasons for it, for example if it comes from a network monitoring system. You'll have to identify the source of the ARP requests - you should see a "tell 192.168..." somewhere, which is always the same in Ping Sweeps, and that is the system scanning.</p><p>If the source is a system that should NOT do anything like this you might have a problem. Next step is to identify what software is running that may cause this, and evaluate if it really a case of mischief.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '12, 17:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8551" class="comments-container"></div><div id="comment-tools-8551" class="comment-tools"></div><div class="clear"></div><div id="comment-8551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8554"></span>

<div id="answer-container-8554" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8554-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are some home routers that do this. I have a Netopia router that does an ARP scan of the entire subnet every five minutes. There is no way to turn it off or change the interval, so it's expected behavior in my network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '12, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-8554" class="comments-container"></div><div id="comment-tools-8554" class="comment-tools"></div><div class="clear"></div><div id="comment-8554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

