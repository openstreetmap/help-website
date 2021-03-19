+++
type = "question"
title = "Only seeing 802.11 packets ... nothing else"
description = '''Under Mac Seria, latest version 2.4.2 (v2.4.2-0-gb6c63ae) install ... I am only seeing 802.11 packets from my Wi-Fi:en0 interface. Am I doing something wrong ? I thought I&#x27;d see TCP and other type of protocol packets ... thanks,'''
date = "2017-10-16T17:35:00Z"
lastmod = "2017-10-16T23:02:00Z"
weight = 63949
keywords = [ "sierra", "en0", "only", "wi-fi", "802.11" ]
aliases = [ "/questions/63949" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Only seeing 802.11 packets ... nothing else](/questions/63949/only-seeing-80211-packets-nothing-else)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63949-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Under Mac Seria, latest version 2.4.2 (v2.4.2-0-gb6c63ae) install ... I am only seeing 802.11 packets from my Wi-Fi:en0 interface.</p><p>Am I doing something wrong ? I thought I'd see TCP and other type of protocol packets ...</p><p>thanks,</p></div><div id="question-tags" class="tags-container tags">sierra en0 only wi-fi 802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '17, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/e9ecc556e2b428f5c6f7caa4d49c8c4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="richiwalt&#39;s gravatar image" /><p>richiwalt<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="richiwalt has no accepted answers">0%</span></p></div></div><div id="comments-container-63949" class="comments-container"></div><div id="comment-tools-63949" class="comment-tools"></div><div class="clear"></div><div id="comment-63949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63955"></span>

<div id="answer-container-63955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63955-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It must be set to monitor mode, so you are getting the raw 802.11 frames that are likely encrypted.</p><p>Under options, there is a check box for monitor mode for each adapter. Uncheck and see what you get. If you are around wifi networks that are unencrytped you will likely see udp and tcp traffic even in this state; otherwise you will need to decrypt. See the wireshark page on decryption to try that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '17, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-63955" class="comments-container"><span id="63965"></span><div id="comment-63965" class="comment"><div id="post-63965-score" class="comment-score"></div><div class="comment-text"><p>Wow ... this site makes sure nubs know who they are ! Looks like I need a measly 15 points to up-vote your answer Bob, and I only have 6 points here ...</p><p>Anyway ... yep ... my interface window needed to be stretched open more in order to see the <strong>MONITOR</strong> checkbox, which toggles the <strong>Wi-Fi: en0</strong> back and forth between <strong>Ethernet</strong> and <strong>802.11 plus radio tap header</strong></p><p><em>(Now, will posting this reply be enough to earn me 7 more points to up-vote your answer? We'll soon see. )</em></p></div><div id="comment-63965-info" class="comment-info"><span class="comment-age">(17 Oct '17, 06:31)</span> richiwalt</div></div><span id="63967"></span><div id="comment-63967" class="comment"><div id="post-63967-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/44453/richiwalt"></a><a href="https://ask.wireshark.org/users/44453/richiwalt">@richiwalt</a>,</p><p>No need to up vote, just "Accept" the answer by clicking the checkmark icon next to it.</p><p>P.S. Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-63967-info" class="comment-info"><span class="comment-age">(17 Oct '17, 06:58)</span> grahamb ♦</div></div></div><div id="comment-tools-63955" class="comment-tools"></div><div class="clear"></div><div id="comment-63955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

