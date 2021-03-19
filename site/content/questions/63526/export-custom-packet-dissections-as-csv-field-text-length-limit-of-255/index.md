+++
type = "question"
title = "Export Custom Packet Dissections as CSV - Field text length limit of 255"
description = '''Just wanted to confirm please, if what I am experiencing is a limitation. And if there is a workaround -- output file to be opened and used in Excel. Using Wireshark 2.4.0 with a custom heuristic LUA dissector, and exporting to CSV file format, some fields with multiple values resulting in text leng...'''
date = "2017-08-28T03:51:00Z"
lastmod = "2017-08-28T03:51:00Z"
weight = 63526
keywords = [ "255", "csv", "text_length" ]
aliases = [ "/questions/63526" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Export Custom Packet Dissections as CSV - Field text length limit of 255](/questions/63526/export-custom-packet-dissections-as-csv-field-text-length-limit-of-255)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63526-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just wanted to confirm please, if what I am experiencing is a limitation. And if there is a workaround -- output file to be opened and used in Excel.</p><p>Using Wireshark 2.4.0 with a custom heuristic LUA dissector, and exporting to CSV file format, some fields with multiple values resulting in text length of greater than 255 are truncated in the CSV file. Sample shown below for a value type column, with 56 "Float" value types.</p><pre><code>&quot;Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Float,Flo&quot;</code></pre><p>I also noticed the 255 text length limit when using PSML file format for export.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">255 csv text_length</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '17, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/7e50c86ac4ee2038257acc83ccb1ce21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="juandering&#39;s gravatar image" /><p>juandering<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="juandering has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Aug '17, 04:01</p></div></div><div id="comments-container-63526" class="comments-container"></div><div id="comment-tools-63526" class="comment-tools"></div><div class="clear"></div><div id="comment-63526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

