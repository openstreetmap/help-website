+++
type = "question"
title = "how to understand odd number packets are evil?"
description = '''Hi, I&#x27;m looking at some of the sharkfest sessions on Youtube. For the sessions presented by Hansang Bae, I noticed an interesting topic which is about &quot;Odd Numbers are Evil&quot;. I don&#x27;t really understand what does it mean,guess the expert here do understand what I mean here. So, could you please explai...'''
date = "2013-12-31T00:08:00Z"
lastmod = "2014-01-03T23:28:00Z"
weight = 28497
keywords = [ "odd_number_packet" ]
aliases = [ "/questions/28497" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to understand odd number packets are evil?](/questions/28497/how-to-understand-odd-number-packets-are-evil)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28497-score" class="post-score" title="current number of votes">0</div><span id="post-28497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm looking at some of the sharkfest sessions on Youtube. For the sessions presented by Hansang Bae, I noticed an interesting topic which is about "Odd Numbers are Evil". I don't really understand what does it mean,guess the expert here do understand what I mean here.</p><p>So, could you please explain what does this kind of issue mean? Is there any document, video that can be referred to?</p><p>thanks a lot!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-odd_number_packet" rel="tag" title="see questions tagged &#39;odd_number_packet&#39;">odd_number_packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '13, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Dec '13, 00:09</strong> </span></p></div></div><div id="comments-container-28497" class="comments-container"></div><div id="comment-tools-28497" class="comment-tools"></div><div class="clear"></div><div id="comment-28497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28515"></span>

<div id="answer-container-28515" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28515-score" class="post-score" title="current number of votes">2</div><span id="post-28515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Odd numbers are evil" refers to the behavior of most TCP stacks to acknowledge each other packet, which means that ACK packets are sent after receiving two data segments. When there is an odd total number of segments in a transmission the last segment has no following segment that gets acknowledged, so the receiver waits and waits and waits, but nothing is received. Finally, a so called "delayed ACK" is sent, but that takes a few hundred milliseconds. This kind of delay can also lead to more problems, one of which Hansang explained in a post in the official Wireshark blog when the Nagle algorithm kicks in and creating more problems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '14, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28515" class="comments-container"><span id="28543"></span><div id="comment-28543" class="comment"><div id="post-28543-score" class="comment-score"></div><div class="comment-text"><p>fantastic!!! This is really what I want. I do observed some traces likes this:</p><p>A to B file transfer:</p><p>.... several ms,packet 1 (A-&gt;B) several ms,packet 2 (A-&gt;B) several ms,packet 3 (A-&gt;B) several ms,packet 4 (A-&gt;B) several ms,packet 5 (A-&gt;B) several ms,packet 6 (A-&gt;B) several ms,packet 7 (A-&gt;B) tens ms, packet 8 (A&lt;-B) &lt;-- Ack for packet 7 ....</p><p>There are 7 packets out from A to B, which is odd number. Then the Ack (packet 8) took tens of ms to acknowledge back.</p><p>One more question, you just said there should be an ACK for every two packets, why did I see only one Ack which acking all of the 7 packets? Is it a just a different implementation of TCP delay-ed Ack?</p></div><div id="comment-28543-info" class="comment-info"><span class="comment-age">(02 Jan '14, 23:37)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="28547"></span><div id="comment-28547" class="comment"><div id="post-28547-score" class="comment-score"></div><div class="comment-text"><p>That would be a little uncommon, because most stacks do in fact ACK every second packet. But there is no rule that doesn't allow for a host to acknowledge a whole bunch of packets in one ACK packets, so it is possible. Something like that is often seen when packet loss occurred and and ACK is sent for all packets that arrived since the gap was detected when the gap is finally closed by a retransmission.</p></div><div id="comment-28547-info" class="comment-info"><span class="comment-age">(03 Jan '14, 01:26)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="28550"></span><div id="comment-28550" class="comment"><div id="post-28550-score" class="comment-score"></div><div class="comment-text"><p>I don't really understand this part of you,</p><p>"Something like that is often seen when packet loss occurred and and ACK is sent for all packets that arrived since the gap was detected when the gap is finally closed by a retransmission."</p><p>Do you mean out-of-order packet arrival? Could you give me an example?</p></div><div id="comment-28550-info" class="comment-info"><span class="comment-age">(03 Jan '14, 07:34)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="28555"></span><div id="comment-28555" class="comment"><div id="post-28555-score" class="comment-score"></div><div class="comment-text"><p>Out-of-Order is usually not enough to provoke it.</p><p>Let's say you have 10 segments sent to the receiver, and the third segment gets lost. The receiver will acknowledge the first two, and acknowledge them again when segment 3 and 4 arrive ("Dup ACK #1"), then again for segments 5 and 6 ("Dup ACK #2") and so so until all 10 segments arrived. When the sender resends the missing segment (making the series of segments complete at the receiver) it will (in most cases) acknowledge all 10 segments in one ACK, and not send 4 ACKs. This is what I meant.</p></div><div id="comment-28555-info" class="comment-info"><span class="comment-age">(03 Jan '14, 10:17)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="28564"></span><div id="comment-28564" class="comment"><div id="post-28564-score" class="comment-score"></div><div class="comment-text"><p>I think when the 3rd segment gets lost, all the arrivals of the left 7 segments (#4,#5,#6,#7,#8,#9,#10) will each cause a Dup ACK to the sender. Most probably this will trigger a Fast Retransmission to fix the gap of segment 3. When the missing segment (#3) arrive, the receiver will Ack all of the bytes till #10. I think this is what you mean here.</p><p>In my trace, there is no retransmission actually. So it way be a tcp stack implementation difference.</p></div><div id="comment-28564-info" class="comment-info"><span class="comment-age">(03 Jan '14, 23:28)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-28515" class="comment-tools"></div><div class="clear"></div><div id="comment-28515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

