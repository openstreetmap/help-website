+++
type = "question"
title = "How to retrieve packets content"
description = '''Hello everyone, I don&#x27;t know what&#x27;s wrong with this portal, I am posting this question 3rd time coz first 2 times it showed post published but it didn&#x27;t. My question is, I have an hour long captured packets from 10 different devices connected to my router. I want to retrieve Audio, Video and image c...'''
date = "2016-08-28T15:49:00Z"
lastmod = "2016-08-29T19:33:00Z"
weight = 55151
keywords = [ "export", "audio", "video", "objects", "packet" ]
aliases = [ "/questions/55151" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to retrieve packets content](/questions/55151/how-to-retrieve-packets-content)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55151-score" class="post-score" title="current number of votes">0</div><span id="post-55151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I don't know what's wrong with this portal, I am posting this question 3rd time coz first 2 times it showed post published but it didn't.</p><p>My question is, I have an hour long captured packets from 10 different devices connected to my router. I want to retrieve Audio, Video and image content with URL of the destination and any relative data from those packets. This is something concerning my kids. I would really appreciate any earliest help.</p><p>Thank you very much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-audio" rel="tag" title="see questions tagged &#39;audio&#39;">audio</span> <span class="post-tag tag-link-video" rel="tag" title="see questions tagged &#39;video&#39;">video</span> <span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '16, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/4807013a3e3abe21d072c88f195c31f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy1970&#39;s gravatar image" /><p><span>andy1970</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy1970 has no accepted answers">0%</span></p></div></div><div id="comments-container-55151" class="comments-container"></div><div id="comment-tools-55151" class="comment-tools"></div><div class="clear"></div><div id="comment-55151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55170"></span>

<div id="answer-container-55170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55170-score" class="post-score" title="current number of votes">0</div><span id="post-55170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1st determine if the traffic you want to see is encrypted or in the clear. You can filter on a TCP stream by right clicking/Follow/TCP Stream, or you can craft a filter to specify all TCP/UDP conversations between the source/destinations IP addresses. By filtering the traffic down to specific user IPs, you can determine what outbound IPs are being visited and then you can do some quick reverse lookups against those IPs (either in a browser or using the CMD/Terminal tool NSlookup, example command follows - $ nslookup "ip addr"). This will give you an idea of what type of network activity is occurring.</p><p>If the traffic is not encrypted, you can go to File/Export Objects/HTTP (or whatever protocol you are interested in) and save it to a folder. Then go digging...For this export process, "Allow Subdissector to Reassemble TCP Streams" needs to be ON and can be found under Edit/Preferences/Protocols Section/TCP.</p><p>If the traffic is encrypted, good luck! You will need keys to decrypt...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '16, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p><span>BruteForce</span><br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span></p></div></div><div id="comments-container-55170" class="comments-container"><span id="55183"></span><div id="comment-55183" class="comment"><div id="post-55183-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, I will try my best to follow these steps. I will follow up on this question in case stuck anywhere. I really appreciate your response.</p></div><div id="comment-55183-info" class="comment-info"><span class="comment-age">(29 Aug '16, 17:09)</span> <span class="comment-user userinfo">andy1970</span></div></div><span id="55184"></span><div id="comment-55184" class="comment"><div id="post-55184-score" class="comment-score"></div><div class="comment-text"><p>After trying for hours, I justrealised, my wireshark is not capturing much from other device. It is capturing only from my Laptop. The other devices have some packets other than TCP, UDP. They have broadcasting, SSDP etc packets only. I checked everything, I am connected to same wifi as of the other devices, wireshark is also connected to the same with promiscuous mode. What's going on? What wrong I am doin here? First I see capture filter is also not working. Only display filter works. Does Wireshark have any issues with Win10?</p></div><div id="comment-55184-info" class="comment-info"><span class="comment-age">(29 Aug '16, 19:11)</span> <span class="comment-user userinfo">andy1970</span></div></div><span id="55185"></span><div id="comment-55185" class="comment"><div id="post-55185-score" class="comment-score"></div><div class="comment-text"><p>There is a lot of info on WiFi captures within the forum. Today there was a good discussion at the following link - <a href="https://ask.wireshark.org/questions/55122/capturing-with-airpcap-and-seeing-only-80211-protocol-not-tcp-or-http-or/55142">https://ask.wireshark.org/questions/55122/capturing-with-airpcap-and-seeing-only-80211-protocol-not-tcp-or-http-or/55142</a></p><p>Also, try the Wiki link - <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></p><p>Additionally, try searching for Wifi, 802.11, or promiscuous mode. That should cover most of the questions you would have for WiFi captures.</p></div><div id="comment-55185-info" class="comment-info"><span class="comment-age">(29 Aug '16, 19:33)</span> <span class="comment-user userinfo">BruteForce</span></div></div></div><div id="comment-tools-55170" class="comment-tools"></div><div class="clear"></div><div id="comment-55170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

