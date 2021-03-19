+++
type = "question"
title = "Why missing control and management frames?"
description = '''Hello! I am studying the 802.11 control and management traffic, which is created between an AP and a station. I use a monitor interface (built with airmon-ng) and use Wireshark to capture the traffic. Wireshark captures beacon frames, probe responses ACKs, etc from the AP. However, I am not able to ...'''
date = "2014-11-26T05:10:00Z"
lastmod = "2014-11-26T05:10:00Z"
weight = 38164
keywords = [ "control", "frames", "management", "missing" ]
aliases = [ "/questions/38164" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why missing control and management frames?](/questions/38164/why-missing-control-and-management-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38164-score" class="post-score" title="current number of votes">0</div><span id="post-38164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I am studying the 802.11 control and management traffic, which is created between an AP and a station. I use a monitor interface (built with airmon-ng) and use Wireshark to capture the traffic. Wireshark captures beacon frames, probe responses ACKs, etc from the AP. However, I am not able to see two way traffic. I mean, I have CTS messages but not RTS. I have ACKs, but I do not see the acknowledged packet. I use my own machine to capture the traffic. I have read these posts, which indeed solve the problem, when I use a third machine to capture packets.</p><p><a href="https://ask.wireshark.org/questions/6141/how-to-capture-all-control-and-mgmt-packets">https://ask.wireshark.org/questions/6141/how-to-capture-all-control-and-mgmt-packets</a> <a href="https://ask.wireshark.org/questions/8075/missing-packets">https://ask.wireshark.org/questions/8075/missing-packets</a></p><p>However, these posts mention: "Your NIC has to choose either to send data or receive data, so you won't get all the packets due to your card having to send out ACKs while capturing."</p><p>I would like to know why capturing two way traffic is impossible, when you use your own machine? Are not sending and receiving two independent processes?</p><p>For example, when you ping, you can see both the reply and the request. This is also the case with ARP messages. You see the ARP request and reply. Why isn't that the case with control and management frames.</p><p>Any help appreciated</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-control" rel="tag" title="see questions tagged &#39;control&#39;">control</span> <span class="post-tag tag-link-frames" rel="tag" title="see questions tagged &#39;frames&#39;">frames</span> <span class="post-tag tag-link-management" rel="tag" title="see questions tagged &#39;management&#39;">management</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '14, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/d3f5e1c327be84a5f9b27e7ee09b6658?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnson91&#39;s gravatar image" /><p><span>johnson91</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnson91 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Nov '14, 05:11</strong> </span></p></div></div><div id="comments-container-38164" class="comments-container"></div><div id="comment-tools-38164" class="comment-tools"></div><div class="clear"></div><div id="comment-38164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

