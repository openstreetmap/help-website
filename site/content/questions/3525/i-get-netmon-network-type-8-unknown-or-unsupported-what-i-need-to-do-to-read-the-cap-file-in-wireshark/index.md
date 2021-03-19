+++
type = "question"
title = "I get (netmon: network type 8 unknown or unsupported) - what I need to do to read the cap file in wireshark?"
description = '''I am using netmonitor 3.4 to capture wireless traffic, because it supports dialup mode devices. When I use editcap or wireshark, I get the above message. i do not have this problem on Vista, only on Windows 7.0 captured files. Is there something I can do - Use Wireshark 1.2.x , capture only on one d...'''
date = "2011-04-15T15:11:00Z"
lastmod = "2011-04-15T15:58:00Z"
weight = 3525
keywords = [ "netmonitor", "nmcap", "microsoft" ]
aliases = [ "/questions/3525" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I get (netmon: network type 8 unknown or unsupported) - what I need to do to read the cap file in wireshark?](/questions/3525/i-get-netmon-network-type-8-unknown-or-unsupported-what-i-need-to-do-to-read-the-cap-file-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3525-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using netmonitor 3.4 to capture wireless traffic, because it supports dialup mode devices. When I use editcap or wireshark, I get the above message. i do not have this problem on Vista, only on Windows 7.0 captured files.</p><p>Is there something I can do - Use Wireshark 1.2.x , capture only on one device instead of all devices?</p></div><div id="question-tags" class="tags-container tags">netmonitor nmcap microsoft</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '11, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/2a048182e9434b4b16a795e30a508480?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwk&#39;s gravatar image" /><p>mwk<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwk has no accepted answers">0%</span></p></div></div><div id="comments-container-3525" class="comments-container"></div><div id="comment-tools-3525" class="comment-tools"></div><div class="clear"></div><div id="comment-3525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3526"></span>

<div id="answer-container-3526" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3526-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Funny you should ask....</p><p>I'm just in the midst of updating Wireshark so it will handle netmon capture files "type 7", "type 8" and "type 9" "Media Types".</p><p>I expect that I'll commit a fix within the next several days.</p><p>Once I've done that, if you want, you'll be able to download a development Wireshark which will be able to handle "type 8" records.</p><p>I don't know of any workaround; maybe someone else will have a suggestion.</p><p>P.S. It would be much appreciated if you could post a bug on bugzilla.wireshark.org and attach a (small) capture file which I can use for testing. (The capture file attachment can be marked private if necessary).</p><p>Re: i do not have this problem on Vista, only on Windows 7.0 captured files.</p><p>I would find it useful if you could also provide a (short) capture file taken on Vista so i can compare it against a capture taken on Windows 7.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '11, 15:58</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Apr '11, 16:11</p></div></div><div id="comments-container-3526" class="comments-container"></div><div id="comment-tools-3526" class="comment-tools"></div><div class="clear"></div><div id="comment-3526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

