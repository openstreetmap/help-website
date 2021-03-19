+++
type = "question"
title = "Decode for LLTD?"
description = '''LLTD is the Link Layer Topology Discovery introduced by Microsoft with Windows Vista. As of now Wireshark recognizes LLTD frames by Ethertype but does not decode the content. Wiki provides a link to a dissector. What are the chances of getting the LLTD dissector into the standard Wireshark build?'''
date = "2011-04-18T02:24:00Z"
lastmod = "2011-04-18T07:45:00Z"
weight = 3552
keywords = [ "windows", "lltd" ]
aliases = [ "/questions/3552" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Decode for LLTD?](/questions/3552/decode-for-lltd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3552-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>LLTD is the Link Layer Topology Discovery introduced by Microsoft with Windows Vista.</p><p>As of now Wireshark recognizes LLTD frames by Ethertype but does not decode the content.</p><p>Wiki provides a link to a dissector. What are the chances of getting the LLTD dissector into the standard Wireshark build?</p></div><div id="question-tags" class="tags-container tags">windows lltd</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-3552" class="comments-container"></div><div id="comment-tools-3552" class="comment-tools"></div><div class="clear"></div><div id="comment-3552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3566"></span>

<div id="answer-container-3566" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3566-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably, the <a href="http://wiki.wireshark.org/MS-LLTD">MS-LLTD</a> wiki page is the one you're referring to. The link from that page to the dissector indicates that it was developed against 1.0.4, so in all likelihood some changes would be needed before it could be incorporated. So I'd say the first step would be for someone to update the dissector to build against the trunk. After that, an enhancement bug request should be filed at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a> with the updated dissector attached.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3566" class="comments-container"><span id="59515"></span><div id="comment-59515" class="comment"><div id="post-59515-score" class="comment-score"></div><div class="comment-text"><p>I just realized that Wireshark is doing a great job on decoding LLTD.</p><p>Closing the question is overdue.</p><p>Thank you to all developers for keeping Wireshark great :)</p></div><div id="comment-59515-info" class="comment-info"><span class="comment-age">(17 Feb '17, 12:13)</span> packethunter</div></div></div><div id="comment-tools-3566" class="comment-tools"></div><div class="clear"></div><div id="comment-3566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

