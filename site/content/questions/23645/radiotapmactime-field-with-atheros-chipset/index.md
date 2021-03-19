+++
type = "question"
title = "radiotap.mactime field with Atheros chipset"
description = '''Hi everybody I try to get the radiotap.mactime field from WiFi dongle with Atheros chipset.  With any Atheros based device, I get an empty field, while I get the correct value with a Broadcam chipset. I&#x27;m on Linux (Ubuntu 12.4) and I tried all what I could to get this data available to tshark (drive...'''
date = "2013-08-08T06:59:00Z"
lastmod = "2014-01-08T11:57:00Z"
weight = 23645
keywords = [ "mactime", "radiotap" ]
aliases = [ "/questions/23645" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [radiotap.mactime field with Atheros chipset](/questions/23645/radiotapmactime-field-with-atheros-chipset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23645-score" class="post-score" title="current number of votes">0</div><span id="post-23645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody I try to get the radiotap.mactime field from WiFi dongle with Atheros chipset. With any Atheros based device, I get an empty field, while I get the correct value with a Broadcam chipset. I'm on Linux (Ubuntu 12.4) and I tried all what I could to get this data available to tshark (drivers and firmware are up to date)</p><p>Any hints from you guys on this ?</p><p>BR</p><p>Olivier.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mactime" rel="tag" title="see questions tagged &#39;mactime&#39;">mactime</span> <span class="post-tag tag-link-radiotap" rel="tag" title="see questions tagged &#39;radiotap&#39;">radiotap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '13, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/cbff72dfe128ae463d35e847c1e5ff46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="omarce&#39;s gravatar image" /><p><span>omarce</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="omarce has no accepted answers">0%</span></p></div></div><div id="comments-container-23645" class="comments-container"><span id="23662"></span><div id="comment-23662" class="comment"><div id="post-23662-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I get an empty field</p></blockquote><p>Empty in what sense? Not present at all, or present but with a bogus value (e.g., always zero)?</p></div><div id="comment-23662-info" class="comment-info"><span class="comment-age">(08 Aug '13, 15:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-23645" class="comment-tools"></div><div class="clear"></div><div id="comment-23645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23669"></span>

<div id="answer-container-23669" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23669-score" class="post-score" title="current number of votes">0</div><span id="post-23669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Guy, the field no present at all. Meanwhile, I found the reason. When looking at radiotap.tsft.present it returns false, so it was normal that mactime was empty.</p><p>The reason was that I used a USB device with an old Atheros chipset, and the associated driver was carl9170 and not ath9k_htc. carl9170 seems not able to reporting mactime.</p><p>I was confused by the fact that I had several dongle, then several drivers loaded.</p><p>BTW I think that it would be better for tshark to return an non empty char string (like "none") rather than an empty string.</p><p>Regards</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '13, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/cbff72dfe128ae463d35e847c1e5ff46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="omarce&#39;s gravatar image" /><p><span>omarce</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="omarce has no accepted answers">0%</span></p></div></div><div id="comments-container-23669" class="comments-container"><span id="23683"></span><div id="comment-23683" class="comment"><div id="post-23683-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I think that it would be better for tshark to return an non empty char string (like "none") rather than an empty string</p></blockquote><p>File a bug on that if you want it changed, but be prepared for other users to say they prefer nothing to be reported for absent fields.</p></div><div id="comment-23683-info" class="comment-info"><span class="comment-age">(09 Aug '13, 12:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="28687"></span><div id="comment-28687" class="comment"><div id="post-28687-score" class="comment-score"></div><div class="comment-text"><p>Hi Olivier,</p><p>Cna you please share both the wireless adapters (Broadcom and Atheros) used that eventually reported the radiotap.mactime ?</p><p>I am facing similar problem when I try with Dlink DWA-160-RevA2 card that AR9170.</p><p>Thanks, Sudheer</p></div><div id="comment-28687-info" class="comment-info"><span class="comment-age">(08 Jan '14, 11:57)</span> <span class="comment-user userinfo">Sudheer</span></div></div></div><div id="comment-tools-23669" class="comment-tools"></div><div class="clear"></div><div id="comment-23669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

