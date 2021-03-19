+++
type = "question"
title = "Fake-field-Wrapper"
description = '''Dears, I have a question, I want to understand the meaning of this message &quot;fake-field-wrapper&quot;, in what situation is used, where can I get or if you can share more documentation related to this message?'''
date = "2017-10-25T06:54:00Z"
lastmod = "2017-10-25T08:55:00Z"
weight = 64185
keywords = [ "fake-field-wrapper" ]
aliases = [ "/questions/64185" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fake-field-Wrapper](/questions/64185/fake-field-wrapper)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64185-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dears, I have a question, I want to understand the meaning of this message "fake-field-wrapper", in what situation is used, where can I get or if you can share more documentation related to this message?</p></div><div id="question-tags" class="tags-container tags">fake-field-wrapper</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '17, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/8ce14c89abe813c7cac4a947dd61afc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miguel198532&#39;s gravatar image" /><p>Miguel198532<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miguel198532 has no accepted answers">0%</span></p></div></div><div id="comments-container-64185" class="comments-container"><span id="64187"></span><div id="comment-64187" class="comment"><div id="post-64187-score" class="comment-score"></div><div class="comment-text"><p>In what context do you see that message?</p></div><div id="comment-64187-info" class="comment-info"><span class="comment-age">(25 Oct '17, 07:02)</span> grahamb ♦</div></div><span id="64190"></span><div id="comment-64190" class="comment"><div id="post-64190-score" class="comment-score"></div><div class="comment-text"><p>In the FCS [Frame check sequence], this is signaling of "Attach Request" sent from POS device to mobile network.</p></div><div id="comment-64190-info" class="comment-info"><span class="comment-age">(25 Oct '17, 08:27)</span> Miguel198532</div></div></div><div id="comment-tools-64185" class="comment-tools"></div><div class="clear"></div><div id="comment-64185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64194"></span>

<div id="answer-container-64194" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64194-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For reference the context appears to be when using PDML output.</p><p>The comment next to the code that outputs the <code>&lt;proto name="fake-field-wrapper""&gt;</code> element is:</p><pre><code>/* Will wrap up top-level field items inside a fake protocol wrapper to preserve the PDML schema */</code></pre><p>and the code that checks if this is necessary is:</p><pre><code>wrap_in_fake_protocol =
    (((fi-&gt;hfinfo-&gt;type != FT_PROTOCOL) ||
      (fi-&gt;hfinfo-&gt;id == proto_data)) &amp;&amp;
     (pdata-&gt;level == 0));</code></pre><p>I'm guessing this means that if the top-level node isn't of type FT_PROTOCOL or just data then the fake-field-wrapper node is printed.</p><p>I'd need to see a capture to work out what's really happening.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '17, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-64194" class="comments-container"></div><div id="comment-tools-64194" class="comment-tools"></div><div class="clear"></div><div id="comment-64194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

