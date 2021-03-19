+++
type = "question"
title = "Dissecting protocol that has message direction based dissectors"
description = '''Hi Forum, I am writing a dissector for a protocol that has different dissectors depending on the direction of the traffic. The protocol is Length|FCode|Data. For the same FCode value the Data is dissected differently depending on its direction. Ie device to host and host to device. Sending request a...'''
date = "2013-01-22T23:23:00Z"
lastmod = "2013-01-22T23:51:00Z"
weight = 17883
keywords = [ "help", "dissectors" ]
aliases = [ "/questions/17883" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting protocol that has message direction based dissectors](/questions/17883/dissecting-protocol-that-has-message-direction-based-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17883-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Forum,</p><p>I am writing a dissector for a protocol that has different dissectors depending on the direction of the traffic.</p><p>The protocol is Length|FCode|Data. For the same FCode value the Data is dissected differently depending on its direction. Ie device to host and host to device. Sending request and response using same function code value.</p><p>How is this typically handled? Are there any example dissectors that do this?</p><p>Thanks</p><p>Stuart</p></div><div id="question-tags" class="tags-container tags">help dissectors</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '13, 23:23</strong></p><img src="https://secure.gravatar.com/avatar/e12bbe1b488f2a19cdf565465e260d19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StuieNorris&#39;s gravatar image" /><p>StuieNorris<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StuieNorris has no accepted answers">0%</span></p></div></div><div id="comments-container-17883" class="comments-container"></div><div id="comment-tools-17883" class="comment-tools"></div><div class="clear"></div><div id="comment-17883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17890"></span>

<div id="answer-container-17890" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17890-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could do something like:</p><pre><code>dir=extract_dir_from_packet(...);
if( dir==FWD ) {
    dissect_foo_fwd(...);
} else {
    dissect_foo_rev(...);
}</code></pre><p>If there is nothing in the packet indicating the direction of the packet, you will need to remember the IP address of the host when your dissector gets called for the first data segment. You can do this with conversations. See <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.developer?revision=46847">README.developer</a> paragraph 2.2.1 (especially 2.2.1.5 and 2.2.1.6).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17890" class="comments-container"><span id="17893"></span><div id="comment-17893" class="comment"><div id="post-17893-score" class="comment-score"></div><div class="comment-text"><p>I read the referenced section but I understand how to implement. however sounds pretty much exactly what I need.</p><p>Are there any existing dissectors that do what I want I could review?</p></div><div id="comment-17893-info" class="comment-info"><span class="comment-age">(23 Jan '13, 01:42)</span> StuieNorris</div></div></div><div id="comment-tools-17890" class="comment-tools"></div><div class="clear"></div><div id="comment-17890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

