+++
type = "question"
title = "How to only capture http info (not just filter)"
description = '''Hi, im looking for a way to use wireshark to only capture http data. Im doing really long captures that seem to slow my vietual machine nearly to a stop. Is there a way i can set it so it only capturea the http information? I dont just want to filter the info but get it so i only have the http stuff...'''
date = "2016-10-16T07:21:00Z"
lastmod = "2016-10-17T03:10:00Z"
weight = 56422
keywords = [ "http" ]
aliases = [ "/questions/56422" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to only capture http info (not just filter)](/questions/56422/how-to-only-capture-http-info-not-just-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56422-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, im looking for a way to use wireshark to only capture http data. Im doing really long captures that seem to slow my vietual machine nearly to a stop. Is there a way i can set it so it only capturea the http information? I dont just want to filter the info but get it so i only have the http stuff jn the capture. Many thanks for any help.</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '16, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/02ee5258c47902d7e590a0eea45d5d0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msriptide&#39;s gravatar image" /><p>msriptide<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msriptide has no accepted answers">0%</span></p></div></div><div id="comments-container-56422" class="comments-container"></div><div id="comment-tools-56422" class="comment-tools"></div><div class="clear"></div><div id="comment-56422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56441"></span>

<div id="answer-container-56441" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56441-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you should use a capture filter :</p><p>Link to WireSharks explanation: <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html">Capture Filter</a></p><p>(edit: typo)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '16, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/d945ac48625d4aef83f374f01ffa946c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SynAck&#39;s gravatar image" /><p>SynAck<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SynAck has one accepted answer">33%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '16, 03:10</p></div></div><div id="comments-container-56441" class="comments-container"><span id="56442"></span><div id="comment-56442" class="comment"><div id="post-56442-score" class="comment-score"></div><div class="comment-text"><p>In practical terms, it means a capture filter like <code>tcp port 80</code> if the http traffic you are after uses the default port at server side. If it uses other ports, let the capture filter allow packets to/from these tcp ports in as well. However, if you do not know in advance which ports are used, you'd be better off with capturing everything (or at least all tcp packets) using a ring buffer of files in tshark, and then analyze the result files one by one using Wireshark. After the initial analysis, you may filter parts of a single tcp stream from several such files into new files and merge the new ones together to have the whole tcp session in a single file.</p></div><div id="comment-56442-info" class="comment-info"><span class="comment-age">(17 Oct '16, 03:17)</span> sindy</div></div><span id="56473"></span><div id="comment-56473" class="comment"><div id="post-56473-score" class="comment-score"></div><div class="comment-text"><p>The problem i have is that is sniffing wireless traffic, if i use port filtering it doesn't capture the handshake and im not getting any data. is there anything else i can do? if i leave it for more than half an hour the files get really large and almost crash my system</p></div><div id="comment-56473-info" class="comment-info"><span class="comment-age">(17 Oct '16, 10:48)</span> msriptide</div></div><span id="56474"></span><div id="comment-56474" class="comment"><div id="post-56474-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><p>is there anything else i can do?</p></blockquote></blockquote><p>Can you move to wired capture? With encrypted wireless, you will only be able to single out data or qos-data frames until you perform the decryption step. Plus you can't be 100% sure you will always be able to decrypt - there is a non-zero probability that you will have packet loss so you may miss one or more EAPOL frames, and not be able to decrypt for that session (until the next session timeout occurs or whatever).</p><p>I would work really hard to move to wired capture mechanism and use a capture filter as @sindy suggested.</p><p>Also Wireshark should NOT be your long term capture solution. Due to the ever-increasing memory consumption, it's the wrong tool. Look at dumpcap, tcpdump, or windump for long term capture. I limit my wireless capture files to 200MB, and post process with various tshark commands to strip out things that I may want.</p></div><div id="comment-56474-info" class="comment-info"><span class="comment-age">(17 Oct '16, 11:10)</span> Bob Jones</div></div></div><div id="comment-tools-56441" class="comment-tools"></div><div class="clear"></div><div id="comment-56441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

