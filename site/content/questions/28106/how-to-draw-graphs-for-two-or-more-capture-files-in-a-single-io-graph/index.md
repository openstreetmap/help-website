+++
type = "question"
title = "How to draw graphs for two or more capture files in a single IO graph?"
description = '''Hi, I would like to know if it is possible to draw graphs for two or more capture files in a single IO graph. I could find only &#x27;compare&#x27; tool but thats not what I am looking for. I just want to plot IO graphs of more than two capture files in a single IO graph. I could find multiple graphs option i...'''
date = "2013-12-14T11:14:00Z"
lastmod = "2013-12-14T11:17:00Z"
weight = 28106
keywords = [ "capture-file", "graph", "multiple", "capture", "iograph" ]
aliases = [ "/questions/28106" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to draw graphs for two or more capture files in a single IO graph?](/questions/28106/how-to-draw-graphs-for-two-or-more-capture-files-in-a-single-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28106-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to know if it is possible to draw graphs for two or more capture files in a single IO graph. I could find only 'compare' tool but thats not what I am looking for. I just want to plot IO graphs of more than two capture files in a single IO graph. I could find multiple graphs option in IO graph of Wireshark but I think it will plot IO graphs related to only one capture file after filtering. Could anyone please help me with this?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">capture-file graph multiple capture iograph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '13, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/f9e1104aabb74d8911ec3bb7c49d0e90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srikanth&#39;s gravatar image" /><p>srikanth<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srikanth has no accepted answers">0%</span></p></div></div><div id="comments-container-28106" class="comments-container"></div><div id="comment-tools-28106" class="comment-tools"></div><div class="clear"></div><div id="comment-28106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28107"></span>

<div id="answer-container-28107" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28107-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can only have one capture file open per Wireshark instance, and thus only draw IO graphs for that one file. If you need to plot more than one file into a single graph you should export your graphs one by one using the "Copy" button on the IO graph bottom, and import them combined into a tool like Excel where you have more options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '13, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28107" class="comments-container"><span id="28109"></span><div id="comment-28109" class="comment"><div id="post-28109-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper! Thank you for the quick reply. That was helpful. And I have one more doubt. Can I get a guide sort of a document for 'filters' in the IO graph window? I want to know what filter I should apply to plot IO graph for malformed packets etc...related to the same capture file.</p></div><div id="comment-28109-info" class="comment-info"><span class="comment-age">(14 Dec '13, 11:30)</span> srikanth</div></div><span id="61149"></span><div id="comment-61149" class="comment"><div id="post-61149-score" class="comment-score"></div><div class="comment-text"><p>Hi, can you help me? i don't get it. How to import them to Excel by 'Copy' from the io graph?</p></div><div id="comment-61149-info" class="comment-info"><span class="comment-age">(02 May '17, 01:00)</span> fiekafy</div></div></div><div id="comment-tools-28107" class="comment-tools"></div><div class="clear"></div><div id="comment-28107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

