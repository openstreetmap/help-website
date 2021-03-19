+++
type = "question"
title = "PCAP file can&#x27;t be opened"
description = '''Hi, Im trying to open a .pcap file but with no luck. I was told I need an older version of Wireshark to open it (no idea why) But I tried 1.6.6, 1.7.1, 1.8.6 and the newest, but without any luck It is a sample od DSS1 communication. Can anyone help? File can be found here: https://www.dropbox.com/s/...'''
date = "2014-10-12T14:50:00Z"
lastmod = "2014-10-12T14:56:00Z"
weight = 36990
keywords = [ "pcap", "wireshark" ]
aliases = [ "/questions/36990" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PCAP file can't be opened](/questions/36990/pcap-file-cant-be-opened)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36990-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Im trying to open a .pcap file but with no luck. I was told I need an older version of Wireshark to open it (no idea why) But I tried 1.6.6, 1.7.1, 1.8.6 and the newest, but without any luck</p><p>It is a sample od DSS1 communication. Can anyone help?</p><p>File can be found here: <a href="https://www.dropbox.com/s/piub0v87leqocst/SS_zadani_protokol_C.pcap">https://www.dropbox.com/s/piub0v87leqocst/SS_zadani_protokol_C.pcap</a></p></div><div id="question-tags" class="tags-container tags">pcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '14, 14:50</strong></p><img src="https://secure.gravatar.com/avatar/d0535852551beb656ffcd93cc3301cdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Salamander&#39;s gravatar image" /><p>Salamander<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Salamander has no accepted answers">0%</span></p></div></div><div id="comments-container-36990" class="comments-container"></div><div id="comment-tools-36990" class="comment-tools"></div><div class="clear"></div><div id="comment-36990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36991"></span>

<div id="answer-container-36991" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36991-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's because that file is not a PCAP file, it's plain ASCII you can open in any text editor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '14, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36991" class="comments-container"><span id="36992"></span><div id="comment-36992" class="comment"><div id="post-36992-score" class="comment-score"></div><div class="comment-text"><p>Jesus, I feel really stupid :D Any way to import it to WS?</p></div><div id="comment-36992-info" class="comment-info"><span class="comment-age">(12 Oct '14, 14:57)</span> Salamander</div></div><span id="36993"></span><div id="comment-36993" class="comment"><div id="post-36993-score" class="comment-score"></div><div class="comment-text"><p>No, I don't think Wireshark can read files like that.</p><p>You may be lucky and be able to convert the file from ASCII to PCAP binary format by using text2pcap (a command line tool installed together with Wireshark), but I'm not sure it's worth the hassle - your file doesn't look like it's formatted in a way you can convert it, but I may be wrong.</p></div><div id="comment-36993-info" class="comment-info"><span class="comment-age">(12 Oct '14, 15:02)</span> Jasper ♦♦</div></div><span id="36994"></span><div id="comment-36994" class="comment"><div id="post-36994-score" class="comment-score"></div><div class="comment-text"><p>but the weird thing is that the file really worked on Wireshark on another machine ... it was version 1.6.6, and it was imported with no problem</p></div><div id="comment-36994-info" class="comment-info"><span class="comment-age">(12 Oct '14, 15:05)</span> Salamander</div></div></div><div id="comment-tools-36991" class="comment-tools"></div><div class="clear"></div><div id="comment-36991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

