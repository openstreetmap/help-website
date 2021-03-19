+++
type = "question"
title = "SSL transfer inexplicable holdoff?"
description = '''First, I apologize for the cropped picture... I tried to get everything relevent. Len=0 on all Red-&amp;gt;Blue packets. So yeah, Red is a workstation downloading a file over SSL from distant server Blue. I have no access or control over distant server blue, nor any of the infrastructure beyond the firs...'''
date = "2012-12-31T17:02:00Z"
lastmod = "2013-01-03T02:44:00Z"
weight = 17365
keywords = [ "transfer", "ssl", "retransmission", "tcp", "backoff" ]
aliases = [ "/questions/17365" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SSL transfer inexplicable holdoff?](/questions/17365/ssl-transfer-inexplicable-holdoff)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17365-score" class="post-score" title="current number of votes">0</div><span id="post-17365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First, I apologize for the cropped picture... I tried to get everything relevent. Len=0 on all Red-&gt;Blue packets.</p><p>So yeah, Red is a workstation downloading a file over SSL from distant server Blue. I have no access or control over distant server blue, nor any of the infrastructure beyond the first two hops. There's some NAT and IOS based firewalls on my end, but other than that, it's all "cloud".</p><p>What's breaking my brain is that transfer goes along just fine, from anywhere to 200 to 1800 seconds, and then Blue goes into what appears to be retransmission backoff... "you never ACK'd, so I send again 1 second later, again 2 seconds, 4 seconds, 8... it goes all the way up to 120s and then just keeps sending one packet at a time every 120s.</p><p>The only two things I can think of that would cause that behavior would be either windowing issues, or dropped packets. I can't see any reason to suspect windowing because none of the packets reflect that ("Win=66000" from RED, "12574" from blue, both are consistent throughout the transfer), so that's out. I also can't say it's dropped packets, because there are literally NO retransmissions in the entire transfer. 300MB transferred over half an hour, and the only thing wireshark flagged on was a zero-window during the first 11 seconds, probably related to me deciding where I wanted to save the stupid thing. So by all accounts... it's moving along flawlessly.<br />
</p><p>What's more, even after the backoff begins, it's sending new packets with new, correct and expected sequence numbers. So it sends Seq#x... I ack Seq#x... it waits 120 seconds and then sends Seq#x+1320. So if it's sending new data, it would have to indicate that it's recieving my ACKs, correct? So no dropped packets, right?<br />
</p><p>I just want to get another opinion on this before I officially give up and blame it on some wonky proxy or web server on the distant end (no proxies on my end at all). And I suppose if anyone happens to have any idea WHY this would happen, I could try to contact the other end and help them out... But mostly I just want to know I'm not insane here.<br />
</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_4.PNG" alt="alt text" /></p><p>Kurt: Enjoy.</p><pre><code>0.000000000,0x3ad1,0,1,1,0x0010
0.015294000,0xf06d,1320,1,1,0x0010
0.022485000,0xf06e,1320,1321,1,0x0010
0.022516000,0x3ad2,0,1,2641,0x0010
0.037713000,0xf06f,1320,2641,1,0x0010
0.052892000,0xf070,1320,3961,1,0x0010
0.052916000,0x3ad3,0,1,5281,0x0010
0.068163000,0xf071,1320,5281,1,0x0010
0.265075000,0x3ad4,0,1,6601,0x0010
1.428516000,0xf0a4,1320,6601,1,0x0010
1.637821000,0x3ad5,0,1,7921,0x0010
3.895291000,0xf0a6,1320,7921,1,0x0010
4.102556000,0x3ad6,0,1,9241,0x0010
8.575147000,0xf0a8,1320,9241,1,0x0010
8.782468000,0x3b60,0,1,10561,0x0010
17.694649000,0xf0aa,1320,10561,1,0x0010
17.908217000,0x3b6b,0,1,11881,0x0010
35.645937000,0xf0ac,1320,11881,1,0x0010
35.847830000,0x3bad,0,1,13201,0x0010
71.292326000,0xf0ae,1320,13201,1,0x0010
71.507379000,0x3c11,0,1,14521,0x0010
142.329028000,0xf0b0,1320,14521,1,0x0010
142.532483000,0x3c3b,0,1,15841,0x0010</code></pre><p>Looking at that, it looks rather information dense. Mind explaining what about that is meaningful?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-transfer" rel="tag" title="see questions tagged &#39;transfer&#39;">transfer</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-backoff" rel="tag" title="see questions tagged &#39;backoff&#39;">backoff</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '12, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/8c8bb4331d25d8ed8241358cecc41b39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="W-George&#39;s gravatar image" /><p><span>W-George</span><br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="W-George has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jan '13, 15:33</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></br></p></div></div><div id="comments-container-17365" class="comments-container"><span id="17372"></span><div id="comment-17372" class="comment"><div id="post-17372-score" class="comment-score"></div><div class="comment-text"><p>can you please add the following output for the time interval when the 'effect' is visible.</p><blockquote><p><code>tshark -nr input.cap -T fields -E separator=, -e frame.time_relative -e ip.id -e tcp.len -e tcp.seq -e tcp.ack -e tcp.flags</code></p></blockquote></div><div id="comment-17372-info" class="comment-info"><span class="comment-age">(01 Jan '13, 03:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17373"></span><div id="comment-17373" class="comment"><div id="post-17373-score" class="comment-score"></div><div class="comment-text"><p>Sure. I'll give that a shot when I'm back in the office in the morning.</p></div><div id="comment-17373-info" class="comment-info"><span class="comment-age">(01 Jan '13, 08:12)</span> <span class="comment-user userinfo">W-George</span></div></div><span id="17385"></span><div id="comment-17385" class="comment"><div id="post-17385-score" class="comment-score"></div><div class="comment-text"><p>did you have a chance to generate the mentioned output?</p></div><div id="comment-17385-info" class="comment-info"><span class="comment-age">(02 Jan '13, 06:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17411"></span><div id="comment-17411" class="comment"><div id="post-17411-score" class="comment-score"></div><div class="comment-text"><p><span>@W-George</span>: the output just lists the relative time, the IP Identification field, length of the TCP playload, sequence number/acknowledge number, and the TCP flags. With that we can see a bit more of what the stacks do.</p><p>It's interesting to see that the IP-ID is increased by 2 for each packet coming from the server when it gets slow. While it may be because the server is talking to someone else in the meantime I suspect that there is in fact one packet belonging to the conversation that doesn't get through to the client. Because when it is still fast, we see sequential IP-IDs.</p></div><div id="comment-17411-info" class="comment-info"><span class="comment-age">(03 Jan '13, 02:44)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-17365" class="comment-tools"></div><div class="clear"></div><div id="comment-17365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17370"></span>

