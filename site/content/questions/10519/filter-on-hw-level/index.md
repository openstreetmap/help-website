+++
type = "question"
title = "Filter on HW Level"
description = '''I&#x27;m using Wireshark for my project and i need support to filter packets from HW level. Basically, i&#x27;m getting lot of packets and i would like to filter some useless packets captured on my interface. Could you please give me a hand? Thanks/ Alexis'''
date = "2012-04-30T07:39:00Z"
lastmod = "2012-04-30T12:36:00Z"
weight = 10519
keywords = [ "capture-filter" ]
aliases = [ "/questions/10519" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Filter on HW Level](/questions/10519/filter-on-hw-level)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10519-score" class="post-score" title="current number of votes">0</div><span id="post-10519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Wireshark for my project and i need support to filter packets from HW level. Basically, i'm getting lot of packets and i would like to filter some useless packets captured on my interface. Could you please give me a hand?</p><p>Thanks/ Alexis</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '12, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/95331cfc69099661972ea1b51b83b40b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexis&#39;s gravatar image" /><p><span>Alexis</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Apr '12, 07:42</strong> </span></p></div></div><div id="comments-container-10519" class="comments-container"></div><div id="comment-tools-10519" class="comment-tools"></div><div class="clear"></div><div id="comment-10519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10524"></span>

<div id="answer-container-10524" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10524-score" class="post-score" title="current number of votes">1</div><span id="post-10524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alexis has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>as already mentioned, please use cpature filters: <a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a></p><p>To give you just some idea:</p><p>port 443 -&gt; filter on TCP/UDP port 443<br />
host 1.1.1.1 -&gt; filter on IP addr 1.1.1.</p><p>Some "lower level" filter</p><p>not proto 6 -&gt; dont't capture IP protocol 6 (tcp)<br />
proto 17 -&gt; capture only IP protocol 17 (udp)<br />
not ether proto 0x0806 -&gt; don't capture ARP</p><p>Even "lower level" filter ;-)</p><p>'tcp[tcpflags] &amp; tcp-syn != 0' -&gt; capture all packets with the SYN flag set (SYN and SYN/ACK!!).</p><p>Check the various tutorials for more filter options and/or the man page of tcpdump.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Apr '12, 09:10</strong> </span></p></div></div><div id="comments-container-10524" class="comments-container"></div><div id="comment-tools-10524" class="comment-tools"></div><div class="clear"></div><div id="comment-10524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10520"></span>

<div id="answer-container-10520" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10520-score" class="post-score" title="current number of votes">1</div><span id="post-10520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should take a look at capture filters. If you open the capture options dialog you'll see an input field where you can specify capture filters. The syntax is that of tcpdump, and a few examples can be found in the capture filter list that you can open with the button next to the capture filter input field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-10520" class="comments-container"><span id="10522"></span><div id="comment-10522" class="comment"><div id="post-10522-score" class="comment-score"></div><div class="comment-text"><p>Basically, i need to filter only some packets. This should be done before any packet is gathered from the interface. The logic is to reduce volume of captured in my storage space. any idea?</p></div><div id="comment-10522-info" class="comment-info"><span class="comment-age">(30 Apr '12, 09:04)</span> <span class="comment-user userinfo">Alexis</span></div></div><span id="10526"></span><div id="comment-10526" class="comment"><div id="post-10526-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "this should be done before any packet is gathered from the interface"? Why does it matter when the filtering is done, as long as the packets don't reach Wireshark (or whatever program is being used)? Filtering with a capture filter can be done with existing software and hardware; filtering packets inside the network adapter itself will probably require specialized hardware that your machine probably doesn't have, and software to support that hardware.</p></div><div id="comment-10526-info" class="comment-info"><span class="comment-age">(30 Apr '12, 09:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="10532"></span><div id="comment-10532" class="comment"><div id="post-10532-score" class="comment-score"></div><div class="comment-text"><p>i mean Filtering while capturing.</p></div><div id="comment-10532-info" class="comment-info"><span class="comment-age">(30 Apr '12, 12:06)</span> <span class="comment-user userinfo">Alexis</span></div></div><span id="10533"></span><div id="comment-10533" class="comment"><div id="post-10533-score" class="comment-score"></div><div class="comment-text"><p>OK, then try a capture filter, as Jasper and Kurt suggested.</p></div><div id="comment-10533-info" class="comment-info"><span class="comment-age">(30 Apr '12, 12:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-10520" class="comment-tools"></div><div class="clear"></div><div id="comment-10520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

