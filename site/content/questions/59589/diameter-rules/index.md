+++
type = "question"
title = "Diameter Rules"
description = '''Hi ! I want to colorize (or filter) Diameter packets, specified on AVP Parameter list where VendorID is not Nokia or 3GPP.  I made filter: diameter.avp.vendorId != 94 &amp;amp;&amp;amp; diameter.avp.vendorId != 10415 However, Wireshark still displaying packets where any (or both) AVP&#x27;s are there with those ...'''
date = "2017-02-21T12:38:00Z"
lastmod = "2017-02-21T18:24:00Z"
weight = 59589
keywords = [ "filter", "diameter" ]
aliases = [ "/questions/59589" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Diameter Rules](/questions/59589/diameter-rules)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59589-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi !</p><p>I want to colorize (or filter) Diameter packets, specified on AVP Parameter list where VendorID is not Nokia or 3GPP. I made filter: diameter.avp.vendorId != 94 &amp;&amp; diameter.avp.vendorId != 10415 However, Wireshark still displaying packets where any (or both) AVP's are there with those Vendor Id's, no matter there is no other VendorId's defined in other AVP's.</p><p>What am I doing wrong ?</p></div><div id="question-tags" class="tags-container tags">filter diameter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '17, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/049954c19a42f88823709640897cb958?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahmediukas&#39;s gravatar image" /><p>ahmediukas<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahmediukas has no accepted answers">0%</span></p></div></div><div id="comments-container-59589" class="comments-container"><span id="59590"></span><div id="comment-59590" class="comment"><div id="post-59590-score" class="comment-score"></div><div class="comment-text"><p>So that filter is matching packets that have <em>only</em> Nokia or 3GPP AVPs, with <em>no</em> AVPs from any other vendor?</p></div><div id="comment-59590-info" class="comment-info"><span class="comment-age">(21 Feb '17, 13:15)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-59589" class="comment-tools"></div><div class="clear"></div><div id="comment-59589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59594"></span>

<div id="answer-container-59594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59594-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try: diameter.avp.vendorId&amp;&amp;!diameter.avp.vendorId==94&amp;&amp;!diameter.avp.vendorId==10415</p><p>The problem with your filter is that it reads as "Match if there is a Vendor ID other than 10415, as well as a Vendor ID other than 94". Since 94 is "not 10415" the first condition matches, and since 10415 is "not 94", the second condition matches. Thus, any Diameter message with both ID's will match the rule, even though the rule is negative matches against them both <em>as values</em>.</p><p>It's a common error when writing display filters, which is why most/all Wireshark versions will put that kind of filter in a cautionary yellow background (saying that it is correct syntax, but probably not what you're trying to do). On the other hand the above example says "match if it contains a vendor id, and it does not contain vendor 94, and it does not contain vendor 10415". That sounds like what you're trying to do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '17, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '17, 18:34</p></div></div><div id="comments-container-59594" class="comments-container"><span id="59624"></span><div id="comment-59624" class="comment"><div id="post-59624-score" class="comment-score"></div><div class="comment-text"><p>Not to open new topic, with same parameters, as AVP's are the list, how would you filter then: Diameter must have "ONLY ONE" AVP in the list with id 94 ?</p></div><div id="comment-59624-info" class="comment-info"><span class="comment-age">(22 Feb '17, 15:17)</span> ahmediukas</div></div><span id="59625"></span><div id="comment-59625" class="comment"><div id="post-59625-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>how would you filter than: Diameter must have only one AVP in the list with id 94 ?</p></blockquote><p>That's not supported by the filter expression mechanism.</p></div><div id="comment-59625-info" class="comment-info"><span class="comment-age">(22 Feb '17, 15:20)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-59594" class="comment-tools"></div><div class="clear"></div><div id="comment-59594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

