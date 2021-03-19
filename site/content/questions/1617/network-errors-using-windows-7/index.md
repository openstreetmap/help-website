+++
type = "question"
title = "Network errors using Windows 7"
description = '''I have two identical Asus motherboards: One running Windows XP, the other running Windows 7. When I run Wireshark on the WinXP machine I get approx&#x27; 1 error in 10,000 packets. When I run Wireshark on the Win7 machine I get over 3,500 errors in 10,000 packets. I&#x27;ve tried swapping the hard drives from...'''
date = "2011-01-04T07:35:00Z"
lastmod = "2011-01-04T08:42:00Z"
weight = 1617
keywords = [ "windows7", "errors" ]
aliases = [ "/questions/1617" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Network errors using Windows 7](/questions/1617/network-errors-using-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1617-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two identical Asus motherboards: One running Windows XP, the other running Windows 7. When I run Wireshark on the WinXP machine I get approx' 1 error in 10,000 packets.</p><p>When I run Wireshark on the Win7 machine I get over 3,500 errors in 10,000 packets.</p><p>I've tried swapping the hard drives from one machine to the other but problem moves with the O/S. It seem to be the Win7 PC that creates a huge number of errors while the WinXP machine creates very few.</p><p>Any clues to this would be useful</p></div><div id="question-tags" class="tags-container tags">windows7 errors</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '11, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/fafcec6a6a08e593ca689920466c3c95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RogerNeale&#39;s gravatar image" /><p>RogerNeale<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RogerNeale has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Feb '12, 18:51</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-1617" class="comments-container"><span id="1618"></span><div id="comment-1618" class="comment"><div id="post-1618-score" class="comment-score"></div><div class="comment-text"><p>Did you check your duplex setting on the Win7 box? To make sure that it matches whatever is set on your switch?</p></div><div id="comment-1618-info" class="comment-info"><span class="comment-age">(04 Jan '11, 08:22)</span> hansangb</div></div></div><div id="comment-tools-1617" class="comment-tools"></div><div class="clear"></div><div id="comment-1617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1619"></span>

<div id="answer-container-1619" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1619-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What kind of errors are you talking about? Checksum errors? It could be that the Win7 network driver does TCP checksum offloading while the XP driver doesn't.</p><p>Have a look at: <a href="http://wiki.wireshark.org/CaptureSetup/Offloading">http://wiki.wireshark.org/CaptureSetup/Offloading</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '11, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1619" class="comments-container"><span id="1621"></span><div id="comment-1621" class="comment"><div id="post-1621-score" class="comment-score"></div><div class="comment-text"><p>Oy! I should have thought of that. That's probably it!</p></div><div id="comment-1621-info" class="comment-info"><span class="comment-age">(04 Jan '11, 10:52)</span> hansangb</div></div></div><div id="comment-tools-1619" class="comment-tools"></div><div class="clear"></div><div id="comment-1619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

