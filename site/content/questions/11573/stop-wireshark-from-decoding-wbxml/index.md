+++
type = "question"
title = "Stop wireshark from decoding wbxml?"
description = '''How do I stop wireshark from attempt to decode wbxml? I want also to be able to see the actual binary data! Also wireshark cannot decode wbxml properly!'''
date = "2012-06-02T16:02:00Z"
lastmod = "2012-06-02T16:43:00Z"
weight = 11573
keywords = [ "decode", "wbxml" ]
aliases = [ "/questions/11573" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Stop wireshark from decoding wbxml?](/questions/11573/stop-wireshark-from-decoding-wbxml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11573-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I stop wireshark from attempt to decode wbxml? I want also to be able to see the actual binary data! Also wireshark cannot decode wbxml properly!</p></div><div id="question-tags" class="tags-container tags">decode wbxml</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '12, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/a810951ad814dab92776baaac095f883?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dakke&#39;s gravatar image" /><p>dakke<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dakke has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jun '12, 21:17</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-11573" class="comments-container"></div><div id="comment-tools-11573" class="comment-tools"></div><div class="clear"></div><div id="comment-11573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11574"></span>

<div id="answer-container-11574" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11574-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Disable wbxml in the GUI:</p><blockquote><p><code>Analyze -&gt; Enabled Protocols -&gt; uncheck the Status for WBXML</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '12, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-11574" class="comments-container"><span id="11577"></span><div id="comment-11577" class="comment"><div id="post-11577-score" class="comment-score"></div><div class="comment-text"><p>...and then submit a bug report with sample capture file so wbxml dissection can hopefully be fixed.</p></div><div id="comment-11577-info" class="comment-info"><span class="comment-age">(02 Jun '12, 21:16)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-11574" class="comment-tools"></div><div class="clear"></div><div id="comment-11574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11575"></span>

<div id="answer-container-11575" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11575-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can always see the undecoded data in the Packet Bytes pane. It will be represented in hexadecimal, not binary, on the left side of the pane, and ASCII to the right.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '12, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-11575" class="comments-container"><span id="11582"></span><div id="comment-11582" class="comment"><div id="post-11582-score" class="comment-score"></div><div class="comment-text"><p>Okay thank you for the answers! I was thinking that the hexadecimal representation could but used but it was far to short to make any sense.</p><p>I released now that the content was gziped from 142 bytes into 15bytes. There is an "Uncompressed entity body(15 bytes)" tab. But since it is 15bytes it must still be compressed? Now how do I decompress gzip?</p></div><div id="comment-11582-info" class="comment-info"><span class="comment-age">(03 Jun '12, 08:58)</span> dakke</div></div><span id="11584"></span><div id="comment-11584" class="comment"><div id="post-11584-score" class="comment-score"></div><div class="comment-text"><p>Nvm I think I found non-gziped data: I assume it is the last 142 bytes in the frame.</p></div><div id="comment-11584-info" class="comment-info"><span class="comment-age">(03 Jun '12, 09:35)</span> dakke</div></div></div><div id="comment-tools-11575" class="comment-tools"></div><div class="clear"></div><div id="comment-11575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

