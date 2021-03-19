+++
type = "question"
title = "Why do I see different data using the same capture file in two places?"
description = '''My partner and I are opening the same capture file without filtering, but we both have different information displayed on the screen. What is happening?'''
date = "2012-06-01T11:50:00Z"
lastmod = "2012-06-01T16:31:00Z"
weight = 11545
keywords = [ "dissection", "results" ]
aliases = [ "/questions/11545" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why do I see different data using the same capture file in two places?](/questions/11545/why-do-i-see-different-data-using-the-same-capture-file-in-two-places)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11545-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My partner and I are opening the same capture file without filtering, but we both have different information displayed on the screen. What is happening?</p></div><div id="question-tags" class="tags-container tags">dissection results</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '12, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/4fbfc9fc0edfc598a3bc1386bf287f2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TecnoSaenz&#39;s gravatar image" /><p>TecnoSaenz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TecnoSaenz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '12, 12:26</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-11545" class="comments-container"><span id="11546"></span><div id="comment-11546" class="comment"><div id="post-11546-score" class="comment-score"></div><div class="comment-text"><p>Are you both using the same version of Wireshark? Are your preferences set the same? What kind of differences are you seeing?</p></div><div id="comment-11546-info" class="comment-info"><span class="comment-age">(01 Jun '12, 12:24)</span> multipleinte...</div></div></div><div id="comment-tools-11545" class="comment-tools"></div><div class="clear"></div><div id="comment-11545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11551"></span>

<div id="answer-container-11551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11551-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are a number of preference settings in Wireshark that can cause the information to be displayed differently. Some of the more common ones are:</p><p>If one of you has network name resolution on and the other one has it off, one of you will see DNS names and the other one will see IP addresses.</p><p>If one of you has transport name resolution on and the other one has it off, one of you will see TCP and UDP port names, the other one will see TCP and UDP port numbers.</p><p>If one of you has MAC name resolution on and the other one has it off, one of you will see the OUI portion of the MAC address as a friendly name, the other one will see only numerical MAC addresses.</p><p>If the two of you have your Time Display Format set differently, you will see different values in the Time column.</p><p>If one of you has added any custom columns, he will see information that the other one does not. If one of you has rearranged your display columns, he will see the information laid out differently.</p><p>If you have different settings for “Allow subdissector to reassemble TCP streams” the information will be presented differently.</p><p>If you have different coloring rules, your packets may be colored differently.</p><p>These are just a few. There are many preferences that can cause information to be displayed differently. If you’re both opening the same capture file, then you should both be seeing the same bits. It’s a matter of how the information is displayed.</p><p>As @multipleinterfaces asked, what differences are you seeing?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '12, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-11551" class="comments-container"></div><div id="comment-tools-11551" class="comment-tools"></div><div class="clear"></div><div id="comment-11551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11557"></span>

<div id="answer-container-11557" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11557-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe your local dns servers resolve ip addresses in the capture file to different names (RFC 1918 addresses). Disable name resolving and compare the results again.</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Name Resolution -&gt; Enable network name resolution</code><br />
</p></blockquote><p>Uncheck that option.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '12, 16:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '12, 16:36</p></div></div><div id="comments-container-11557" class="comments-container"></div><div id="comment-tools-11557" class="comment-tools"></div><div class="clear"></div><div id="comment-11557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

