+++
type = "question"
title = "Block sniffing on ports - UBUNTU"
description = '''The server where Wireshark is running has two network interfaces with two networks. The «sniffed» network, and the «office» one, from where people connect to the server. I don´t want wireshark to be able to sniff the office network. How do I do that?'''
date = "2012-09-14T08:15:00Z"
lastmod = "2012-09-14T12:29:00Z"
weight = 14267
keywords = [ "ports", "block", "ubuntu" ]
aliases = [ "/questions/14267" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Block sniffing on ports - UBUNTU](/questions/14267/block-sniffing-on-ports-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14267-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The server where Wireshark is running has two network interfaces with two networks. The «sniffed» network, and the «office» one, from where people connect to the server. I don´t want wireshark to be able to sniff the office network. How do I do that?</p></div><div id="question-tags" class="tags-container tags">ports block ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '12, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/43c3ba915f22dca0a0ea08398fc0b74b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ASantos&#39;s gravatar image" /><p>ASantos<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ASantos has no accepted answers">0%</span></p></div></div><div id="comments-container-14267" class="comments-container"></div><div id="comment-tools-14267" class="comment-tools"></div><div class="clear"></div><div id="comment-14267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14270"></span>

<div id="answer-container-14270" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14270-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do that on Linux (that I know of).</p><p>If you were using a BSD-derived OS then it would be possible as each interface has its own (file-based) permissions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-14270" class="comments-container"><span id="14318"></span><div id="comment-14318" class="comment"><div id="post-14318-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff</p></div><div id="comment-14318-info" class="comment-info"><span class="comment-age">(17 Sep '12, 02:05)</span> ASantos</div></div><span id="19580"></span><div id="comment-19580" class="comment"><div id="post-19580-score" class="comment-score"></div><div class="comment-text"><p>Actually, there are no per-<em>network interface</em> files on *BSD or OS X I know of that would control access to interfaces. The BPF <em>device</em> files have permissions, but once you've opened a BPF device file, you could bind the BPF device to any network interface.</p><p>So that won't work on *BSD or OS X, either.</p><p>On Tru64 UNIX, you could set a per-interface flag indicating whether a given interface can be put in promicuous mode by non-privileged users, but that's the only per-interface privilege control I know of.</p></div><div id="comment-19580-info" class="comment-info"><span class="comment-age">(16 Mar '13, 16:55)</span> Guy Harris ♦♦</div></div><span id="19584"></span><div id="comment-19584" class="comment"><div id="post-19584-score" class="comment-score"></div><div class="comment-text"><p>It would be interesting to see if AppArmor could be of service here. I'm not sure it offers the granularity required.</p></div><div id="comment-19584-info" class="comment-info"><span class="comment-age">(17 Mar '13, 03:41)</span> Jaap ♦</div></div></div><div id="comment-tools-14270" class="comment-tools"></div><div class="clear"></div><div id="comment-14270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

