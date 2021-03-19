+++
type = "question"
title = "SCCP Called Party&#x27;s Address Indicator is being parsed incorrectly"
description = '''Bit no. 1 of the Address Indicator field - according to RFC 3868 - is the SSN Indicator bit. However, Wireshark version 1.10.8 is looking at bit 2 as the SSN Indicator bit - bit 2 is actually the Point Code Indicator bit. By looking at the wrong bit, Wireshark fails to parse the remaining encapsulat...'''
date = "2014-06-25T10:36:00Z"
lastmod = "2014-06-25T17:42:00Z"
weight = 34183
keywords = [ "ssn", "sccp" ]
aliases = [ "/questions/34183" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [SCCP Called Party's Address Indicator is being parsed incorrectly](/questions/34183/sccp-called-partys-address-indicator-is-being-parsed-incorrectly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34183-score" class="post-score" title="current number of votes">0</div><span id="post-34183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Bit no. 1 of the Address Indicator field - according to RFC 3868 - is the SSN Indicator bit. However, Wireshark version 1.10.8 is looking at bit 2 as the SSN Indicator bit - bit 2 is actually the Point Code Indicator bit. By looking at the wrong bit, Wireshark fails to parse the remaining encapsulated data.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssn" rel="tag" title="see questions tagged &#39;ssn&#39;">ssn</span> <span class="post-tag tag-link-sccp" rel="tag" title="see questions tagged &#39;sccp&#39;">sccp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '14, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/7ce6ff64276001746b07675e5f4b728f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave%20S&#39;s gravatar image" /><p><span>Dave S</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave S has no accepted answers">0%</span></p></div></div><div id="comments-container-34183" class="comments-container"></div><div id="comment-tools-34183" class="comment-tools"></div><div class="clear"></div><div id="comment-34183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="34189"></span>

<div id="answer-container-34189" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34189-score" class="post-score" title="current number of votes">0</div><span id="post-34189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you talking about SCCP or SUA (RFC 3868)? They are different.</p><p>I'm guessing you're talking about SCCP in which case the answer is that which bit is the SSN-indicator and which is the PC-indicator are different depending on the MTP3 standard you're using. Check the MTP3 preferences and choose the ITU, ANSI, China, or Japan variant. Or try the "determine the standard heuristically" checkbox.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-34189" class="comments-container"></div><div id="comment-tools-34189" class="comment-tools"></div><div class="clear"></div><div id="comment-34189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34191"></span>

<div id="answer-container-34191" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34191-score" class="post-score" title="current number of votes">0</div><span id="post-34191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The bit used for SSN depends on the MTP3 standard configured in the dissector. Did you try switching the configuration between ANSI and ITU?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-34191" class="comments-container"></div><div id="comment-tools-34191" class="comment-tools"></div><div class="clear"></div><div id="comment-34191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34197"></span>

<div id="answer-container-34197" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34197-score" class="post-score" title="current number of votes">0</div><span id="post-34197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As others indicated, by far the most common problem when you see this type of decoding error in Wireshark for any SS7-based protocol is that MTP3 standards differ.</p><p>Go to Edit &gt; Preferences &gt; Protocols &gt; MTP3. From there confirm the MTP3 standard in use and hit OK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 17:42</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jun '14, 17:43</strong> </span></p></div></div><div id="comments-container-34197" class="comments-container"></div><div id="comment-tools-34197" class="comment-tools"></div><div class="clear"></div><div id="comment-34197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

