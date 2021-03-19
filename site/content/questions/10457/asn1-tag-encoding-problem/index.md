+++
type = "question"
title = "ASN.1 Tag Encoding Problem"
description = '''Hello, I have an application that uses ASN.1 ber to encode its data to transmit. One particular field encodes an OCTET STRING, and uses an implicit application tag. The hex bytes are these: 5F 01 04 .. .. .. .. Where 0x5F01 is the tag and 0x04 the length. This encodes the APPLICATION type, with a ta...'''
date = "2012-04-26T02:38:00Z"
lastmod = "2012-04-27T03:53:00Z"
weight = 10457
keywords = [ "asn.1", "datatypes", "format", "asn1" ]
aliases = [ "/questions/10457" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [ASN.1 Tag Encoding Problem](/questions/10457/asn1-tag-encoding-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10457-score" class="post-score" title="current number of votes">1</div><span id="post-10457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have an application that uses ASN.1 ber to encode its data to transmit. One particular field encodes an OCTET STRING, and uses an implicit application tag. The hex bytes are these:</p><p>5F 01 04 .. .. .. ..</p><p>Where 0x5F01 is the tag and 0x04 the length. This encodes the APPLICATION type, with a tag number of 1. However, an APPLICATION type with tag number of 1 should (AFAIK) encodes as 0x41. I.e. this data file is encoding the tag number 1 in a high-tag-number form I thought was reserved for tag numbers of &gt;30.</p><p>Is this a violation of ASN.1 standard?</p><p>I'm trying to write the ASN.1 syntax to describe this data, and so far have this:</p><p>version [APPLICATION 1] IMPLICIT OCTET STRING SIZE(4)</p><p>but this will always produce 0x41 as the tag. I need 0x5F01. Is there any modifier I can use to force high-tag-number form? Unfortunately, I have no control over the file data format.</p><p>Thanks for any help</p><p>Regards Rob Smith</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asn.1" rel="tag" title="see questions tagged &#39;asn.1&#39;">asn.1</span> <span class="post-tag tag-link-datatypes" rel="tag" title="see questions tagged &#39;datatypes&#39;">datatypes</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span> <span class="post-tag tag-link-asn1" rel="tag" title="see questions tagged &#39;asn1&#39;">asn1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '12, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/e02eb1d578b44d1506bd1db73e0faa4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="salukibob&#39;s gravatar image" /><p><span>salukibob</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="salukibob has no accepted answers">0%</span></p></div></div><div id="comments-container-10457" class="comments-container"></div><div id="comment-tools-10457" class="comment-tools"></div><div class="clear"></div><div id="comment-10457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10465"></span>

<div id="answer-container-10465" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10465-score" class="post-score" title="current number of votes">1</div><span id="post-10465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="salukibob has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The tag 5F01 is [APPLICATION 1] but should be encoded in one octet instead of 2 since the value is between zero and 30 (inclusive) as indicated in X.690 clause 8.1.2.2. Note that some tools (such as the one from OSS Nokalva - <a href="http://www.oss.com">www.oss.com</a>) have a runtime flag for relaxing the strict rule checking thus allowing you to decode messages with tags like this that deviate slightly from the specified rules.</p><p>If you are able to have the encoder that generated those encodings corrected, that would be ideal, but if not, you could consider an ASN.1 tool such as the one from OSS Nokalva that is able to handle this kind of deviation from the strict ASN.1 rules.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '12, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/d3518c24282d7bd7eb83f7ec4e2e840d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul&#39;s gravatar image" /><p><span>Paul</span><br />
<span class="score" title="72 reputation points">72</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul has one accepted answer">33%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Apr '12, 11:27</strong> </span></p></div></div><div id="comments-container-10465" class="comments-container"></div><div id="comment-tools-10465" class="comment-tools"></div><div class="clear"></div><div id="comment-10465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10459"></span>

<div id="answer-container-10459" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10459-score" class="post-score" title="current number of votes">1</div><span id="post-10459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Although the encoding is correct, X.690 clause 8.1.2.2 says "the identifier octets shall comprise of a single octet..." so the encoder breaks that rule.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '12, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-10459" class="comments-container"><span id="10474"></span><div id="comment-10474" class="comment"><div id="post-10474-score" class="comment-score"></div><div class="comment-text"><p>I did suspect that the encoder was breaking the rules slightly. Unfortunately I have no control over its output.</p><p>Luckily the decoder I am using accepts it, so must not enforce the X.690 rules quite so strictly. I do however need to re-encode data back into this format, so I was hoping that the basic ASN.1 syntax would have a modifier to allow this. Nevermind. Looks like an ugly hack will be necessary!</p><p>Thanks for your comments.</p></div><div id="comment-10474-info" class="comment-info"><span class="comment-age">(27 Apr '12, 03:53)</span> <span class="comment-user userinfo">salukibob</span></div></div></div><div id="comment-tools-10459" class="comment-tools"></div><div class="clear"></div><div id="comment-10459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

