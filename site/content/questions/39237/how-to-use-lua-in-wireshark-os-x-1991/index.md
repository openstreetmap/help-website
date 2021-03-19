+++
type = "question"
title = "How to use lua in wireshark os x 1.99.1"
description = '''Hi, It recognizes my LUA script in About-&amp;gt;Plugins but i can&#x27;t figure out how to apply the filter to my pcap. In the Windows version there is a Tools menu that lets me select the dissector, but in the 1.99.1 version for OS X I don&#x27;t see a tools menu. Is it just missing in this release or is there ...'''
date = "2015-01-17T20:35:00Z"
lastmod = "2015-01-18T08:14:00Z"
weight = 39237
keywords = [ "os", "tools", "lua", "osx" ]
aliases = [ "/questions/39237" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use lua in wireshark os x 1.99.1](/questions/39237/how-to-use-lua-in-wireshark-os-x-1991)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39237-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>It recognizes my LUA script in About-&gt;Plugins but i can't figure out how to apply the filter to my pcap. In the Windows version there is a Tools menu that lets me select the dissector, but in the 1.99.1 version for OS X I don't see a tools menu. Is it just missing in this release or is there another way to use the dissector.</p><p>Thank you, Dan</p></div><div id="question-tags" class="tags-container tags">os tools lua osx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '15, 20:35</strong></p><img src="https://secure.gravatar.com/avatar/028bda98b466e74870b70347cfe66b01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="musca999&#39;s gravatar image" /><p>musca999<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="musca999 has no accepted answers">0%</span></p></div></div><div id="comments-container-39237" class="comments-container"></div><div id="comment-tools-39237" class="comment-tools"></div><div class="clear"></div><div id="comment-39237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39243"></span>

<div id="answer-container-39243" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39243-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On OSX, the 1.99.x version's default GUI is <a href="http://en.wikipedia.org/wiki/Qt_(software)">Qt-based</a> instead of <a href="http://en.wikipedia.org/wiki/GTK%2B">GTK-based</a>. The Qt version is better in many ways, but unfortunately it does not yet have all the features the GTK-based Wireshark has; one of the missing things is GUI access for Lua plugins. Adding menu items, creating new windows, etc., is all missing for Lua in Qt-based Wireshark.</p><p>But why do you need it? Why does your dissector need to be invoked from the Tools menu, or why does a filter need to be invoked from the Tools menu?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '15, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39243" class="comments-container"></div><div id="comment-tools-39243" class="comment-tools"></div><div class="clear"></div><div id="comment-39243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

