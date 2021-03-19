+++
type = "question"
title = "Dissect question: how to dissect protocol that has fragment packets"
description = '''Hi there, I&#x27;d like to dissect a protocol which could be captured by fragment packets. I hit a problem while doing re-assemble using the dissector. I found the wireshark normally load only parts of the captured file (not all of the captured packet) and only dissect a packet when I navigate to a parti...'''
date = "2015-01-06T01:58:00Z"
lastmod = "2015-01-07T01:00:00Z"
weight = 38900
keywords = [ "dissect", "reassemble" ]
aliases = [ "/questions/38900" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissect question: how to dissect protocol that has fragment packets](/questions/38900/dissect-question-how-to-dissect-protocol-that-has-fragment-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38900-score" class="post-score" title="current number of votes">0</div><span id="post-38900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I'd like to dissect a protocol which could be captured by fragment packets. I hit a problem while doing re-assemble using the dissector. I found the wireshark normally load only parts of the captured file (not all of the captured packet) and only dissect a packet when I navigate to a particular row. That brings me an issue, as I drag the progress bar with the mouse to some later position of the captured file, it is possible that only packet (N ~ M) are displayed while packet N is the latest part of a reassembled PDU, that makes the dissector could not work since wireshark does not put packet number less than N being dissected. Is there any expert give me some clue on how to work this out?</p><p>Thanks, Jianhui</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissect" rel="tag" title="see questions tagged &#39;dissect&#39;">dissect</span> <span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '15, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/bbf88acd96e1a1f909172c86bd1cce6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jianhui&#39;s gravatar image" /><p><span>Jianhui</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jianhui has no accepted answers">0%</span></p></div></div><div id="comments-container-38900" class="comments-container"></div><div id="comment-tools-38900" class="comment-tools"></div><div class="clear"></div><div id="comment-38900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38901"></span>

<div id="answer-container-38901" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38901-score" class="post-score" title="current number of votes">0</div><span id="post-38901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.dissector;h=c50957459c03e872b110be55ef457c2f6c45bdc3;hb=HEAD">doc/README.dissector</a>, in the source tree, section 2.7 Reassembly/desegmentation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '15, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38901" class="comments-container"><span id="38915"></span><div id="comment-38915" class="comment"><div id="post-38915-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb,</p><p>Thanks for the quick response! I may not explain my issue correctly. I could work with segment/reassembly without problem (as long as those packets are loaded and dissected). The issue is when I open a captured file and scroll to the end of the captured file, I found wireshark does not call dissect_packet for each packet, but just those packet that is visible to the TreeView. This leads to the 1st visible packet could not be dissected correctly as it contains only later part of the whole PDU.</p><p>Thanks, Jianhui</p></div><div id="comment-38915-info" class="comment-info"><span class="comment-age">(06 Jan '15, 19:12)</span> <span class="comment-user userinfo">Jianhui</span></div></div><span id="38916"></span><div id="comment-38916" class="comment"><div id="post-38916-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb,</p><p>My intention is to show the 'last fragment' packet in the TreeView COL_INFO as "[Fragment]", but when I scroll back several packets and the rest part of the PDU is being dissected I can update the COL_INFO of the 'last fragment' packet's COL_INFO to something else.</p><p>Is there a way that I could go back and update the Info column of a packet, for example when its selected in the GUI and re-dissected, so I can correct COL_INFO of that packet?</p><p>Thanks, Jianhui</p></div><div id="comment-38916-info" class="comment-info"><span class="comment-age">(06 Jan '15, 19:18)</span> <span class="comment-user userinfo">Jianhui</span></div></div><span id="38918"></span><div id="comment-38918" class="comment"><div id="post-38918-score" class="comment-score"></div><div class="comment-text"><p>The file is read in sequence (all packets) only on the first pass. Writing to columns and reassembly code must not be under if(tree) as a tree may not be available. Some reassembly code may have to be protected by (pinfo)-&gt;fd-&gt;flags.visited or PINFO_FD_VISITED(pinfo)e.g only done once.</p><p>Hope this helps.</p></div><div id="comment-38918-info" class="comment-info"><span class="comment-age">(07 Jan '15, 01:00)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-38901" class="comment-tools"></div><div class="clear"></div><div id="comment-38901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

