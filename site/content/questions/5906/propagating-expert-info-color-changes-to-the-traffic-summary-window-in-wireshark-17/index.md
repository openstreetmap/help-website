+++
type = "question"
title = "propagating expert info color changes to the traffic summary window in Wireshark 1.7"
description = '''I have an RPC sub-dissector and I want to highlight certain packets dissected by my subdissector in the traffic summary window (topmost pane of Wireshark GUI). I&#x27;m currently calling expert_add_info_format() from my dissector, and this successfully changes the color of the packet in the protocol tree...'''
date = "2011-08-27T19:17:00Z"
lastmod = "2011-08-28T01:23:00Z"
weight = 5906
keywords = [ "expert-info", "coloring", "colorize" ]
aliases = [ "/questions/5906" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [propagating expert info color changes to the traffic summary window in Wireshark 1.7](/questions/5906/propagating-expert-info-color-changes-to-the-traffic-summary-window-in-wireshark-17)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5906-score" class="post-score" title="current number of votes">1</div><span id="post-5906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an RPC sub-dissector and I want to highlight certain packets dissected by my subdissector in the traffic summary window (topmost pane of Wireshark GUI). I'm currently calling expert_add_info_format() from my dissector, and this successfully changes the color of the packet in the protocol tree of the detailed view (middle pane of Wireshark GUI), but for some reason it is not propagating this color change up to the same packet in the traffic summary window. Portmap and TCP are successfully highlighting various packets in the traffic summary window, so I know this feature is working in the build I have. I looked through the packet-portmap.c and packet-tcp.c source code for hints, but I can't figure out how they are making this color change. Am I missing something?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-expert-info" rel="tag" title="see questions tagged &#39;expert-info&#39;">expert-info</span> <span class="post-tag tag-link-coloring" rel="tag" title="see questions tagged &#39;coloring&#39;">coloring</span> <span class="post-tag tag-link-colorize" rel="tag" title="see questions tagged &#39;colorize&#39;">colorize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '11, 19:17</strong></p><img src="https://secure.gravatar.com/avatar/199e687252bd158fbbb998dd44604a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="infiniteloop&#39;s gravatar image" /><p><span>infiniteloop</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="infiniteloop has no accepted answers">0%</span></p></div></div><div id="comments-container-5906" class="comments-container"></div><div id="comment-tools-5906" class="comment-tools"></div><div class="clear"></div><div id="comment-5906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5907"></span>

<div id="answer-container-5907" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5907-score" class="post-score" title="current number of votes">0</div><span id="post-5907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="infiniteloop has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The coloring in the packet-list is handled by the "coloring rules" and not by the dissectors directly. If you open the frame details in the middle pane, you can see which coloring rule was responsible for the coloring and which filter was used by the coloring rule.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '11, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5907" class="comments-container"></div><div id="comment-tools-5907" class="comment-tools"></div><div class="clear"></div><div id="comment-5907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

