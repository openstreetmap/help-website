+++
type = "question"
title = "Wireshark is Phoning Home (checking for updates)"
description = '''Lately I&#x27;ve been putting up a quarantine on the Windows desktop when I step away to see if any spyware/malware lurks within. Part of the exercise is to run Wireshark to capture suspicious traffic on one particular path. Immediately upon starting Wireshark, I saw this: Nov 8 00:51:23 asa5505 %ASA-4-1...'''
date = "2013-11-07T17:45:00Z"
lastmod = "2013-11-07T18:29:00Z"
weight = 26761
keywords = [ "check", "updates", "wireshark" ]
aliases = [ "/questions/26761" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark is Phoning Home (checking for updates)](/questions/26761/wireshark-is-phoning-home-checking-for-updates)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26761-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Lately I've been putting up a quarantine on the Windows desktop when I step away to see if any spyware/malware lurks within.</p><p>Part of the exercise is to run Wireshark to capture suspicious traffic on one particular path.</p><p>Immediately upon starting Wireshark, I saw this:</p><p>Nov 8 00:51:23 asa5505 %ASA-4-106100: access-list forward-inside denied tcp inside/10.29.87.10(54796) -&gt; outside/108.162.204.234(443) hit-cnt 1 first hit [0x2b7f3f90, 0x0]</p><p>Nov 8 00:51:24 asa5505 %ASA-4-106100: access-list forward-inside denied tcp inside/10.29.88.10(54797) -&gt; outside/108.162.203.234(443) hit-cnt 1 first hit [0xe0514b70, 0x0]</p><p>Running a second instance of Wireshark shows that that a DNS query to www.wireshark.org is made and resolves to the above address, and the connection attempts follow immediately. 100% reproducible.</p><p>So Wireshark is clearly phoning home. NOT liking this one bit.</p><p>What gives here?</p><p>Version 1.10.3 (SVN Rev 53022 from /trunk-1.10)</p><p>Compiled (64-bit). . .</p></div><div id="question-tags" class="tags-container tags">check updates wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '13, 17:45</strong></p><img src="https://secure.gravatar.com/avatar/2178feea77e6da3295835390700ebe72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="starlight&#39;s gravatar image" /><p>starlight<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="starlight has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '13, 04:16</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-26761" class="comments-container"><span id="26762"></span><div id="comment-26762" class="comment"><div id="post-26762-score" class="comment-score"></div><div class="comment-text"><p>Before anyone asks: NO BROWSERS are running on the machine when this happens. No other application that could possibly make the request. The requests appear within one second of starting Wireshark. The quarantine ACL traps no network traffic that cannot be accounted for.</p><p>Wireshark is sending out one TCP connection request to www.wireshark.org:443 from each interface on the system.</p></div><div id="comment-26762-info" class="comment-info"><span class="comment-age">(07 Nov '13, 18:08)</span> starlight</div></div></div><div id="comment-tools-26761" class="comment-tools"></div><div class="clear"></div><div id="comment-26761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26764"></span>

<div id="answer-container-26764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26764-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has joined the ranks of programs that can automatically check for updates. That's probably what you're seeing. To confirm / turn off, go to Edit &gt; Preferences, and in the User Interface section, uncheck "Check for updates."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '13, 18:29</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-26764" class="comments-container"><span id="26765"></span><div id="comment-26765" class="comment"><div id="post-26765-score" class="comment-score"></div><div class="comment-text"><p>Yes, that's fixed it. Setting is not where one would expect to look--an automatic update did cross my mind.</p></div><div id="comment-26765-info" class="comment-info"><span class="comment-age">(07 Nov '13, 19:16)</span> starlight</div></div><span id="26774"></span><div id="comment-26774" class="comment"><div id="post-26774-score" class="comment-score"></div><div class="comment-text"><p>@starlight: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-26774-info" class="comment-info"><span class="comment-age">(08 Nov '13, 04:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26764" class="comment-tools"></div><div class="clear"></div><div id="comment-26764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

