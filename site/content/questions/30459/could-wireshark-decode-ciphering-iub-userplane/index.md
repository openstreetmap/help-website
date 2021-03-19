+++
type = "question"
title = "Could wireshark decode ciphering Iub Userplane"
description = '''Hi:- Customer test Ping from UE to server in their WCDMA network. They capture wireshark log in Iub. The question is, can they decode the &quot;ping&quot; in userplane? Please notice ciphering is on in the network. Many thanks bmo'''
date = "2014-03-05T22:10:00Z"
lastmod = "2014-03-07T17:29:00Z"
weight = 30459
keywords = [ "wcdma", "ciphering", "iub", "pdcp" ]
aliases = [ "/questions/30459" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Could wireshark decode ciphering Iub Userplane](/questions/30459/could-wireshark-decode-ciphering-iub-userplane)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30459-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi:-</p><p>Customer test Ping from UE to server in their WCDMA network. They capture wireshark log in Iub. The question is, can they decode the "ping" in userplane? Please notice ciphering is on in the network.</p><p>Many thanks bmo</p></div><div id="question-tags" class="tags-container tags">wcdma ciphering iub pdcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '14, 22:10</strong></p><img src="https://secure.gravatar.com/avatar/c0c2aceaaf1a5eaba645bd3ab7fbfd61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmo&#39;s gravatar image" /><p>bmo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmo has no accepted answers">0%</span></p></div></div><div id="comments-container-30459" class="comments-container"></div><div id="comment-tools-30459" class="comment-tools"></div><div class="clear"></div><div id="comment-30459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30590"></span>

<div id="answer-container-30590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30590-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's a big difference between decoding and deciphering. If you're referring to normal 'decoding' of IuB user-plane frames, I don't believe Wireshark can do it but some specialized analyzers can (eg: Tektronix).</p><p>Usually, it's way easier to capture it at the Iu interface after the RNC has done the decoding for you and put the packet into a simple GTP header.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '14, 17:29</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Mar '14, 17:32</p></div></div><div id="comments-container-30590" class="comments-container"></div><div id="comment-tools-30590" class="comment-tools"></div><div class="clear"></div><div id="comment-30590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

