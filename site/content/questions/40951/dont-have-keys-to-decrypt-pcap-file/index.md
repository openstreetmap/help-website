+++
type = "question"
title = "dont have keys to decrypt pcap file"
description = '''Hi all,  I have a pcap file which I want to decrypt in wireshark. The file has full tcp &amp;amp; tls handshake. But to decrypt it I dont have keys. Any ideas how can it be done ? Thanks &amp;amp; Regards, nm'''
date = "2015-03-28T00:41:00Z"
lastmod = "2015-03-28T09:29:00Z"
weight = 40951
keywords = [ "tls" ]
aliases = [ "/questions/40951" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dont have keys to decrypt pcap file](/questions/40951/dont-have-keys-to-decrypt-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40951-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I have a pcap file which I want to decrypt in wireshark. The file has full tcp &amp; tls handshake. But to decrypt it I dont have keys. Any ideas how can it be done ?</p><p>Thanks &amp; Regards, nm</p></div><div id="question-tags" class="tags-container tags">tls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '15, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/4bd7e87670b03c767c5207e72374d19d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nm04&#39;s gravatar image" /><p>nm04<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nm04 has no accepted answers">0%</span></p></div></div><div id="comments-container-40951" class="comments-container"></div><div id="comment-tools-40951" class="comment-tools"></div><div class="clear"></div><div id="comment-40951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40956"></span>

<div id="answer-container-40956" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40956-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It can't be done without the keys.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '15, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40956" class="comments-container"><span id="40996"></span><div id="comment-40996" class="comment"><div id="post-40996-score" class="comment-score"></div><div class="comment-text"><p>Jasper, I read on internet that if I have full capture it can be done. Apart from this cipher suites used is RSA and DHE.<br />
</p></div><div id="comment-40996-info" class="comment-info"><span class="comment-age">(30 Mar '15, 04:09)</span> nm04</div></div><span id="40997"></span><div id="comment-40997" class="comment"><div id="post-40997-score" class="comment-score"></div><div class="comment-text"><p>you can't, if you don't have the keys. That what crypto is good for - preventing reading the content when you're not authorized (meaning: have no keys).</p><p>What you have read is that you need the TLS handshake to be able decrypt the conversation with the keys. Because if you have the keys but not the handshake you can't decrypt the conversation either.</p></div><div id="comment-40997-info" class="comment-info"><span class="comment-age">(30 Mar '15, 04:12)</span> Jasper ♦♦</div></div><span id="41000"></span><div id="comment-41000" class="comment"><div id="post-41000-score" class="comment-score"></div><div class="comment-text"><p>the NSA claims it can be done ;-))</p></div><div id="comment-41000-info" class="comment-info"><span class="comment-age">(30 Mar '15, 04:20)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-40956" class="comment-tools"></div><div class="clear"></div><div id="comment-40956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

