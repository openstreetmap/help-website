+++
type = "question"
title = "NAS Tracking Area Identity List not properly dissected"
description = '''Hi, I am sending Tracking Area Identity List IE with multiple Partial Tracking Area Identity List in NAS Attach Accept message. Wireshark is decoding only first Partial Tracking Area Identity List and showing Extraneous data for rest of the Partial Lists. Kindly provide your inputs.'''
date = "2016-08-18T09:57:00Z"
lastmod = "2016-08-18T10:51:00Z"
weight = 54955
keywords = [ "nas" ]
aliases = [ "/questions/54955" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [NAS Tracking Area Identity List not properly dissected](/questions/54955/nas-tracking-area-identity-list-not-properly-dissected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54955-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am sending Tracking Area Identity List IE with multiple Partial Tracking Area Identity List in NAS Attach Accept message. Wireshark is decoding only first Partial Tracking Area Identity List and showing Extraneous data for rest of the Partial Lists. Kindly provide your inputs.</p></div><div id="question-tags" class="tags-container tags">nas</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '16, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/6a1bfed0a10314b121f5edde7049a2b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="waniakshay&#39;s gravatar image" /><p>waniakshay<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="waniakshay has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Aug '16, 08:49</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54955" class="comments-container"></div><div id="comment-tools-54955" class="comment-tools"></div><div class="clear"></div><div id="comment-54955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54958"></span>

<div id="answer-container-54958" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54958-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a bug in Wireshark.</p><p>I have a <a href="https://code.wireshark.org/review/#/c/17151/">fix for this</a>, but it would be great if you could share your NAS Attach Accept message so that I can test my patch.</p><p>Edit: the fix is now merged and will be part of Wireshark 2.0.6 and 2.2 when they will be released. You can also grab an automated nightly build. It would still be useful that you share an example or test the fix and report that it works as expected now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '16, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Aug '16, 23:45</p></div></div><div id="comments-container-54958" class="comments-container"><span id="54968"></span><div id="comment-54968" class="comment"><div id="post-54968-score" class="comment-score"></div><div class="comment-text"><p>Please find below the hex dump of Attach Accept message -</p><p>0000 27 d1 c6 3e 2e 01 07 42 01 24 0e 22 00 f1 10 31 0010 32 01 00 f1 10 00 64 2b 6a 00 2a 52 01 c1 01 05 0020 05 04 61 70 6e 31 05 01 c0 10 00 0f 5d 01 00 30 0030 10 0b 52 1f 73 8c fe 56 76 4b 56 56 00 6c 00 6c 0040 00 5e 02 01 01 50 0b f6 00 f1 10 00 02 01 00 00 0050 00 1e 53 12 17 22</p><p>Please let me know if it works. Thanks.</p></div><div id="comment-54968-info" class="comment-info"><span class="comment-age">(18 Aug '16, 23:47)</span> waniakshay</div></div><span id="54971"></span><div id="comment-54971" class="comment"><div id="post-54971-score" class="comment-score"></div><div class="comment-text"><p>Tested with latest automated build. It works perfectly. Thanks a lot.</p></div><div id="comment-54971-info" class="comment-info"><span class="comment-age">(19 Aug '16, 02:17)</span> waniakshay</div></div><span id="54980"></span><div id="comment-54980" class="comment"><div id="post-54980-score" class="comment-score"></div><div class="comment-text"><p>Thanks for confirming. If my answer solved your issue, please consider accepting it by clicking on the check mark next to the answer.</p></div><div id="comment-54980-info" class="comment-info"><span class="comment-age">(19 Aug '16, 08:25)</span> Pascal Quantin</div></div></div><div id="comment-tools-54958" class="comment-tools"></div><div class="clear"></div><div id="comment-54958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

