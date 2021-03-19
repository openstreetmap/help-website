+++
type = "question"
title = "What is tns.port?"
description = '''I was looking at the sqloracle dissector (packet-sqloracle.c) and I noticed that it doesn&#x27;t register a TCP port; instead, it registers tns.port, as follows: dissector_add_uint(&quot;tns.port&quot;, TCP_PORT_TNS, sqloracle_handle);  What is tns.port? Is this dissector able to be used, or is it there &quot;in case s...'''
date = "2013-03-07T14:05:00Z"
lastmod = "2013-03-07T14:41:00Z"
weight = 19290
keywords = [ "sqloracle", "dissector" ]
aliases = [ "/questions/19290" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What is tns.port?](/questions/19290/what-is-tnsport)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19290-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was looking at the sqloracle dissector (packet-sqloracle.c) and I noticed that it doesn't register a TCP port; instead, it registers <code>tns.port</code>, as follows:</p><pre><code>dissector_add_uint(&quot;tns.port&quot;, TCP_PORT_TNS, sqloracle_handle);</code></pre><p>What is <code>tns.port</code>?</p><p>Is this dissector able to be used, or is it there "in case someone wants to use it in the future"?</p></div><div id="question-tags" class="tags-container tags">sqloracle dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '13, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/8df259c952186aa93179732461b8d1e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moshe&#39;s gravatar image" /><p>moshe<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moshe has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Mar '13, 14:05</p></div></div><div id="comments-container-19290" class="comments-container"></div><div id="comment-tools-19290" class="comment-tools"></div><div class="clear"></div><div id="comment-19290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19292"></span>

<div id="answer-container-19292" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19292-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK: it's there in case someone wants to try to use it as the base for creating an sqloracle dissector.</p><p>See:</p><p><a href="https://www.wireshark.org/lists/wireshark-dev/200704/msg00176.html">EMail 1</a> and <a href="https://www.wireshark.org/lists/wireshark-dev/200704/msg00186.html">EMail 2</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '13, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Mar '13, 14:42</p></div></div><div id="comments-container-19292" class="comments-container"><span id="19295"></span><div id="comment-19295" class="comment"><div id="post-19295-score" class="comment-score"></div><div class="comment-text"><p>I had found the same emails when I googled. Given that they're more than five years old, I'm hoping for something slightly more authoritative, and if there have been any updates since then.</p></div><div id="comment-19295-info" class="comment-info"><span class="comment-age">(07 Mar '13, 17:12)</span> moshe</div></div><span id="19296"></span><div id="comment-19296" class="comment"><div id="post-19296-score" class="comment-score"></div><div class="comment-text"><p>AFAIK no one has done any work on this (or at least no one has submitted any patches on this).</p></div><div id="comment-19296-info" class="comment-info"><span class="comment-age">(07 Mar '13, 17:21)</span> Bill Meier ♦♦</div></div><span id="21421"></span><div id="comment-21421" class="comment"><div id="post-21421-score" class="comment-score"></div><div class="comment-text"><p>I contacted the wireshark devs - it appears that TNS is something that <em>may</em> run on top of TCP/UDP, specifically for Oracle SQL traffic. This dissector was removed in r48349 and was the only occurrence of <code>tns.port</code>s use. You can read more at the <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8449">bug report</a> I filed.</p></div><div id="comment-21421-info" class="comment-info"><span class="comment-age">(23 May '13, 11:34)</span> moshe</div></div></div><div id="comment-tools-19292" class="comment-tools"></div><div class="clear"></div><div id="comment-19292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

