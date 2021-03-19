+++
type = "question"
title = "Wireshark does not detect my Sierra Aircard mobile broadband adapter"
description = '''Wireshark does not detect my Sierra Aircard on Win 7 64 Bit'''
date = "2011-11-09T21:29:00Z"
lastmod = "2012-07-16T04:55:00Z"
weight = 7353
keywords = [ "sierrawireless", "aircard", "windows7", "64-bit" ]
aliases = [ "/questions/7353" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark does not detect my Sierra Aircard mobile broadband adapter](/questions/7353/wireshark-does-not-detect-my-sierra-aircard-mobile-broadband-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7353-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark does not detect my Sierra Aircard on Win 7 64 Bit</p></div><div id="question-tags" class="tags-container tags">sierrawireless aircard windows7 64-bit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '11, 21:29</strong></p><img src="https://secure.gravatar.com/avatar/6247246101823169ef6cb8e2975bc0fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rahaf&#39;s gravatar image" /><p>Rahaf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rahaf has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Feb '12, 14:07</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7353" class="comments-container"><span id="7365"></span><div id="comment-7365" class="comment"><div id="post-7365-score" class="comment-score"></div><div class="comment-text"><p><em>sigh</em> does it say "Microsoft" as Adapter somewhere?</p></div><div id="comment-7365-info" class="comment-info"><span class="comment-age">(10 Nov '11, 03:24)</span> Landi</div></div></div><div id="comment-tools-7353" class="comment-tools"></div><div class="clear"></div><div id="comment-7353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9262"></span>

<div id="answer-container-9262" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9262-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your Sierra Aircard is an adapter to connect your machine to the Internet through the mobile phone network; that means it probably looks like a PPP adapter to Windows, and <a href="http://www.winpcap.org/misc/faq.htm#Q-5">WinPcap does not support capturing on PPP adapters on Windows 7</a>. Wireshark uses WinPcap to capture traffic on Windows, so you can't use Wireshark to capture traffic on your mobile Internet connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '12, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9262" class="comments-container"></div><div id="comment-tools-9262" class="comment-tools"></div><div class="clear"></div><div id="comment-9262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12747"></span>

<div id="answer-container-12747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12747-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In case of Mobile Broadband Network Interface, WinPcap does not support capturing on it also. So our company made new filter driver for this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/a2cfcbb9754e717cee243a66c37ab35d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Louis&#39;s gravatar image" /><p>Louis<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Louis has no accepted answers">0%</span></p></div></div><div id="comments-container-12747" class="comments-container"></div><div id="comment-tools-12747" class="comment-tools"></div><div class="clear"></div><div id="comment-12747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

