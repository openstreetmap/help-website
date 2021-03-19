+++
type = "question"
title = "Connection loss after start capture"
description = '''Hello, I&#x27;ve just came in contact with wireshark and tried to capture my ping to www.google.com But after starting the capture it seems i dont have any internet connection anymore. The ping say &quot;Host unreachable&quot; and if chromium tells me &quot;DNS_PROBE_FINISHED_NO_INTERNET&quot; Does anyone know a solution fo...'''
date = "2015-07-19T13:21:00Z"
lastmod = "2015-07-19T13:46:00Z"
weight = 44299
keywords = [ "capture", "wireshark", "loss" ]
aliases = [ "/questions/44299" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Connection loss after start capture](/questions/44299/connection-loss-after-start-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44299-score" class="post-score" title="current number of votes">0</div><span id="post-44299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I've just came in contact with wireshark and tried to capture my ping to www.google.com But after starting the capture it seems i dont have any internet connection anymore. The ping say "Host unreachable" and if chromium tells me "DNS_PROBE_FINISHED_NO_INTERNET"</p><p>Does anyone know a solution for this problem?</p><p>With best Regards, Tak3r07</p><p>Btw I'm on Arch linux, Wifi: Broadcom Corporation BCM4352 802.11ac Wireless Network Adapter (rev 03) Using wireshark-gtk</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-loss" rel="tag" title="see questions tagged &#39;loss&#39;">loss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '15, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/5ee444d4e1ce6d795851f6f644a7374d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tak3r07&#39;s gravatar image" /><p><span>Tak3r07</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tak3r07 has no accepted answers">0%</span></p></div></div><div id="comments-container-44299" class="comments-container"></div><div id="comment-tools-44299" class="comment-tools"></div><div class="clear"></div><div id="comment-44299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44300"></span>

<div id="answer-container-44300" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44300-score" class="post-score" title="current number of votes">0</div><span id="post-44300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's just a guess but if you're capturing on the same WiFi adapter that you're using to connect to the internet it may be that the WiFi card becomes "receive only" when you capture on it. WiFi is half duplex, meaning you can either send or receive packets. If you force the card to receive at all times (meaning, capturing everything) you cannot send anymore. Which equals connection loss.</p><p>You should capture on an additional WiFi card, or use a cable adapter (which can do receive and send at the same time)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '15, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44300" class="comments-container"><span id="44301"></span><div id="comment-44301" class="comment"><div id="post-44301-score" class="comment-score"></div><div class="comment-text"><p>I get what you say. I'll try to use usb tethering with my mobile device and use this interface to receive and my wifi interface to send. Thank you Edit: I only receive arp-requests over usb-tethering, Edit2: Solved it by using "all" interface instead of specific wlan "wlp2s0" interface</p></div><div id="comment-44301-info" class="comment-info"><span class="comment-age">(19 Jul '15, 13:46)</span> <span class="comment-user userinfo">Tak3r07</span></div></div></div><div id="comment-tools-44300" class="comment-tools"></div><div class="clear"></div><div id="comment-44300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

