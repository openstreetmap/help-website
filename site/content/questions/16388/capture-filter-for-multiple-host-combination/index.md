+++
type = "question"
title = "Capture filter for multiple host combination"
description = '''I need a capture filter like the one mentioned below: /usr/sbin/tshark -i any (host IP1 or host IP2 or host IP3 and (host IP4 or host IP5)) and (udp or sctp) -w &quot;file.pcap&quot; In nutshell, I want udp and sctp packets that are sent from/to IP1 or IP2 and between IP3-IP4 and IP3-IP5. Now problem is the w...'''
date = "2012-11-28T06:52:00Z"
lastmod = "2012-11-28T07:02:00Z"
weight = 16388
keywords = [ "capture-filter" ]
aliases = [ "/questions/16388" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter for multiple host combination](/questions/16388/capture-filter-for-multiple-host-combination)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16388-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need a capture filter like the one mentioned below: <code>/usr/sbin/tshark -i any (host IP1 or host IP2 or host IP3 and (host IP4 or host IP5)) and (udp or sctp) -w "file.pcap"</code></p><p>In nutshell, I want udp and sctp packets that are sent from/to IP1 or IP2 and between IP3-IP4 and IP3-IP5.</p><p>Now problem is the way tshark processes these filters. I am not being able to get the capture.</p><p>Please suggest and help !</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '12, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/e007baa1950a507d2163e10837a2861d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajat&#39;s gravatar image" /><p>Rajat<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '12, 09:23</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-16388" class="comments-container"></div><div id="comment-tools-16388" class="comment-tools"></div><div class="clear"></div><div id="comment-16388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16389"></span>

<div id="answer-container-16389" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16389-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 'correct' filter (but not necessarily the best/fastest filter), would be:</p><blockquote><p><code>tshark -ni any '((host 10.0.0.1 or host 10.0.0.2) and (udp or sctp)) or (host 10.0.0.3 and host 10.0.0.4 and (udp or sctp)) or (host 10.0.0.3 and host 10.0.0.5 and (udp or sctp))'</code><br />
</p></blockquote><p>where:</p><blockquote><p><code>IP1 == 10.0.0.1</code><br />
<code>IP2 == 10.0.0.2</code><br />
<code>IP3 == 10.0.0.3</code><br />
</p></blockquote><p>etc.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '12, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Nov '12, 04:33</p></div></div><div id="comments-container-16389" class="comments-container"><span id="16414"></span><div id="comment-16414" class="comment"><div id="post-16414-score" class="comment-score"></div><div class="comment-text"><p>Hi, this filter works fine on Windows but fails on linux. I am using Wireshark:1.6.3 on both. Seems in linux "(" is not accepted. Can you please help?</p></div><div id="comment-16414-info" class="comment-info"><span class="comment-age">(29 Nov '12, 02:49)</span> Rajat</div></div><span id="16415"></span><div id="comment-16415" class="comment"><div id="post-16415-score" class="comment-score"></div><div class="comment-text"><p>The error in linux is: -bash: syntax error near unexpected token `('</p><p>Same command on Windows works.. But fails on linux.</p></div><div id="comment-16415-info" class="comment-info"><span class="comment-age">(29 Nov '12, 02:50)</span> Rajat</div></div><span id="16416"></span><div id="comment-16416" class="comment"><div id="post-16416-score" class="comment-score"></div><div class="comment-text"><p>Try using double quotes</p></div><div id="comment-16416-info" class="comment-info"><span class="comment-age">(29 Nov '12, 03:12)</span> grahamb ♦</div></div><span id="16417"></span><div id="comment-16417" class="comment"><div id="post-16417-score" class="comment-score"></div><div class="comment-text"><p>there was an error. Imbalance of opening/closing braces (copy-paste error). Please try the updated filter.</p></div><div id="comment-16417-info" class="comment-info"><span class="comment-age">(29 Nov '12, 04:33)</span> Kurt Knochner ♦</div></div><span id="16418"></span><div id="comment-16418" class="comment"><div id="post-16418-score" class="comment-score"></div><div class="comment-text"><p>Interesting that the borked version worked on Windows but not on Linux</p></div><div id="comment-16418-info" class="comment-info"><span class="comment-age">(29 Nov '12, 05:52)</span> grahamb ♦</div></div><span id="16419"></span><div id="comment-16419" class="comment not_top_scorer"><div id="post-16419-score" class="comment-score"></div><div class="comment-text"><p>It does not.</p><p>Fault filter:</p><blockquote><p><code>tshark -ni 2 '(host 10.0.0.1 or host 10.0.0.2 and (udp or sctp)) or (host 10.0.0.3 and host 10.0.0.4 and (udp or sctp)) or ((host 10.0.0.3 and host 10.0.0.5 and (udp or sctp))'</code><br />
</p></blockquote><p>I get this error: <code>tshark: Invalid capture filter</code><br />
</p><p>So, I don't know what filter @Rajat actually usesd.</p></div><div id="comment-16419-info" class="comment-info"><span class="comment-age">(29 Nov '12, 05:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16389" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-16389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

