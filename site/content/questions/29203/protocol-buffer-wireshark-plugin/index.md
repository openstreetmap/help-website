+++
type = "question"
title = "Protocol Buffer Wireshark Plugin"
description = '''I am looking for a wireshark plugin for google protocol buffer. And I found this GPB Wireshark plugin (http://code.google.com/p/protobuf-wireshark/) Apparently only UDP….Is there a GPB plugin for wireshark that works for TCP?'''
date = "2014-01-27T11:51:00Z"
lastmod = "2014-04-15T01:31:00Z"
weight = 29203
keywords = [ "buffer", "protocol", "wireshark", "google", "plugin" ]
aliases = [ "/questions/29203" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Protocol Buffer Wireshark Plugin](/questions/29203/protocol-buffer-wireshark-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29203-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for a wireshark plugin for google protocol buffer. And I found this GPB Wireshark plugin (<a href="http://code.google.com/p/protobuf-wireshark/)">http://code.google.com/p/protobuf-wireshark/)</a></p><p>Apparently only UDP….Is there a GPB plugin for wireshark that works for TCP?</p></div><div id="question-tags" class="tags-container tags">buffer protocol wireshark google plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '14, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/6a5cd0523513188644be89583edf1c46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user12321&#39;s gravatar image" /><p>user12321<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user12321 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jan '14, 11:53</p></div></div><div id="comments-container-29203" class="comments-container"></div><div id="comment-tools-29203" class="comment-tools"></div><div class="clear"></div><div id="comment-29203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31825"></span>

<div id="answer-container-31825" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31825-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The URL you found, hosts pretty much the only (well) known Protobuf dissector. There might be others, but they are apparently not published anywhere.</p><p>There is another project that does protobuf dissection however that's nothing you can 'just use' (I guess).</p><blockquote><p><a href="https://github.com/pathorn/sst-dissector">https://github.com/pathorn/sst-dissector</a></p></blockquote><p>It's more something you could use as an example to build your own dissector.</p><p>So, these are your options:</p><ul><li>ask the author of <a href="http://code.google.com/p/protobuf-wireshark/">http://code.google.com/p/protobuf-wireshark/</a> to modify to code for TCP</li><li>make the necessary modifications your self</li><li>try to modify the code <a href="https://github.com/pathorn/sst-dissector">https://github.com/pathorn/sst-dissector</a> as you need it</li><li>wait until somebody writes the dissector you need</li><li>pay somebody to do the work for you</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31825" class="comments-container"><span id="31835"></span><div id="comment-31835" class="comment"><div id="post-31835-score" class="comment-score"></div><div class="comment-text"><ul><li>Add an enhancement request (if there isn't one already) to the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>.</li></ul></div><div id="comment-31835-info" class="comment-info"><span class="comment-age">(15 Apr '14, 02:23)</span> grahamb ♦</div></div><span id="31866"></span><div id="comment-31866" class="comment"><div id="post-31866-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your suggestions. I have written the dissector by myself.</p></div><div id="comment-31866-info" class="comment-info"><span class="comment-age">(15 Apr '14, 22:05)</span> user12321</div></div><span id="32004"></span><div id="comment-32004" class="comment"><div id="post-32004-score" class="comment-score"></div><div class="comment-text"><p>O.K. do you mind to share the code with the Wireshark community? If so, please submit your code for review.</p><blockquote><p><a href="https://code.wireshark.org/review/Documentation/prolog-cookbook.html">https://code.wireshark.org/review/Documentation/prolog-cookbook.html</a></p></blockquote></div><div id="comment-32004-info" class="comment-info"><span class="comment-age">(19 Apr '14, 16:41)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-31825" class="comment-tools"></div><div class="clear"></div><div id="comment-31825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

