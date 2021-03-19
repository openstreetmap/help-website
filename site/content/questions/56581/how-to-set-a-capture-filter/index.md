+++
type = "question"
title = "How to set a capture filter"
description = '''I&#x27;m new to Wireshark and have a very basic question. How do I set a capture filter? However I set one - including selecting the samples that are included in Wireshark - it is flagged pink. I believe that means I have a syntax error. That certainly can&#x27;t be the case with the sample filters so somethi...'''
date = "2016-10-22T16:45:00Z"
lastmod = "2016-10-22T18:29:00Z"
weight = 56581
keywords = [ "capture_filter" ]
aliases = [ "/questions/56581" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to set a capture filter](/questions/56581/how-to-set-a-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56581-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to Wireshark and have a very basic question. How do I set a capture filter? However I set one - including selecting the samples that are included in Wireshark - it is flagged pink. I believe that means I have a syntax error. That certainly can't be the case with the sample filters so something else must be going wrong.</p><p>The filter I want to set is "host wdmycloud" or "host 192.168.1.47" - a NAS on my LAN.</p><p>I don't see how it could matter, but I'm running Wireshark on Windows 10 using Win10Pcap rather than the Pcap that comes with Wireshark. Packet capture seems to work fine ... as long as I don't want to filter it.<br />
</p></div><div id="question-tags" class="tags-container tags">capture_filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '16, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/e4ee37f08a93628abb707f1b0a2473e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pokeefe0001&#39;s gravatar image" /><p>pokeefe0001<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pokeefe0001 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-56581" class="comments-container"><span id="56614"></span><div id="comment-56614" class="comment"><div id="post-56614-score" class="comment-score"></div><div class="comment-text"><p>Note that Win10Pcap is an external project that is not recommended by the Wireshark project.</p><p>WinPcap 4.1.3 works just as well on Windows 10 as it does on older versions of Windows, but if you need features not provided by WinPcap such as Local Loopback or 802.11 monitor mode capture then use the experimental replacement <a href="https://github.com/nmap/npcap">npcap</a>.</p></div><div id="comment-56614-info" class="comment-info"><span class="comment-age">(24 Oct '16, 07:36)</span> grahamb ♦</div></div></div><div id="comment-tools-56581" class="comment-tools"></div><div class="clear"></div><div id="comment-56581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56582"></span>

<div id="answer-container-56582" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56582-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unless you've set a default interface, when you first launch Wireshark, no interface is selected.</p><p>Select the capture interface <em>before</em> you enter the capture filter. The syntax check will stay red until you've selected an interface and entered valid capture filter syntax.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '16, 18:29</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-56582" class="comments-container"><span id="56583"></span><div id="comment-56583" class="comment"><div id="post-56583-score" class="comment-score"></div><div class="comment-text"><p>Thank you. Maybe that should have been obvious, but I missed it.</p><p>Is there a way to "close" a thread on this forum?</p></div><div id="comment-56583-info" class="comment-info"><span class="comment-age">(22 Oct '16, 20:13)</span> pokeefe0001</div></div><span id="56584"></span><div id="comment-56584" class="comment"><div id="post-56584-score" class="comment-score"></div><div class="comment-text"><p>Actually, it's not that obvious, because in earlier versions, Wireshark's syntax checking would turn green as soon as you typed a valid filter, even if no interface was selected.</p><p>If you're happy with the answer, you can click to Accept it, but it's not necessary to close a thread.</p></div><div id="comment-56584-info" class="comment-info"><span class="comment-age">(22 Oct '16, 21:20)</span> Jim Aragon</div></div><span id="56595"></span><div id="comment-56595" class="comment"><div id="post-56595-score" class="comment-score"></div><div class="comment-text"><p>It's not a forum, it's a Q&amp;A site, so this isn't really a "thread" to close. Think of it as a crowd-sourced FAQ; we keep it "open" so that somebody can search the site to see if anybody else has asked the same question and gotten an answer, in which case they don't have to ask the question themselves and wait for the answer. To say "OK, this answer solved my problem, so I don't have to ask any more", you accept the answer in question, as Jim Aragon suggests.</p></div><div id="comment-56595-info" class="comment-info"><span class="comment-age">(23 Oct '16, 18:12)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-56582" class="comment-tools"></div><div class="clear"></div><div id="comment-56582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

