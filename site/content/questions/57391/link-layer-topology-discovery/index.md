+++
type = "question"
title = "Link Layer Topology Discovery"
description = '''Im New to wireshark and new to networking. Im trying to solve a issue with our phones, everyday at 5:30pm our phones loose connection. While exploring wireshark I found my first error and was hoping someone here can explain to me what I am reading It seems like for my Netgear switch there is a Link ...'''
date = "2016-11-15T07:41:00Z"
lastmod = "2016-11-16T00:20:00Z"
weight = 57391
keywords = [ "wireshark" ]
aliases = [ "/questions/57391" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Link Layer Topology Discovery](/questions/57391/link-layer-topology-discovery)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57391-score" class="post-score" title="current number of votes">0</div><span id="post-57391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im New to wireshark and new to networking. Im trying to solve a issue with our phones, everyday at 5:30pm our phones loose connection. While exploring wireshark I found my first error and was hoping someone here can explain to me what I am reading</p><p>It seems like for my Netgear switch there is a Link Layer Topology Discovery error, or its highlighted in red. Under that TLVs than TLV ITem (Friendly Name) than finally this error.</p><p>[Expert Info (Error/Malformed) : Invalid Friendly Name length] <strong><em><a href="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-11-15_at_8.40.09_AM.png">screen shot</a></em></strong> Any Help explaining what this is?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '16, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/f9529cb2f323c7df6b01cd2fd670b5a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adandy&#39;s gravatar image" /><p><span>adandy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adandy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Nov '16, 07:42</strong> </span></p></div></div><div id="comments-container-57391" class="comments-container"><span id="57392"></span><div id="comment-57392" class="comment"><div id="post-57392-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-57392-info" class="comment-info"><span class="comment-age">(15 Nov '16, 08:36)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-57391" class="comment-tools"></div><div class="clear"></div><div id="comment-57391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57403"></span>

<div id="answer-container-57403" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57403-score" class="post-score" title="current number of votes">1</div><span id="post-57403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like some incomplete work in the dissector or maybe a different implementation of the LLTP protocol. In the source code of the dissector I find:</p><pre><code>case 0x11: /* Friendly Name */
    if (length != 0)
        expert_add_info_format(pinfo, tlv_item, &amp;ei_lltd_tlv_length_invalid, &quot;Invalid Friendly Name length&quot;);
    break;</code></pre><p>Which means, the length of the Friendly Name should be 0, which kind of contradicts the reason for having a Friendly Name TLV. My best guess is that this field was not used in the test data that was used to create the dissector but is indeed used by your netgear device. Could you add a bug-report to <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and attach a little tracefile with this packet in it to the bug-report?</p><p>Unfortunately, I'm afraid this brings you no closer to finding the source of your VoIP problems...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '16, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-57403" class="comments-container"></div><div id="comment-tools-57403" class="comment-tools"></div><div class="clear"></div><div id="comment-57403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

