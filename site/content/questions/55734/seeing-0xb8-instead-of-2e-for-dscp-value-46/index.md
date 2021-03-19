+++
type = "question"
title = "Seeing 0xb8 instead of 2e for dscp value 46"
description = '''Not sure why I would see Differentiated Services Field: 0xb8 I would expect to see Differentiated Services Field: 0x2e if my DSCP value is 46? 0100 .... = Version: 4 .... 0101 = Header Length: 20 bytes (5) Differentiated Services Field: 0xb8 (DSCP: EF PHB, ECN: Not-ECT)  1011 10.. = Differentiated S...'''
date = "2016-09-21T15:11:00Z"
lastmod = "2016-09-21T15:39:00Z"
weight = 55734
keywords = [ "ip.dsfield.dscp" ]
aliases = [ "/questions/55734" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Seeing 0xb8 instead of 2e for dscp value 46](/questions/55734/seeing-0xb8-instead-of-2e-for-dscp-value-46)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55734-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Not sure why I would see Differentiated Services Field: 0xb8 I would expect to see Differentiated Services Field: 0x2e if my DSCP value is 46?</p><pre><code>0100 .... = Version: 4
.... 0101 = Header Length: 20 bytes (5)
Differentiated Services Field: 0xb8 (DSCP: EF PHB, ECN: Not-ECT)
    1011 10.. = Differentiated Services Codepoint: Expedited Forwarding (46)
    .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)</code></pre></div><div id="question-tags" class="tags-container tags">ip.dsfield.dscp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '16, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/314d0fd3405183279133c3d208abe35e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r1limited&#39;s gravatar image" /><p>r1limited<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r1limited has no accepted answers">0%</span></p></div></div><div id="comments-container-55734" class="comments-container"></div><div id="comment-tools-55734" class="comment-tools"></div><div class="clear"></div><div id="comment-55734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55735"></span>

<div id="answer-container-55735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55735-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Differentiated Services field is divided into two subfields: Differentiated Services Codepoint, which takes up 6 bits, and the Explicit Congestion Notification field, which takes the other two bits.</p><p>Yes, in your image, the Differentiated Services Codepoint is binary 101110, which is decimal 46, which would be hex 0x2e. However, the Differentiated Service Field is all 8 bits--the Differentiated Services Codepoint <em>and</em> the Explicit Congestion Notification field.</p><p>The whole thing is 1011 1000, which is decimal 184 and hex 0xb8.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '16, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-55735" class="comments-container"><span id="55736"></span><div id="comment-55736" class="comment"><div id="post-55736-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for that explanation</p></div><div id="comment-55736-info" class="comment-info"><span class="comment-age">(21 Sep '16, 15:41)</span> r1limited</div></div></div><div id="comment-tools-55735" class="comment-tools"></div><div class="clear"></div><div id="comment-55735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

