+++
type = "question"
title = "Finding an easy source of ASN.1 definitions for SULP, LPP, and RRLP to update Wireshark"
description = '''I&#x27;m looking to update the ASN.1 definitions of the SULP, LPP, and RRLP from their respective specifications. However I was wondering if anybody knew of a better source for ASN.1 definitions than the protocol specifications themselves? Copying and pasting from PDF files would be rather tedious.'''
date = "2013-06-26T08:23:00Z"
lastmod = "2013-06-27T18:31:00Z"
weight = 22363
keywords = [ "rrlp", "lpp", "sulp", "asn1" ]
aliases = [ "/questions/22363" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Finding an easy source of ASN.1 definitions for SULP, LPP, and RRLP to update Wireshark](/questions/22363/finding-an-easy-source-of-asn1-definitions-for-sulp-lpp-and-rrlp-to-update-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22363-score" class="post-score" title="current number of votes">0</div><span id="post-22363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking to update the ASN.1 definitions of the SULP, LPP, and RRLP from their respective specifications. However I was wondering if anybody knew of a better source for ASN.1 definitions than the protocol specifications themselves? Copying and pasting from PDF files would be rather tedious.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rrlp" rel="tag" title="see questions tagged &#39;rrlp&#39;">rrlp</span> <span class="post-tag tag-link-lpp" rel="tag" title="see questions tagged &#39;lpp&#39;">lpp</span> <span class="post-tag tag-link-sulp" rel="tag" title="see questions tagged &#39;sulp&#39;">sulp</span> <span class="post-tag tag-link-asn1" rel="tag" title="see questions tagged &#39;asn1&#39;">asn1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '13, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/8625d84693a5ea5a99823fddd974ca00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FComstock&#39;s gravatar image" /><p><span>FComstock</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FComstock has no accepted answers">0%</span></p></div></div><div id="comments-container-22363" class="comments-container"></div><div id="comment-tools-22363" class="comment-tools"></div><div class="clear"></div><div id="comment-22363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22367"></span>

<div id="answer-container-22367" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22367-score" class="post-score" title="current number of votes">1</div><span id="post-22367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, I am not aware of a source for these ASN.1 modules in text format. You can, however copy all of the text from the PDF into a Word file in .doc (not .docx) format, and can then use the OSS ASN.1 Studio (available from link:<a href="http://www.oss.com">OSS Nokalva</a>) to import the ASN.1 modules from the Word file. This will likely be much easier than going through and trying to copy/paste each of the ASN.1 modules yourself.</p><p>Unfortunately, ETSI and 3GPP do not seem to provide an equivalent of the ITU-T ASN.1 Module Database where you can find all of the ASN.1 modules from ITU-T Recommendations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '13, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/d3518c24282d7bd7eb83f7ec4e2e840d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul&#39;s gravatar image" /><p><span>Paul</span><br />
<span class="score" title="72 reputation points">72</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul has one accepted answer">33%</span></p></div></div><div id="comments-container-22367" class="comments-container"></div><div id="comment-tools-22367" class="comment-tools"></div><div class="clear"></div><div id="comment-22367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22431"></span>

<div id="answer-container-22431" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22431-score" class="post-score" title="current number of votes">1</div><span id="post-22431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can the platform vendor provide them for you? I don't know of a centralized source for ASN.1 definition files in text form, though to save you some typing I would think the platform vendor should be able to provide this. I've also been able to google some ASN.1 decoders in the past which also included the text definition files for some of the major vendors (Nokia, Ericsson), though I don't remember ever finding any for the mobile positioning platforms (CDRs mostly).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '13, 18:31</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jun '13, 18:32</strong> </span></p></div></div><div id="comments-container-22431" class="comments-container"></div><div id="comment-tools-22431" class="comment-tools"></div><div class="clear"></div><div id="comment-22431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

