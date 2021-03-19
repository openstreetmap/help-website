+++
type = "question"
title = "where is &quot;ssl_set_master_secret() called in Wireshark?"
description = '''I&#x27;m not able to find where is it called? or how is it used?  here is a link for this function from wireshark documentation.'''
date = "2015-04-09T15:21:00Z"
lastmod = "2015-04-10T06:14:00Z"
weight = 41334
keywords = [ "ssl", "wireshark" ]
aliases = [ "/questions/41334" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [where is "ssl\_set\_master\_secret() called in Wireshark?](/questions/41334/where-is-ssl_set_master_secret-called-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41334-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm not able to find where is it called? or how is it used? here is a <a href="https://www.wireshark.org/docs/wsar_html/epan/packet-ssl_8h.html#a17f7d91c30a3769e8b618aa967a6a3a1">link</a> for this function from wireshark documentation.</p></div><div id="question-tags" class="tags-container tags">ssl wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '15, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-41334" class="comments-container"></div><div id="comment-tools-41334" class="comment-tools"></div><div class="clear"></div><div id="comment-41334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41350"></span>

<div id="answer-container-41350" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41350-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe that this <code>ssl_set_master_secret()</code> function is exported for third-party plugins. These can then supply secrets to the SSL dissector.</p><p>For offline captures, it might be easier to include a SSL keylog file next to the capture which is more portable than a binary plugin. For live captures, you can still use the SSL keylog file if the SSL client/server can provide such secrets (<a href="https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/Key_Log_Format">NSS</a> can do this, <a href="https://git.lekensteyn.nl/peter/wireshark-notes/tree/patches/cyassl-Implement-SSLKEYLOGFILE-support-for-ClientRandom.patch">CyaSSL can be patched</a>, <a href="http://security.stackexchange.com/q/80158/2630">OpenSSL can also be forced with a debugger/interposing library</a>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '15, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-41350" class="comments-container"></div><div id="comment-tools-41350" class="comment-tools"></div><div class="clear"></div><div id="comment-41350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