<div id="answer-container-17370" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17370-score" class="post-score" title="current number of votes">2</div><span id="post-17370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="W-George has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's a little hard to say for sure, since we can't see the sequence numbers used by the server, but when I compare the length of the server packets they seem to relate to the increasing ACK numbers coming from the client. So in that regard I'd agree with you that it seems that there is no packet loss.</p><p>The interesting thing is that the "bad" time delays start at 1 second and double up each time. This is a typical "uh, there's somehting going wrong here" backoff mechanism, but it is impossible to tell without looking at the server side (which you said you can't).</p><p>If I'd have to guess I'd suspect a bandwidth managing device throttling down the conversation close to the server side. Whenever a communication seems fine end-to-end (with matching sequence/ack numbers and no packet loss) I'd almost bet on a device in the middle fooling things up. Only way to tell is to capture at client and server simultaneously, but this doesn't seem to be possible in this case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '13, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17370" class="comments-container"><span id="17378"></span><div id="comment-17378" class="comment"><div id="post-17378-score" class="comment-score"></div><div class="comment-text"><p>So yes, the ACK numbers you see do coincide with the sequence numbers of the server's packets, and they're all 1320 apart, which coincides with the data portion of the packet. One potential issue is that I've got two routers using IP Inspect, but neither of them claims to be dropping packets. However, to my knowledge, this behavior has only been observed from this one distant end. I was just able to successfully download the file at my house, but the transfer this time was from a completely seperate IP address space (different Class A network, even). So that doesn't help really.</p></div><div id="comment-17378-info" class="comment-info"><span class="comment-age">(02 Jan '13, 04:58)</span> <span class="comment-user userinfo">W-George</span></div></div></div><div id="comment-tools-17370" class="comment-tools"></div><div class="clear"></div><div id="comment-17370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

