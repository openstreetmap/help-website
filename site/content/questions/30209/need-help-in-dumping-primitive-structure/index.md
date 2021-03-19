+++
type = "question"
title = "Need help in dumping primitive structure"
description = '''Hi All, I am absolutely new to wireshark. Currently we are planning to use wireshark to capture traces of our communication protocol stack. We intend to write plugins to dump the primitive structures sent between various components  ( interface structures between various layers of our protocol stack...'''
date = "2014-02-26T10:13:00Z"
lastmod = "2014-02-26T14:09:00Z"
weight = 30209
keywords = [ "structures", "dump" ]
aliases = [ "/questions/30209" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need help in dumping primitive structure](/questions/30209/need-help-in-dumping-primitive-structure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30209-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am absolutely new to wireshark. Currently we are planning to use wireshark to capture traces of our communication protocol stack.</p><p>We intend to write plugins to dump the primitive structures sent between various components ( interface structures between various layers of our protocol stack ). Are there any sample plugins already available which I can re-use to dump structures ?</p><p>Looking forward for help.</p><p>Regards, Sameer...</p></div><div id="question-tags" class="tags-container tags">structures dump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '14, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/ca15801eb19cd976a02767f0788ae6fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sameer&#39;s gravatar image" /><p>Sameer<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sameer has no accepted answers">0%</span></p></div></div><div id="comments-container-30209" class="comments-container"></div><div id="comment-tools-30209" class="comment-tools"></div><div class="clear"></div><div id="comment-30209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30216"></span>

<div id="answer-container-30216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30216-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Essentially you are discussing development of a dissector for your protocol(s). Wireshark creates a big infrastructure around the topics of traffic capture, reading capture files, dissection of capture traffic and displaying the results of the dissection. A dissector sits in the middle of this and dissects the structures in your protocol and hands them off to the rest of the infrastructure for display and other processing (stats, graphs etc.)</p><p>There are a number of ways of creating a dissector, each method has its pros and cons regarding ease of development, flexibility and speed in use. My <a href="http://sharkfest.wireshark.org/sharkfest.13/presentations/PA-10_Writing-a-Wireshark-Dissector_Graham-Bloice.zip">SharkFest presentation</a> for SF13 (presenting it again at SF'14) discusses three common approaches that you could look at.</p><p>If you decide on a C based dissector, then of course you have all the existing dissectors as samples to work with along with the extensive <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">developers guide</a> and other documentation that can be found in the source tree <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree;f=doc;hb=HEAD">doc</a> directory.</p><p>Finally remember the licencing of Wireshark, it is GPL 2.0 that means if you distribute the software you must make your source code changes available on request.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '14, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-30216" class="comments-container"><span id="30229"></span><div id="comment-30229" class="comment"><div id="post-30229-score" class="comment-score"></div><div class="comment-text"><p>Many Thanks for your pointers will go through you presentation and material. I am going to write dissector in C so hopefully will be able to reuse samples.</p></div><div id="comment-30229-info" class="comment-info"><span class="comment-age">(27 Feb '14, 01:57)</span> Sameer</div></div></div><div id="comment-tools-30216" class="comment-tools"></div><div class="clear"></div><div id="comment-30216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

