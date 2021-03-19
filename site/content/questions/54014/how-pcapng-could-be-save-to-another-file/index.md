+++
type = "question"
title = "how pcapng could be save to another file?"
description = '''Hello, do anyone know to deal with it? I have a captured *.pcapng file and it has lots of data. I hope to filter specified port&#x27;s log to another pacapng file in command line. Could it be possible? If Wireshark/tshark does not provide this method, whether it is possible to complete it with lua? Thank...'''
date = "2016-07-12T19:03:00Z"
lastmod = "2016-07-12T23:47:00Z"
weight = 54014
keywords = [ "to", "line", "save", "command" ]
aliases = [ "/questions/54014" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how pcapng could be save to another file?](/questions/54014/how-pcapng-could-be-save-to-another-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54014-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, do anyone know to deal with it?</p><p>I have a captured *.pcapng file and it has lots of data. I hope to filter specified port's log to another pacapng file in command line. Could it be possible?</p><p>If Wireshark/tshark does not provide this method, whether it is possible to complete it with lua?</p><p>Thanks a lot.</p></div><div id="question-tags" class="tags-container tags">to line save command</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '16, 19:03</strong></p><img src="https://secure.gravatar.com/avatar/63ae5524674656eabfec055769fb0b35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Youping%20Kang&#39;s gravatar image" /><p>Youping Kang<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Youping Kang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jul '16, 00:29</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-54014" class="comments-container"></div><div id="comment-tools-54014" class="comment-tools"></div><div class="clear"></div><div id="comment-54014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54018"></span>

<div id="answer-container-54018" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54018-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can certainly do that with Wireshark. Load the file, apply a display filter to select only those packets you are interested in, then save the file selecting to save only those frames shown.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '16, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54018" class="comments-container"><span id="54054"></span><div id="comment-54054" class="comment"><div id="post-54054-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jaap. But what I will filter is volume data and thousands of files. I could not operate this way one by one. So I need a way in command line.</p></div><div id="comment-54054-info" class="comment-info"><span class="comment-age">(13 Jul '16, 21:29)</span> Youping Kang</div></div><span id="54055"></span><div id="comment-54055" class="comment"><div id="post-54055-score" class="comment-score"></div><div class="comment-text"><p>The command line tool is called tshark, the manual is <a href="https://www.wireshark.org/docs/man-pages/tshark.html">here</a>.</p><p>In short, you would use</p><p><code>tshark -r original_pcapng_to_be_filtered -Y "your_display_filter_expression" -w filtered_pcapng_file_to_be_written</code>.</p><p>You'll use a script to provide the input and output file names.</p></div><div id="comment-54055-info" class="comment-info"><span class="comment-age">(14 Jul '16, 00:33)</span> sindy</div></div></div><div id="comment-tools-54018" class="comment-tools"></div><div class="clear"></div><div id="comment-54018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

