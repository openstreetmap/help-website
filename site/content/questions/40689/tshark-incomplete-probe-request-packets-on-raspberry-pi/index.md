+++
type = "question"
title = "tshark: incomplete probe request packets on raspberry pi"
description = '''Hi all, I&#x27;m running the following tshark scan to get MAC/SSID/signal dbm from probe requests: sudo tshark -I -i wlan0 -T fields -e wlan.sa_resolved -e wlan_mgt.ssid -e radiotap.dbm_antsignal type mgt subtype probe-req  On a Raspberry Pi. The results are nearly always partial packets, generally just ...'''
date = "2015-03-19T08:13:00Z"
lastmod = "2015-03-22T02:33:00Z"
weight = 40689
keywords = [ "raspberry", "tshark", "bash", "wifi" ]
aliases = [ "/questions/40689" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: incomplete probe request packets on raspberry pi](/questions/40689/tshark-incomplete-probe-request-packets-on-raspberry-pi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40689-score" class="post-score" title="current number of votes">0</div><span id="post-40689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm running the following tshark scan to get MAC/SSID/signal dbm from probe requests:</p><pre><code>sudo tshark -I -i wlan0 -T fields -e wlan.sa_resolved -e wlan_mgt.ssid -e radiotap.dbm_antsignal type mgt subtype probe-req</code></pre><p>On a Raspberry Pi. The results are nearly always partial packets, generally just the signal dbm and occasionally an SSID, but pretty much never a MAC address. When I run the same scan on my Macbook Pro in the same room, it generates all three fields for every result. I assumed this was a weaker wifi adaptor on the Pi, so I bought a Linksys AE3000 adaptor (and a couple of others to test), and got the same results. Have tried running the adaptor from a powered USB hub, same result. The Pi is running from a power supply, not battery. Anyone experienced the same thing, or have thoughts on why this is?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-raspberry" rel="tag" title="see questions tagged &#39;raspberry&#39;">raspberry</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-bash" rel="tag" title="see questions tagged &#39;bash&#39;">bash</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '15, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/6ad9c485468672305ea947f0acdebd32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="youcloudsofddom&#39;s gravatar image" /><p><span>youcloudsofddom</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="youcloudsofddom has no accepted answers">0%</span></p></div></div><div id="comments-container-40689" class="comments-container"></div><div id="comment-tools-40689" class="comment-tools"></div><div class="clear"></div><div id="comment-40689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40763"></span>

<div id="answer-container-40763" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40763-score" class="post-score" title="current number of votes">0</div><span id="post-40763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Solved: discovered that the current build of tshark that Debian runs does not support wlan.sa_resolved, hence the 'lack' of data in the packets!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '15, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/6ad9c485468672305ea947f0acdebd32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="youcloudsofddom&#39;s gravatar image" /><p><span>youcloudsofddom</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="youcloudsofddom has no accepted answers">0%</span></p></div></div><div id="comments-container-40763" class="comments-container"></div><div id="comment-tools-40763" class="comment-tools"></div><div class="clear"></div><div id="comment-40763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

