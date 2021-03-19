+++
type = "question"
title = "Display decrypted WLAN traffic that has the Protected bit set"
description = '''I have APs that can capture Radiotap packets before/after encryption/decryption, so they&#x27;re in plaintext. Is it possible to have wireshark de-encapsulate the data packets so I can see what protocols are being used? I&#x27;ve uploaded an example capture to Cloudshark, it&#x27;s an iPad associating and visiting...'''
date = "2014-02-23T19:46:00Z"
lastmod = "2014-02-27T00:15:00Z"
weight = 30115
keywords = [ "wlan" ]
aliases = [ "/questions/30115" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Display decrypted WLAN traffic that has the Protected bit set](/questions/30115/display-decrypted-wlan-traffic-that-has-the-protected-bit-set)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30115-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have APs that can capture Radiotap packets before/after encryption/decryption, so they're in plaintext. Is it possible to have wireshark de-encapsulate the data packets so I can see what protocols are being used?</p><p>I've uploaded an <a href="http://cloudshark.org/captures/01f23a12b3ef">example capture</a> to Cloudshark, it's an iPad associating and visiting <a href="http://bbcnews.com/">http://bbcnews.com/</a>. At packet 198 you can see a DNS request, 199 is the response, then 206 is an HTTP request.</p></div><div id="question-tags" class="tags-container tags">wlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '14, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/7838ca8bcdfdc99e04610c875bf01260?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TRS-80&#39;s gravatar image" /><p>TRS-80<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TRS-80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Feb '14, 00:16</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-30115" class="comments-container"><span id="30139"></span><div id="comment-30139" class="comment"><div id="post-30139-score" class="comment-score"></div><div class="comment-text"><p>what is the capture format of your AP?</p><p>As long as the AP writes a pcap file in a format that Wireshark understands, it should be able to dissect the content of the file, with or without radiotap header.</p><p>Is it possible to post a small sample capture file somewhere (google drive, dropbox, cloudshark.org)?</p></div><div id="comment-30139-info" class="comment-info"><span class="comment-age">(24 Feb '14, 10:22)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30115" class="comment-tools"></div><div class="clear"></div><div id="comment-30115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30225"></span>

<div id="answer-container-30225" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30225-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The issue isn't encapsulation.</p><p>The issue is that the frames have the "this is protected data", i.e. "this is encrypted data", flag set, but the data appears <em>not</em> to be encrypted.</p><p>Therefore, what you want to do is to set the "Ignore the Protection bit" preference for the "IEEE 802.11" protocol to "Yes - without IV"; Wireshark should then assume that those frames are decrypted, and dissect them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '14, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-30225" class="comments-container"><span id="30250"></span><div id="comment-30250" class="comment"><div id="post-30250-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that shows some a bit more detail, but I'm only seeing dissecting as far as LLC, the data isn't being further dissected down to TCP/UDP and higher layer protocols.</p></div><div id="comment-30250-info" class="comment-info"><span class="comment-age">(27 Feb '14, 16:56)</span> TRS-80</div></div><span id="30252"></span><div id="comment-30252" class="comment"><div id="post-30252-score" class="comment-score">1</div><div class="comment-text"><p>Try setting "Ignore the Protection bit" to "Yes - with IV"; that worked for me.</p></div><div id="comment-30252-info" class="comment-info"><span class="comment-age">(27 Feb '14, 17:01)</span> Guy Harris ♦♦</div></div><span id="30253"></span><div id="comment-30253" class="comment"><div id="post-30253-score" class="comment-score"></div><div class="comment-text"><p>Ah-hah, that does the job. Thanks.</p></div><div id="comment-30253-info" class="comment-info"><span class="comment-age">(27 Feb '14, 17:31)</span> TRS-80</div></div></div><div id="comment-tools-30225" class="comment-tools"></div><div class="clear"></div><div id="comment-30225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

