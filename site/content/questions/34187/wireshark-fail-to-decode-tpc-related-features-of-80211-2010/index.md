+++
type = "question"
title = "Wireshark fail to decode TPC related features of 802.11-2010"
description = ''' Please see the above image. Wireshark can&#x27;t decode power control related tags of IEEE802.11-2012 . I am using Wireshark Version 1.10.8 (v1.10.8-2-g52a5244 from master-1.10). '''
date = "2014-06-25T12:41:00Z"
lastmod = "2014-06-25T18:59:00Z"
weight = 34187
keywords = [ "802.11" ]
aliases = [ "/questions/34187" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark fail to decode TPC related features of 802.11-2010](/questions/34187/wireshark-fail-to-decode-tpc-related-features-of-80211-2010)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34187-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://imgur.com/XdNuzKg" alt="alt text" /></p><p>Please see the above image. Wireshark can't decode power control related tags of IEEE802.11-2012 . I am using Wireshark Version 1.10.8 (v1.10.8-2-g52a5244 from master-1.10).</p></div><div id="question-tags" class="tags-container tags">802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '14, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/c30247a32173ffc150dbb96e9e3e8d9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CHANDRA&#39;s gravatar image" /><p>CHANDRA<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CHANDRA has no accepted answers">0%</span></p></img></div></div><div id="comments-container-34187" class="comments-container"><span id="34188"></span><div id="comment-34188" class="comment"><div id="post-34188-score" class="comment-score"></div><div class="comment-text"><p>Here is link for the image mentioned in question</p><p><a href="http://imgur.com/XdNuzKg">http://imgur.com/XdNuzKg</a></p></div><div id="comment-34188-info" class="comment-info"><span class="comment-age">(25 Jun '14, 12:45)</span> CHANDRA</div></div></div><div id="comment-tools-34187" class="comment-tools"></div><div class="clear"></div><div id="comment-34187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34201"></span>

<div id="answer-container-34201" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34201-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 802.11 dissector is probably assuming that the tag in question is an "old-style" version, and needs to be updated to handle longer tags. Please file a bug report on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>; please attach the image and, if possible, a capture file with those tags.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 18:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34201" class="comments-container"></div><div id="comment-tools-34201" class="comment-tools"></div><div class="clear"></div><div id="comment-34201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

