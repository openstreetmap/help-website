+++
type = "question"
title = "Need to filter based on &quot;InDiscards&quot;"
description = '''Not having any luck trying to filter my capture down to InDiscards. I&#x27;m getting a lot of InDiscards on my Cisco 5505. I enabled port mirroring and ran the capture. Any tips on how to find InDiscards in wireshark?'''
date = "2015-02-20T11:07:00Z"
lastmod = "2015-02-20T16:00:00Z"
weight = 39987
keywords = [ "discards", "indiscards" ]
aliases = [ "/questions/39987" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need to filter based on "InDiscards"](/questions/39987/need-to-filter-based-on-indiscards)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39987-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Not having any luck trying to filter my capture down to InDiscards. I'm getting a lot of InDiscards on my Cisco 5505. I enabled port mirroring and ran the capture.</p><p>Any tips on how to find InDiscards in wireshark?</p></div><div id="question-tags" class="tags-container tags">discards indiscards</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '15, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/2ad9a969da92f606c1a74342548adf47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ParseMeHard&#39;s gravatar image" /><p>ParseMeHard<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ParseMeHard has no accepted answers">0%</span></p></div></div><div id="comments-container-39987" class="comments-container"></div><div id="comment-tools-39987" class="comment-tools"></div><div class="clear"></div><div id="comment-39987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39996"></span>

<div id="answer-container-39996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39996-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will not be able to filter on In-Discards in Wireshark. In-Discards are valid inbound frames that are discarded by the switch because they do not need to be switched. See <a href="http://www.cisco.com/c/en/us/support/docs/switches/catalyst-6500-series-switches/12027-53.html">this web page</a> for an explanation, including why In-Discards are not always a problem. (It's for a Catalyst 6500 series switch, but the principle is the same.) The discarded frames may or may not be in your capture, depending on where your capture point is.</p><p>You said you enabled port mirroring. If the port you mirrored <em>would have been</em> the egress port for the discarded frames, then they will not be in your capture because they will have been discarded at the ingress port. If the port you mirrored is the ingress port for those frames, then it depends on whether the Cisco switch performs the mirroring function before or after the discard function.</p><p>In-Discard is an action taken by the switch, not an attribute of the frame, which is why you can't identify or filter on them in Wireshark. Even if these frames are in your capture, because they haven't been discarded yet, there is nothing in the frame that tells you that the frame is going to eventually be discarded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '15, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Feb '15, 16:05</p></div></div><div id="comments-container-39996" class="comments-container"></div><div id="comment-tools-39996" class="comment-tools"></div><div class="clear"></div><div id="comment-39996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

