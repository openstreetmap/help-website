+++
type = "question"
title = "TDS (SQL Server) protocol getting byte order wrong?"
description = '''I have the same &quot;TDS5 query[Mailformed Packet]&quot; but when I look at the TDS packet, the decoded length for token 0x21 is 822083584(equivalent to hex 0x31000000) but the byte stream associated with it is 0x00000031. There are exactly 0x31 bytes of data followed the length field. I wonder that the TDS ...'''
date = "2012-11-24T08:58:00Z"
lastmod = "2012-11-24T10:15:00Z"
weight = 16264
keywords = [ "tds", "big-endian", "sql" ]
aliases = [ "/questions/16264" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TDS (SQL Server) protocol getting byte order wrong?](/questions/16264/tds-sql-server-protocol-getting-byte-order-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16264-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the same "TDS5 query[Mailformed Packet]" but when I look at the TDS packet, the decoded length for token 0x21 is 822083584(equivalent to hex 0x31000000) but the byte stream associated with it is 0x00000031. There are exactly 0x31 bytes of data followed the length field. I wonder that the TDS decoder mix up on the big/little endian in the interpretation. I run the wireshark on Windows(litte-endian) to analyze the packets while the packet captured were between two Solaris servers(big-endian).</p><p>I assume that "[Mailformed Packet]" is spilled out by TDS decoder since it believe it should see 822083584 bytes of data after the length field but it only see 49 bytes(0x31). If this is on the right track, than the question is whether TDS decoder decodes incorrectly all the time or it could decode correctly if the packets captured on little-endian OS? If TDS decoder can decode correctly some time, is there information(endian related) in the packets to allow TDS decoder always decode correctly?</p><p>-Frank</p></div><div id="question-tags" class="tags-container tags">tds big-endian sql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '12, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/96be47acb1aadcf1a87bd27a05e6e830?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frank&#39;s gravatar image" /><p>frank<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frank has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 24 Nov '12, 09:46</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-16264" class="comments-container"></div><div id="comment-tools-16264" class="comment-tools"></div><div class="clear"></div><div id="comment-16264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16265"></span>

<div id="answer-container-16265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16265-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The TDS decoder has a "TDS decode as" preference; it can be set to "Little Endian", which is the default (regardless of whether the machine on which Wireshark is running, or the machine on which the traffic is captured, is big-endian or little-endian), or to "Big Endian". You should set it to "Big Endian" if the traffic is, as appears to be the case, big-endian. The byte order of the host on which the capture was done, or on which Wireshark is running (which are not necessarily the same host), isn't relevant here.</p><p>At least in some versions of the login messages, there's a byte-order indicator, which could be used to determine the byte order of the session, but currently isn't being used for that. That wouldn't, of course, help if the login wasn't captured.</p><p>The dissector could also possibly check the sanity of the 4-byte length field for those tokens that have them, and switch the byte order if the high-order bits of the length field in the current byte order are set and the low-order bits are clear.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '12, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16265" class="comments-container"></div><div id="comment-tools-16265" class="comment-tools"></div><div class="clear"></div><div id="comment-16265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

