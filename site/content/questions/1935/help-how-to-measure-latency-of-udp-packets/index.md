+++
type = "question"
title = "help: how to measure latency of udp packets"
description = '''Hello all, I have a capture file where i used wireshark to capture the skype voice chat between 3 persons. I need to measure the latency. That is the time a packet takes to travel from source to destination. How to go about seeing this? Thank You Vin'''
date = "2011-01-25T14:59:00Z"
lastmod = "2011-01-26T12:22:00Z"
weight = 1935
keywords = [ "latency", "skype" ]
aliases = [ "/questions/1935" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [help: how to measure latency of udp packets](/questions/1935/help-how-to-measure-latency-of-udp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1935-score" class="post-score" title="current number of votes">0</div><span id="post-1935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I have a capture file where i used wireshark to capture the skype voice chat between 3 persons. I need to measure the latency. That is the time a packet takes to travel from source to destination. How to go about seeing this?</p><p>Thank You Vin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-skype" rel="tag" title="see questions tagged &#39;skype&#39;">skype</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '11, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/375b21761941366ec3c840f0fe106ca0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="magnetpest2k5&#39;s gravatar image" /><p><span>magnetpest2k5</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="magnetpest2k5 has no accepted answers">0%</span></p></div></div><div id="comments-container-1935" class="comments-container"></div><div id="comment-tools-1935" class="comment-tools"></div><div class="clear"></div><div id="comment-1935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1938"></span>

<div id="answer-container-1938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1938-score" class="post-score" title="current number of votes">0</div><span id="post-1938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(After re-reading your question ;-) I think you have to go the Iperf or Jperf UDP test route in a client/server relationship. It's all about how accurately you can sync your timeclocks because UDP is connectionless. In TCP, you could measure the time between the SYN and SYN/ACK. If it was a VOIP call, you could analyze the RTP streams. Visualware has some good info on latency statistics as well as a UDP measurement called MyCapacity. But with UDP, you're kinda stuck. I have a skype trace file and did some graphing with frame.time_delta_displayed. It gives you a good picture of the delays but I don't think it's really accurate as far as a proper speedtest because of the timing issues. If you and your friends are using those nifty Mikrotik RB750s, you can do a UDP test with it's Btest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '11, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/3a22303bd948b6cb232874f271c074fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobertM&#39;s gravatar image" /><p><span>RobertM</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobertM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jan '11, 17:39</strong> </span></p></div></div><div id="comments-container-1938" class="comments-container"><span id="1944"></span><div id="comment-1944" class="comment"><div id="post-1944-score" class="comment-score"></div><div class="comment-text"><p>Thank You for the information. I have one more question is there any way we can see the time stamps of the udp packets?</p></div><div id="comment-1944-info" class="comment-info"><span class="comment-age">(26 Jan '11, 08:05)</span> <span class="comment-user userinfo">magnetpest2k5</span></div></div></div><div id="comment-tools-1938" class="comment-tools"></div><div class="clear"></div><div id="comment-1938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1945"></span>

<div id="answer-container-1945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1945-score" class="post-score" title="current number of votes">0</div><span id="post-1945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm guessing you mean the timestamps of skype and not wiresharks timestamps? I don't have that trace with me right now but this should help: <a href="http://www.docstoc.com/docs/65908880/An-Analysis-of-Skype-Voip-Application-for-Use-in-a-Corporate">"Skype analysis"</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '11, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/3a22303bd948b6cb232874f271c074fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobertM&#39;s gravatar image" /><p><span>RobertM</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobertM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jan '11, 08:52</strong> </span></p></div></div><div id="comments-container-1945" class="comments-container"><span id="1948"></span><div id="comment-1948" class="comment"><div id="post-1948-score" class="comment-score"></div><div class="comment-text"><p>Thank You that was informative. The article shows the departing time for voip packets. Can you tell me how can I get the departing time of packets in my case. Wireshark does show the arrival time of the captured packet but not the departure time.</p></div><div id="comment-1948-info" class="comment-info"><span class="comment-age">(26 Jan '11, 12:22)</span> <span class="comment-user userinfo">magnetpest2k5</span></div></div></div><div id="comment-tools-1945" class="comment-tools"></div><div class="clear"></div><div id="comment-1945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

