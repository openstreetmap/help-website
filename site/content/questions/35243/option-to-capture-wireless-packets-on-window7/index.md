+++
type = "question"
title = "Option to capture wireless packets on window7"
description = '''Is there any way to capture wireless packets on windows 7 using wireshark? I don&#x27;t see any option to select the wireless interface on win7. Any specific versions, i need to use?'''
date = "2014-08-05T23:41:00Z"
lastmod = "2014-08-06T01:33:00Z"
weight = 35243
keywords = [ "win7" ]
aliases = [ "/questions/35243" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Option to capture wireless packets on window7](/questions/35243/option-to-capture-wireless-packets-on-window7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35243-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to capture wireless packets on windows 7 using wireshark? I don't see any option to select the wireless interface on win7. Any specific versions, i need to use?</p></div><div id="question-tags" class="tags-container tags">win7</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '14, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/f31ad5d200a7017bb52dfed216b8f888?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ram&#39;s gravatar image" /><p>ram<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ram has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Aug '14, 23:43</p></div></div><div id="comments-container-35243" class="comments-container"></div><div id="comment-tools-35243" class="comment-tools"></div><div class="clear"></div><div id="comment-35243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35252"></span>

<div id="answer-container-35252" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35252-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can capture on my internal WiFi card using Wireshark on Windows 7 without a problem. The only thing that's missing in the capture is the radio layer (beacon frames, association requests etc.) - the only way to get those on Windows is to buy an <a href="http://www.riverbed.com/products/performance-management-control/network-performance-management/wireless-packet-capture.html">AirPCAP adapter from Riverbed</a>. The reason is that it is not possible to enable monitor mode for normal WiFi cards on Windows.</p><p>If you don't see the wireless interface at all you might have a card that isn't recognized by WinPCAP, which happened to me for some USB WiFi cards.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '14, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35252" class="comments-container"><span id="35254"></span><div id="comment-35254" class="comment"><div id="post-35254-score" class="comment-score"></div><div class="comment-text"><p>Which wireshark version you are using??</p></div><div id="comment-35254-info" class="comment-info"><span class="comment-age">(06 Aug '14, 02:22)</span> ram</div></div><span id="35255"></span><div id="comment-35255" class="comment"><div id="post-35255-score" class="comment-score"></div><div class="comment-text"><p>1.10, 1.12, 1.99, my internal Intel card works with all of them, Win7 x64 or x32. No radio layer, though, as I explained.</p></div><div id="comment-35255-info" class="comment-info"><span class="comment-age">(06 Aug '14, 02:24)</span> Jasper ♦♦</div></div><span id="35257"></span><div id="comment-35257" class="comment"><div id="post-35257-score" class="comment-score"></div><div class="comment-text"><p>@ram: Do you see the ethernet interface, or no interfaces at all?</p></div><div id="comment-35257-info" class="comment-info"><span class="comment-age">(06 Aug '14, 02:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-35252" class="comment-tools"></div><div class="clear"></div><div id="comment-35252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

