+++
type = "question"
title = "Memory Consumption"
description = '''The new version of wireshark 1.6.8 + are consuming excessive amounts of RAM memory, and has used up all the memory on the machine I am using. Are you planning to go back to how 1.2.7 works, not using local RAM or at least minimize it so it doesn&#x27;t grow more than 5 mb of memory. with this memory usag...'''
date = "2012-07-20T11:38:00Z"
lastmod = "2012-07-20T14:00:00Z"
weight = 12882
keywords = [ "excessive", "consumption", "memory" ]
aliases = [ "/questions/12882" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Memory Consumption](/questions/12882/memory-consumption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12882-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The new version of wireshark 1.6.8 + are consuming excessive amounts of RAM memory, and has used up all the memory on the machine I am using.</p><p>Are you planning to go back to how 1.2.7 works, not using local RAM or at least minimize it so it doesn't grow more than 5 mb of memory.</p><p>with this memory usage on 1.6.8 and up, we cannot upgrade because this causes our servers problems when we are doing long term packet captures.</p><p>Also in 1.8.0, what happened to all the capture information in the options? how do I get those back?</p><p>Thanks Geoff</p><p>[email protected]<a href="http://pivotinc.com">pivotinc.com</a></p></div><div id="question-tags" class="tags-container tags">excessive consumption memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jul '12, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/ba313449913390c2b18531f263428e9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PapaPanthers&#39;s gravatar image" /><p>PapaPanthers<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PapaPanthers has no accepted answers">0%</span></p></div></div><div id="comments-container-12882" class="comments-container"><span id="12888"></span><div id="comment-12888" class="comment"><div id="post-12888-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Also in 1.8.0, what happened to all the capture information in the options? how do I get those back?</p></blockquote><p>To what capture information are you referring here?</p></div><div id="comment-12888-info" class="comment-info"><span class="comment-age">(20 Jul '12, 14:00)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-12882" class="comment-tools"></div><div class="clear"></div><div id="comment-12882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="12884"></span>

<div id="answer-container-12884" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12884-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately more features means more memory usage :-(</p><p>Wireshark isn't the tool of choice for long term captures as it maintains state info about the captured packets so will always run out of memory eventually. Dumpcap will capture without retaining state so can be used for longer captures, but even that may cause issues as the capture files grows ever larger. In this case use the Dumpcap -b options to limit each capture file by size or time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '12, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-12884" class="comments-container"><span id="24041"></span><div id="comment-24041" class="comment"><div id="post-24041-score" class="comment-score"></div><div class="comment-text"><p>It really is not OK, I was analysing IAX phone call, 1 minute of traffic (70 packets 100 bytes long) consumed several hundreds MBytes of memory in Wireshark 1.10, co I was trying older and older versions (latest from each stable branch). 1.6 and newer exhibit this problem, versions up to 1.4 are OK - described traffic consumed just few MBytes, that means that memory consumption between versions 1.4 and 1.6 increased hundred fold.</p></div><div id="comment-24041-info" class="comment-info"><span class="comment-age">(25 Aug '13, 14:40)</span> xtonda</div></div><span id="24049"></span><div id="comment-24049" class="comment"><div id="post-24049-score" class="comment-score"></div><div class="comment-text"><p>If you really have a 7k capture that causes Wireshark to consume several hundred MB of memory please raise an issue at the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark bugzilla</a> adding your capture as an attachment. Note that without a sample capture it's more difficult for developers to ascertain the nature of the problem and this difficulty can exceed the motivation available to resolve the issue.</p></div><div id="comment-24049-info" class="comment-info"><span class="comment-age">(26 Aug '13, 02:01)</span> grahamb ♦</div></div></div><div id="comment-tools-12884" class="comment-tools"></div><div class="clear"></div><div id="comment-12884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12885"></span>

<div id="answer-container-12885" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12885-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">Out of Memory</a> problem has been known since at least September 2005. Version 1.2.7 was <a href="http://www.wireshark.org/lists/wireshark-announce/201003/msg00000.html">released</a> on March 31, 2010.</p><p>As <a href="http://ask.wireshark.org/questions/9137#9138">suggested</a> <a href="ask.wireshark.org/questions/6320#6322">elsewhere</a>, you should use <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> for long running captures, not Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '12, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-12885" class="comments-container"></div><div id="comment-tools-12885" class="comment-tools"></div><div class="clear"></div><div id="comment-12885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12887"></span>

<div id="answer-container-12887" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12887-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Are you planning to go back to how 1.2.7 works, not using local RAM or at least minimize it so it doesn't grow more than 5 mb of memory.</p></blockquote><p>1.2.7, and every version of the software back to Ethereal 0.1, uses local RAM (as does every other application on your machine). Later versions might use more memory to store reassembled packet data, keep track of relationships between packets, etc.. We have, over time, made some changes to reduce the memory consumption of the packet list display (by using a different widget) and the table of all packets (by allocating them in bulk and not keeping two pointers in every entry in the table).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '12, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12887" class="comments-container"><span id="24047"></span><div id="comment-24047" class="comment"><div id="post-24047-score" class="comment-score"></div><div class="comment-text"><p>If you are on Windows it is possible you are the victim of a GTK+ bug affecting Windows server where large amounts of memory are lost when the screen is updated or something like that. It might be related to remote desktop as well.</p></div><div id="comment-24047-info" class="comment-info"><span class="comment-age">(26 Aug '13, 00:21)</span> Anders ♦</div></div></div><div id="comment-tools-12887" class="comment-tools"></div><div class="clear"></div><div id="comment-12887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

