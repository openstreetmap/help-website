+++
type = "question"
title = "[closed] PMTUD and retransmission - Out-Of-Order?"
description = '''Hello, I have a trace showing PMTUD in action.  I was surprised to see that the retransmitted segment is not flagged as tcp.analysis.retransmission but as tcp.analysis.out_of_order Here is the trace |frame contains d748:8e30:5e03|  I&#x27;m talking about frame 73 carrying the same sequence number as 65 b...'''
date = "2013-08-29T11:16:00Z"
lastmod = "2013-08-29T11:16:00Z"
weight = 24172
keywords = [ "pmtu", "out-of-order", "retransmission", "discovery" ]
aliases = [ "/questions/24172" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] PMTUD and retransmission - Out-Of-Order?](/questions/24172/pmtud-and-retransmission-out-of-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24172-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a trace showing PMTUD in action.</p><p>I was surprised to see that the retransmitted segment is not flagged as <code>tcp.analysis.retransmission</code> but as <code>tcp.analysis.out_of_order</code> Here is the trace <a href="https://www.cloudshark.org/captures/4ebfd727cc6c?filter=frame%20contains%20d748%3A8e30%3A5e03">|frame contains d748:8e30:5e03|</a> <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-3.png" alt="alt text" /> I'm talking about frame 73 carrying the same sequence number as 65 but with a reduced MSS.</p><p>Shouldn't this be flagged as a retransmision? Thanks in advance for your input.</p></div><div id="question-tags" class="tags-container tags">pmtu out-of-order retransmission discovery</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '13, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>closed 14 Nov '13, 01:03</p></div></div><div id="comments-container-24172" class="comments-container"></div><div id="comment-tools-24172" class="comment-tools"></div><div class="clear"></div><div id="comment-24172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Problem is not reproducible or outdated" by mrEEde 14 Nov '13, 01:03

</div>

</div>

</div>

