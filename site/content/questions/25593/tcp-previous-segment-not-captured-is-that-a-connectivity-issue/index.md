+++
type = "question"
title = "TCP:  Previous segment not captured, Is that a connectivity issue?"
description = '''Hi guys, I&#x27;ve been analyzing the packets sent between one server (172.20.3.188) and some clients, after I put the capture on Wireshark and I saw that there is some messages that say &quot;Protocol TCP. Previous segment not captured&quot; and &quot;TCP: ACKed segment that wasn&#x27;t captured (common at capture start)&quot;....'''
date = "2013-10-03T08:21:00Z"
lastmod = "2013-10-04T11:32:00Z"
weight = 25593
keywords = [ "prev_seg_lost", "tcp", "wireshark" ]
aliases = [ "/questions/25593" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP: Previous segment not captured, Is that a connectivity issue?](/questions/25593/tcp-previous-segment-not-captured-is-that-a-connectivity-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25593-score" class="post-score" title="current number of votes">0</div><span id="post-25593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, I've been analyzing the packets sent between one server (172.20.3.188) and some clients, after I put the capture on Wireshark and I saw that there is some messages that say "Protocol TCP. Previous segment not captured" and "TCP: ACKed segment that wasn't captured (common at capture start)". Looking on the internet I found that is a connectivity issue, but I'm not so able to understand it at all. I was wondering if you can give me some ideas/advices about what could be happening. I uploaded the capture, here is the link, <a href="http://www.cloudshark.org/captures/416284356bd1.">http://www.cloudshark.org/captures/416284356bd1.</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-prev_seg_lost" rel="tag" title="see questions tagged &#39;prev_seg_lost&#39;">prev_seg_lost</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '13, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/5f0a6fabfe916dc503e5ca0871e02333?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EduardoHzz&#39;s gravatar image" /><p><span>EduardoHzz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EduardoHzz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Oct '13, 23:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-25593" class="comments-container"><span id="25596"></span><div id="comment-25596" class="comment"><div id="post-25596-score" class="comment-score">1</div><div class="comment-text"><p>Clicking on the link gives a "404 Not Found"</p></div><div id="comment-25596-info" class="comment-info"><span class="comment-age">(03 Oct '13, 08:50)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="25599"></span><div id="comment-25599" class="comment"><div id="post-25599-score" class="comment-score"></div><div class="comment-text"><p>Do I have to download any software to share this?, Let see if this does work <a href="http://www.cloudshark.org/captures/3ce0dafb3430">http://www.cloudshark.org/captures/3ce0dafb3430</a></p><p>Ans: 1. No 2. This link works ....</p></div><div id="comment-25599-info" class="comment-info"><span class="comment-age">(03 Oct '13, 09:07)</span> <span class="comment-user userinfo">EduardoHzz</span></div></div></div><div id="comment-tools-25593" class="comment-tools"></div><div class="clear"></div><div id="comment-25593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25598"></span>

<div id="answer-container-25598" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25598-score" class="post-score" title="current number of votes">1</div><span id="post-25598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The messages just mean exactly what they say: one or more tcp segments were not captured.</p><p>This will happen if (a) a capture is started in the middle of a TCP "conversation" (obviously) or (b) one or more frames are dropped (not captured) during a capture.</p><p>(a) is normal (b) might happen for a number of reasons (e.g., machine which is running Wireshark is slow).</p><p>In any case, the messages don't normally indicate an issue .... Looking at the capture might or might not provide more information.</p><hr /><p>Looking at the capture:</p><p>It seems to me that you are having a problem with the actual capture: That is; there are significant gaps of 1 or more seconds in the capture (e.g. between frames 6967 and 6968).</p><p>This has to be a problem with the capture itself because the traffic on the various connections continues on; IOW the sending/receiving nodes think everything is OK; They are seeing the frames even if they are missing from the capture file.</p><p>Looking at the I/O graph (Statistics IO Graph) shows a number of obvious gaps.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture.jpeg" alt="i/o graph" /></p><p>So: answering your original question: This is a "capture" issue (which causes the "previous segment lost" &amp; etc expert messages.</p><p>Is there a specific problem you are trying to analyze ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Oct '13, 11:03</strong> </span></p></div></div><div id="comments-container-25598" class="comments-container"><span id="25603"></span><div id="comment-25603" class="comment"><div id="post-25603-score" class="comment-score"></div><div class="comment-text"><p>Hi, yes I'm trying to identify why the server is not receveing some responses from (in this case) a network element. I work with a UNIX server connecting to it by telnet using a virtual machine. I made the capture using command snoop between the server(UNIX) and the network element. I saved the result of the command in a file, and after that I imported this file to Wireshark. In the network element configuration is defined 15 seconds to send the request to time out. I want to identify why the network element is taking more than 15 seconds to respond. So, I think it cuold be a conectivity issue or something related to the network.</p></div><div id="comment-25603-info" class="comment-info"><span class="comment-age">(03 Oct '13, 09:39)</span> <span class="comment-user userinfo">EduardoHzz</span></div></div><span id="25651"></span><div id="comment-25651" class="comment"><div id="post-25651-score" class="comment-score"></div><div class="comment-text"><p>A multiple loss of packets Can generate loss of connection? By the way thank you for your comments and time.</p></div><div id="comment-25651-info" class="comment-info"><span class="comment-age">(04 Oct '13, 09:20)</span> <span class="comment-user userinfo">EduardoHzz</span></div></div><span id="25654"></span><div id="comment-25654" class="comment"><div id="post-25654-score" class="comment-score"></div><div class="comment-text"><p>It seems as though you are trying to somehow relate "loss of connection" (whereever you are getting that from) to the "missing captured packets" in the capture.</p><p>I don't think that's possible.</p><p>IOW: All I am noting is that the capture file has gaps and that (in the cases I looked at) the "conversations" (connections) were not impacted.</p><p>Given that the conversations don't seem to be impacted, to my mind pretty much the <em>only</em> thing that can be inferred from the "capture gaps" is that there's a capture problem.</p><p>You should fix <em>that</em> problem before you try to do any real analysis.</p></div><div id="comment-25654-info" class="comment-info"><span class="comment-age">(04 Oct '13, 11:32)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-25598" class="comment-tools"></div><div class="clear"></div><div id="comment-25598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

