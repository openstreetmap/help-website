+++
type = "question"
title = "Bluez SCO extraction with wireshark"
description = '''I can see that a log file can be generated with hcidump or btmon, but I am looking for a way to extract audio as a check point in the audio chain to determine where audio is lost. I can see if using the above SCO prints are present as human readable hex prints, but it is not clear if 1) the SCO Rex/...'''
date = "2016-11-15T05:23:00Z"
lastmod = "2016-11-16T23:22:00Z"
weight = 57389
keywords = [ "bluez-sco-capture", "cvsd-export-wav", "sco-wav-export" ]
aliases = [ "/questions/57389" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bluez SCO extraction with wireshark](/questions/57389/bluez-sco-extraction-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57389-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can see that a log file can be generated with hcidump or btmon, but I am looking for a way to extract audio as a check point in the audio chain to determine where audio is lost.</p><p>I can see if using the above SCO prints are present as human readable hex prints, but it is not clear if 1) the SCO Rex/Tx data are part of a btsnoop.log (or a text output file of btmon output) and 2) If Wireshark can export the SCO data as a .wav which can then be Analyzer in an audio tool for missing audio data in any one direction?</p><p>If it makes any difference the audio is not piped over HCI to the BT adaptor, but non the less if I am looking at stock btmon prints SCO prints are seen for each direction.</p><p>Many Thanks, Mark</p></div><div id="question-tags" class="tags-container tags">bluez-sco-capture cvsd-export-wav sco-wav-export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '16, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/ba47e134edf9bc10fbc8cb5c13b3fe86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Markro&#39;s gravatar image" /><p>Markro<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Markro has no accepted answers">0%</span></p></div></div><div id="comments-container-57389" class="comments-container"></div><div id="comment-tools-57389" class="comment-tools"></div><div class="clear"></div><div id="comment-57389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57430"></span>

<div id="answer-container-57430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57430-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Mark, Unfortunately Wireshark does not support extracting SCO or other audio analyse like for A2DP. However that may be changed. Please fill in the bug/enhanced request (so nobody forgot about it) for this feature and please attach example file contains SCO (it is quite rare to see SCO). I already have a proof of concept of (I successfully extract some streams). And yes, SCO must by piped over HCI - otherwise only air logs can contain it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '16, 23:22</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p>Michał Łabędzki<br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></div></div><div id="comments-container-57430" class="comments-container"><span id="57444"></span><div id="comment-57444" class="comment"><div id="post-57444-score" class="comment-score"></div><div class="comment-text"><p>Thanks Michal.</p><p>I am trying to get bluez btmon to generate a btsnoop log (not sure yet if btsnoop log can contain audio packets ?) I know if letting btmon just print to command line there are SCO event prints.</p><p>My attempt to us "btmon -w /tmp/btsnoop.log" was not so great, but hopefully have more luck tomorrow.</p></div><div id="comment-57444-info" class="comment-info"><span class="comment-age">(17 Nov '16, 13:08)</span> Markro</div></div><span id="59834"></span><div id="comment-59834" class="comment"><div id="post-59834-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the long delay here...</p><p>I have a file generated by using btmon -w - not quite sure how I attach it or how I request an enhancement ?</p><p>I am pretty sure the audio on the system I recorded it off sends audio over usb or something, but it seems to print audio packets into the wireshark log so happy days.</p><p>Once I find the submit enhancement page I will add log and request.</p></div><div id="comment-59834-info" class="comment-info"><span class="comment-age">(03 Mar '17, 11:33)</span> Markro</div></div><span id="59835"></span><div id="comment-59835" class="comment"><div id="post-59835-score" class="comment-score"></div><div class="comment-text"><p>Nope, I failed that aptitude test. I cannot find how I make a enhancement request and attach a log file.</p></div><div id="comment-59835-info" class="comment-info"><span class="comment-age">(03 Mar '17, 11:43)</span> Markro</div></div><span id="59840"></span><div id="comment-59840" class="comment"><div id="post-59840-score" class="comment-score"></div><div class="comment-text"><p>I worked it out. I raised enhancement/bug 13451</p></div><div id="comment-59840-info" class="comment-info"><span class="comment-age">(03 Mar '17, 14:16)</span> Markro</div></div></div><div id="comment-tools-57430" class="comment-tools"></div><div class="clear"></div><div id="comment-57430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

