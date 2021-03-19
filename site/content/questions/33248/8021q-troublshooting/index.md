+++
type = "question"
title = "802.1q troublshooting"
description = '''Hello I have a Mikrotik router trunked to a an ESXi server. The trunk port is setup according to VMware and MikroTik, but I can not ping across. I would like to capture the trunking traffic, but not sure how to filter it to see what is going on and try to diagnose the problem. I would like just to s...'''
date = "2014-06-01T15:39:00Z"
lastmod = "2014-06-01T16:09:00Z"
weight = 33248
keywords = [ "trunking" ]
aliases = [ "/questions/33248" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [802.1q troublshooting](/questions/33248/8021q-troublshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33248-score" class="post-score" title="current number of votes">0</div><span id="post-33248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I have a Mikrotik router trunked to a an ESXi server. The trunk port is setup according to VMware and MikroTik, but I can not ping across. I would like to capture the trunking traffic, but not sure how to filter it to see what is going on and try to diagnose the problem.</p><p>I would like just to see only the 802.1q protocol and not the rest of the traffic trying to get across, or any other troubleshooting tips that can help me troubleshoot this problem.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-trunking" rel="tag" title="see questions tagged &#39;trunking&#39;">trunking</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '14, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/c2f1187b3da18669b131dbe3021a68a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrjoli021&#39;s gravatar image" /><p><span>mrjoli021</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrjoli021 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '14, 15:41</strong> </span></p></div></div><div id="comments-container-33248" class="comments-container"></div><div id="comment-tools-33248" class="comment-tools"></div><div class="clear"></div><div id="comment-33248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33251"></span>

<div id="answer-container-33251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33251-score" class="post-score" title="current number of votes">0</div><span id="post-33251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like just to see only the 802.1q protocol, and not the rest of the traffic trying to get across</p></blockquote><p>There is no 802.1q 'protocol'. 802.1q simply adds tags to a frame to mark the vlan it belongs to. So, it does not make sense to capture only the VLAN tags, without the rest of the frame (if I understand your question in the right way).</p><p>So, here is what I would do:</p><ul><li>start a packet capture on the mikrotik (see the manual), without any filters</li><li>configure a mirror port on the switch that connects the mikrotik and the esxi server. Capture any traffic on the port that the esxi is attached to.</li><li>limit the capture size in Wireshark/tcpdump to 100 bytes (-s)</li><li>ping in either direction</li><li>stop the packet captures</li><li>analyze the files with Wireshark</li></ul><p>BTW: If you want to see only VLAN traffic, you could use the capture filter: <strong>vlan</strong>, however that does not make much sense on a trunk port of the switch, as almost all frames will be tagged.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '14, 16:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '14, 16:31</strong> </span></p></div></div><div id="comments-container-33251" class="comments-container"></div><div id="comment-tools-33251" class="comment-tools"></div><div class="clear"></div><div id="comment-33251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

