+++
type = "question"
title = "Ssh display filter doesn&#x27;t match TCP port 22 packets?"
description = '''While analyzing packets for an ssl issue today, I entered &quot;ssl&quot; into the Display Filter, and no packets were found. Further inspection showed that there WERE TCP packets using port 22 in this trace. I was very surprised that my filter didn&#x27;t find them. Some more experimentation showed the following ...'''
date = "2014-01-09T21:17:00Z"
lastmod = "2014-01-09T21:38:00Z"
weight = 28760
keywords = [ "ssh", "display-filter" ]
aliases = [ "/questions/28760" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Ssh display filter doesn't match TCP port 22 packets?](/questions/28760/ssh-display-filter-doesnt-match-tcp-port-22-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28760-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While analyzing packets for an ssl issue today, I entered "ssl" into the Display Filter, and no packets were found. Further inspection showed that there WERE TCP packets using port 22 in this trace. I was very surprised that my filter didn't find them.</p><p>Some more experimentation showed the following Wireshark behavior for packets using TCP port 22...</p><p>If a successful SSL connection was established (3-way handshake completed), the ssh filter found those ssl packets.</p><p>BUT, if an SSL connection was attempted, but not completed (destination did not respond to the SYN packets), the filter did not find these packets. I expected that the "ssl" display filter would match any TCP packets using port 22, but that was not the case.</p><p>Is this expected behavior??</p><p>Thx, Feenyman99</p></div><div id="question-tags" class="tags-container tags">ssh display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '14, 21:17</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p>feenyman99<br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-28760" class="comments-container"></div><div id="comment-tools-28760" class="comment-tools"></div><div class="clear"></div><div id="comment-28760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28761"></span>

<div id="answer-container-28761" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28761-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is expected behavior. If there is no data in the packet, then it's not an SSH packet, it's just a TCP packet. Wireshark behaves this way with all the higher-level protocols that run on top of TCP. For this reason, "tcp.port==22" is usually a better display filter than "ssh".</p><p>Even when the connection is successful, the "ssh" filter is only showing you the packets with data in them. It does not display the connection establishment process, the connection termination process, or any TCP packets that don't have data in them, such as naked ACKs, Zero Window, Keep-Alives, etc.</p><p>Use "tcp.port==22" when you want to see all the packets. Use "ssh" when you really only want to see the packets with data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '14, 21:38</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-28761" class="comments-container"><span id="28777"></span><div id="comment-28777" class="comment"><div id="post-28777-score" class="comment-score"></div><div class="comment-text"><p>Wow... This certainly proves the adage that you learn something everyday. I've been using Wireshark/Ethereal for 10+ years, and I never noticed this behavior. The most common "protocol" filter I use is probably "dns", which, unless it uses TCP, is almost never "data-less", so the "dns" filter will find the same packets as udp.port == 53.</p><p>I also often use "http", but I never noticed till I just now tried it again, that when i do that, the 3-way handshakes don't appear.</p><p>The only reason I noticed this behavior the other day, and submitted this question, is that I was troubleshooting an SSH connection attempt that never completed, and hence there were no data packets.</p><p>Anyway... Thanx for the clarification. I'm a wiser man today :-)</p></div><div id="comment-28777-info" class="comment-info"><span class="comment-age">(10 Jan '14, 11:28)</span> feenyman99</div></div></div><div id="comment-tools-28761" class="comment-tools"></div><div class="clear"></div><div id="comment-28761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

