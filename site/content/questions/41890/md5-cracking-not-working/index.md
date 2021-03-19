+++
type = "question"
title = "md5 cracking not working"
description = '''Hi, so i was able to sniff packets from my network and i got my username and password but the password was not in plain text. Here is the details Form item: &quot;username&quot; = &quot;work&quot;  Key: username  Value: work  Form item: &quot;password&quot; = &quot;c7bcd01cacc676d4b0a0a83b696dabc9&quot;  Key: password  Value: c7bcd01cacc6...'''
date = "2015-04-27T08:21:00Z"
lastmod = "2015-04-27T08:52:00Z"
weight = 41890
keywords = [ "wireshark", "md5" ]
aliases = [ "/questions/41890" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [md5 cracking not working](/questions/41890/md5-cracking-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41890-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, so i was able to sniff packets from my network and i got my username and password but the password was not in plain text. Here is the details</p><p>Form item: "username" = "work" Key: username Value: work Form item: "password" = "c7bcd01cacc676d4b0a0a83b696dabc9" Key: password Value: c7bcd01cacc676d4b0a0a83b696dabc9</p><p>and then i tried decrypting the password using an md5 decrypter but it gave me an error about not finding any hashes. What could the problem be?</p></div><div id="question-tags" class="tags-container tags">wireshark md5</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '15, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/07e0106d0a725b0de1b4c95fec8cb048?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="orobogenius&#39;s gravatar image" /><p>orobogenius<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="orobogenius has no accepted answers">0%</span></p></div></div><div id="comments-container-41890" class="comments-container"></div><div id="comment-tools-41890" class="comment-tools"></div><div class="clear"></div><div id="comment-41890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41894"></span>

<div id="answer-container-41894" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41894-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't turn an md5 hash back into a password. What you can do, and I suspect this is what your "decrypter" does, is to create a database of md5 hashes of all the possible passwords (a <a href="http://en.wikipedia.org/wiki/Rainbow_table">rainbow table</a>), then look up your hash in the database. If it's there, bingo, if it's not, then you need a better rainbow table.</p><p>Note there may be multiple passwords that hash to the same value as it's known that md5 suffers from <a href="http://en.wikipedia.org/wiki/MD5#Collision_vulnerabilities">hash collisions</a>.</p><p>Also note that this is pretty much off-topic for this site.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '15, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Apr '15, 08:52</p></div></div><div id="comments-container-41894" class="comments-container"></div><div id="comment-tools-41894" class="comment-tools"></div><div class="clear"></div><div id="comment-41894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

