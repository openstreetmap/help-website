+++
type = "question"
title = "Suppress TCP Retransmission Note in Dual Int Trace"
description = '''We need to capture packets as they pass through a router. We plan to use a capture unit with two NICs capturing from both with a single instance of dumpcap. This gives us traffic from both interfaces in a single pcapng file with frames from each NIC distinguished with the Interface Number. I decided...'''
date = "2015-08-29T08:44:00Z"
lastmod = "2015-08-29T09:43:00Z"
weight = 45508
keywords = [ "dual-nic" ]
aliases = [ "/questions/45508" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Suppress TCP Retransmission Note in Dual Int Trace](/questions/45508/suppress-tcp-retransmission-note-in-dual-int-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45508-score" class="post-score" title="current number of votes">0</div><span id="post-45508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We need to capture packets as they pass through a router. We plan to use a capture unit with two NICs capturing from both with a single instance of dumpcap. This gives us traffic from both interfaces in a single pcapng file with frames from each NIC distinguished with the Interface Number. I decided to test this with the following setup.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/dual_int.png" alt="alt text" /></p><p>The capture worked OK but every data packet has a TCP Retransmission partner, and ACK packet has a Dup ACK partner.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/dual_int_screenshot2_MBQTemv.png" alt="alt text" /></p><p>I did suspect this would happen, hence the test.</p><p>Is there a way to supress this? I'd like to be able to see true TCP Retransmissions but not have them flagged for the same packet appearing on another interface.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dual-nic" rel="tag" title="see questions tagged &#39;dual-nic&#39;">dual-nic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '15, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></img></div></div><div id="comments-container-45508" class="comments-container"></div><div id="comment-tools-45508" class="comment-tools"></div><div class="clear"></div><div id="comment-45508-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45509"></span>

<div id="answer-container-45509" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45509-score" class="post-score" title="current number of votes">2</div><span id="post-45509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This may explain the reason why this happens, plus how to get around it:</p><p><a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '15, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-45509" class="comments-container"><span id="45510"></span><div id="comment-45510" class="comment"><div id="post-45510-score" class="comment-score"></div><div class="comment-text"><p>What I would really like is a TCP Preference option that forces Wireshark to add interface number to the 5-tuple (a 6-tuple).</p><p>It needs to be an option because you might want the packets from two interfaces to be treated as one aggregate flow - e.g. SPANs or TAPs on teamed adapter interfaces.</p><p>I just wondered if anyone had discovered a trick to overcome the issue.</p></div><div id="comment-45510-info" class="comment-info"><span class="comment-age">(29 Aug '15, 09:39)</span> <span class="comment-user userinfo">PaulOfford</span></div></div><span id="45511"></span><div id="comment-45511" class="comment"><div id="post-45511-score" class="comment-score"></div><div class="comment-text"><p>As far as I know there is no trick, as long as you want to keep the duplicate packets in the same file.</p><p>You might want to open a Feature Request at <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a> for the 6-tuple ;-)</p></div><div id="comment-45511-info" class="comment-info"><span class="comment-age">(29 Aug '15, 09:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-45509" class="comment-tools"></div><div class="clear"></div><div id="comment-45509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

