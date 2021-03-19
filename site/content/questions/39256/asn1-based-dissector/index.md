+++
type = "question"
title = "ASN1 based dissector"
description = '''Hi i have to develop a dissecctor similar to 3g/lte protocols. One good thing is i have ASN1 code for the protocols for different layers. i have adaption layer , control layer and connection layer. I have the asn1 file and how to i generate plug in dissector? I have gone through toyasn1 example coul...'''
date = "2015-01-18T17:34:00Z"
lastmod = "2015-01-19T01:29:00Z"
weight = 39256
keywords = [ "asn1" ]
aliases = [ "/questions/39256" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ASN1 based dissector](/questions/39256/asn1-based-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39256-score" class="post-score" title="current number of votes">0</div><span id="post-39256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i have to develop a dissecctor similar to 3g/lte protocols.</p><p>One good thing is i have ASN1 code for the protocols for different layers.</p><p>i have adaption layer , control layer and connection layer. I have the asn1 file and how to i generate plug in dissector?</p><p>I have gone through toyasn1 example could not understand which asn1 file i should put first which one 2nd. and how do i link each other, Anyone help me??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asn1" rel="tag" title="see questions tagged &#39;asn1&#39;">asn1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '15, 17:34</strong></p><img src="https://secure.gravatar.com/avatar/f5d7eabc47e3ec65bf163fde972483d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kuhan&#39;s gravatar image" /><p><span>Kuhan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kuhan has no accepted answers">0%</span></p></div></div><div id="comments-container-39256" class="comments-container"></div><div id="comment-tools-39256" class="comment-tools"></div><div class="clear"></div><div id="comment-39256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39263"></span>

<div id="answer-container-39263" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39263-score" class="post-score" title="current number of votes">0</div><span id="post-39263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure I understand the question. If it's 3 protocols perhaps you should have 3 dissectors? If not look at the other asn1 based dissector. There is plenty of 3gpp specified ones. If your protocol is similary structured. If the specifications are publically available provide a link.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '15, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-39263" class="comments-container"><span id="39265"></span><div id="comment-39265" class="comment"><div id="post-39265-score" class="comment-score"></div><div class="comment-text"><p>hi Anders Thanks for your response. i have 3 different layers physical Layer --&gt; control layer --&gt; Connection Layer --&gt; Adaption layer. If we leave physical layer then i have 3 different ASN1 files. How do i relate these ? as you said if i create seperate dissector for all 3 then how do i connect each other ? its is similar to 3G protocol layers running on top of UDP layer</p></div><div id="comment-39265-info" class="comment-info"><span class="comment-age">(19 Jan '15, 00:14)</span> <span class="comment-user userinfo">Kuhan</span></div></div><span id="39269"></span><div id="comment-39269" class="comment"><div id="post-39269-score" class="comment-score"></div><div class="comment-text"><p>Hard to say without knowing the details of the protocol(s) and how the ASN1 files correlates. But if say the Connection layer has something like AdaptaionLayerData ::= OCTET STRING then you have to use the .cnf to insert code to call the AdaptationLayer Dissector with a tvb containing the "OCTET STRING" that would then be the "entry point" to AdatationLayer.asn1 AplicationLayerMessage ::= SEQUENCE OF ....</p></div><div id="comment-39269-info" class="comment-info"><span class="comment-age">(19 Jan '15, 01:29)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-39263" class="comment-tools"></div><div class="clear"></div><div id="comment-39263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

