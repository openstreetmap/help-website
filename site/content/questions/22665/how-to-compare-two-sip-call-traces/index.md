+++
type = "question"
title = "How to compare two SIP call traces?"
description = '''Hello All, I have a question as I have started working on Wireshark recently. I have two capture files and under both the Pcaps, there are so many VoIP calls but I am only interested in one VoIP (SIP) call which is actually somewhat similar in both the captures. The flow of that call includes multip...'''
date = "2013-07-04T10:35:00Z"
lastmod = "2013-07-06T16:45:00Z"
weight = 22665
keywords = [ "compare_2_voipcalls", "compare_two_traces", "compare_2_sip_calls", "compare_two_calls" ]
aliases = [ "/questions/22665" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to compare two SIP call traces?](/questions/22665/how-to-compare-two-sip-call-traces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22665-score" class="post-score" title="current number of votes">0</div><span id="post-22665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I have a question as I have started working on Wireshark recently.</p><p>I have two capture files and under both the Pcaps, there are so many VoIP calls but I am only interested in one VoIP (SIP) call which is actually somewhat similar in both the captures. The flow of that call includes multiple legs as the call is going through an SBC and also it includes multiple re-invites. So basically the call flow of that call is really big and call flow is same in both Pcaps. There can be some differences in the Headers of SIP Invite message or any other followed message.</p><p>So the question is that is it possible to compare these two calls, which exist in different Pcaps, and identify the differences in Headers (or the Values under Headers or any other type of differences) of the messages of those calls.</p><p>Please let me know how to achieve the same.</p><p>Thanks in advance!!!</p><p>Regards, Ayush</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compare_2_voipcalls" rel="tag" title="see questions tagged &#39;compare_2_voipcalls&#39;">compare_2_voipcalls</span> <span class="post-tag tag-link-compare_two_traces" rel="tag" title="see questions tagged &#39;compare_two_traces&#39;">compare_two_traces</span> <span class="post-tag tag-link-compare_2_sip_calls" rel="tag" title="see questions tagged &#39;compare_2_sip_calls&#39;">compare_2_sip_calls</span> <span class="post-tag tag-link-compare_two_calls" rel="tag" title="see questions tagged &#39;compare_two_calls&#39;">compare_two_calls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '13, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/faf3976e48e16619eaa84650d80003fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ayush%20J&#39;s gravatar image" /><p><span>Ayush J</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ayush J has no accepted answers">0%</span></p></div></div><div id="comments-container-22665" class="comments-container"></div><div id="comment-tools-22665" class="comment-tools"></div><div class="clear"></div><div id="comment-22665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22699"></span>

<div id="answer-container-22699" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22699-score" class="post-score" title="current number of votes">0</div><span id="post-22699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The first thing to do would be to cleanly define the call and filter out all the other VoIP calls you mention. If you can write out a display filter that cleanly matches only the traffic you want, or mark them all, you can export only that one call into its own .pcap file to isolate it (do the same for both packet captures, so you have only that one call in both new .pcap files).</p><p>Once you have the two calls lined up, you should be able to do an eye-ball comparison but if you want something that will look at each packet and say what header is different in what way automatically, the only things that come to mind are the protocol hierarchy view in Wireshark (Statistics &gt; Protocol Hierarachy) which will at least give you a protocol comparison, and the Summary view (Statistics &gt; Summary) which will give you a break down of byte counts and packet counts.</p><p>Beyond that, you can eye-ball the traces packet for packet since they're the same call as you say. You could do a quick scan on the Length field, or set TCP length as a column and compare those as well to see if there are any payload differences at those levels.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '13, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-22699" class="comments-container"></div><div id="comment-tools-22699" class="comment-tools"></div><div class="clear"></div><div id="comment-22699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

