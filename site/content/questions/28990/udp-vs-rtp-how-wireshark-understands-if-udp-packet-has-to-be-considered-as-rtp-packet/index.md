+++
type = "question"
title = "UDP vs RTP [How wireshark understands if UDP packet has to be considered as RTP packet?]"
description = '''How wireshark understands if UDP packet has to be considered as RTP packet? For instance... when i select &quot;Try to decode RTP outside of conversations&quot; [Edit -&amp;gt;Preferences -&amp;gt; RTP -&amp;gt; Try to decode RTP outside of conversations, only few UDP packets turn into RTP Packets. What information [i.e....'''
date = "2014-01-17T02:54:00Z"
lastmod = "2014-01-17T03:38:00Z"
weight = 28990
keywords = [ "rtp" ]
aliases = [ "/questions/28990" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UDP vs RTP \[How wireshark understands if UDP packet has to be considered as RTP packet?\]](/questions/28990/udp-vs-rtp-how-wireshark-understands-if-udp-packet-has-to-be-considered-as-rtp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28990-score" class="post-score" title="current number of votes">0</div><span id="post-28990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How wireshark understands if UDP packet has to be considered as RTP packet? For instance... when i select "Try to decode RTP outside of conversations" [Edit -&gt;Preferences -&gt; RTP -&gt; Try to decode RTP outside of conversations, only few UDP packets turn into RTP Packets.</p><p>What information [i.e. payload, version etc..] wireshark checks in UDP Packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '14, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/f06f6b3ad79b8afedef1058c188cc863?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lte007&#39;s gravatar image" /><p><span>lte007</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lte007 has one accepted answer">100%</span></p></div></div><div id="comments-container-28990" class="comments-container"></div><div id="comment-tools-28990" class="comment-tools"></div><div class="clear"></div><div id="comment-28990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28991"></span>

<div id="answer-container-28991" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28991-score" class="post-score" title="current number of votes">2</div><span id="post-28991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check the code in packet-rtp.c function dissect_rtp_heur_common(). In general there isn't a good signature for RTP packets so any heuristic will be weak. If you have the control signaling seting up the RTP flow your trace wireshark should be able to determine which packets are RTP or if this feature is missing for the control signaling dissector used in your trace it could be added.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '14, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-28991" class="comments-container"></div><div id="comment-tools-28991" class="comment-tools"></div><div class="clear"></div><div id="comment-28991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

