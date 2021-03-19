+++
type = "question"
title = "Knowing the context I&#x27;m dissecting in"
description = '''I&#x27;ve written a dissector which can dissect a custom wrapper for bluetooth (one emitted by a bluetooth sniffer). I have it working nicely from a pcap file as USER10. I also added a heuristic to UDP so that I can do a live capture by writing to a local UDP port (pipes don&#x27;t work yet in wireshark 1.11)...'''
date = "2014-04-23T06:27:00Z"
lastmod = "2014-04-23T08:00:00Z"
weight = 32099
keywords = [ "dissector", "programming" ]
aliases = [ "/questions/32099" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Knowing the context I'm dissecting in](/questions/32099/knowing-the-context-im-dissecting-in)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32099-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've written a dissector which can dissect a custom wrapper for bluetooth (one emitted by a bluetooth sniffer). I have it working nicely from a pcap file as USER10. I also added a heuristic to UDP so that I can do a live capture by writing to a local UDP port (pipes don't work yet in wireshark 1.11).</p><p>The dissector decodes from and to addresses and puts those in the COL_DEF_DST and COL_DST_SRC columns, which is fine as a USER10 protocol, but when wrapped in UDP obviously I can't override the SRC and DST of 127.0.0.1 which the UDP dissector provides. What I'd like to do when decoded under UDP is put that information in the comment, it's not great, but at least it's there.</p><p>Is there a way I can tell the context I'm dissecting in and determine if UDP is 'above' me, so I know I need to put the from and to into the comment instead of setting the columns?</p></div><div id="question-tags" class="tags-container tags">dissector programming</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/32b9484a7a9c2d4c347a1dae9db3d1fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rols&#39;s gravatar image" /><p>rols<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rols has no accepted answers">0%</span></p></div></div><div id="comments-container-32099" class="comments-container"></div><div id="comment-tools-32099" class="comment-tools"></div><div class="clear"></div><div id="comment-32099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32104"></span>

<div id="answer-container-32104" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32104-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You coud try using pinfo-&gt;ptype == PT_UDP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32104" class="comments-container"></div><div id="comment-tools-32104" class="comment-tools"></div><div class="clear"></div><div id="comment-32104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

