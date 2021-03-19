+++
type = "question"
title = "Use tshark to get smpp operations results"
description = '''Hello, Is it possible to use tshark command to get the same results of the action to clic in Telephony menu -&amp;gt; SMPP Operations Any advice is appreciated. Thank you for your response. Luis'''
date = "2013-04-18T13:08:00Z"
lastmod = "2013-04-19T06:11:00Z"
weight = 20589
keywords = [ "smpp", "tshark" ]
aliases = [ "/questions/20589" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Use tshark to get smpp operations results](/questions/20589/use-tshark-to-get-smpp-operations-results)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20589-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is it possible to use tshark command to get the same results of the action to clic in Telephony menu -&gt; SMPP Operations Any advice is appreciated. Thank you for your response.</p><p>Luis</p></div><div id="question-tags" class="tags-container tags">smpp tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '13, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/4eb7e6a4a3c2c3542c00650cf619cf6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lgonzalezsa&#39;s gravatar image" /><p>lgonzalezsa<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lgonzalezsa has no accepted answers">0%</span></p></div></div><div id="comments-container-20589" class="comments-container"></div><div id="comment-tools-20589" class="comment-tools"></div><div class="clear"></div><div id="comment-20589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20598"></span>

<div id="answer-container-20598" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20598-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this.</p><blockquote><p><code>tshark -nr input.pcap -q -z smpp_commands,tree</code><br />
</p></blockquote><p>Probably not the <strong>same</strong>, but maybe good enough.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 16:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20598" class="comments-container"><span id="20624"></span><div id="comment-20624" class="comment"><div id="post-20624-score" class="comment-score"></div><div class="comment-text"><p>Good enough! Thank you Kurt</p><p>Best regards,</p><p>Luis</p></div><div id="comment-20624-info" class="comment-info"><span class="comment-age">(19 Apr '13, 06:25)</span> lgonzalezsa</div></div></div><div id="comment-tools-20598" class="comment-tools"></div><div class="clear"></div><div id="comment-20598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20622"></span>

<div id="answer-container-20622" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20622-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark rules!!!! owesome</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '13, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/ca20bac738bbb8b012045602a77d7115?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fachav2&#39;s gravatar image" /><p>fachav2<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fachav2 has no accepted answers">0%</span></p></div></div><div id="comments-container-20622" class="comments-container"></div><div id="comment-tools-20622" class="comment-tools"></div><div class="clear"></div><div id="comment-20622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

