+++
type = "question"
title = "does mtu size on capture NIC limit the size of packets you can capture?"
description = '''I&#x27;m wondering, because I captured traffic on a network link that handles &quot;jumbo&quot; frames, but the capture NIC I used had the MTU set at the default 1500 value. I looked at the resulting .pcap file, and I do have frames with byte sizes exceeding 1500. So can anyone confirm that the promisc function of...'''
date = "2012-05-22T20:49:00Z"
lastmod = "2012-05-23T05:29:00Z"
weight = 11232
keywords = [ "promiscuous", "mtu" ]
aliases = [ "/questions/11232" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [does mtu size on capture NIC limit the size of packets you can capture?](/questions/11232/does-mtu-size-on-capture-nic-limit-the-size-of-packets-you-can-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11232-score" class="post-score" title="current number of votes">0</div><span id="post-11232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wondering, because I captured traffic on a network link that handles "jumbo" frames, but the capture NIC I used had the MTU set at the default 1500 value. I looked at the resulting .pcap file, and I do have frames with byte sizes exceeding 1500. So can anyone confirm that the promisc function of the NIC is not subject to the MTU set on the NIC? Or must one set the MTU size on the capture NIC to say 9000 to be able to capture jumbo frames without incident?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-mtu" rel="tag" title="see questions tagged &#39;mtu&#39;">mtu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '12, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/e0423b823331f6b489f99b939d5c669d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="willdennis&#39;s gravatar image" /><p><span>willdennis</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="willdennis has no accepted answers">0%</span></p></div></div><div id="comments-container-11232" class="comments-container"></div><div id="comment-tools-11232" class="comment-tools"></div><div class="clear"></div><div id="comment-11232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11242"></span>

<div id="answer-container-11242" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11242-score" class="post-score" title="current number of votes">2</div><span id="post-11242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="willdennis has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The MTU size does not limit capturing (<strong>receiving</strong>) large packets, as it's the Maximum <strong>Transmission</strong> Unit (MTU) ;-)) There might be issues with your nic driver if we talk about jumbo frames, but that's a different problem.</p><p>Try yourself:</p><blockquote><p><code>ifconfig eth0 mtu 500</code></p></blockquote><p>Now capture some traffic. You will see packets &gt; 500 bytes.</p><p>See also this question: <code>http://ask.wireshark.org/questions/10862/working-on-jumbo-frames-with-wireshark</code></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 23:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '12, 06:37</strong> </span></p></div></div><div id="comments-container-11242" class="comments-container"><span id="11251"></span><div id="comment-11251" class="comment"><div id="post-11251-score" class="comment-score"></div><div class="comment-text"><p>Sometimes it pays to remember what the acronym stands for :) Thanks, Kurt!</p></div><div id="comment-11251-info" class="comment-info"><span class="comment-age">(23 May '12, 05:29)</span> <span class="comment-user userinfo">willdennis</span></div></div></div><div id="comment-tools-11242" class="comment-tools"></div><div class="clear"></div><div id="comment-11242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11238"></span>

<div id="answer-container-11238" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11238-score" class="post-score" title="current number of votes">2</div><span id="post-11238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My guess would be that the NIC implements <a href="http://en.wikipedia.org/wiki/Jon_Postel">Postel's</a> <a href="http://en.wikipedia.org/wiki/Robustness_principle">law</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 21:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-11238" class="comments-container"></div><div id="comment-tools-11238" class="comment-tools"></div><div class="clear"></div><div id="comment-11238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

