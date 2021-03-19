+++
type = "question"
title = "Why does loading a small pcap take lots of memory on 1 machine but not on another?"
description = '''When I try and load a small capture (&amp;lt;5MB) Wireshark take over 2.5GB of ram and it takes a long time for the capture to appear on the screen. When my coworker loadss the same file on his machine running the same version of Wireshark it comes right up and utilizes little memory. Any ideas? Thanks ...'''
date = "2016-07-19T11:35:00Z"
lastmod = "2016-07-20T06:19:00Z"
weight = 54168
keywords = [ "ram", "out-of-memory", "memory" ]
aliases = [ "/questions/54168" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why does loading a small pcap take lots of memory on 1 machine but not on another?](/questions/54168/why-does-loading-a-small-pcap-take-lots-of-memory-on-1-machine-but-not-on-another)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I try and load a small capture (&lt;5MB) Wireshark take over 2.5GB of ram and it takes a long time for the capture to appear on the screen. When my coworker loadss the same file on his machine running the same version of Wireshark it comes right up and utilizes little memory. Any ideas? Thanks for the assist!</p></div><div id="question-tags" class="tags-container tags">ram out-of-memory memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '16, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/b963f7b58022c26d13366b942684a229?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kdonovan9&#39;s gravatar image" /><p>kdonovan9<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kdonovan9 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '16, 08:05</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-54168" class="comments-container"><span id="54169"></span><div id="comment-54169" class="comment"><div id="post-54169-score" class="comment-score"></div><div class="comment-text"><p>Did you try with identical Wireshark Versions and identical profiles? Profile settings can affect how Wireshark behaves, so even the same version may show differences.</p><p>Easiest way to test is to create a new (=default) profile on both machines, and load the trace again.</p></div><div id="comment-54169-info" class="comment-info"><span class="comment-age">(19 Jul '16, 11:45)</span> Jasper ♦♦</div></div></div><div id="comment-tools-54168" class="comment-tools"></div><div class="clear"></div><div id="comment-54168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54170"></span>

<div id="answer-container-54170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54170-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd suggest comparing your <code>preferences</code> files. I wouldn't be surprised if you had something like TCP reassembly enabled while your colleague had it disabled. You can find your <code>preferences</code> file via <code>Help -&gt; About Wireshark -&gt; Folders -&gt; Personal configuration</code>.</p><p>You could also look for any other differences between the machines, such as OS, 64-bit vs. 32-bit, etc. Compare <code>Help -&gt; About Wireshark</code> information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '16, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54170" class="comments-container"></div><div id="comment-tools-54170" class="comment-tools"></div><div class="clear"></div><div id="comment-54170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54185"></span>

<div id="answer-container-54185" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54185-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another possibility we saw recently is that your ssl_keylog file has grown to a huge size. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12501">bug 12501</a> for the history.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '16, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-54185" class="comments-container"><span id="63143"></span><div id="comment-63143" class="comment"><div id="post-63143-score" class="comment-score"></div><div class="comment-text"><p>I have this same problem. I downgraded to 2.2.8 and removed my personal settings as well. My sslkeylog is 70M. I will have to see what I did to enable the use of that file and see if my slowness comes back.</p></div><div id="comment-63143-info" class="comment-info"><span class="comment-age">(26 Jul '17, 10:47)</span> garrywx</div></div><span id="63146"></span><div id="comment-63146" class="comment"><div id="post-63146-score" class="comment-score"></div><div class="comment-text"><p>Ok that was it for sure. Recreated my problem after changing the setting under Pref-&gt;Protocols-&gt;SSL (Pre)-Master-Secret Log filename to point at my 70M file. I then deleted the file and performance is back to normal.</p></div><div id="comment-63146-info" class="comment-info"><span class="comment-age">(26 Jul '17, 11:04)</span> garrywx</div></div></div><div id="comment-tools-54185" class="comment-tools"></div><div class="clear"></div><div id="comment-54185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

