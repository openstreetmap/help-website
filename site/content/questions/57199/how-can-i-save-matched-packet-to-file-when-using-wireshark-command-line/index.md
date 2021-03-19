+++
type = "question"
title = "how can I save matched packet to file when using wireshark command line?"
description = '''When I run &quot;Wireshark.exe -R &quot;tcp.options.mss_val == 1460&quot; -w mms1460.cap -r tcp.cap&quot;, wireshark is opened and all packets whose mss=1460 is displayed, but I can not find where is &quot;mss1460.cap&quot;,why? Thanks a lot'''
date = "2016-11-09T00:41:00Z"
lastmod = "2016-11-09T03:17:00Z"
weight = 57199
keywords = [ "wireshark" ]
aliases = [ "/questions/57199" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how can I save matched packet to file when using wireshark command line?](/questions/57199/how-can-i-save-matched-packet-to-file-when-using-wireshark-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57199-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I run "Wireshark.exe -R "tcp.options.mss_val == 1460" -w mms1460.cap -r tcp.cap", wireshark is opened and all packets whose mss=1460 is displayed, but I can not find where is "mss1460.cap",why? Thanks a lot</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '16, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/069467bd1edc7bb03aa0fb74d7e673af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="w44524&#39;s gravatar image" /><p>w44524<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="w44524 has no accepted answers">0%</span></p></div></div><div id="comments-container-57199" class="comments-container"><span id="57202"></span><div id="comment-57202" class="comment"><div id="post-57202-score" class="comment-score"></div><div class="comment-text"><p>leaving aside that the command line says m<strong>m</strong>s1460.cap and you then look for m<strong>s</strong>s1460.cap, I'd assume that you should run tshark instead of Wireshark to get the output file written. The explanation of -w in Wireshark manual suggests that it indicates where to save the captured data, so maybe it is not taken into account if you don't actually capture.</p></div><div id="comment-57202-info" class="comment-info"><span class="comment-age">(09 Nov '16, 02:13)</span> sindy</div></div></div><div id="comment-tools-57199" class="comment-tools"></div><div class="clear"></div><div id="comment-57199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57204"></span>

<div id="answer-container-57204" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57204-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As Sindy is saying, you better use tshark, the tool intended for that purpose. The command in tshark is quite similar. You only need to change the -R for the filter to -Y</p><p>tshark.exe -Y "tcp.options.mss_val == 1460" -w mms1460.cap -r tcp.cap</p><p>In the Wireshark manual I see that -w is to "set the name of the file to be used to save captured packets" so I'm guessing if that switch is only intended for capturing traffic and writing the output and not when you;re reading the trace.</p><p>Hope this helps</p><p>Osito</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '16, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/0e9b510379013638f59658b49d7d38cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osito&#39;s gravatar image" /><p>osito<br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osito has one accepted answer">50%</span></p></div></div><div id="comments-container-57204" class="comments-container"></div><div id="comment-tools-57204" class="comment-tools"></div><div class="clear"></div><div id="comment-57204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

