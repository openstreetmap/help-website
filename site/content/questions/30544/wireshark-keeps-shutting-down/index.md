+++
type = "question"
title = "Wireshark keeps shutting down..."
description = '''I am new to Wireshark. That being said, I am trying to analyze server packets for a period of time. Wireshark runs for a random period of time -- say 5-10 minutes and then keeps shutting down saying an unexpected error has occurred. I lose my file of captured data, etc. I have tried using multiple f...'''
date = "2014-03-07T07:26:00Z"
lastmod = "2014-03-07T07:27:00Z"
weight = 30544
keywords = [ "unexpectedly", "shutdown", "error" ]
aliases = [ "/questions/30544" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark keeps shutting down...](/questions/30544/wireshark-keeps-shutting-down)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30544-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to Wireshark. That being said, I am trying to analyze server packets for a period of time. Wireshark runs for a random period of time -- say 5-10 minutes and then keeps shutting down saying an unexpected error has occurred. I lose my file of captured data, etc. I have tried using multiple file settings as well.<br />
</p><p>Suggestions? Trying to find my packet errors is hard enough without the tool randomly losing everything.<br />
</p></div><div id="question-tags" class="tags-container tags">unexpectedly shutdown error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '14, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/1bd4c534d91f362ab2ee3aa19363d2da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cboshdave&#39;s gravatar image" /><p>cboshdave<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cboshdave has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-30544" class="comments-container"><span id="30574"></span><div id="comment-30574" class="comment"><div id="post-30574-score" class="comment-score"></div><div class="comment-text"><p>Please add more details</p><ul><li>OS and OS version</li><li>Wireshark version</li><li>Capture setup (on system, switch mirror port, TAP)</li><li>How much traffic do you see on the captured port</li><li>How do you start Wireshark (RPD: see the comment of @Anders)</li><li>Do you use Capture filters? If no: why? If yes: which one?</li></ul></div><div id="comment-30574-info" class="comment-info"><span class="comment-age">(07 Mar '14, 10:42)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30544" class="comment-tools"></div><div class="clear"></div><div id="comment-30544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30545"></span>

<div id="answer-container-30545" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30545-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '14, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30545" class="comments-container"><span id="30564"></span><div id="comment-30564" class="comment"><div id="post-30564-score" class="comment-score"></div><div class="comment-text"><p>Which os? Windows server and remote desktop has problems. Thank or dumpcap might be used as a workaround. Your capture files may be left in your temp direct after a crash.</p></div><div id="comment-30564-info" class="comment-info"><span class="comment-age">(07 Mar '14, 08:43)</span> Anders ♦</div></div><span id="30648"></span><div id="comment-30648" class="comment"><div id="post-30648-score" class="comment-score"></div><div class="comment-text"><p>Running "dumpcap" from the command prompt seemed to do the trick. Thanks!! i was able to capture the information over an extended period of time without crashing!! I appreciate it.<br />
</p></div><div id="comment-30648-info" class="comment-info"><span class="comment-age">(10 Mar '14, 06:51)</span> cboshdave</div></div><span id="30653"></span><div id="comment-30653" class="comment"><div id="post-30653-score" class="comment-score"></div><div class="comment-text"><p>@cboshdave</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-30653-info" class="comment-info"><span class="comment-age">(10 Mar '14, 07:52)</span> grahamb ♦</div></div></div><div id="comment-tools-30545" class="comment-tools"></div><div class="clear"></div><div id="comment-30545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

