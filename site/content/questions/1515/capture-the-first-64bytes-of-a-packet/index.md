+++
type = "question"
title = "Capture the first 64bytes of a packet?"
description = '''Does Wireshark provide the option of capturing just the first x number of bytes of a packet or frame? Thanks.'''
date = "2010-12-29T11:01:00Z"
lastmod = "2010-12-29T11:34:00Z"
weight = 1515
keywords = [ "capture", "partial", "packet" ]
aliases = [ "/questions/1515" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture the first 64bytes of a packet?](/questions/1515/capture-the-first-64bytes-of-a-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1515-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does Wireshark provide the option of capturing just the first x number of bytes of a packet or frame? Thanks.</p></div><div id="question-tags" class="tags-container tags">capture partial packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '10, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/f85fa7a7d0e72c2b17f545a68d5c0b45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesClassV&#39;s gravatar image" /><p>JamesClassV<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesClassV has no accepted answers">0%</span></p></div></div><div id="comments-container-1515" class="comments-container"></div><div id="comment-tools-1515" class="comment-tools"></div><div class="clear"></div><div id="comment-1515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1516"></span>

<div id="answer-container-1516" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1516-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are two ways to do this. One would be to recomiple the kernel of your operating system to capture 64 bytes (reprogram winpcap), <strong>OR</strong> in the capture options window (ctrl-K), you can use the Limit Each Packet to ... bytes" dialog.</p><p>I would go with option #2! :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '10, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-1516" class="comments-container"><span id="1519"></span><div id="comment-1519" class="comment"><div id="post-1519-score" class="comment-score"></div><div class="comment-text"><p>lol @option #1... Hansang, having fun? :-)))</p></div><div id="comment-1519-info" class="comment-info"><span class="comment-age">(29 Dec '10, 14:50)</span> Jasper ♦♦</div></div><span id="1539"></span><div id="comment-1539" class="comment"><div id="post-1539-score" class="comment-score"></div><div class="comment-text"><p>With all the progammers around here, you never know! ;)</p></div><div id="comment-1539-info" class="comment-info"><span class="comment-age">(30 Dec '10, 07:24)</span> hansangb</div></div></div><div id="comment-tools-1516" class="comment-tools"></div><div class="clear"></div><div id="comment-1516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1518"></span>

<div id="answer-container-1518" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1518-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you hansangb! Option 2 it is!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '10, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/f85fa7a7d0e72c2b17f545a68d5c0b45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesClassV&#39;s gravatar image" /><p>JamesClassV<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesClassV has no accepted answers">0%</span></p></div></div><div id="comments-container-1518" class="comments-container"></div><div id="comment-tools-1518" class="comment-tools"></div><div class="clear"></div><div id="comment-1518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

