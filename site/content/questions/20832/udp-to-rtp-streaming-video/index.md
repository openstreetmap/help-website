+++
type = "question"
title = "UDP to RTP- streaming video"
description = '''hi, I&#x27;m testing the arbiter of an especial switch by streaming and playing a video on 2 ports.I need a software to measure the delay and quantify it. The application I have used is VLC player. I could do the streaming test by setting only the RTP protocol on VLC. But when I play the video on another...'''
date = "2013-04-28T03:58:00Z"
lastmod = "2013-04-29T08:49:00Z"
weight = 20832
keywords = [ "rtp" ]
aliases = [ "/questions/20832" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UDP to RTP- streaming video](/questions/20832/udp-to-rtp-streaming-video)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20832-score" class="post-score" title="current number of votes">0</div><span id="post-20832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, I'm testing the arbiter of an especial switch by streaming and playing a video on 2 ports.I need a software to measure the delay and quantify it. The application I have used is VLC player. I could do the streaming test by setting only the RTP protocol on VLC. But when I play the video on another PC and capture the packets by Wireshark, I could see UDP packets, and I can't measure the delay! Is it valid to decode UDP to RTP by wireshark? Doesn't it affect on the accuracy of my test?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '13, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/27d0c530990bfd14399cc634d519521d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nice_star2008&#39;s gravatar image" /><p><span>nice_star2008</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nice_star2008 has no accepted answers">0%</span></p></div></div><div id="comments-container-20832" class="comments-container"></div><div id="comment-tools-20832" class="comment-tools"></div><div class="clear"></div><div id="comment-20832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20833"></span>

<div id="answer-container-20833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20833-score" class="post-score" title="current number of votes">0</div><span id="post-20833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm testing the arbiter of an especial switch by streaming and playing a video on 2 ports.I need a software to measure the delay and quantify it.</p></blockquote><p>Do you want to measure the delay produced by the 'special' switch?</p><p>If so, you would have to capture the packets <strong>with a TAP</strong> on the incoming and outgoing port of the switch. You should not use a mirror port on the switch, as that might tamper with the results.</p><p><strong>HOWEVER</strong>, unless that 'special' switch is kind of broken, I don't think you will be able to measure any delay (created by the switch), as the accuracy of the time source of the capturing device might not not be good enough to detect any such delay.</p><blockquote><p>I could see UDP packets, and I can't measure the delay! Is it valid to decode UDP to RTP by wireshark?</p></blockquote><p>Well, it depends what has been transmitted. If those UDP packets are indeed RTP packets, then it's 'save' to decode those UDP packets as RTP (right click and choose "Decode As").</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '13, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '13, 10:52</strong> </span></p></div></div><div id="comments-container-20833" class="comments-container"><span id="20836"></span><div id="comment-20836" class="comment"><div id="post-20836-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much in advance Mr. Kurt. I am testing the Reference switch of NetFPGA. It has a Round-Robin arbiter for servicing the ports. I'm going to stream a video (real-time packets) on one port, play it on another port and measure the delay between this sending and receiving to test the QoS. If the Qos is not acceptable, I should change the arbiter, reprogram NetFPGA and measure the delay again. What do you mean by TAP? How should I determine the kind of packets? Are video packets indeed RTP packets?</p><p>Thanks</p></div><div id="comment-20836-info" class="comment-info"><span class="comment-age">(29 Apr '13, 02:41)</span> <span class="comment-user userinfo">nice_star2008</span></div></div><span id="20840"></span><div id="comment-20840" class="comment"><div id="post-20840-score" class="comment-score"></div><div class="comment-text"><blockquote><p>What do you mean by TAP?</p></blockquote><p>see here: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_network_tap">http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_network_tap</a></p><p>I would recommend to use two TAPs for your requirements. But if you don't have a TAP at hand, you can start with two mirror/monitor ports on the switch.</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch">http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch</a></p></blockquote><p><strong>However:</strong> you can't fully trust that setup, unless you know very well how the switch handles those mirrored packets and how much delay is added by the port mirroring!</p><blockquote><p>Are video packets indeed RTP packets?</p></blockquote><p>That depends on the streaming method.</p><blockquote><p>How should I determine the kind of packets?</p></blockquote><p>Hard to tell without a sample. Can you please post a <strong>small</strong> sample file somewhere (google docs, dropbox, cloudshark.org. BEWARE privacy issues!!)</p></div><div id="comment-20840-info" class="comment-info"><span class="comment-age">(29 Apr '13, 08:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20833" class="comment-tools"></div><div class="clear"></div><div id="comment-20833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

