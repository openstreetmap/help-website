+++
type = "question"
title = "MSS=1460, but the packet length=7306"
description = '''I wanted to understand how the process of exchanging data works, and according to the info I found on the internet, when two points want to transmit data, they do the three-way handshake and set some options. There&#x27;s one concerning MSS, and both machines sent value of 1460. But when you look at the ...'''
date = "2015-06-30T03:32:00Z"
lastmod = "2015-07-01T07:51:00Z"
weight = 43715
keywords = [ "length" ]
aliases = [ "/questions/43715" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [MSS=1460, but the packet length=7306](/questions/43715/mss1460-but-the-packet-length7306)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43715-score" class="post-score" title="current number of votes">0</div><span id="post-43715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to understand how the process of exchanging data works, and according to the info I found on the internet, when two points want to transmit data, they do the three-way handshake and set some options. There's one concerning MSS, and both machines sent value of 1460. But when you look at the following image, you can see that the packet size is way above the limit. I know that you should also add 20+20+14 for headers, but 7306 &gt;&gt; 1514.</p><p>Take a look at the picture: <img src="https://osqa-ask.wireshark.org/upfiles/2015-06-30-12:21:53_Selection.png" alt="wireshark 7306" /></p><p>There's also no fragmentation:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2015-06-30-12:23:35_Selection.png" alt="no fragmentation" /></p><p>MTU size on both systems is the same (1500), so does anyone could explain this behavior?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '15, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/95d5949e0a326d0c91c81f6565cafd1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morfik&#39;s gravatar image" /><p><span>morfik</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morfik has no accepted answers">0%</span></p></img></div></div><div id="comments-container-43715" class="comments-container"></div><div id="comment-tools-43715" class="comment-tools"></div><div class="clear"></div><div id="comment-43715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43718"></span>

<div id="answer-container-43718" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43718-score" class="post-score" title="current number of votes">3</div><span id="post-43718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jasper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Likely down to <a href="https://en.wikipedia.org/wiki/Large_segment_offload">Large Segment Offload</a> (or TSO) where the NIC splits the traffic into MTU sized frames.</p><p>Your capture point is before the NIC has split the data. Try capturing off-machine using a span or mirror port on a switch to see the "real" traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-43718" class="comments-container"><span id="43724"></span><div id="comment-43724" class="comment"><div id="post-43724-score" class="comment-score"></div><div class="comment-text"><p>Thanks to the information that <strong>grahamb</strong> provided, I manage to figure out where the "problem" was.</p><p>I was using LXC container, it's something like a virtual machine, and according to <a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=2055140">this article</a> , TSO/LSO is used for better performance of the virtual systems or the whole working station.</p><p>I check whether the virtual interfaces have the TSO/LSO option set, and they have:</p><pre><code># ethtool -k veth10-sid  | grep &quot;tcp-segmentation-offload&quot;
tcp-segmentation-offload: on</code></pre><p>This is just one of the ends of the tunnel. So if someone wanted to have (for instance for testing purposes) "normal size" of the packets, he could turn that option off on both ends, using the following command:</p><pre><code># ethtool -K veth10-sid tso off
# ethtool -k veth10-sid  | grep &quot;tcp-segmentation-offload&quot;
tcp-segmentation-offload: off</code></pre><p>And now the packets have 1514 bytes in length.</p></div><div id="comment-43724-info" class="comment-info"><span class="comment-age">(30 Jun '15, 04:12)</span> <span class="comment-user userinfo">morfik</span></div></div><span id="43735"></span><div id="comment-43735" class="comment"><div id="post-43735-score" class="comment-score"></div><div class="comment-text"><p><strong>note:</strong> converted your answer to a comment to the answer of <span>@grahamb</span> and changed the acceptance to his answer as it was the one that helped.</p></div><div id="comment-43735-info" class="comment-info"><span class="comment-age">(30 Jun '15, 09:47)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="43743"></span><div id="comment-43743" class="comment"><div id="post-43743-score" class="comment-score"></div><div class="comment-text"><p>It's weird that the comment is the real answer. The info that grahamb provided was useful. It pointed me in the right direction, but that wasn't the answer to the question. Besides, if I wanted to comment the answer, and I thought it satisfied me, I would just post a comment: "it works, thx" -- which means absolutely nothing to the people who read this question. In the "comment" you have the right solution how to change some settings in linux and what exactly caused the problem, which was lxc.</p></div><div id="comment-43743-info" class="comment-info"><span class="comment-age">(30 Jun '15, 11:31)</span> <span class="comment-user userinfo">morfik</span></div></div><span id="43745"></span><div id="comment-43745" class="comment"><div id="post-43745-score" class="comment-score"></div><div class="comment-text"><p>Your question was (paraphrased) "why are my segments too big" and "can anyone explain this behaviour", I answered that. Marking my answer as "Accepted" helps others with the same question.</p><p>You didn't indicate that you wanted to be rid if the large segments, nor did you let on that this was on a VM. If you had done so the answer would be different.</p></div><div id="comment-43745-info" class="comment-info"><span class="comment-age">(30 Jun '15, 12:14)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43782"></span><div id="comment-43782" class="comment not_top_scorer"><div id="post-43782-score" class="comment-score"></div><div class="comment-text"><p>I didn't even know that LXC would matter, so how could I include that in the question? You just gave me general info, and there was nothing concerning LXC containers either. Your answer just pointed me in the right direction, but it was actually me who provided the info what exactly caused the packet to have more bytes and how to disable/enable the TSO feature for the LXC container's interfaces (in the case that someone was asking himself whether there's a possibility to do so). So I don't really think this should be a comment.</p></div><div id="comment-43782-info" class="comment-info"><span class="comment-age">(01 Jul '15, 06:23)</span> <span class="comment-user userinfo">morfik</span></div></div><span id="43786"></span><div id="comment-43786" class="comment"><div id="post-43786-score" class="comment-score">1</div><div class="comment-text"><p><span>@grahamb</span> did give you the most probably root cause of the issue (and actually the right one). Your question was general and you got a general (valid) answer. From this point of view, his response is perfectly valid and should be identified as the right one for anyone doing a query for an issue with MTU (as your initial question and keywords indicated).</p><p>Your did find what was the right technical configuration required for your use case, but that will not always be applicable to other users (especially as your initial question and keywords did not make any reference to LXC.</p></div><div id="comment-43786-info" class="comment-info"><span class="comment-age">(01 Jul '15, 07:51)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-43718" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-43718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

