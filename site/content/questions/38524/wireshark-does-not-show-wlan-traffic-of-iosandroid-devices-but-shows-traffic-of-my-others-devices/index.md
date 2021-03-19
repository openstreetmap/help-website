+++
type = "question"
title = "Wireshark does not show wlan traffic of iOs/Android devices (but shows traffic of my others devices)"
description = '''Hello, i am trying to capture the Wifi traffic of my home network with Wireshark. For that, i run a Backtrack Live CD on a laptop with a DLINK AirPlus DWL g650 wifi adapter. I set my WPA key in wireshark, and running wlan interface in monitor mode enabled. I can capture the traffic of my 3 others la...'''
date = "2014-12-11T02:16:00Z"
lastmod = "2014-12-12T05:16:00Z"
weight = 38524
keywords = [ "wireless", "ios", "android", "wlan", "iphone" ]
aliases = [ "/questions/38524" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark does not show wlan traffic of iOs/Android devices (but shows traffic of my others devices)](/questions/38524/wireshark-does-not-show-wlan-traffic-of-iosandroid-devices-but-shows-traffic-of-my-others-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38524-score" class="post-score" title="current number of votes">0</div><span id="post-38524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i am trying to capture the Wifi traffic of my home network with Wireshark.</p><p>For that, i run a Backtrack Live CD on a laptop with a DLINK AirPlus DWL g650 wifi adapter. I set my WPA key in wireshark, and running wlan interface in monitor mode enabled.</p><p>I can capture the traffic of my 3 others laptop computers connected with wifi to the AP (two Windows XP and one Vista) with no problem. (Of course, i just had to deauth then reauth the computers in order to capture the EAPOL keys with wireshark)</p><p>When i browse something on the laptops, i see the traffic clear (HTTP headers etc..) and see the local IP addresses (192.168.1.x) in wireshark.</p><p><strong>But,</strong> when i connect my 2 phones to the AP. (iphone and huawei android) i can see the EAPOL keys coming in wireshark, but when i browse something on the phone , nothing clear showing in wireshark, not even the 192.168.1.x addresses IP. (i am not connected to the 3G but really to my local network, tried airplane mode with wifi too) and instead of clear traffic i got a bunch of: "IEEE 802 Null function (no data)" entries in wireshark.</p><p>Why wireshark can decrypt my PCs traffic but it will not decrypt traffic of android or ios device??</p><p>I tried forcing deauth several times with aireplay etc.. and manual deauth/auth got EAPOL, but it's like the traffic isn't decrypted correctly?</p><p>i tried with another phone, a Nokia n97 which is not android, and it works good i can see everything...</p><p>just not working with android and ios?</p><p>Some one does have an explaination?? :)</p><p>Thanks you to all</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-iphone" rel="tag" title="see questions tagged &#39;iphone&#39;">iphone</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '14, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/9eb17b2a837c9e5dbcc1f57cc88ddc0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tobby84&#39;s gravatar image" /><p><span>Tobby84</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tobby84 has no accepted answers">0%</span></p></div></div><div id="comments-container-38524" class="comments-container"></div><div id="comment-tools-38524" class="comment-tools"></div><div class="clear"></div><div id="comment-38524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38540"></span>

<div id="answer-container-38540" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38540-score" class="post-score" title="current number of votes">0</div><span id="post-38540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>i found the issue,</p><p>it's my router, that is 802.11 B/G/N</p><p>and my adapter (dlink dwl g650) is only B/G,</p><p>so it work as soon as the adapters of the device i want to capture are B/G too.</p><p>Unfortunately my iPhone and Android phone are B/G/N, so it's N by default and by the way i can't capture them with my dlink adapter. I had to force the B/G mode in the router settings and i can capture the ios/android with no problem.</p><p>Thanks all</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '14, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/9eb17b2a837c9e5dbcc1f57cc88ddc0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tobby84&#39;s gravatar image" /><p><span>Tobby84</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tobby84 has no accepted answers">0%</span></p></div></div><div id="comments-container-38540" class="comments-container"></div><div id="comment-tools-38540" class="comment-tools"></div><div class="clear"></div><div id="comment-38540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

