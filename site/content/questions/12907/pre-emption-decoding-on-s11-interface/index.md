+++
type = "question"
title = "pre-emption decoding on S11 interface"
description = '''Hello, within the Create Session request message on the S11 inteface the wireshark within  Bearer Context IE decodes  Bearer Level Quality of Service (Bearer QoS) in ARP field the wireshark decoded preemption values  .... ...1 = PVI (Pre-emption Vulnerability): Enabled  ..00 01.. = PL (Priority Leve...'''
date = "2012-07-23T01:18:00Z"
lastmod = "2012-07-23T08:46:00Z"
weight = 12907
keywords = [ "preemption" ]
aliases = [ "/questions/12907" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pre-emption decoding on S11 interface](/questions/12907/pre-emption-decoding-on-s11-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12907-score" class="post-score" title="current number of votes">0</div><span id="post-12907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>within the Create Session request message on the S11 inteface the wireshark within Bearer Context IE decodes Bearer Level Quality of Service (Bearer QoS) in ARP field the wireshark decoded preemption values</p><pre><code>        .... ...1 = PVI (Pre-emption Vulnerability): Enabled
        ..00 01.. = PL (Priority Level): 1
        .1.. .... = PCI (Pre-emption Capability): Enabled</code></pre><p>from within the 3GPP a different value seems to be given:</p><p>First 29.274 Section 8.15 Bearer Quality of Service (Bearer QoS) and further reference to Spec 29.212<br />
5.3.46 Pre-emption-Capability AVP PRE-EMPTION_CAPABILITY_ENABLED (0) PRE-EMPTION_CAPABILITY_DISABLED (1)</p><p>5.3.47 Pre-emption-Vulnerability AVP PRE-EMPTION_VULNERABILITY_ENABLED (0) PRE-EMPTION_VULNERABILITY_DISABLED (1)</p><p>So in other words: the wireshark wants to make us believe that value 1 is enabled while the 3GPP states that value 1 is disabled.</p><p>How to explain this mismatch?</p><p>Best regards</p><p>Dieter</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-preemption" rel="tag" title="see questions tagged &#39;preemption&#39;">preemption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '12, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/54bfcbc1e8470a2ea0b8aed6add976e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="demx1874&#39;s gravatar image" /><p><span>demx1874</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="demx1874 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12907" class="comments-container"></div><div id="comment-tools-12907" class="comment-tools"></div><div class="clear"></div><div id="comment-12907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12919"></span>

<div id="answer-container-12919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12919-score" class="post-score" title="current number of votes">1</div><span id="post-12919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A bug in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '12, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-12919" class="comments-container"><span id="12922"></span><div id="comment-12922" class="comment"><div id="post-12922-score" class="comment-score"></div><div class="comment-text"><p>Fixed in <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=43930">http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=43930</a></p></div><div id="comment-12922-info" class="comment-info"><span class="comment-age">(23 Jul '12, 08:46)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-12919" class="comment-tools"></div><div class="clear"></div><div id="comment-12919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

