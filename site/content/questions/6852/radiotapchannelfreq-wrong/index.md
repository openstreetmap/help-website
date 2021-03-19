+++
type = "question"
title = "radiotap.channel.freq wrong?"
description = '''This may actually be a radiotap question, forgive me if this is going to the wrong place... I&#x27;ve been seeing a lot of weird 2.4 GHz channels reported, using an Intel wireless card in a Dell, when the only channels in play should be 1, 6, and 11 (and 5, that&#x27;s a different problem). On the other hand,...'''
date = "2011-10-11T13:27:00Z"
lastmod = "2011-10-11T16:16:00Z"
weight = 6852
keywords = [ "frequency", "radiotap" ]
aliases = [ "/questions/6852" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [radiotap.channel.freq wrong?](/questions/6852/radiotapchannelfreq-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6852-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This may actually be a radiotap question, forgive me if this is going to the wrong place...</p><p>I've been seeing a lot of weird 2.4 GHz channels reported, using an Intel wireless card in a Dell, when the only channels in play should be 1, 6, and 11 (and 5, that's a different problem). On the other hand, the 802.11 header reports the "correct" channel. I went around with a Wi-Spy spectrum analyzer and the channels do appear to lie within the frequency ranges they belong in.</p><p>AirDefense Mobile seems to be doing the same thing, with a Netgear WNDA3100.</p><p>Is this because of the receive sensitivity being good enough for these cards to pick up channels outside the ones they should be tuned to?</p></div><div id="question-tags" class="tags-container tags">frequency radiotap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '11, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/c73c0d5c54e0b4f623bc7da0010d591e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Yerger&#39;s gravatar image" /><p>David Yerger<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Yerger has no accepted answers">0%</span></p></div></div><div id="comments-container-6852" class="comments-container"><span id="6859"></span><div id="comment-6859" class="comment"><div id="post-6859-score" class="comment-score"></div><div class="comment-text"><p>What OS are you running on the Dell, what Intel adapter are you using, and what frequencies are being reported?</p><p>When you say "AirDefense Mobile seems to be doing the same thing", is it also reporting weird frequencies? (BTW, the only NetGear adapter the <a href="http://www.airdefense.net/products/admobile/index.php">AirDefense Mobile</a> page currently mentions is the WAG511.)</p></div><div id="comment-6859-info" class="comment-info"><span class="comment-age">(11 Oct '11, 19:27)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-6852" class="comment-tools"></div><div class="clear"></div><div id="comment-6852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6856"></span>

<div id="answer-container-6856" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6856-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Or you might wonder how the radiotap header gets filled, where does this information come from? If it's a faulty driver (what else is new) it may report incorrect values, even though the IEEE 802.11 info says the correct values.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '11, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6856" class="comments-container"><span id="6858"></span><div id="comment-6858" class="comment"><div id="post-6858-score" class="comment-score"></div><div class="comment-text"><p>AirDefense Mobile <a href="%5Bhttp://www.airdefense.net/products/admobile/index.php">appears to be running on Windows</a>. They run on Windows XP, so they presumably don't depend on Windows Native Wi-Fi, as I don't think that's available in XP, so they might have their own drivers.</p><p>Presumably the Dell is <em>not</em> running Windows, as, otherwise, he wouldn't be getting radiotap headers.</p><p>So there'd have to be two broken drivers for two different OSes and two different wireless adapters.</p></div><div id="comment-6858-info" class="comment-info"><span class="comment-age">(11 Oct '11, 19:25)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-6856" class="comment-tools"></div><div class="clear"></div><div id="comment-6856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

