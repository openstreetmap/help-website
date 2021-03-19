+++
type = "question"
title = "ESP decryption"
description = '''Hello everybody! :) I&#x27;m testing IPSec by pinging two machines which I previously had configured. The thing is that when I try to decrypt ESP Payload (by configuring the SAs in Wireshark) it just decrypts packets in one direction; in fact it&#x27;s the one which appears first in the list of SAs. If I swit...'''
date = "2013-08-26T20:13:00Z"
lastmod = "2013-08-28T21:10:00Z"
weight = 24079
keywords = [ "esp" ]
aliases = [ "/questions/24079" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ESP decryption](/questions/24079/esp-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24079-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody! :)</p><p>I'm testing IPSec by pinging two machines which I previously had configured. The thing is that when I try to decrypt ESP Payload (by configuring the SAs in Wireshark) it just decrypts packets in one direction; in fact it's the one which appears first in the list of SAs. If I switch the list order, then Wireshark updates the captures and decrypts the ones in the other direction, but never both.</p><p>More weird is that in the SPI field I had to put a * to both of the SAs because either I put the hex value or the decimal value, none of them work.</p><p>Is this a bug or am I doing something wrong? I just don't get it. :/</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">esp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '13, 20:13</strong></p><img src="https://secure.gravatar.com/avatar/31bf8af9dafc6a4bccf3edb19be4e541?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BeRniTo&#39;s gravatar image" /><p>BeRniTo<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BeRniTo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Aug '13, 05:51</p></div></div><div id="comments-container-24079" class="comments-container"><span id="24089"></span><div id="comment-24089" class="comment"><div id="post-24089-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is this a bug or am I doing something wrong? I just don't get it. :/</p></blockquote><p>what is your Wireshark version and OS?</p></div><div id="comment-24089-info" class="comment-info"><span class="comment-age">(27 Aug '13, 03:14)</span> Kurt Knochner ♦</div></div><span id="24095"></span><div id="comment-24095" class="comment"><div id="post-24095-score" class="comment-score"></div><div class="comment-text"><p>Sorry, forgot to add that info!</p><p>Wireshark 1.10.1 on Windows 7 Home Edition</p></div><div id="comment-24095-info" class="comment-info"><span class="comment-age">(27 Aug '13, 05:50)</span> BeRniTo</div></div><span id="24154"></span><div id="comment-24154" class="comment"><div id="post-24154-score" class="comment-score"></div><div class="comment-text"><p>Anyone????</p></div><div id="comment-24154-info" class="comment-info"><span class="comment-age">(28 Aug '13, 15:05)</span> BeRniTo</div></div></div><div id="comment-tools-24079" class="comment-tools"></div><div class="clear"></div><div id="comment-24079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24157"></span>

<div id="answer-container-24157" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24157-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Got it... had to write the SPIs in hex as 0x00000100 instead of just 0x100 or 256.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '13, 21:10</strong></p><img src="https://secure.gravatar.com/avatar/31bf8af9dafc6a4bccf3edb19be4e541?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BeRniTo&#39;s gravatar image" /><p>BeRniTo<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BeRniTo has no accepted answers">0%</span></p></div></div><div id="comments-container-24157" class="comments-container"></div><div id="comment-tools-24157" class="comment-tools"></div><div class="clear"></div><div id="comment-24157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

