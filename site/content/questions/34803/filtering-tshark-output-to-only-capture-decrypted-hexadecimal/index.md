+++
type = "question"
title = "Filtering TShark output to only capture decrypted hexadecimal"
description = '''I&#x27;m using tshark to decode WPA packets and I was wondering if there was a way I could filter this output: Frame (137 bytes): 0000 00 00 14 00 ee 18 00 00 10 6c 85 09 c0 00 dd 9c .........l..... 0010 59 00 00 41 08 41 24 00 00 18 f8 f5 c2 c6 00 25 Y..A.A.$......% Decrypted CCMP data (73 bytes): 0000 ...'''
date = "2014-07-21T11:06:00Z"
lastmod = "2014-07-21T11:06:00Z"
weight = 34803
keywords = [ "filter", "decryption", "wpa", "tshark", "display-filter" ]
aliases = [ "/questions/34803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering TShark output to only capture decrypted hexadecimal](/questions/34803/filtering-tshark-output-to-only-capture-decrypted-hexadecimal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using tshark to decode WPA packets and I was wondering if there was a way I could filter this output:</p><pre><code>Frame (137 bytes):
0000  00 00 14 00 ee 18 00 00 10 6c 85 09 c0 00 dd 9c   .........l.....
0010  59 00 00 41 08 41 24 00 00 18 f8 f5 c2 c6 00 25   Y..A.A.$......%
Decrypted CCMP data (73 bytes):
0000  aa aa 03 00 00 00 08 00 45 00 00 41 8b 67 00 00  ........E..A.g..
0010  80 11 f1 40 c0 a8 01 0c d4 36 28 19 fc 82 00 35  [email protected](....5</code></pre><p>to just the decrypted Hex:</p><pre><code>aa aa 03 00 00 00 08 00 45 00 00 41 8b 67 00 00
80 11 f1 40 c0 a8 01 0c d4 36 28 19 fc 82 00 35</code></pre></div><div id="question-tags" class="tags-container tags">filter decryption wpa tshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '14, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/d5dceed823c94e5e7f69b722b3cfc7c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jd45093&#39;s gravatar image" /><p>jd45093<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jd45093 has no accepted answers">0%</span></p></div></div><div id="comments-container-34803" class="comments-container"></div><div id="comment-tools-34803" class="comment-tools"></div><div class="clear"></div><div id="comment-34803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

