+++
type = "question"
title = "Question on IP fragmentation"
description = '''I recently read this piece of information in a book which i want to understand more clearly with experts help from here. &quot;When a Packet gets fragmented all the fragmented packets gets same TTL Value.If they take different path through a network,they may end up with destination with varying TTL Value...'''
date = "2013-06-28T07:23:00Z"
lastmod = "2013-06-28T14:12:00Z"
weight = 22451
keywords = [ "fragmentation" ]
aliases = [ "/questions/22451" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Question on IP fragmentation](/questions/22451/question-on-ip-fragmentation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22451-score" class="post-score" title="current number of votes">0</div><span id="post-22451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently read this piece of information in a book which i want to understand more clearly with experts help from here.</p><p>"When a Packet gets fragmented all the fragmented packets gets same TTL Value.If they take different path through a network,they may end up with destination with varying TTL Values.When the first fragment arrives at the destination,however the destination host will begin counting down from the TTL Value of that packet in seconds.All the fragments must arrive before the timer expires or the fragment is considered "incomplete".</p><p>Can i assume that if the first fragment comes to end host with TTL value X and end host waits for X seconds before gathering all the Fragmented packets?</p><p>Can I safely assume that reassembly always happens at DIP(Destination IP in IP Header) or Is it at the default gateway router of End host?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '13, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-22451" class="comments-container"></div><div id="comment-tools-22451" class="comment-tools"></div><div class="clear"></div><div id="comment-22451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22452"></span>

<div id="answer-container-22452" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22452-score" class="post-score" title="current number of votes">1</div><span id="post-22452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What book is that and when was it published? This mechanism seems really outdated, but I might be wrong... I mean, lets consider a starting TTL of 255. It's pretty safe to assume that it will end up at the destination with nothing less than a TTL of 200, since the maximum hop distance across the internet is somewhere between 22 and 30 hops, so assuming 55 hops is really generous. That would mean that - according to your book - the receiver waits for 200 seconds in case a fragment doesn't arrive. 200 seconds are an eternity in modern networks, and if a host would really wait this long before dropping the partially received fragments it could be attacked in a very simple denial of service attack.</p><p>My guess is that modern stacks drop fragments based on a multiple of the RTT, not on TTL. I'd have to check this in a lab setup, though - I haven't found any specification yet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '13, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22452" class="comments-container"><span id="22453"></span><div id="comment-22453" class="comment"><div id="post-22453-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper.This was from Wireshark Network Analysis by Laura Chappell[2nd edition 2012 Publication]</p></div><div id="comment-22453-info" class="comment-info"><span class="comment-age">(28 Jun '13, 08:04)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="22454"></span><div id="comment-22454" class="comment"><div id="post-22454-score" class="comment-score"></div><div class="comment-text"><p>Yep, just found it in that book, too. Not sure if it is correct thought; waiting that long would be very dangerous. I'll have to investigate further.</p><p>Also, to answer your questions I somehow skipped in the original answer: the reassembly is done on the receiving node, not a router in front of it. And as soon as all fragments are received the reassembled packet is passed up the stack; there is no sense in waiting for the TTL to expire until doing that, because it would mean artificial pauses that aren't necessary.</p></div><div id="comment-22454-info" class="comment-info"><span class="comment-age">(28 Jun '13, 08:09)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="22458"></span><div id="comment-22458" class="comment"><div id="post-22458-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper if MTU is same between End Router and the host connected to it then what prevents the reassembly on Router itself rather than end host?(Pardon me if this sounds silly)</p></div><div id="comment-22458-info" class="comment-info"><span class="comment-age">(28 Jun '13, 10:24)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="22459"></span><div id="comment-22459" class="comment"><div id="post-22459-score" class="comment-score">3</div><div class="comment-text"><p>From RFC 1122</p><pre><code>There MUST be a reassembly timeout.  The reassembly timeout
value SHOULD be a fixed value, not set from the remaining TTL.
It is recommended that the value lie between 60 seconds and 120
seconds.  If this timeout expires, the partially-reassembled
datagram MUST be discarded and an ICMP Time Exceeded message
sent to the source host (if fragment zero has been received).
</code></pre><p>I believe there was an earlier RFC that suggested to use the remaining TTL as a timeout value, but I was unable to find it.</p></div><div id="comment-22459-info" class="comment-info"><span class="comment-age">(28 Jun '13, 13:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22460"></span><div id="comment-22460" class="comment"><div id="post-22460-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>what prevents the reassembly on Router itself</p></blockquote><p>If a router would do reassembly for all nodes (connected to its network) it would have to reserve a huge buffer for the reassembly of the packets. That would certainly overload the router, so it's better to distribute that task and let the final node, the receiver, reassemble the packets.</p><p>Nevertheless, you can configure routers to do exactly that. So the real reason that prevents reassembly on the router itself is a matter of configuration.</p></div><div id="comment-22460-info" class="comment-info"><span class="comment-age">(28 Jun '13, 13:44)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22461"></span><div id="comment-22461" class="comment not_top_scorer"><div id="post-22461-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer Kurt.</p></div><div id="comment-22461-info" class="comment-info"><span class="comment-age">(28 Jun '13, 14:12)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div></div><div id="comment-tools-22452" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-22452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

