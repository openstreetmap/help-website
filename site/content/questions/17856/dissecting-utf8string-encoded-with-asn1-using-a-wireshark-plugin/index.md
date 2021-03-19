+++
type = "question"
title = "Dissecting UTF8String encoded with ASN.1 using a Wireshark plugin"
description = '''Hello, community. In Dissecting UTF8String encoded with ASN.1 it was about built-in Wireshark dissectors dissecting UTF6AString values coded in ASN.1. That issue was successfully clarified. But what about plugins. There is a source file ~/plugins/asn1/packet-asn1.c where UTF8String is mentioned but ...'''
date = "2013-01-22T06:29:00Z"
lastmod = "2013-01-22T11:06:00Z"
weight = 17856
keywords = [ "utf8", "dissect", "utf8string", "asn1" ]
aliases = [ "/questions/17856" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting UTF8String encoded with ASN.1 using a Wireshark plugin](/questions/17856/dissecting-utf8string-encoded-with-asn1-using-a-wireshark-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17856-score" class="post-score" title="current number of votes">0</div><span id="post-17856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, community. In <a href="http://ask.wireshark.org/questions/17686">Dissecting UTF8String encoded with ASN.1</a> it was about built-in Wireshark dissectors dissecting UTF6AString values coded in ASN.1. That issue was successfully clarified. But what about plugins. There is a source file ~/plugins/asn1/packet-asn1.c where UTF8String is mentioned but not processed. Is it the file to be worked on?</p><p>BR</p><p>Ewgenij</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-utf8" rel="tag" title="see questions tagged &#39;utf8&#39;">utf8</span> <span class="post-tag tag-link-dissect" rel="tag" title="see questions tagged &#39;dissect&#39;">dissect</span> <span class="post-tag tag-link-utf8string" rel="tag" title="see questions tagged &#39;utf8string&#39;">utf8string</span> <span class="post-tag tag-link-asn1" rel="tag" title="see questions tagged &#39;asn1&#39;">asn1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '13, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/74ba4ba7a26d5efda01b6ae18bbe48e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewgenijkkg&#39;s gravatar image" /><p><span>Ewgenijkkg</span><br />
<span class="score" title="66 reputation points">66</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewgenijkkg has 3 accepted answers">60%</span></p></div></div><div id="comments-container-17856" class="comments-container"></div><div id="comment-tools-17856" class="comment-tools"></div><div class="clear"></div><div id="comment-17856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17863"></span>

<div id="answer-container-17863" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17863-score" class="post-score" title="current number of votes">1</div><span id="post-17863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, that plugin processes asn1 descriptions in some format and dissects according to that I beleve. It is an old not maintained plugin. New ASN1 based dissectors should use asn2wrs and the per/ber dissectors. The needed funktions should be available from plugins too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-17863" class="comments-container"></div><div id="comment-tools-17863" class="comment-tools"></div><div class="clear"></div><div id="comment-17863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

