+++
type = "question"
title = "confused about RTO value displayed by wireshark"
description = '''Hello, at work we are analyzing captures due to a production enviroment problem. We are looking at a packet loss burst (3 consecutive lost packets) and their retransmission time. I added the tcp.analysis.rto value as column but i noted that for all retransmitted packets their rto value is not referr...'''
date = "2015-10-18T12:32:00Z"
lastmod = "2015-11-19T02:26:00Z"
weight = 46675
keywords = [ "rto", "retransmission", "tcp" ]
aliases = [ "/questions/46675" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [confused about RTO value displayed by wireshark](/questions/46675/confused-about-rto-value-displayed-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46675-score" class="post-score" title="current number of votes">0</div><span id="post-46675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, at work we are analyzing captures due to a production enviroment problem. We are looking at a packet loss burst (3 consecutive lost packets) and their retransmission time. I added the tcp.analysis.rto value as column but i noted that for all retransmitted packets their rto value is not referred to the "original" packet time. also looking at the packet details, wireshark tells the frame number used to calculate the delta time, but it's a successive frame! Am i misunderstanding something about the RTO? shouldn't rto timer start when the packet is sent?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rto" rel="tag" title="see questions tagged &#39;rto&#39;">rto</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '15, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/965308e51ed9202c5a526c0e93078099?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryu80&#39;s gravatar image" /><p><span>ryu80</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryu80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Oct '15, 07:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-46675" class="comments-container"><span id="46904"></span><div id="comment-46904" class="comment"><div id="post-46904-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>here the capture <a href="https://www.cloudshark.org/captures/ca907de31560">https://www.cloudshark.org/captures/ca907de31560</a></p><p>due to security reasons i had to remove the payload and i had to change the addresses .</p><p>looking at the trace the frames the server with 10.1.1.2 address sent 3 packets that are lost :</p><p>frame 90 is retransmitted with frame 112 (but rto is based on delta from frame 104)</p><p>frame 91 is retransmitted with frame 120 (but rto is based on delta from frame 104)</p><p>frame 92 is retransmitted with frame 128 (but rto is based on delta from frame 124)</p><p>can you help me to understand why sometimes rto isn't based on delta from the original frame? thank you very much</p></div><div id="comment-46904-info" class="comment-info"><span class="comment-age">(24 Oct '15, 10:20)</span> <span class="comment-user userinfo">ryu80</span></div></div></div><div id="comment-tools-46675" class="comment-tools"></div><div class="clear"></div><div id="comment-46675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46695"></span>

<div id="answer-container-46695" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46695-score" class="post-score" title="current number of votes">0</div><span id="post-46695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The RTO timer starts when the packet is sent but it sounds like the TCP dissector is showing you the time between retransmissions--in other words the value of the connection's RTO timer when the packet was last sent (i.e., it's showing you what the RTO value was, not the total time since the original transmission--which isn't something the TCP stack tracks).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-46695" class="comments-container"><span id="46721"></span><div id="comment-46721" class="comment"><div id="post-46721-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer, for example here a capture where the retrasmitted packet is the number 128 <img src="http://s2.postimg.org/x1fjhh8e1/rto_example3.jpg" alt="alt text" /></p><p>but wireshark calculate rto from frame 124 ... Anyway i still don't understand why wireshark shouldn't calculate it from the packet with the same seq number <img src="http://s10.postimg.org/amrcuhs95/rto_example1.jpg" alt="alt text" /> in this case the rto should be around 1.6 seconds, am i right?</p></div><div id="comment-46721-info" class="comment-info"><span class="comment-age">(19 Oct '15, 14:21)</span> <span class="comment-user userinfo">ryu80</span></div></div><span id="46723"></span><div id="comment-46723" class="comment"><div id="post-46723-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us an example trace. I think it would be easier to follow you.</p></div><div id="comment-46723-info" class="comment-info"><span class="comment-age">(19 Oct '15, 15:33)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46935"></span><div id="comment-46935" class="comment"><div id="post-46935-score" class="comment-score"></div><div class="comment-text"><p>I uploaded a dumpfile, below the cloudshark link</p></div><div id="comment-46935-info" class="comment-info"><span class="comment-age">(26 Oct '15, 07:25)</span> <span class="comment-user userinfo">ryu80</span></div></div><span id="47742"></span><div id="comment-47742" class="comment"><div id="post-47742-score" class="comment-score"></div><div class="comment-text"><p>Any suggestion? it seems that wireshark to calculate RTO considers the last received segment with some payload data. I find it hard to believe there is a bug related to rto calculation.</p></div><div id="comment-47742-info" class="comment-info"><span class="comment-age">(19 Nov '15, 02:26)</span> <span class="comment-user userinfo">ryu80</span></div></div></div><div id="comment-tools-46695" class="comment-tools"></div><div class="clear"></div><div id="comment-46695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

