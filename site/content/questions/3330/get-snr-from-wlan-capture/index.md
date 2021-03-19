+++
type = "question"
title = "Get SNR from WLAN capture."
description = '''I&#x27;m trying to compare Omnipeek to Wireshark/AirPCap. I downloaded a few 802.11 captures from sample section so I&#x27;m just trying to compare the 2, omnipeek has column for SNR dBm and I am trying to see if wireshark can display the same SNR from the wireless clients.  If anyone is running AirPcap are y...'''
date = "2011-04-04T12:31:00Z"
lastmod = "2012-10-27T13:26:00Z"
weight = 3330
keywords = [ "802.11", "wifi", "snr", "wlan", "rssi" ]
aliases = [ "/questions/3330" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get SNR from WLAN capture.](/questions/3330/get-snr-from-wlan-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3330-score" class="post-score" title="current number of votes">0</div><span id="post-3330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to compare Omnipeek to Wireshark/AirPCap.</p><p>I downloaded a few 802.11 captures from sample section so I'm just trying to compare the 2, omnipeek has column for SNR dBm and I am trying to see if wireshark can display the same SNR from the wireless clients.</p><p>If anyone is running AirPcap are you able to easily the SNR value of your 802.11 clients?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-snr" rel="tag" title="see questions tagged &#39;snr&#39;">snr</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-rssi" rel="tag" title="see questions tagged &#39;rssi&#39;">rssi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '11, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/ed389dc0a4eba98c891ec08938648c7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveO86&#39;s gravatar image" /><p><span>SteveO86</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveO86 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Feb '12, 20:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3330" class="comments-container"></div><div id="comment-tools-3330" class="comment-tools"></div><div class="clear"></div><div id="comment-3330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15315"></span>

<div id="answer-container-15315" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15315-score" class="post-score" title="current number of votes">0</div><span id="post-15315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark currently can display the signal and noise values as columns <em>if</em> they're present in the capture, as they can be with radiotap or PPI captures. AirPcap can supply both radiotap and PPI headers; at least in my test with an original AirPcap adapter, the radiotap headers it supplies have both signal and noise in dBm. The SNR would be the difference between the signal and noise values in dBm (as dB are a logarithmic measure, a "ratio" between two values measured in dB would be the difference between the two values).</p><p>Wireshark doesn't currently calculate an SNR from signal and noise values, so it can't directly display the SNR.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '12, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15315" class="comments-container"></div><div id="comment-tools-15315" class="comment-tools"></div><div class="clear"></div><div id="comment-15315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

