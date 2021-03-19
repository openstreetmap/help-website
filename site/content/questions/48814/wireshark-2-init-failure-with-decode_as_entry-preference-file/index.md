+++
type = "question"
title = "Wireshark 2 init failure with &quot;decode_as_entry&quot; preference file."
description = '''Hi, Latest Wireshark 2 initialization hangs if my personal preference file &quot;decode_as_entries&quot; has following line: decode_as_entry: ethertype,16400,(none),IPv4 Wireshark 2 initialization hangs at phase &quot;Loading module preferences&quot;. Error: Unhandled exception at 0x01285EE9 in Wireshark.exe: 0xC000000...'''
date = "2016-01-03T15:16:00Z"
lastmod = "2016-01-04T06:30:00Z"
weight = 48814
keywords = [ "wireshark-2", "decode_as_entries" ]
aliases = [ "/questions/48814" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 2 init failure with "decode\_as\_entry" preference file.](/questions/48814/wireshark-2-init-failure-with-decode_as_entry-preference-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48814-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Latest Wireshark 2 initialization hangs if my personal preference file "decode_as_entries" has following line: decode_as_entry: ethertype,16400,(none),IPv4</p><p>Wireshark 2 initialization hangs at phase "Loading module preferences". Error: Unhandled exception at 0x01285EE9 in Wireshark.exe: 0xC0000005: Access violation reading location 0x00000000. change_dissector_if_matched(gpointer item, gpointer user_data) { ... if (strcmp(lookup-&gt;dissector_short_name, dissector_handle_get_short_name(handle)) == 0) {</p><p>Where 1st parameter has dissector_short_name "IPv4". This is a fresh re-build w/o any plugin.</p><p>P.S. WS 1.12 is good with this pref file.</p><p>Any hints, or maybe a fixed available for this?</p><p>Thanks, Jack</p></div><div id="question-tags" class="tags-container tags">wireshark-2 decode_as_entries</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '16, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/e1984914b8c461cdc39fe81b37c37b98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JackaJack&#39;s gravatar image" /><p>JackaJack<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JackaJack has no accepted answers">0%</span></p></div></div><div id="comments-container-48814" class="comments-container"></div><div id="comment-tools-48814" class="comment-tools"></div><div class="clear"></div><div id="comment-48814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48836"></span>

<div id="answer-container-48836" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48836-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for reporting the issue. I filled <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11958">bug 11958</a> and proposed a fix.</p><p>Edit: patch is now merged, it will be available soon in the nightly builds.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '16, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jan '16, 12:40</p></div></div><div id="comments-container-48836" class="comments-container"></div><div id="comment-tools-48836" class="comment-tools"></div><div class="clear"></div><div id="comment-48836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48817"></span>

<div id="answer-container-48817" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48817-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's been some recent changes for the Decode As functionality, what version of 2.x are you running? If it's not the latest, please try that first, else if it's the latest, please raise an entry on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '16, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jan '16, 16:29</p></div></div><div id="comments-container-48817" class="comments-container"></div><div id="comment-tools-48817" class="comment-tools"></div><div class="clear"></div><div id="comment-48817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

