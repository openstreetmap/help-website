+++
type = "question"
title = "How to tell packet loss is happen locally?"
description = '''We have a program for receive udp multicast broadcast, the packet rate it will receive can be up to 3000 packet/sec. ~1500bytes max. size per packet.  Our situation is that we are experiencing packet loss when it hit that rate. Assuming packet never loss during network transportation, we want to kno...'''
date = "2013-01-02T19:45:00Z"
lastmod = "2013-01-03T07:22:00Z"
weight = 17406
keywords = [ "multicast" ]
aliases = [ "/questions/17406" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tell packet loss is happen locally?](/questions/17406/how-to-tell-packet-loss-is-happen-locally)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17406-score" class="post-score" title="current number of votes">0</div><span id="post-17406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a program for receive udp multicast broadcast, the packet rate it will receive can be up to 3000 packet/sec. ~1500bytes max. size per packet.</p><p>Our situation is that we are experiencing packet loss when it hit that rate. Assuming packet never loss during network transportation, we want to know are the packets loss cause by overflow in the network card buffer, or is the network card not fast enough, and it dropped the packets?</p><p>Could you please tell us how to analysis this with Wireshark? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multicast" rel="tag" title="see questions tagged &#39;multicast&#39;">multicast</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '13, 19:45</strong></p><img src="https://secure.gravatar.com/avatar/eaebacafc90c2a4a4e75f053e3c16432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bryanevil&#39;s gravatar image" /><p><span>bryanevil</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bryanevil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jan '13, 19:47</strong> </span></p></div></div><div id="comments-container-17406" class="comments-container"></div><div id="comment-tools-17406" class="comment-tools"></div><div class="clear"></div><div id="comment-17406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17408"></span>

<div id="answer-container-17408" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17408-score" class="post-score" title="current number of votes">2</div><span id="post-17408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't unless you span the port the servers/PCs (consumers of multicast) are spanned. Only then can you tell if you the packets made it past the egress buffers of your switch. But before you go that route, make sure your systems UDP buffers are tuned. Many OS's have fine tuned TCP buffers but the UDP buffers are left untouched. It's very likely that you will see drops in the UDP buffers during the bursts. Check with "netstat -s" to see the drops. Also, google for "udp buffer tuning" and you'll get some hits for your flavor of OS. Good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '13, 20:52</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-17408" class="comments-container"><span id="17410"></span><div id="comment-17410" class="comment"><div id="post-17410-score" class="comment-score"></div><div class="comment-text"><p>SPAN ports might not be good enough since it may drop frames in overload situations as well. I'd go for a full duplex tap here, and keep an eye on the drop counter while capturing to see if the capturing PC can cope with the number of packets.</p><p><span>@hansang</span>, I converted your comment to an answer, because it is an answer ;-)</p></div><div id="comment-17410-info" class="comment-info"><span class="comment-age">(03 Jan '13, 02:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="17414"></span><div id="comment-17414" class="comment"><div id="post-17414-score" class="comment-score"></div><div class="comment-text"><p>LOL! And how do you like my current Karma being at 666! And to your point about spans, I should have added that for MC troubleshooting, you don't even need RX+TX spans (the default). it's unidirectional traffic anyway. This changes if you're trying to troubleshoot MC control plane or app level feedback.</p></div><div id="comment-17414-info" class="comment-info"><span class="comment-age">(03 Jan '13, 07:22)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-17408" class="comment-tools"></div><div class="clear"></div><div id="comment-17408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

