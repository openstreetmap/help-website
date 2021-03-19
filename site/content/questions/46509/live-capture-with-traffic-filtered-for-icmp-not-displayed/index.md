+++
type = "question"
title = "Live capture with traffic filtered for ICMP not displayed"
description = '''I&#x27;m just learning Wireshark. While following a tutorial, I set a filter for ICMP traffic and started my capture. I then pinged Google and Yahoo, yet no packets were displayed. I could see that it was capturing network traffic at the bottom of the app window. I stopped the capture, removed the filter...'''
date = "2015-10-13T13:05:00Z"
lastmod = "2015-10-13T15:37:00Z"
weight = 46509
keywords = [ "icmp", "bug" ]
aliases = [ "/questions/46509" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Live capture with traffic filtered for ICMP not displayed](/questions/46509/live-capture-with-traffic-filtered-for-icmp-not-displayed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46509-score" class="post-score" title="current number of votes">0</div><span id="post-46509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm just learning Wireshark. While following a tutorial, I set a filter for ICMP traffic and started my capture. I then pinged Google and Yahoo, yet no packets were displayed. I could see that it was capturing network traffic at the bottom of the app window. I stopped the capture, removed the filter, and started another capture of all traffic, but nothing was displayed. Again I could see at the bottom of the app that traffic was being captured . I saved the original ICMP capture to disk, then restarted Wireshark. I was then able to capture and display all traffic again. I then loaded the saved ICMP file, Which I was able to view, but it had all protocols displayed, not just ICMP. I applied the ICMP filter to the saved file, and it filtered properly. OK, so I thought this may have been a one-time glitch, so I tried a live capture with the ICMP filter applied again. I got the same results; capturing traffic, but nothing displayed. I then tried a live capture filtered for DNS. YAY, works great! Did I find a bug, or am I doing something wrong? My OS is Windows 10, Build 10565. My Wireshark version is 1.12.7</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '15, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/9c28d7eb4a78be6863055ad4623e9797?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattmc61&#39;s gravatar image" /><p><span>mattmc61</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattmc61 has no accepted answers">0%</span></p></div></div><div id="comments-container-46509" class="comments-container"><span id="46515"></span><div id="comment-46515" class="comment"><div id="post-46515-score" class="comment-score"></div><div class="comment-text"><p>what was your filter expression?</p></div><div id="comment-46515-info" class="comment-info"><span class="comment-age">(13 Oct '15, 13:49)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="46518"></span><div id="comment-46518" class="comment"><div id="post-46518-score" class="comment-score"></div><div class="comment-text"><p>I simply entered: ICMP</p></div><div id="comment-46518-info" class="comment-info"><span class="comment-age">(13 Oct '15, 13:54)</span> <span class="comment-user userinfo">mattmc61</span></div></div></div><div id="comment-tools-46509" class="comment-tools"></div><div class="clear"></div><div id="comment-46509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46528"></span>

<div id="answer-container-46528" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46528-score" class="post-score" title="current number of votes">0</div><span id="post-46528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please run the following commands and report back if you see ICMP traffic.</p><blockquote><p>dumpcap -D -M</p></blockquote><p>pick the interface you want to capture traffic on</p><blockquote><p>tshark -ni 1 -f "icmp"</p></blockquote><p>Please replace '1' with the ID of your interface.</p><p>If you do see ICMP traffic here, it's a problem with the way you are using Wireshark. Then we would need a more detailed description and/or screenshots!</p><p>If you don't see ICMP traffic, you either picked the wrong interface (please double check) or there is a problem on your system, like security software intercepting ICMP traffic (AV, IDS, Endpoint Security, etc.)</p><p>Another possible problem could be some form of offloading in the network driver. Please check that as well (google will tell you how to do that!).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Oct '15, 15:12</strong> </span></p></div></div><div id="comments-container-46528" class="comments-container"><span id="46530"></span><div id="comment-46530" class="comment"><div id="post-46530-score" class="comment-score"></div><div class="comment-text"><p>I am capturing ICMP traffic, as originally stated, just not with a live capture filtered for ICMP....I'll follow your directions and report back in a bit.</p></div><div id="comment-46530-info" class="comment-info"><span class="comment-age">(13 Oct '15, 15:04)</span> <span class="comment-user userinfo">mattmc61</span></div></div><span id="46533"></span><div id="comment-46533" class="comment"><div id="post-46533-score" class="comment-score"></div><div class="comment-text"><p>OK, I solved it. My ISP is using IPv6 extensively. I was capturing ICMPv6 packets, not ICMP(v4)! There is a little bug though.....</p><p>When I set my filter for "ICMP", then start a capture, then ping Google and Yahoo, no ICMP (obviously) packets are displayed (because they are responding with ICMPv6).</p><p>HOWEVER.... After stopping the capture, I save the capture to disk. When I load the file, even without a filter, it will not display ANY packets from the file.</p><p>If I Stop and then restart Wireshark, The file will then display all the protocols captured.</p><p>Thanks for your help, I appreciate your effort!</p></div><div id="comment-46533-info" class="comment-info"><span class="comment-age">(13 Oct '15, 15:36)</span> <span class="comment-user userinfo">mattmc61</span></div></div><span id="46534"></span><div id="comment-46534" class="comment"><div id="post-46534-score" class="comment-score"></div><div class="comment-text"><p>You're welcome!</p></div><div id="comment-46534-info" class="comment-info"><span class="comment-age">(13 Oct '15, 15:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-46528" class="comment-tools"></div><div class="clear"></div><div id="comment-46528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

