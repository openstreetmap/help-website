+++
type = "question"
title = "Name resolution only from hosts files, no DNS, even from Trace"
description = '''Hi There, Wireshark 1.12.0 First of all, I had a look in the following bug: https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7380 which did not really answered my question. My question: is there a way to disable the fact that Wireshark takes resolution information from the trace (i.e. check the D...'''
date = "2014-08-12T03:13:00Z"
lastmod = "2014-08-12T05:11:00Z"
weight = 35429
keywords = [ "resolution", "hosts", "dns" ]
aliases = [ "/questions/35429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Name resolution only from hosts files, no DNS, even from Trace](/questions/35429/name-resolution-only-from-hosts-files-no-dns-even-from-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35429-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There,</p><p>Wireshark 1.12.0</p><p>First of all, I had a look in the following bug: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7380">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7380</a> which did not really answered my question.</p><p>My question: is there a way to disable the fact that Wireshark takes resolution information from the trace (i.e. check the DNS lookups inside the trace) to resolve IPs?</p><p>I have all the resolutions from a hosts files, and I don't want the resolution to be based on any DNS solution (either from external DNS server, or from inside DNS request from trace), but ONLY from the hosts file I defined.</p><p>Is this possible? I don't find any parameter looking like this in the preferences.</p><p>Thanks Best Regards Louis</p></div><div id="question-tags" class="tags-container tags">resolution hosts dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '14, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/6bbe03d9e54c7f6e4cb27b1d530ed94c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ketzaldev&#39;s gravatar image" /><p>ketzaldev<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ketzaldev has one accepted answer">100%</span></p></div></div><div id="comments-container-35429" class="comments-container"></div><div id="comment-tools-35429" class="comment-tools"></div><div class="clear"></div><div id="comment-35429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35432"></span>

<div id="answer-container-35432" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35432-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, after looking for this for a few hours, I finally found the solution, where I was not expecting to find it.</p><p>There is a parameter in the preferences, under "Protocols-&gt;DNS", called "Use DNS Packet data for address resolution", that you have to untick. I would have expect to see such a parameter in the "Name Resolution" tab, which would make more sense.</p><p>anyway, problem fixed...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '14, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/6bbe03d9e54c7f6e4cb27b1d530ed94c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ketzaldev&#39;s gravatar image" /><p>ketzaldev<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ketzaldev has one accepted answer">100%</span></p></div></div><div id="comments-container-35432" class="comments-container"></div><div id="comment-tools-35432" class="comment-tools"></div><div class="clear"></div><div id="comment-35432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

