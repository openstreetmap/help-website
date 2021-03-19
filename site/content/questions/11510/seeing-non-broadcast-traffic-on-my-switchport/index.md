+++
type = "question"
title = "Seeing non-broadcast traffic on my switchport"
description = '''Some of this info has been posted as a reply in an earlier question. My main concern is during a capture I am seeing packets not destined for my IP. I have no SPAN sessions configured and some packets are from other networks even. (Kurt) I am using a Cisco IronPort web security appliance that utiliz...'''
date = "2012-05-31T15:57:00Z"
lastmod = "2012-05-31T17:54:00Z"
weight = 11510
keywords = [ "cef", "non-broadcast" ]
aliases = [ "/questions/11510" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Seeing non-broadcast traffic on my switchport](/questions/11510/seeing-non-broadcast-traffic-on-my-switchport)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11510-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Some of this info has been posted as a reply in an earlier question. My main concern is during a capture I am seeing packets not destined for my IP. I have no SPAN sessions configured and some packets are from other networks even.</p><p>(Kurt) I am using a Cisco IronPort web security appliance that utilizes WCCP as well as a Catalyst 6500 which uses CEF.</p><p>I am not very familiar with either of those technologies but will be doing some research.</p></div><div id="question-tags" class="tags-container tags">cef non-broadcast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '12, 15:57</strong></p><img src="https://secure.gravatar.com/avatar/c2b0501505637d339f1cd1f19a7d047e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davj1&#39;s gravatar image" /><p>davj1<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davj1 has no accepted answers">0%</span></p></div></div><div id="comments-container-11510" class="comments-container"></div><div id="comment-tools-11510" class="comment-tools"></div><div class="clear"></div><div id="comment-11510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11511"></span>

<div id="answer-container-11511" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11511-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>It happens. You usually see one unicast frame every once in a while that is not for you.</p><p>The reason is that the switch has removed the MAC address of the target from its internal table, and the next time a frame comes in it has to flood it to all ports because it doesn't know anymore where the target system is connected at. As soon as the answer comes back in it records the port of the MAC address and you'll see no more frames of that communication. Until the switch once again forgets the entry...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '12, 17:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-11511" class="comments-container"></div><div id="comment-tools-11511" class="comment-tools"></div><div class="clear"></div><div id="comment-11511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11512"></span>

<div id="answer-container-11512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11512-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>We are using Cisco gear here but on my workstation I'm seeing a packet every now and then that has nothing to do with my IP nor is it a broadcast.<br />
</p></blockquote><p>If the addresses are neither broadcast nor multicast (please double check IP and MAC), then I would say its either a bug of the switch firmware or maybe a kind of overload situation, where the switch runs into "fail-open" mode to prevent network interruption. Check the switch logs.<br />
</p><blockquote><p>I can give some more insight to my specific situation. This was a simple TCP SYN<br />
from one machine to another. One machine on the same network as mine, the sending<br />
machine on a completely different network. No SPAN sessions are configured on my switch.<br />
</p></blockquote><p>Please check what @Jasper said.</p><blockquote><p>This was a simple TCP SYN from one machine to another. One machine on the same network as mine, the sending machine on a completely different network.</p></blockquote><p>If the SYN was initiated from the remote server, it's probably the problem that @Jasper mentioned. If so (and it's not the WCCP/CEF problem - see below), please mark his answer as the correct one.</p><p>If the SYN was initiated from the local server, it's most certainly not the problem that @Jasper mentioned, as it would mean that the switch did not know the mac address of the router, which would be rather uncommon in a busy network.</p><blockquote><p>(Kurt) I am using a Cisco IronPort web security appliance that utilizes WCCP as well as a Catalyst 6500 which uses CEF.<br />
</p></blockquote><p>In that case it could be a similar problem I discovered once with WCCP and CEF, if the IP addresses you see, would be forwarded via WCCP.</p><p><strong>Problem:</strong> Once in a while (maybe 1-4 times a week) a SQL "batch sync job" failed after one server was moved to a different data center.<br />
</p><p>There was a Riverbed involved that used WCCP to get the traffic forwarded from the internal router (out of path deployment). I analyzed the problem and found a <strong>single SYN packet</strong> being <strong>forwarded by CEF</strong> to the wrong gateway (according to the routing table) <strong>instead of being forwarded by WCCP</strong> to the Riverbed. This misrouted packet, caused a problem due to asymmetric routing through the Riverbed, with the result, that the TCP connection could not be established. Unfortunately that software was dumb enough not to retry and thus it generated a severe problem with the SQL data sync !??! Don't ask, it was a (possibly) dumb OS (AS400) and (possibly) dumb software ;-)</p><p>I never found a plausible explanation, but disabling CEF solved the problem. I did this, because I found some hints after running some commands on the cisco router (I believe "show wccp" and "show cef"). Unfortunately I cannot remember the details of what I saw/found. However, it was pretty easy to spot, as I'm not a Cisco specialist (just enough know-how to configure the basics+).</p><p><strong>WARNING</strong>: Disabling CEF led to a remarkable higher CPU load on the router (~ +10-15%), however that was tolerable as it fixed a tedious problem ;-)<br />
</p><p>Just an idea....</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '12, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 May '12, 18:03</p></div></div><div id="comments-container-11512" class="comments-container"><span id="11538"></span><div id="comment-11538" class="comment"><div id="post-11538-score" class="comment-score"></div><div class="comment-text"><p>Thank you to both of you for the ideas. Jasper, I am fighting to like your answer. I think it's 100% right but it just seems so simple I hate to agree with it :) I am definitely only seeing sporadic packets make it to me and I have not yet verified that they did NOT make it to the intended device so I think I'll go with that.</p><p>Kurt - Hopefully I can keep that obscure knowledge in the back of my head. Your answer lead me to do some research and learning on CEF and WCCP. This being my first couple years as a CCNA, I always enjoy learning something new.</p></div><div id="comment-11538-info" class="comment-info"><span class="comment-age">(01 Jun '12, 10:35)</span> davj1</div></div><span id="11542"></span><div id="comment-11542" class="comment"><div id="post-11542-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Kurt - Hopefully I can keep that obscure knowledge in the back of my head.</p></blockquote><p>maybe it's better not to memorize that kind of things ;-))</p><blockquote><p>I am definitely only seeing sporadic packets make it to me and I have not yet verified that they did NOT make it to the intended device so I think I'll go with that.</p></blockquote><p>did you check the direction of those SYN packets? Is the initiator (source ip) the internal endpoint or the external endpoint - see my explanation above.</p><p>If you can't decide between the answers, then mark Jaspers answer as the correct one, as he was first, and it's a very plausible explanation. If you want, you can also click on the "Like" button of my answer to award some points to me as well. Fair solution ;-))</p></div><div id="comment-11542-info" class="comment-info"><span class="comment-age">(01 Jun '12, 11:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11512" class="comment-tools"></div><div class="clear"></div><div id="comment-11512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

