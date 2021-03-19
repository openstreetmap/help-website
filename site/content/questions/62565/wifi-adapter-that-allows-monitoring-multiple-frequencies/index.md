+++
type = "question"
title = "wifi adapter that allows monitoring multiple frequencies"
description = '''I&#x27;m looking for a cheap USB adapter for monitor mode that will allow me to monitor multiple frequencies at once. Where can I find something like that? Do I just have to buy 14 cheap ones and use one per channel?'''
date = "2017-07-06T04:33:00Z"
lastmod = "2017-07-06T22:05:00Z"
weight = 62565
keywords = [ "hardware" ]
aliases = [ "/questions/62565" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wifi adapter that allows monitoring multiple frequencies](/questions/62565/wifi-adapter-that-allows-monitoring-multiple-frequencies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62565-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for a cheap USB adapter for monitor mode that will allow me to monitor multiple frequencies at once. Where can I find something like that? Do I just have to buy 14 cheap ones and use one per channel?</p></div><div id="question-tags" class="tags-container tags">hardware</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '17, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/fe16a31076f182a20808a52cc4b76217?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Monkeybusiness&#39;s gravatar image" /><p>Monkeybusiness<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Monkeybusiness has no accepted answers">0%</span></p></div></div><div id="comments-container-62565" class="comments-container"></div><div id="comment-tools-62565" class="comment-tools"></div><div class="clear"></div><div id="comment-62565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62586"></span>

<div id="answer-container-62586" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62586-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><blockquote><p>Do I just have to buy 14 cheap ones and use one per channel?</p></blockquote></blockquote><p>Generally, yes, for simultaneous capture.</p><p>Another option is to trigger some sort of scan behavior so you channel hop through the defined channel sets. This can be effective if you only need to collect limited information, like only see networks that are available, i.e. you are just picking up beacons. However, if you intend to do packet capture and need coherent sets of continuous data, then multiple radios are called for. Some devices may have multiple radios installed - not so much at the adapter level, but most enterprise APs have multiple radios installed - often two or three. Not sure how you could leverage that to reduce devices, but it is still one radio - one channel.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '17, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-62586" class="comments-container"></div><div id="comment-tools-62586" class="comment-tools"></div><div class="clear"></div><div id="comment-62586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62597"></span>

<div id="answer-container-62597" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62597-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In simple terms, as you seem to understand there are 14 channels (for 2.4GHz) WiFi. The very point on those channels as that multiple simultaneous conversations can happen on those channels at the one instant. (Because WiFi actually spans multiple channels, you are limited to maybe a set of 3 simultaneous channels). A WiFi radio can't really tune to all the frequencies at once. (WiFi is of course more complicated in that you phase encoding as well as code hopping to make things worse).</p><p>So as Bob points out you do either need to have multiple receiving radios, or say one radio that scans a channels for say a second, then moves on to the next, etc). It all depends whether you are hoping to see all of traffic or just a sample to get an indication of how the channels are being used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '17, 22:05</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-62597" class="comments-container"></div><div id="comment-tools-62597" class="comment-tools"></div><div class="clear"></div><div id="comment-62597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

