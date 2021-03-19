+++
type = "question"
title = "Decode EtherType as 6LoWPAN"
description = '''Hi, I&#x27;m currently implementing this Internet draft which allows for sending 6LoWPAN frames over an Ethernet connection (which can be kind of useful for debugging your embedded software using a local TAP ;-)). Since there is no Ethertype for this yet, I used a random one that isn&#x27;t assigned yet (0x87...'''
date = "2016-09-29T05:01:00Z"
lastmod = "2016-09-29T07:24:00Z"
weight = 55984
keywords = [ "decode_as", "ethertype", "6lowpan" ]
aliases = [ "/questions/55984" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode EtherType as 6LoWPAN](/questions/55984/decode-ethertype-as-6lowpan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm currently implementing <a href="https://tools.ietf.org/html/draft-ietf-6lo-ethertype-request-01">this Internet draft</a> which allows for sending 6LoWPAN frames over an Ethernet connection (which can be kind of useful for debugging your embedded software using a local TAP ;-)). Since there is no Ethertype for this yet, I used a random one that isn't assigned yet (<code>0x87dd</code>) in the hopes I could just use the <code>Decode as...</code> dialog to properly dissect this in Wireshark. However, 6LoWPAN does not show up in the selection for "Current". So how can I set this?</p><p>Thanks for your reply!</p></div><div id="question-tags" class="tags-container tags">decode_as ethertype 6lowpan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '16, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/19f6904220614ebeaa6a661a1cdb8fb9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miri64&#39;s gravatar image" /><p>miri64<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miri64 has no accepted answers">0%</span></p></div></div><div id="comments-container-55984" class="comments-container"><span id="59011"></span><div id="comment-59011" class="comment"><div id="post-59011-score" class="comment-score"></div><div class="comment-text"><p>Follow-up: The draft became RFC 7973 in the meantime [1] and the ethertype 0xa0ed is now registered at the IEEE for this.</p><p>[1] <a href="https://tools.ietf.org/html/rfc7973">https://tools.ietf.org/html/rfc7973</a></p></div><div id="comment-59011-info" class="comment-info"><span class="comment-age">(24 Jan '17, 08:18)</span> miri64</div></div></div><div id="comment-tools-55984" class="comment-tools"></div><div class="clear"></div><div id="comment-55984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55987"></span>

<div id="answer-container-55987" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55987-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the IEEE registry, an Ethertype for prototype use:</p><p><span class="small"></span></p><pre><code>88b6      IEEE 802.1               IEEE Std 802 - Local Experimental Ethertype 2.  This Ethertype value is
          802.1 CHAIR c/o IEEE     available for public use and for prototype and vendor-specific protocol
          Piscataway  NJ  08554    development, as defined in Amendment 802a to IEEE Std 802.
          US</code></pre><p>as 0x87dd is already assigned, just not for a published protocol.</p><p>Anyway, as for using Decode as for 6LoWPAN, its dissector needs to be registered for this purpose with the Ethernet dissector. Obviously currently it's not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '16, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Sep '16, 10:15</p></div></div><div id="comments-container-55987" class="comments-container"><span id="56004"></span><div id="comment-56004" class="comment"><div id="post-56004-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the edit, but I was suggesting a proper ethertype to use.</p></div><div id="comment-56004-info" class="comment-info"><span class="comment-age">(30 Sep '16, 04:32)</span> Jaap ♦</div></div><span id="56007"></span><div id="comment-56007" class="comment"><div id="post-56007-score" class="comment-score"></div><div class="comment-text"><p>Ah, sorry I misunderstood and thought it was a cut'n'pasteo, although I still don't understand what you were trying to show.</p><p>For the OP, 0x87dd has been assigned (as per the <a href="http://standards-oui.ieee.org/ethertype/eth.txt">IEEE registry</a>) so be careful with that.</p></div><div id="comment-56007-info" class="comment-info"><span class="comment-age">(30 Sep '16, 05:08)</span> grahamb ♦</div></div><span id="56021"></span><div id="comment-56021" class="comment"><div id="post-56021-score" class="comment-score"></div><div class="comment-text"><p>I was trying to show that ethertype 88B6 is explicitly assigned for this purpose, experimental use, what this is until a proper assignment has been made.</p></div><div id="comment-56021-info" class="comment-info"><span class="comment-age">(30 Sep '16, 07:50)</span> Jaap ♦</div></div><span id="56024"></span><div id="comment-56024" class="comment"><div id="post-56024-score" class="comment-score"></div><div class="comment-text"><p>Hopefully fixed up now.</p></div><div id="comment-56024-info" class="comment-info"><span class="comment-age">(30 Sep '16, 08:15)</span> grahamb ♦</div></div></div><div id="comment-tools-55987" class="comment-tools"></div><div class="clear"></div><div id="comment-55987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

