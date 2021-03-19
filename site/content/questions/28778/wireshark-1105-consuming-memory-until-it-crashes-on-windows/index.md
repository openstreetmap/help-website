+++
type = "question"
title = "Wireshark 1.10.5 consuming memory until it crashes on windows"
description = '''Wireshark 1.10.5, installed just today on w2k8 r2 system. Normally I run Wireshark on Linux (openSUSE 12.x still, x86_64) and use it for hours on end and it&#x27;s just fine. Today I needed to do some SSL decryption so I had to fire up a VM and install Wireshark there. Getting the latest and installing i...'''
date = "2014-01-10T11:51:00Z"
lastmod = "2014-01-10T17:21:00Z"
weight = 28778
keywords = [ "windows", "ssl", "memory" ]
aliases = [ "/questions/28778" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 1.10.5 consuming memory until it crashes on windows](/questions/28778/wireshark-1105-consuming-memory-until-it-crashes-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28778-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark 1.10.5, installed just today on w2k8 r2 system.</p><p>Normally I run Wireshark on Linux (openSUSE 12.x still, x86_64) and use it for hours on end and it's just fine. Today I needed to do some SSL decryption so I had to fire up a VM and install Wireshark there. Getting the latest and installing it everything is fine, I can filter into the stream I want (tcp.port==636), packet decryption works, but memory growth is incredible. What starts as a 72 MB process (as shown in default Task Manager) while opening these little 200 or 900 KB files quickly balloons up past a couple hundred GB. In each case after getting into the trace for a while (maybe fifteen minutes of poking through a stream packet by packet, maybe one hundred packets or so until I get to the end of the stream) Wireshark has taken so much memory that it starts erroring and eventually windows tells me that it is a bad process and kills it. Restarting everything is fine again, the problem continues. Just now to do some verification, I scrolled quickly through about forty packets of SSLized LDAP packets, just going through the packet list, and the memory footprint went from 190 MB to 390 MB. Scrolling back down through the same list gets me up to 620 MB.</p><p>I know that memory growth is not a memory leak, but this is not normal memory growth, and having the application crash with a &lt; 1 MB file open on any system is probably pushing the limits of what should ever happen. I do not know if this is related to the SSL decryption, but it could be. Otherwise, these traces were taken with tcpdump on SUSE Linux Enterprise Server (SLES) 11 SP3 x86_64 filtering on ports 53, 389, 524, and 636.</p></div><div id="question-tags" class="tags-container tags">windows ssl memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '14, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/5e3d0d9274e8f74936c85b39491c8c57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dajoker&#39;s gravatar image" /><p>dajoker<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dajoker has no accepted answers">0%</span></p></div></div><div id="comments-container-28778" class="comments-container"><span id="28791"></span><div id="comment-28791" class="comment"><div id="post-28791-score" class="comment-score">1</div><div class="comment-text"><p>Seems it is already reported, and a problem with wireshark when accessed on a windows box via RDP. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8281">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8281</a></p></div><div id="comment-28791-info" class="comment-info"><span class="comment-age">(10 Jan '14, 22:12)</span> dajoker</div></div><span id="28797"></span><div id="comment-28797" class="comment"><div id="post-28797-score" class="comment-score"></div><div class="comment-text"><p>Thanks for checking for an existing bug, I forgot to mention to do that first.</p></div><div id="comment-28797-info" class="comment-info"><span class="comment-age">(11 Jan '14, 07:56)</span> Jasper ♦♦</div></div></div><div id="comment-tools-28778" class="comment-tools"></div><div class="clear"></div><div id="comment-28778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28788"></span>

<div id="answer-container-28788" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28788-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds more like a memory leak to me, but this is something the developers may have to take a look at. If you can provide the trace and the steps to reproduce the problem you could open a bug at <a href="http://bugs.wireshark.org">Bugzilla</a>. Even if you can't share the trace you could at least describe how the problem may be reproducible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '14, 17:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28788" class="comments-container"></div><div id="comment-tools-28788" class="comment-tools"></div><div class="clear"></div><div id="comment-28788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

