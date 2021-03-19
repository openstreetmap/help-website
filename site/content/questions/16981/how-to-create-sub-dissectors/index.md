+++
type = "question"
title = "how to create sub dissectors"
description = '''Hey, I&#x27;m building a dissector which is the main dissector. After I read some variable, according to it, I want to continue dissecting with a suitable sub dissector. I didn&#x27;t find any simple example about &quot;sub dissectors&quot;. Alternatively, I thought about continue dissecting with the same dissector (be...'''
date = "2012-12-17T09:04:00Z"
lastmod = "2012-12-17T18:51:00Z"
weight = 16981
keywords = [ "dissector", "subdissector", "sub-dissector", "wireshark" ]
aliases = [ "/questions/16981" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to create sub dissectors](/questions/16981/how-to-create-sub-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16981-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, I'm building a dissector which is the main dissector. After I read some variable, according to it, I want to continue dissecting with a suitable sub dissector. I didn't find any simple example about "sub dissectors".</p><p>Alternatively, I thought about continue dissecting with the same dissector (because it is the same protocol, just different versions), with somehow writing inside the main dissector all of the dissecting options for each version. This solution doesn't seems right...</p><p>Can someone please help me with that?</p></div><div id="question-tags" class="tags-container tags">dissector subdissector sub-dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '12, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p>hudac<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div></div><div id="comments-container-16981" class="comments-container"></div><div id="comment-tools-16981" class="comment-tools"></div><div class="clear"></div><div id="comment-16981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17005"></span>

<div id="answer-container-17005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17005-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>My inclination would be to suggest that dissecting variants of a protocol (e.g., different protocol versions) be done in one dissector.</p><p>A number of Wireshark dissectors do just that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '12, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-17005" class="comments-container"><span id="17014"></span><div id="comment-17014" class="comment"><div id="post-17014-score" class="comment-score"></div><div class="comment-text"><p>thanks,</p><p>"A number of Wireshark dissectors do just that."</p><p>What do you mean by that line?</p></div><div id="comment-17014-info" class="comment-info"><span class="comment-age">(18 Dec '12, 01:31)</span> hudac</div></div><span id="17021"></span><div id="comment-17021" class="comment"><div id="post-17021-score" class="comment-score"></div><div class="comment-text"><p>The dissector has separate code which is executed depending upon the protocol version determined by the dissector.</p></div><div id="comment-17021-info" class="comment-info"><span class="comment-age">(18 Dec '12, 05:31)</span> Bill Meier ♦♦</div></div><span id="18286"></span><div id="comment-18286" class="comment"><div id="post-18286-score" class="comment-score"></div><div class="comment-text"><p>That's a really interesting approach, would you be so kind to point out some of the dissectors doing that? I'm also reading the developer's readme, but I often get lost..</p></div><div id="comment-18286-info" class="comment-info"><span class="comment-age">(04 Feb '13, 09:03)</span> cico</div></div><span id="18290"></span><div id="comment-18290" class="comment"><div id="post-18290-score" class="comment-score">1</div><div class="comment-text"><p>A very simple case is packet-bt-utp.c</p><p>It can be as simple as something like</p><pre><code>version = tvb_get...();
if (version == ... {
    ... /* dissect version 1 fields */
}</code></pre><p>and so on.</p></div><div id="comment-18290-info" class="comment-info"><span class="comment-age">(04 Feb '13, 10:27)</span> Bill Meier ♦♦</div></div><span id="18292"></span><div id="comment-18292" class="comment"><div id="post-18292-score" class="comment-score"></div><div class="comment-text"><p>That's brilliant, exactly what I was asking for! Thank you so much, I would have never found it :)</p></div><div id="comment-18292-info" class="comment-info"><span class="comment-age">(04 Feb '13, 11:13)</span> cico</div></div></div><div id="comment-tools-17005" class="comment-tools"></div><div class="clear"></div><div id="comment-17005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

