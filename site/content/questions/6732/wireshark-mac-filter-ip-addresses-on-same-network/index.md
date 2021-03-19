+++
type = "question"
title = "wireshark mac filter ip addresses on same network"
description = '''Hi all,  Im having problems with setting up my wireshark correctly. It works on my machine and i can see all packets that are sent/received. But when i try to filter via ip.addr == xx.xx.xxx.xxx, for example, it doesn&#x27;t work. All i am able to see on the wireshark is a few hits from dropbox and i kno...'''
date = "2011-10-05T02:05:00Z"
lastmod = "2011-10-05T08:06:00Z"
weight = 6732
keywords = [ "mac", "filtering", "problems", "iphone", "network" ]
aliases = [ "/questions/6732" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark mac filter ip addresses on same network](/questions/6732/wireshark-mac-filter-ip-addresses-on-same-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6732-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Im having problems with setting up my wireshark correctly. It works on my machine and i can see all packets that are sent/received. But when i try to filter via ip.addr == xx.xx.xxx.xxx, for example, it doesn't work. All i am able to see on the wireshark is a few hits from dropbox and i know the machine that im trying to 'sniff' is on the internet and surfing as its right next to me. I have tired the same concept with iPhones on the same network.</p><p>I am trying to do this wirelessly, not sure if this has any relevance and all the other interfaces that i am trying to sniff are wirelessly connected too.</p><p>Help would be greatly appreciated</p><p>Thanks</p><p>Nicky</p></div><div id="question-tags" class="tags-container tags">mac filtering problems iphone network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '11, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/2b5ceacc861c470afc612d72811198d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gengisnicky31&#39;s gravatar image" /><p>Gengisnicky31<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gengisnicky31 has no accepted answers">0%</span></p></div></div><div id="comments-container-6732" class="comments-container"><span id="6797"></span><div id="comment-6797" class="comment"><div id="post-6797-score" class="comment-score"></div><div class="comment-text"><p>Are you trying to filter packets while they're being captured, so that packets neither to nor from xx.xx.xxx.xxx are discarded and aren't in the capture, or are you trying to filter packets after they're captured?</p></div><div id="comment-6797-info" class="comment-info"><span class="comment-age">(07 Oct '11, 13:30)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-6732" class="comment-tools"></div><div class="clear"></div><div id="comment-6732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6736"></span>

<div id="answer-container-6736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6736-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If using wireless on windows with builtin wireless adapter -&gt; forget it.</p><p>If using wireless on linux -&gt; search for "wireless" in this Q&amp;A and read the top posts, there are detailed answers</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '11, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Oct '11, 08:07</p></div></div><div id="comments-container-6736" class="comments-container"><span id="6764"></span><div id="comment-6764" class="comment"><div id="post-6764-score" class="comment-score"></div><div class="comment-text"><p>Im using Apple Mac OS X 10.6.8, how does this change things now?...</p></div><div id="comment-6764-info" class="comment-info"><span class="comment-age">(06 Oct '11, 15:50)</span> Gengisnicky31</div></div><span id="6776"></span><div id="comment-6776" class="comment"><div id="post-6776-score" class="comment-score"></div><div class="comment-text"><p>Go with the top posts for wireless data capture and try the hints listed there in detail. If that does not provide you with results, please edit your question and precisely describe which steps are not working.</p></div><div id="comment-6776-info" class="comment-info"><span class="comment-age">(07 Oct '11, 01:29)</span> Landi</div></div></div><div id="comment-tools-6736" class="comment-tools"></div><div class="clear"></div><div id="comment-6736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

