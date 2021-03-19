+++
type = "question"
title = "Export header information - convert to csv"
description = '''Hi, I am currently trying to capture packets and then export the information about each packet as a .csv. Right now, the .csv only has the date, source, destination, protocol, etc. information. I would also like to export information about the header - hardware source/destination addresss, network a...'''
date = "2014-06-11T09:14:00Z"
lastmod = "2014-06-11T09:35:00Z"
weight = 33646
keywords = [ "header", "hexdump", "transport" ]
aliases = [ "/questions/33646" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Export header information - convert to csv](/questions/33646/export-header-information-convert-to-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33646-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am currently trying to capture packets and then export the information about each packet as a .csv. Right now, the .csv only has the date, source, destination, protocol, etc. information. I would also like to export information about the header - hardware source/destination addresss, network address, etc. How do I do that?</p></div><div id="question-tags" class="tags-container tags">header hexdump transport</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '14, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/057ed44ce723dc35fa796f4a8467bbbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuanjiang&#39;s gravatar image" /><p>yuanjiang<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuanjiang has no accepted answers">0%</span></p></div></div><div id="comments-container-33646" class="comments-container"></div><div id="comment-tools-33646" class="comment-tools"></div><div class="clear"></div><div id="comment-33646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33647"></span>

<div id="answer-container-33647" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33647-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Add the columns you need in the preferences. The export as CSV uses the columns that Wireshark displays. If there is no preset for a column you need you can add it nonetheless by using a custom colum, which can display almost anything that there are display filters for. Easiest way to add custom columns is by finding a value you want as a column and right click to use "Apply as Column".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '14, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33647" class="comments-container"><span id="33651"></span><div id="comment-33651" class="comment"><div id="post-33651-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much for the quick reply! It worked ;)</p></div><div id="comment-33651-info" class="comment-info"><span class="comment-age">(11 Jun '14, 09:36)</span> yuanjiang</div></div></div><div id="comment-tools-33647" class="comment-tools"></div><div class="clear"></div><div id="comment-33647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33649"></span>

<div id="answer-container-33649" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33649-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "Export Packet Dissections As CSV" option only outputs the columns you have on display. Add the appropriate columns to the display and your export will include them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '14, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33649" class="comments-container"><span id="33650"></span><div id="comment-33650" class="comment"><div id="post-33650-score" class="comment-score"></div><div class="comment-text"><p>too slow, again!</p></div><div id="comment-33650-info" class="comment-info"><span class="comment-age">(11 Jun '14, 09:35)</span> grahamb ♦</div></div><span id="33652"></span><div id="comment-33652" class="comment"><div id="post-33652-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much!</p></div><div id="comment-33652-info" class="comment-info"><span class="comment-age">(11 Jun '14, 09:36)</span> yuanjiang</div></div></div><div id="comment-tools-33649" class="comment-tools"></div><div class="clear"></div><div id="comment-33649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

