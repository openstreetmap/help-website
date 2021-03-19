+++
type = "question"
title = "Does the packet make it to the other end?"
description = '''I have two wireshark captures. One showing the packets leaving one location. The other capture shows packets arriving at the destination. What is a good reference point to look at in the leaving packet so I can tell it&#x27;s the packet that arrived at the destination. I thought I could do that with sequ...'''
date = "2010-09-15T09:49:00Z"
lastmod = "2010-09-15T15:15:00Z"
weight = 84
keywords = [ "packets", "lost" ]
aliases = [ "/questions/84" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Does the packet make it to the other end?](/questions/84/does-the-packet-make-it-to-the-other-end)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-84-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two wireshark captures. One showing the packets leaving one location. The other capture shows packets arriving at the destination. What is a good reference point to look at in the leaving packet so I can tell it's the packet that arrived at the destination. I thought I could do that with sequence numbers but it doesn't seem to work that way. So any unique fixed value in the packet should help. Thanks, Gary</p></div><div id="question-tags" class="tags-container tags">packets lost</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '10, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/79e2938a11fa583058e06dab30eca850?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GaryC&#39;s gravatar image" /><p>GaryC<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GaryC has no accepted answers">0%</span></p></div></div><div id="comments-container-84" class="comments-container"><span id="85"></span><div id="comment-85" class="comment"><div id="post-85-score" class="comment-score"></div><div class="comment-text"><p>What kind of traffic? TCP? UDP? DECnet phase IV?</p></div><div id="comment-85-info" class="comment-info"><span class="comment-age">(15 Sep '10, 10:02)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-84" class="comment-tools"></div><div class="clear"></div><div id="comment-84-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="96"></span>

<div id="answer-container-96" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-96-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Gerald is totally right in asking about which protocol is used to be able to answer your question.</p><p>If I'm assuming that the sequence number you are referring to is the TCP sequence number and that these TCP packets are transported by IPv4, then indeed the sequence number might be changed by devices in between the client and the server (firewalls tend to do that for instance). A field this is mostly not altered is the IP identification in the IP header. This field is only changed when there is an application level proxy in between (loadbalancers often also behave as application level proxies, so they often create new IP identification values).</p><p>So if you look at the ip.id of the packet at the client end, you will most likely find it also at the server end. You can copy it in the client trace (rightclick on the ip.id in the packet details and choose "Copy as filter") and then use "Edit -&gt; Find Packet" (or &lt;ctrl&gt;-F) in the server trace and paste the filter in and click on "Find".</p><p>Beware that IP identification fields are 16 bit, so there will be multiple instances in a tracefile with many packets...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-96" class="comments-container"></div><div id="comment-tools-96" class="comment-tools"></div><div class="clear"></div><div id="comment-96-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="118"></span>

<div id="answer-container-118" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-118-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you both for your comments. First off I'm looking now at the Identification number to see if that will work and I really appreciate the idea. It gives me something to try. Some additional details I should have included in the original question are: I'm looking at TCP and the packets I'm looking at are keeping the far end device alive. The far end device will reset periodically as in randomly once a day or every other day. The packets are all in the same subnet but are making it to the far end through a wireless bridge. It appears that they stop going through then the far end device resets and when it comes back up the packets are fine for another 24 or 48 hours (but not exactly) for example once at 4:49 am and the other capture of the failure was at 9:19 am on the following day. I believe the packets are actually stopped and lost rather than late as a result of the failure. Thanks again, Gary</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 15:15</strong></p><img src="https://secure.gravatar.com/avatar/79e2938a11fa583058e06dab30eca850?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GaryC&#39;s gravatar image" /><p>GaryC<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GaryC has no accepted answers">0%</span></p></div></div><div id="comments-container-118" class="comments-container"></div><div id="comment-tools-118" class="comment-tools"></div><div class="clear"></div><div id="comment-118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

