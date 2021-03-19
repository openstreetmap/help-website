+++
type = "question"
title = "Difference between IMPLICIT and EXPLICIT tags (ASN.1)"
description = '''Can someone explain to me with an example how implicit tagging reduces overhead of number of bytes transfered in ASN.1 ? Thanks.'''
date = "2012-01-08T12:17:00Z"
lastmod = "2012-01-18T09:40:00Z"
weight = 8277
keywords = [ "asn1" ]
aliases = [ "/questions/8277" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between IMPLICIT and EXPLICIT tags (ASN.1)](/questions/8277/difference-between-implicit-and-explicit-tags-asn1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8277-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone explain to me with an example how implicit tagging reduces overhead of number of bytes transfered in ASN.1 ?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">asn1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '12, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/d698b590fa03c946629a0ac3689494b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmalik10&#39;s gravatar image" /><p>mmalik10<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmalik10 has no accepted answers">0%</span></p></div></div><div id="comments-container-8277" class="comments-container"></div><div id="comment-tools-8277" class="comment-tools"></div><div class="clear"></div><div id="comment-8277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8455"></span>

<div id="answer-container-8455" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8455-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When using BER (BASIC ENCODING RULES) or DER (DISTINGUISHED ENCODING RULES), data for types are encoding using a Type-Length-Value format. Each primitive ASN.1 Type such as INTEGER has a UNIVERSAL TAG assigned by the ASN.1 standard. If you have just</p><p>A ::= INTEGER</p><p>This has a tag of UNIVERSAL 2, so an encoding of the interger value 5 in BER would be in hex 02 01 05.</p><p>B ::= [2] IMPLICIT INTEGER</p><p>For B, with an implicit tag, this says to replace the existing tag on INTEGER with [2], so the encoding in BER of the value 5 would be in hex 82 01 05.</p><p>C ::= [2] EXPLICIT INTEGER</p><p>For C, with an explicit tag, this says to add [2] in front of the existing tag, so the encoding in BER of the value 5 would be in hex A2 03 02 01 05.</p><p>There is a free ASN.1 book you can download from <a href="http://www.oss.com/asn1/resources/books-whitepapers-pubs/asn1-books.html">http://www.oss.com/asn1/resources/books-whitepapers-pubs/asn1-books.html</a> which explains tagging in much more detail.</p><p>Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '12, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/d3518c24282d7bd7eb83f7ec4e2e840d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul&#39;s gravatar image" /><p>Paul<br />
<span class="score" title="72 reputation points">72</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul has one accepted answer">33%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jan '12, 10:46</p></div></div><div id="comments-container-8455" class="comments-container"><span id="11449"></span><div id="comment-11449" class="comment"><div id="post-11449-score" class="comment-score"></div><div class="comment-text"><p>which one of the books in that page do you recommend?</p></div><div id="comment-11449-info" class="comment-info"><span class="comment-age">(29 May '12, 09:27)</span> hablutzel1</div></div><span id="11451"></span><div id="comment-11451" class="comment"><div id="post-11451-score" class="comment-score"></div><div class="comment-text"><p>Either of the first two books on that page are excellent. I have heard comments that the first one (by Olivier Dubuisson) might be easier to understand, while others enjoy the British humor punctuating the thorough explanations in the second one (by John Larmouth). Both are excellent resources.</p></div><div id="comment-11451-info" class="comment-info"><span class="comment-age">(29 May '12, 10:03)</span> Paul</div></div></div><div id="comment-tools-8455" class="comment-tools"></div><div class="clear"></div><div id="comment-8455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8296"></span>

<div id="answer-container-8296" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8296-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take this ASN1 description</p><p>Foo SEQUENCE of {</p><p>bar [1] Bar,</p><p>bar2 [2] Bar2 }</p><p>Bar ::= INTEGER</p><p>When EXPLICIT the encoding of the INTEGER type for Bar will be included adding at least 2 bytes, for IMPLICIT only the encoding of the tag will be there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '12, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-8296" class="comments-container"><span id="58131"></span><div id="comment-58131" class="comment"><div id="post-58131-score" class="comment-score"></div><div class="comment-text"><p>the encoding is clear but How decoder knows the real type of ASN.1 data?</p></div><div id="comment-58131-info" class="comment-info"><span class="comment-age">(15 Dec '16, 02:05)</span> IBrahim El-K...</div></div></div><div id="comment-tools-8296" class="comment-tools"></div><div class="clear"></div><div id="comment-8296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

