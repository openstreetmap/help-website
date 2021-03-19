+++
type = "question"
title = "IO Graph doesn&#x27;t draw"
description = '''So i successfully logged packets from my server and i now copied the hexdump file to my desktop and opened them in wireshark and i can see all the packages just fine. However, when i open statistics-&amp;gt;iograph, nothing is simply drawn. I have looked at youtube videos and they need no configuration ...'''
date = "2015-03-15T06:38:00Z"
lastmod = "2015-03-18T11:43:00Z"
weight = 40572
keywords = [ "iograph" ]
aliases = [ "/questions/40572" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [IO Graph doesn't draw](/questions/40572/io-graph-doesnt-draw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40572-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So i successfully logged packets from my server and i now copied the hexdump file to my desktop and opened them in wireshark and i can see all the packages just fine.</p><p>However, when i open statistics-&gt;iograph, nothing is simply drawn. I have looked at youtube videos and they need no configuration whatsoever to make the graph visible and i have checked the options.</p><p>I logged the output on my server with ubuntu 14.04 and opened up the hexdump on my desktop running arch linux (so it's a git version of 1.12.3 wireshark)</p><p>Any ideas why it doesn't work?</p><p>Here's a screenshot of how it looks, tried to hide my ip addresses though.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_wCC37e8.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">iograph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '15, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/fcd1d9bdaa1feee2fd77396057fb8f10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johan-bjareholt&#39;s gravatar image" /><p>johan-bjareholt<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johan-bjareholt has one accepted answer">50%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '15, 06:47</p></div></div><div id="comments-container-40572" class="comments-container"><span id="40660"></span><div id="comment-40660" class="comment"><div id="post-40660-score" class="comment-score"></div><div class="comment-text"><p>Please try the following:</p><ul><li>open a sample from here <a href="https://wiki.wireshark.org/SampleCaptures">https://wiki.wireshark.org/SampleCaptures</a> and try the graph</li><li>if it doesn't work try installing wireshark with "pacman -Syu wireshark-gtk wireshark-cli"</li></ul></div><div id="comment-40660-info" class="comment-info"><span class="comment-age">(18 Mar '15, 07:54)</span> Roland</div></div><span id="40665"></span><div id="comment-40665" class="comment"><div id="post-40665-score" class="comment-score"></div><div class="comment-text"><p>The samples works!</p><p>I guess that there's something wrong with my capturing format i guess, will investigate further.</p></div><div id="comment-40665-info" class="comment-info"><span class="comment-age">(18 Mar '15, 10:23)</span> johan-bjareholt</div></div></div><div id="comment-tools-40572" class="comment-tools"></div><div class="clear"></div><div id="comment-40572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40667"></span>

<div id="answer-container-40667" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40667-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found the solution.</p><p>When i saved the file on the server when it wasn't working, i simply saved the stdout from tshark to a file, like this "tshark &gt; test.pcap".</p><p>What i did to make it work, was to instead of just using stdout, i used the -w parameter like this "tshark -w test.pcap" and it now works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '15, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/fcd1d9bdaa1feee2fd77396057fb8f10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johan-bjareholt&#39;s gravatar image" /><p>johan-bjareholt<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johan-bjareholt has one accepted answer">50%</span></p></div></div><div id="comments-container-40667" class="comments-container"></div><div id="comment-tools-40667" class="comment-tools"></div><div class="clear"></div><div id="comment-40667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40637"></span>

<div id="answer-container-40637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40637-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you try clicking the Graph 1, 2, 3, etc buttons?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '15, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/e7d1d3994349a9ea0554a6430dbe2ec8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naskop&#39;s gravatar image" /><p>naskop<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naskop has no accepted answers">0%</span></p></div></div><div id="comments-container-40637" class="comments-container"><span id="40641"></span><div id="comment-40641" class="comment"><div id="post-40641-score" class="comment-score"></div><div class="comment-text"><p>As seen on the screenshot, they are all clicked. Tried again now just to be sure and it's no different.</p></div><div id="comment-40641-info" class="comment-info"><span class="comment-age">(17 Mar '15, 10:18)</span> johan-bjareholt</div></div></div><div id="comment-tools-40637" class="comment-tools"></div><div class="clear"></div><div id="comment-40637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

