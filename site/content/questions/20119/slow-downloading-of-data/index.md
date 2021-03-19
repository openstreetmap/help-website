+++
type = "question"
title = "Slow downloading of data"
description = '''We are facing issue with slow downloading of data from any website whether inside our network or on internet. Could someone please help me with document that could help us isolate cause of issue.'''
date = "2013-04-05T10:12:00Z"
lastmod = "2013-12-13T23:38:00Z"
weight = 20119
keywords = [ "download", "wireshark" ]
aliases = [ "/questions/20119" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Slow downloading of data](/questions/20119/slow-downloading-of-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20119-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are facing issue with slow downloading of data from any website whether inside our network or on internet. Could someone please help me with document that could help us isolate cause of issue.</p></div><div id="question-tags" class="tags-container tags">download wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '13, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/6615a61d69b703d89076bb0f18342bbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m_1607&#39;s gravatar image" /><p>m_1607<br />
<span class="score" title="35 reputation points">35</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m_1607 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Apr '13, 08:54</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-20119" class="comments-container"><span id="20134"></span><div id="comment-20134" class="comment"><div id="post-20134-score" class="comment-score"></div><div class="comment-text"><blockquote><p>slow downloading of data from any website</p></blockquote><p>do you mean low download rate or slow start of connections?</p><blockquote><p>whether inside our network or on internet.</p></blockquote><p>do you mean this: You see this issue on the <strong>same</strong> PC/Laptop no matter if it is connected to your internal network or any other network?</p></div><div id="comment-20134-info" class="comment-info"><span class="comment-age">(06 Apr '13, 09:11)</span> Kurt Knochner ♦</div></div><span id="20145"></span><div id="comment-20145" class="comment"><div id="post-20145-score" class="comment-score"></div><div class="comment-text"><p>Sorry not giving enough explanation.</p><p>Yes all traffic on complete network is slow from all pc . and looking from firewall to ISP no packet loss. Just wish to understand where to start to isolate this.</p></div><div id="comment-20145-info" class="comment-info"><span class="comment-age">(06 Apr '13, 22:17)</span> m_1607</div></div></div><div id="comment-tools-20119" class="comment-tools"></div><div class="clear"></div><div id="comment-20119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20127"></span>

<div id="answer-container-20127" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20127-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll have to do packet captures that document the problem while it occurs and then analyze the cause. While this may sound simple it requires a certain skill to do it right, so maybe the answers to <a href="http://ask.wireshark.org/questions/19980/how-to-study-to-use-wireshark">this</a> questions can help with getting there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '13, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20127" class="comments-container"></div><div id="comment-tools-20127" class="comment-tools"></div><div class="clear"></div><div id="comment-20127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28098"></span>

<div id="answer-container-28098" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28098-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the problem may be in your internet connection . So, boost up your internet connection by using the following steps :</p><ol><li>Clear cookies from your browser</li><li>Close unwanted background tasks when you are working with the internet .</li><li>Scan your internet by using standard Anti-virus software</li><li>Reset your modem and reconnect with the internet.</li><li>Test your internet speed often by using <a href="http://www.scanmyspeed.com/">Scanmyspeed.com</a></li></ol><p>After that, you can try to download data from any site and see the improvement .</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 23:38</strong></p><img src="https://secure.gravatar.com/avatar/c9650cc3fbbbb7b8a9c5d7788eafee3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="creamuser&#39;s gravatar image" /><p>creamuser<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="creamuser has no accepted answers">0%</span></p></div></div><div id="comments-container-28098" class="comments-container"></div><div id="comment-tools-28098" class="comment-tools"></div><div class="clear"></div><div id="comment-28098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

