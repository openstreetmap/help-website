+++
type = "question"
title = "NAT breaks relative sequence numbers"
description = '''I have a capture situation where traffic from a particular host is seen with a translated IP in one direction and an untranslated IP in the reverse direction. Wireshark treats this as two separate connections, and sets relative sequence numbers independently. Is there a way to force Wireshark to use...'''
date = "2016-01-16T10:51:00Z"
lastmod = "2016-01-16T11:25:00Z"
weight = 49275
keywords = [ "relative", "number", "nat", "sequence" ]
aliases = [ "/questions/49275" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [NAT breaks relative sequence numbers](/questions/49275/nat-breaks-relative-sequence-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49275-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture situation where traffic from a particular host is seen with a translated IP in one direction and an untranslated IP in the reverse direction. Wireshark treats this as two separate connections, and sets relative sequence numbers independently. Is there a way to force Wireshark to use the translated IP and the untranslated IP as a single connection for relative sequence number purposes?</p></div><div id="question-tags" class="tags-container tags">relative number nat sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '16, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/3692efbae740e7e090820d147c0f5e98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulS&#39;s gravatar image" /><p>PaulS<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulS has no accepted answers">0%</span></p></div></div><div id="comments-container-49275" class="comments-container"><span id="49276"></span><div id="comment-49276" class="comment"><div id="post-49276-score" class="comment-score"></div><div class="comment-text"><p>(I know that I can disable the relative sequence numbers, but I'm looking for a way to still be able to use them.)</p></div><div id="comment-49276-info" class="comment-info"><span class="comment-age">(16 Jan '16, 11:05)</span> PaulS</div></div><span id="49277"></span><div id="comment-49277" class="comment"><div id="post-49277-score" class="comment-score"></div><div class="comment-text"><p>(I imagine if I could capture the three-way-handshake at the very start of the buffer that might get very close to what I want, but usually the three-way-handshake happened before I started the capture.)</p></div><div id="comment-49277-info" class="comment-info"><span class="comment-age">(16 Jan '16, 11:11)</span> PaulS</div></div></div><div id="comment-tools-49275" class="comment-tools"></div><div class="clear"></div><div id="comment-49275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49278"></span>

<div id="answer-container-49278" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49278-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In your situation, I would use <a href="https://www.tracewrangler.com/">TraceWrangler</a> and its <a href="https://www.tracewrangler.com/documentation/TraceWrangler.html?IPv4.html">IPv4 replacement capability</a> to substitute the IP address in one of the directions before starting the TCP analysis.</p><p>As NAT often translates also ports (strictly speaking NAT does not but in common language no one distinguishes between NAT and NAPT), it may be necessary to use also client port substitution at TCP layer.</p><p>Beware: When the current version of TraceWrangler substitutes tcp ports selectively by the "original" socket, it actually does that <em>after</em> already changing the IP. So if you want to substitute original socket (IP:port) A:a with B:b, your "anonymization" task has to contain two rules:</p><ul><li><p>at IPv4 layer "Replace IP addresses by list", the table must contain "original IP" A and "replacement" B</p></li><li><p>at TCP layer "Replace TCP ports by socket list", the row in the table must contain "original IP" B, "original port" a and "replacement port" b.</p></li></ul><p>@Jasper, is this intentional or it just happened?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '16, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '16, 12:48</p></div></div><div id="comments-container-49278" class="comments-container"><span id="49282"></span><div id="comment-49282" class="comment"><div id="post-49282-score" class="comment-score"></div><div class="comment-text"><p>@sindy no, that sounds like a typical bug of the category "Jasper hasn't thought this through well enough" ;-)</p><p>Funny enough the reason for this annoying behavior is calculating TCP checksums: sanitized packets are reassembled from top to bottom (= TCP before IP), and for the TCP sequence I need to look at the IPv4 PseudoHeader. Which means that IPv4 addresses need to be sanitized early (before actually sanitizing the IPv4 <strong>layer</strong>), and that happens before doing the socket replacement thing.</p><p>Thanks for the "bug report" :-)</p></div><div id="comment-49282-info" class="comment-info"><span class="comment-age">(16 Jan '16, 17:32)</span> Jasper ♦♦</div></div><span id="49284"></span><div id="comment-49284" class="comment"><div id="post-49284-score" class="comment-score"></div><div class="comment-text"><p>Fixed in the current semi-auto build.</p></div><div id="comment-49284-info" class="comment-info"><span class="comment-age">(16 Jan '16, 17:56)</span> Jasper ♦♦</div></div></div><div id="comment-tools-49278" class="comment-tools"></div><div class="clear"></div><div id="comment-49278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

