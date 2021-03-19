+++
type = "question"
title = "BFD with MPLS packets are not proper in wireshark.[Not visible]"
description = '''Hi Team, i am new to this tool. my question looks silly. sorry for that :). How to check/analyze BFD in MPLS packet through wireshark 1.6 version. or suggest any alternate solution. thanks  Rajesh Kumar v'''
date = "2012-12-28T00:02:00Z"
lastmod = "2012-12-28T01:37:00Z"
weight = 17296
keywords = [ "wireshark", "mpls", "rajesh", "bfd" ]
aliases = [ "/questions/17296" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [BFD with MPLS packets are not proper in wireshark.\[Not visible\]](/questions/17296/bfd-with-mpls-packets-are-not-proper-in-wiresharknot-visible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17296-score" class="post-score" title="current number of votes">0</div><span id="post-17296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Team, i am new to this tool. my question looks silly. sorry for that :).</p><p>How to check/analyze BFD in MPLS packet through wireshark 1.6 version. or suggest any alternate solution.</p><p>thanks Rajesh Kumar v</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-mpls" rel="tag" title="see questions tagged &#39;mpls&#39;">mpls</span> <span class="post-tag tag-link-rajesh" rel="tag" title="see questions tagged &#39;rajesh&#39;">rajesh</span> <span class="post-tag tag-link-bfd" rel="tag" title="see questions tagged &#39;bfd&#39;">bfd</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '12, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/ed8e2bca2294d43ea522352f36f11717?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajesh%20Kumar%20V&#39;s gravatar image" /><p><span>Rajesh Kumar V</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajesh Kumar V has no accepted answers">0%</span></p></div></div><div id="comments-container-17296" class="comments-container"></div><div id="comment-tools-17296" class="comment-tools"></div><div class="clear"></div><div id="comment-17296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17299"></span>

<div id="answer-container-17299" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17299-score" class="post-score" title="current number of votes">1</div><span id="post-17299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just open a capture file with the latest 1.6 version and Wireshark should be able to detect the BFD protocol. If you need the extensions defined in the latest RFCs, you should upgrade to Wireshark 1.8 (stable) or 1.9 (development).</p><p>If Wireshark does not detect the BFD protocol in your packets, choose one of those packets and:</p><blockquote><p><code>right click -&gt; Decode as -&gt; BFD Control</code><br />
</p></blockquote><p>If that does not help, you either need to upgrade Wireshark or there is something 'wrong' with your BFD packets. In that case, please post a sample capture file somewhere.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '12, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-17299" class="comments-container"><span id="17300"></span><div id="comment-17300" class="comment"><div id="post-17300-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your prompt response. i am not able to see BFD protocal.</p><p>even Decode is not helping. i think my version of wire shark not supporting this.</p><p>may be i ll check the same in 1.8 or 1.9 version and update you further.</p><p>Summary of the packet for reference. 0.851093 0.851093 0a.00.0f 0a.00.00 FC 70 [Malformed Packet]</p><p>thanks Rajesh Kumar V</p></div><div id="comment-17300-info" class="comment-info"><span class="comment-age">(28 Dec '12, 01:30)</span> <span class="comment-user userinfo">Rajesh Kumar V</span></div></div><span id="17301"></span><div id="comment-17301" class="comment"><div id="post-17301-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Summary of the packet for reference. 0.851093 0.851093 0a.00.0f 0a.00.00 FC 70 [Malformed Packet]</p></blockquote><p>unfortunately that is not enough to troubleshoot the problem. Is it possible to post the <strong>pcap file</strong> somewhere (your web server, google docs, one-click file hoster, <a href="http://cloudshark.org">cloudshark.org</a>)? Beware the privacy issues in doing so!</p></div><div id="comment-17301-info" class="comment-info"><span class="comment-age">(28 Dec '12, 01:37)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17299" class="comment-tools"></div><div class="clear"></div><div id="comment-17299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

