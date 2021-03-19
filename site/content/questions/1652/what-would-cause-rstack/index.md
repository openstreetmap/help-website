+++
type = "question"
title = "What would cause [RST,ACK]"
description = '''I trying to track down a connection issue. What I&#x27;m seeing is s [SYN] followed by a {RST,ACK} series of packets. What would cause this?'''
date = "2011-01-06T11:06:00Z"
lastmod = "2011-01-07T13:52:00Z"
weight = 1652
keywords = [ "rst" ]
aliases = [ "/questions/1652" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What would cause \[RST,ACK\]](/questions/1652/what-would-cause-rstack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1652-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I trying to track down a connection issue. What I'm seeing is s [SYN] followed by a {RST,ACK} series of packets. What would cause this?</p></div><div id="question-tags" class="tags-container tags">rst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '11, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/c3bd1443d5ce7c6fbcb0e450a31f84b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vmjr&#39;s gravatar image" /><p>vmjr<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vmjr has one accepted answer">100%</span></p></div></div><div id="comments-container-1652" class="comments-container"></div><div id="comment-tools-1652" class="comment-tools"></div><div class="clear"></div><div id="comment-1652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1656"></span>

<div id="answer-container-1656" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1656-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is very simply that the port you are trying to connect to is not being listened to on the remote host. Either your service is not running on the host, or possibly it has been firewalled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '11, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jan '11, 22:43</p></div></div><div id="comments-container-1656" class="comments-container"><span id="1659"></span><div id="comment-1659" class="comment"><div id="post-1659-score" class="comment-score"></div><div class="comment-text"><p>Two things: I think you mean "service is NOT running on the host". and usually a firewall does not reply with a RST packet if it is configured correctly. It will just drop the SYN with no answer at all. There are some IDS/IPS systems that issue forged RST packets sometimes though.</p></div><div id="comment-1659-info" class="comment-info"><span class="comment-age">(06 Jan '11, 18:57)</span> Jasper ♦♦</div></div><span id="1661"></span><div id="comment-1661" class="comment"><div id="post-1661-score" class="comment-score"></div><div class="comment-text"><p>Just fixed the not. I agree generally a firewall will be stealthy - but just covering the bases for the original poster.</p></div><div id="comment-1661-info" class="comment-info"><span class="comment-age">(06 Jan '11, 22:45)</span> martyvis</div></div></div><div id="comment-tools-1656" class="comment-tools"></div><div class="clear"></div><div id="comment-1656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1677"></span>

<div id="answer-container-1677" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1677-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have seen a SYN with a RST,ACK sent back. In this case is was a portmap failure on a CISCO ASA firewall. A nonat statement is needed to tell the firewall to not nat the packet as it passes through the firewall.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '11, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/d5aa09edfeeb0600f74a72e63806f227?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erics&#39;s gravatar image" /><p>erics<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erics has no accepted answers">0%</span></p></div></div><div id="comments-container-1677" class="comments-container"></div><div id="comment-tools-1677" class="comment-tools"></div><div class="clear"></div><div id="comment-1677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

