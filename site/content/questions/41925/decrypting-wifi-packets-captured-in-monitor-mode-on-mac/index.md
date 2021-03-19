+++
type = "question"
title = "Decrypting WiFi packets captured in monitor mode on Mac"
description = '''Folks, I have been trying my utmost to get decrypted packets on my MacBook Pro. I&#x27;ve trawled the net, found all sorts of suggestions. I&#x27;ve set up monitor mode, set the SSID and the Password. Even messed around with the Terminal level Airport commands and all to no avail. Am I missing something? Part...'''
date = "2015-04-28T09:16:00Z"
lastmod = "2015-04-28T16:44:00Z"
weight = 41925
keywords = [ "osx", "mac", "802.11", "monitor-mode", "decryption" ]
aliases = [ "/questions/41925" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting WiFi packets captured in monitor mode on Mac](/questions/41925/decrypting-wifi-packets-captured-in-monitor-mode-on-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41925-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Folks,</p><p>I have been trying my utmost to get decrypted packets on my MacBook Pro. I've trawled the net, found all sorts of suggestions. I've set up monitor mode, set the SSID and the Password. Even messed around with the Terminal level Airport commands and all to no avail.</p><p>Am I missing something? Part of my frustration is due to the rather "hidden" way some of these features are accessed in WireShark, have I missed something?</p><p>When I go Monitor mode more or less all I see are 802.11 packets, if I come out of monitor mode I see traffic similar to that which I would see using wired ethernet. I'm attempting to get as full a picture of a network as I can. We've been bleeding data out of the WAN port on a router and the network consists of both Wired and WiFi attached devices. Whilst I'm pretty sure I know the reason for the excessive traffic I've found that monitoring wired ethernet is not giving me the full picture. I've like to get a handle on what the iOS devices on the network are doing as well.</p><p>Using Mac OS OS X 10.8.5 (12F2518) on a MacBook pro 2.2 GHz Intel Core i7 running WireShark 1.12.4 and XQuartz 2.7.7</p></div><div id="question-tags" class="tags-container tags">osx mac 802.11 monitor-mode decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '15, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/3644eaaf31be8ed38c9a3d8e1761e7d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithGould&#39;s gravatar image" /><p>KeithGould<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithGould has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Apr '15, 16:40</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-41925" class="comments-container"></div><div id="comment-tools-41925" class="comment-tools"></div><div class="clear"></div><div id="comment-41925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41930"></span>

<div id="answer-container-41930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41930-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>have I missed something?</p></blockquote><p>Have you tried putting all machines (other than the Mac) to sleep (that's what "turning off" a smartphone or tablet will normally do), starting the capture, and then waking the machines up, so that you <a href="https://wiki.wireshark.org/HowToDecrypt802.11">capture the initial EAPOL handshake</a> for all of those machines? For WPA/WPA2 networks, you need more than the password, you need the initial EAPOL handshake as well.</p><p>(Yes, this is a lot of work. That is <em>by design</em> - the whole <em>point</em> of WEP and WPA/WPA2 is to make networks hard to sniff!)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '15, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41930" class="comments-container"><span id="41934"></span><div id="comment-41934" class="comment"><div id="post-41934-score" class="comment-score"></div><div class="comment-text"><p>Many thanks. As part of my testing I have woken my own iPhone and got it to refresh it's eMail accounts, but I missed the fact that other devices would need to be nudged as well.</p><p>I've not detected any decrypted packets from the iPhone using my current technique but I'll see what happens when I switch it off and then turn it back on again. I'll post again once I've had the opportunity to test this.</p></div><div id="comment-41934-info" class="comment-info"><span class="comment-age">(28 Apr '15, 22:15)</span> KeithGould</div></div></div><div id="comment-tools-41930" class="comment-tools"></div><div class="clear"></div><div id="comment-41930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

