+++
type = "question"
title = "Export wireshark capture to csv or excel file"
description = '''Am using Wireshark: 1.12.7.  Wanted to export wireshark captured file into a CSV or excel file., including the packet payload.  Present export option is exporting only columns that are displayed [ i.e from No, Timestamp .. Packet Info].  Please teach me how to do this.  Also is there any way., I can...'''
date = "2015-08-14T22:42:00Z"
lastmod = "2015-08-15T07:05:00Z"
weight = 45128
keywords = [ "csv", "export" ]
aliases = [ "/questions/45128" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Export wireshark capture to csv or excel file](/questions/45128/export-wireshark-capture-to-csv-or-excel-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45128-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Am using Wireshark: 1.12.7.</p><p>Wanted to export wireshark captured file into a CSV or excel file., <strong>including</strong> the packet payload.</p><p>Present export option is exporting only columns that are displayed [ i.e from No, Timestamp .. Packet Info].</p><p>Please teach me how to do this.</p><p>Also is there any way., I can customize Wireshark to decipher the packet payload bytes (say 20-30bytes) and display additional information for me ?</p></div><div id="question-tags" class="tags-container tags">csv export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '15, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/756de87a42e96ac80d8f1a204fd29497?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pp_prasana&#39;s gravatar image" /><p>pp_prasana<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pp_prasana has no accepted answers">0%</span></p></div></div><div id="comments-container-45128" class="comments-container"></div><div id="comment-tools-45128" class="comment-tools"></div><div class="clear"></div><div id="comment-45128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45141"></span>

<div id="answer-container-45141" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45141-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I thought that using the menu item File -&gt; Export Packet Dissections -&gt; As "CSV" and then checking the "Packet bytes" option would do the trick, but as you noted it only exports the columns on view.</p><p>Adding the "data.data" field as a column and using the same menu item gives you only 24 bytes (48 hex chars) of the packet data.</p><p>To "customize" Wireshark to dissect the packet data you'll need to write a dissector. I covered the basic options in my talk at SharkFest: <a href="https://sharkfest.wireshark.org/assets/presentations15/03.pptx">Writing a Wireshark Dissector using WSGD, Lua and C</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '15, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45141" class="comments-container"><span id="45277"></span><div id="comment-45277" class="comment"><div id="post-45277-score" class="comment-score"></div><div class="comment-text"><p>@grahamb: Thanks for the answer, sir.</p><p>Is there a way to get the complete payload (instead of just 24 bytes) exported ?</p><p>I can do some tweaking using excel formula and dissect the packet.</p><p>Let me go thru' suggested PPT and get back if I need any specific clarification from that.</p></div><div id="comment-45277-info" class="comment-info"><span class="comment-age">(20 Aug '15, 11:56)</span> pp_prasana</div></div><span id="45278"></span><div id="comment-45278" class="comment"><div id="post-45278-score" class="comment-score"></div><div class="comment-text"><p>Looks WSGD is pretty simple. Let me try that and get back.</p></div><div id="comment-45278-info" class="comment-info"><span class="comment-age">(20 Aug '15, 12:06)</span> pp_prasana</div></div></div><div id="comment-tools-45141" class="comment-tools"></div><div class="clear"></div><div id="comment-45141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

