+++
type = "question"
title = "tshark fields"
description = '''I am using tshark to see some packets, but when I user the -T fields -e xxxx, I don&#x27;t see a number instead of the actual meaning, is there an option I should put to be albe to see the field name and not the number For example I am looking at SGs failure, instead of seeing sgsap.msg_type as &quot;SGsAP-PA...'''
date = "2015-04-14T12:29:00Z"
lastmod = "2015-04-15T02:32:00Z"
weight = 41439
keywords = [ "fields", "tshark", "name" ]
aliases = [ "/questions/41439" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark fields](/questions/41439/tshark-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41439-score" class="post-score" title="current number of votes">0</div><span id="post-41439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using tshark to see some packets, but when I user the -T fields -e xxxx, I don't see a number instead of the actual meaning, is there an option I should put to be albe to see the field name and not the number For example I am looking at SGs failure, instead of seeing sgsap.msg_type as "SGsAP-PAGING-REJECT", I see sgsap.msg_type "2", If I use tshark -r file.pcap, I am going to see the output as I see it in wireshark with the names</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '15, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/6405df934432bb5e3c624ba812de640e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alfromero&#39;s gravatar image" /><p><span>alfromero</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alfromero has no accepted answers">0%</span></p></div></div><div id="comments-container-41439" class="comments-container"></div><div id="comment-tools-41439" class="comment-tools"></div><div class="clear"></div><div id="comment-41439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41445"></span>

<div id="answer-container-41445" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41445-score" class="post-score" title="current number of votes">1</div><span id="post-41445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tshark <strong>-T fields -e xxx</strong> prints the <strong>raw values</strong> and there is no way to get the "text representation" of those values without a code change.</p><p>So, what you can do it to run the following command and then parse the output with a script:</p><blockquote><p>tshrak -V -r input.pcap</p></blockquote><p>Sample Output:</p><pre><code>SGs Application Part (SGsAP)
    SGSAP Message Type: SGsAP-LOCATION-UPDATE-REQUEST (0x09)    &lt;&lt;&lt;======= HERE !!!
    IMSI - IMSI (310444001001001)
        Element ID: 0x01
        Length: 8
        0011 .... = Identity Digit 1: 3
        .... 1... = Odd/even indication: Odd number of identity digits
        .... .001 = Mobile Identity Type: IMSI (1)
        BCD Digits: 310444001001001
    MME name - mmec01.mmegi9900.mme.epc.mnc012.mcc310.3gppnetwork.org
        Element ID: 0x09
        Length: 55
        MME name: mmec01.mmegi9900.mme.epc.mnc012.mcc310.3gppnetwork.org
    EPS location update type - IMSI attach
        Element ID: 0x0a
        Length: 1
        EPS location update type: IMSI attach (1)</code></pre><p>As an alternative, you can also run this command to get more structured output</p><blockquote><p>tshrak -r input.pcap -T pdml</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '15, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41445" class="comments-container"></div><div id="comment-tools-41445" class="comment-tools"></div><div class="clear"></div><div id="comment-41445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

