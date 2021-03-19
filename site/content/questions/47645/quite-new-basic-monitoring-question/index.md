+++
type = "question"
title = "Quite new-- basic monitoring question"
description = '''Hello, everyone! I recently got a Raspberry Pi and I&#x27;m trying to use it to count the traffic outside my house based on wifi pings from smart phones. Seems pretty basic... I set my interface to monitor mode and used tshark to capture to a file for 5 minutes.  But while looking at the captured packets...'''
date = "2015-11-16T12:55:00Z"
lastmod = "2015-12-07T08:59:00Z"
weight = 47645
keywords = [ "smartphone", "iphone", "montior" ]
aliases = [ "/questions/47645" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Quite new-- basic monitoring question](/questions/47645/quite-new-basic-monitoring-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47645-score" class="post-score" title="current number of votes">0</div><span id="post-47645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, everyone!</p><p>I recently got a Raspberry Pi and I'm trying to use it to count the traffic outside my house based on wifi pings from smart phones. Seems pretty basic... I set my interface to monitor mode and used tshark to capture to a file for 5 minutes.</p><p>But while looking at the captured packets I can't seem to find any that match my iPhone's MAC address (Found in Settings &gt; General &gt; About &gt; Wifi Address). I figured as a test I would at least be able to pick up my phone but it doesn't seem to be capturing it. Any suggestions on what I may be doing wrong?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smartphone" rel="tag" title="see questions tagged &#39;smartphone&#39;">smartphone</span> <span class="post-tag tag-link-iphone" rel="tag" title="see questions tagged &#39;iphone&#39;">iphone</span> <span class="post-tag tag-link-montior" rel="tag" title="see questions tagged &#39;montior&#39;">montior</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '15, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/28c5564a74d4c4cff2a8ad144015b143?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wonderlemming&#39;s gravatar image" /><p><span>wonderlemming</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wonderlemming has no accepted answers">0%</span></p></div></div><div id="comments-container-47645" class="comments-container"></div><div id="comment-tools-47645" class="comment-tools"></div><div class="clear"></div><div id="comment-47645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48273"></span>

<div id="answer-container-48273" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48273-score" class="post-score" title="current number of votes">1</div><span id="post-48273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Update: I discovered by taking my computer &amp; phone into the sublevels of a parking garage so that the only signals I would be picking up would be from my phone. Tuuuurns out, iPhones mask their MAC addresses while sending out probe requests. With a little research I found out that iPhones do this to try and protect your identity a little better.</p><p>So, I was picking up my phone but not with the MAC address it listed in the settings!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '15, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/28c5564a74d4c4cff2a8ad144015b143?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wonderlemming&#39;s gravatar image" /><p><span>wonderlemming</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wonderlemming has no accepted answers">0%</span></p></div></div><div id="comments-container-48273" class="comments-container"><span id="48330"></span><div id="comment-48330" class="comment"><div id="post-48330-score" class="comment-score"></div><div class="comment-text"><p>This security feature is documented at Apple Support for iOS 8 release. Refer to the link below:</p><p><a href="https://support.apple.com/en-us/HT201395">https://support.apple.com/en-us/HT201395</a></p><p>Refer to the WiFi section of the release, restated here for convenience: "WiFi:</p><p>Available for: iPhone 4s and later, iPod touch (5th generation) and later, iPad 2 and later</p><p>Impact: A device may be passively tracked by its WiFi MAC address Description: An information disclosure existed because a stable MAC address was being used to scan for WiFi networks. This issue was addressed by randomizing the MAC address for passive WiFi scans."</p><p>As stated by <span>@wonderlemming</span>, this means that Probe Requests from iOS devices will have a randomized MAC address. With that being said, I have done some WiFi sniffing and found real MAC addresses from Apple devices running iOS 8 or later.</p></div><div id="comment-48330-info" class="comment-info"><span class="comment-age">(07 Dec '15, 08:59)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-48273" class="comment-tools"></div><div class="clear"></div><div id="comment-48273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47659"></span>

<div id="answer-container-47659" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47659-score" class="post-score" title="current number of votes">0</div><span id="post-47659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Checkout the info collected on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">WLAN capture</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '15, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-47659" class="comments-container"></div><div id="comment-tools-47659" class="comment-tools"></div><div class="clear"></div><div id="comment-47659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

