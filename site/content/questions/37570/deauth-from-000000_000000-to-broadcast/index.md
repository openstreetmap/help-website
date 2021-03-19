+++
type = "question"
title = "deauth from 00:00:00_00:00:00 to broadcast"
description = '''What would be the point of a constant stream like this? IEEE 802.11 Deauthentication, Flags: ........C Type/Subtype: Deauthentication (0x0c) Receiver address: Broadcast (ff:ff:ff:ff:ff:ff) Destination address: Broadcast (ff:ff:ff:ff:ff:ff) Transmitter address: 00:00:00_00:00:00 (00:00:00:00:00:00) S...'''
date = "2014-11-04T12:45:00Z"
lastmod = "2014-11-04T13:28:00Z"
weight = 37570
keywords = [ "broadcast", "deauthentication" ]
aliases = [ "/questions/37570" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [deauth from 00:00:00\_00:00:00 to broadcast](/questions/37570/deauth-from-000000_000000-to-broadcast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What would be the point of a constant stream like this?</p><pre><code>IEEE 802.11 Deauthentication, Flags: ........C
Type/Subtype: Deauthentication (0x0c)
Receiver address: Broadcast (ff:ff:ff:ff:ff:ff)
Destination address: Broadcast (ff:ff:ff:ff:ff:ff)
Transmitter address: 00:00:00_00:00:00 (00:00:00:00:00:00)
Source address: 00:00:00_00:00:00 (00:00:00:00:00:00)
BSS Id: 00:00:00_00:00:00 (00:00:00:00:00:00)
IEEE 802.11 wireless LAN management frame
Reason code: Previous authentication no longer valid (0x0002)</code></pre></div><div id="question-tags" class="tags-container tags">broadcast deauthentication</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '14, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/b7aaacbb68a5826835191c06b36e2804?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redhern&#39;s gravatar image" /><p>redhern<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redhern has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '14, 13:23</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-37570" class="comments-container"></div><div id="comment-tools-37570" class="comment-tools"></div><div class="clear"></div><div id="comment-37570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37572"></span>

<div id="answer-container-37572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37572-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What would be the point of a constant stream like this?</p></blockquote><p>One possible reason, but not necessarily what's happening on your network!</p><p>Maybe someone is trying to crack your wifi keys. In order to capture the session init (required to crack keys) you need to de-authenticate the attached stations.</p><blockquote><p><a href="http://lewiscomputerhowto.blogspot.de/2014/06/how-to-hack-wpawpa2-wi-fi-with-kali.html">http://lewiscomputerhowto.blogspot.de/2014/06/how-to-hack-wpawpa2-wi-fi-with-kali.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '14, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37572" class="comments-container"><span id="38239"></span><div id="comment-38239" class="comment"><div id="post-38239-score" class="comment-score"></div><div class="comment-text"><p>Where can I find this deauthentication packet? (Like under which field?) Thanks.</p></div><div id="comment-38239-info" class="comment-info"><span class="comment-age">(30 Nov '14, 01:30)</span> Prasad Falke</div></div><span id="38264"></span><div id="comment-38264" class="comment"><div id="post-38264-score" class="comment-score"></div><div class="comment-text"><p>well, you posted one in your question !?!</p></div><div id="comment-38264-info" class="comment-info"><span class="comment-age">(01 Dec '14, 16:55)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-37572" class="comment-tools"></div><div class="clear"></div><div id="comment-37572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

