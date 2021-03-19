+++
type = "question"
title = "Fileshark_pcap.lua not working with Wireshark 2.0.0"
description = '''I am trying to get the Fileshark_pcap.lua example on the wiki page to parse a pcap recording.  https://wiki.wireshark.org/Lua/Examples My configuration: Windows 10, Wireshark 2.0.0 x64 I copied both the fileshark_pcap.lua and linktype.lua into my personal plugins folder. In the about dialog under th...'''
date = "2015-11-19T20:54:00Z"
lastmod = "2015-11-20T01:12:00Z"
weight = 47780
keywords = [ "lua", "2.0", "file" ]
aliases = [ "/questions/47780" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Fileshark\_pcap.lua not working with Wireshark 2.0.0](/questions/47780/fileshark_pcaplua-not-working-with-wireshark-200)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47780-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to get the Fileshark_pcap.lua example on the wiki page to parse a pcap recording. <a href="https://wiki.wireshark.org/Lua/Examples">https://wiki.wireshark.org/Lua/Examples</a></p><p>My configuration: Windows 10, Wireshark 2.0.0 x64</p><p>I copied both the fileshark_pcap.lua and linktype.lua into my personal plugins folder. In the about dialog under the plugins tab I see both lua scripts listed. I also see the PCAPFILE protocol in the preferences.</p><p>When using the file open windows I do not have an option for "Fileshark", thus I am unable to load a pcap file with the lua plugin. I also tried from the command line with no success as well.</p><p>If anyone can point me in the right direction that would be appreciated.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">lua 2.0 file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '15, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/334b3772ba24e093b1c83a07da9e12c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20B&#39;s gravatar image" /><p>Rob B<br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob B has no accepted answers">0%</span></p></div></div><div id="comments-container-47780" class="comments-container"></div><div id="comment-tools-47780" class="comment-tools"></div><div class="clear"></div><div id="comment-47780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47782"></span>

<div id="answer-container-47782" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47782-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Works for me.</p><p>Are you setting the correct option for Fileshark Pcap? The droplist to set is <strong>not</strong> the "Files of type:" one, it's the second droplist that doesn't have a label in between the "Read Filter:" edit box and the "MAC name resolution" checkbox.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '15, 01:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Nov '15, 06:34</p></div></div><div id="comments-container-47782" class="comments-container"><span id="47788"></span><div id="comment-47788" class="comment"><div id="post-47788-score" class="comment-score"></div><div class="comment-text"><p>That was it. Thanks.</p></div><div id="comment-47788-info" class="comment-info"><span class="comment-age">(20 Nov '15, 05:30)</span> Rob B</div></div></div><div id="comment-tools-47782" class="comment-tools"></div><div class="clear"></div><div id="comment-47782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

