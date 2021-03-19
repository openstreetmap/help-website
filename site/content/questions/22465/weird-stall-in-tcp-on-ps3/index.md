+++
type = "question"
title = "Weird stall in TCP on PS3"
description = '''The PS3 tcp stack is a particularly fragile piece of software and it often drops incoming packets, resulting in stalled connections. However, here I have a very strange TCP phenomenon that I cannot quite understand. This happens fairly frequently, I have a script that can make it happen at will. I a...'''
date = "2013-06-29T05:19:00Z"
lastmod = "2013-07-02T07:02:00Z"
weight = 22465
keywords = [ "dup-ack", "ps3", "tcp" ]
aliases = [ "/questions/22465" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Weird stall in TCP on PS3](/questions/22465/weird-stall-in-tcp-on-ps3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22465-score" class="post-score" title="current number of votes">0</div><span id="post-22465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The PS3 tcp stack is a particularly fragile piece of software and it often drops incoming packets, resulting in stalled connections. However, here I have a very strange TCP phenomenon that I cannot quite understand. This happens fairly frequently, I have a script that can make it happen at will. I am making a http request for 1000000 bytes to a server some 40ms RTT away. The funny thing is the server sending a bunch of duplicate acks and then pausing before retransmitting. I see this very regularly. What is going on? See The funny thing is that after receiving some data, and acking it all (some 31k) the server then pauses, and after some 10ms proceeds to send <a href="http://www.cloudshark.org/captures/d46dcdc803c1?filter=tcp.stream%20eq%2012">http://www.cloudshark.org/captures/d46dcdc803c1?filter=tcp.stream%20eq%2012</a> , the problem starts with packet 456.</p><p>Stream 12 recovers, but others do not, e.g. stream 19, where we time out. in stream 19, the retransmit is acked, and yet, the server just stops sending data.</p><p>The only thing I can imagine going on is for all the ack packets from the PS3 to the server being lost somehow upstream. But I don't see this problem occurring for a PC machine doing the same thing. The only difference I can think of is the ps3's relatively small rcv window size of 64k.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-ps3" rel="tag" title="see questions tagged &#39;ps3&#39;">ps3</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '13, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/abd1db44a5e5138fbfec8ccf71d47691?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KristjanValur&#39;s gravatar image" /><p><span>KristjanValur</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KristjanValur has no accepted answers">0%</span></p></div></div><div id="comments-container-22465" class="comments-container"></div><div id="comment-tools-22465" class="comment-tools"></div><div class="clear"></div><div id="comment-22465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22467"></span>

<div id="answer-container-22467" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22467-score" class="post-score" title="current number of votes">2</div><span id="post-22467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like the server is having a problem with the TSval of 0. It starts sending packets with a TSecr of 4, which it shouldn't (as it never received a tsval of 4). Since it has 4 in it's TCP control block, all the ACK's from the client are rejected (as they have a tsval of 0 which is lower than the 4 in it's control block). Therefor it considers the data it has sent as un-acknowledged and after the (3 second) retransmission timer goes off, it starts retransmitting. Now things go well, because by that time the tsval has increased to 12.</p><p>The question is whether a tsval of 0 is allowed. <a href="http://tools.ietf.org/html/rfc1323">RFC 1323</a> is not clear on this. It only states that TSval should be 0 when the field is not supposed to be valid, so one might consider it an invalid value.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '13, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22467" class="comments-container"><span id="22470"></span><div id="comment-22470" class="comment"><div id="post-22470-score" class="comment-score"></div><div class="comment-text"><p>Interesting! It looks as though I'll have to create a defect with Sony to fix their stuff. It also seems to be server related so I need to figure out what the Cdn provider is running and check if it can be upgraded . Thank you.</p></div><div id="comment-22470-info" class="comment-info"><span class="comment-age">(29 Jun '13, 07:26)</span> <span class="comment-user userinfo">KristjanValur</span></div></div><span id="22473"></span><div id="comment-22473" class="comment"><div id="post-22473-score" class="comment-score"></div><div class="comment-text"><p>Well, I'm not sure if it is faulty behavior per se, but the server does not seem to cope with it very well. It wouldn't hurt to bring it to their attention though :-)</p></div><div id="comment-22473-info" class="comment-info"><span class="comment-age">(29 Jun '13, 13:48)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="22503"></span><div id="comment-22503" class="comment"><div id="post-22503-score" class="comment-score"></div><div class="comment-text"><p>On looking more closely, I don't think the PS3 is at fault. It simply has a slow running clock and 0 should be a valid value. See stream 19 as an example. Soon, the ps3 is sending a a TSval of 2. However, the server's data segemnts all contain TSecr of 18 which has, again, never been seen. This time round when the retransmitt occurs, things don't correct themselves, because the PS3's ACK clock has only advanced to 12. This definitely looks like a faulty server side TCP stack to me. Thanks again for bringing my attention to the timestamp options, threre seem to be endless nuances to the TCP protocol.</p></div><div id="comment-22503-info" class="comment-info"><span class="comment-age">(01 Jul '13, 02:37)</span> <span class="comment-user userinfo">KristjanValur</span></div></div><span id="22504"></span><div id="comment-22504" class="comment"><div id="post-22504-score" class="comment-score"></div><div class="comment-text"><p>Btw, I don't think that the RFC specifies that incoming segments with unexpected TSval values should be dropped, as seems to be the case here. the RTTE should be a wholly separate thing, run as an add on to regular stream control flow and not affect packet processing in other ways, right?</p></div><div id="comment-22504-info" class="comment-info"><span class="comment-age">(01 Jul '13, 02:44)</span> <span class="comment-user userinfo">KristjanValur</span></div></div><span id="22506"></span><div id="comment-22506" class="comment"><div id="post-22506-score" class="comment-score"></div><div class="comment-text"><p>OK, I did not look at the other sessions. But I think you're right that the server has a faulty TCP implementation, as it is echo'ing timestamps it has not seen. You might also want to check any intermediate device if you see this behavior with other sites too, they might be altering the timestamps (although I have not seen any device do that myself).</p><p>The RFC 1323 does say the following in par 4.2:</p><pre><code>  &quot;The basic idea
  is that a segment can be discarded as an old duplicate if it is
  received with a timestamp SEG.TSval less than some timestamp
  recently received on this connection.&quot;</code></pre><p>So I do think the server drops the ACK packets, this seems to be backed up by the fact that is starts retransmitting from the start of the session.</p></div><div id="comment-22506-info" class="comment-info"><span class="comment-age">(01 Jul '13, 03:23)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="22555"></span><div id="comment-22555" class="comment not_top_scorer"><div id="post-22555-score" class="comment-score"></div><div class="comment-text"><p>Hey, when testing this from a PC, I found that the latest windows clients don't use tcp timestamps for connections they initiate. This can be changed with a netsh option, however. I'm curious, why is this? RFC1323 introduces TS as a means of RTTE, but the wikipedia article on TCP mentions its primary use being PAWS. Surely both are important? Any idea why windows isn't using them by default?</p></div><div id="comment-22555-info" class="comment-info"><span class="comment-age">(02 Jul '13, 07:02)</span> <span class="comment-user userinfo">KristjanValur</span></div></div></div><div id="comment-tools-22467" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-22467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

