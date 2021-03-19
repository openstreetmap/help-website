+++
type = "question"
title = "How can I find my 3G network card in the &#x27;interface&#x27;?"
description = '''Test system1: Windows7 home edition Software ver.: wireshark-win64-1.6.7.exe Question: Afer the installation of wireshark, I run it, I can see my 3G network card(Huawei E367) on the dailog: capture-- interface. Second day, I run wireshark again, but I can&#x27;t find my 3G network card. I check the NPF d...'''
date = "2012-04-14T23:28:00Z"
lastmod = "2012-04-14T23:43:00Z"
weight = 10154
keywords = [ "3g", "network", "card" ]
aliases = [ "/questions/10154" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I find my 3G network card in the 'interface'?](/questions/10154/how-can-i-find-my-3g-network-card-in-the-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10154-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Test system1: Windows7 home edition Software ver.: wireshark-win64-1.6.7.exe Question: Afer the installation of wireshark, I run it, I can see my 3G network card(Huawei E367) on the dailog: capture-- interface. Second day, I run wireshark again, but I can't find my 3G network card. I check the NPF driver, it is normal running. Why? Test system2: Windows xp professional Software ver.: wireshark-win32-1.6.7.exe Question: The phenomenon is the same as test system1. Why?</p></div><div id="question-tags" class="tags-container tags">3g network card</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '12, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/0fc286a3f846dcf16911c529ee8136f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bryan%20Liu&#39;s gravatar image" /><p>Bryan Liu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bryan Liu has no accepted answers">0%</span></p></div></div><div id="comments-container-10154" class="comments-container"></div><div id="comment-tools-10154" class="comment-tools"></div><div class="clear"></div><div id="comment-10154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10156"></span>

<div id="answer-container-10156" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10156-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Why?</p></blockquote><p>Because mobile phone modems show up as PPP connections, Wireshark uses WinPcap to capture traffic on Windows, and <a href="http://www.winpcap.org/misc/faq.htm#Q-5">WinPcap can't handle PPP connections on Windows 7 and requires special work to handle them on Windows XP</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '12, 23:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10156" class="comments-container"><span id="10160"></span><div id="comment-10160" class="comment"><div id="post-10160-score" class="comment-score"></div><div class="comment-text"><p>As you know, I can capture the Huawei 3G network card data flow while I run wireshark first time. But the second time, Huawei 3G network card can not be shown in the 'Interface', so I am confused. How can I make the definite object shown in the interface of wireshark?</p></div><div id="comment-10160-info" class="comment-info"><span class="comment-age">(15 Apr '12, 04:31)</span> Bryan Liu</div></div></div><div id="comment-tools-10156" class="comment-tools"></div><div class="clear"></div><div id="comment-10156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

