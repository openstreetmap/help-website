+++
type = "question"
title = "Missing Frame and Decrypted SSL data tabs WS v2.2.1"
description = '''Hi All, I am new to networking and using wire shark and I am trying to decrypt SSL/TLS traffic, but I don&#x27;t see either the Frame or Decrypted SSL data tabs at the bottom of the screen. I am using WS version 2.2.1. Any help would be great. Adam'''
date = "2016-12-16T05:47:00Z"
lastmod = "2016-12-20T07:18:00Z"
weight = 58165
keywords = [ "tabs", "missing" ]
aliases = [ "/questions/58165" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing Frame and Decrypted SSL data tabs WS v2.2.1](/questions/58165/missing-frame-and-decrypted-ssl-data-tabs-ws-v221)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58165-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am new to networking and using wire shark and I am trying to decrypt SSL/TLS traffic, but I don't see either the Frame or Decrypted SSL data tabs at the bottom of the screen.</p><p>I am using WS version 2.2.1.</p><p>Any help would be great.</p><p>Adam</p></div><div id="question-tags" class="tags-container tags">tabs missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '16, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/275f9b5f6073ff95d9cbbcebd0232232?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adam-C&#39;s gravatar image" /><p>Adam-C<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adam-C has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Dec '16, 05:49</p></div></div><div id="comments-container-58165" class="comments-container"><span id="58234"></span><div id="comment-58234" class="comment"><div id="post-58234-score" class="comment-score"></div><div class="comment-text"><p>What have you tried?</p></div><div id="comment-58234-info" class="comment-info"><span class="comment-age">(19 Dec '16, 10:41)</span> Lekensteyn</div></div><span id="58254"></span><div id="comment-58254" class="comment"><div id="post-58254-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I was following this tutorial: <a href="https://support.citrix.com/article/CTX116557">https://support.citrix.com/article/CTX116557</a></p><p>But get stuck at the point 6 the part where I need to click on the decrypt SSL TLS data tab as I don't have one, looking at the screen shot in the tutorial I don't have a frame tab either.</p></div><div id="comment-58254-info" class="comment-info"><span class="comment-age">(20 Dec '16, 06:52)</span> Adam-C</div></div></div><div id="comment-tools-58165" class="comment-tools"></div><div class="clear"></div><div id="comment-58165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58255"></span>

<div id="answer-container-58255" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58255-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It would seem that decryption has failed for you. What is the cipher in use? Have you confirmed it's not a DH one? See the note at the top of the tutorial.</p><p>There is also the Wireshark wiki page on <a href="https://wiki.wireshark.org/SSL">SSL</a> that has some test captures that can be decrypted, see <a href="https://wiki.wireshark.org/SSL#Example_capture_file">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '16, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58255" class="comments-container"><span id="58488"></span><div id="comment-58488" class="comment"><div id="post-58488-score" class="comment-score"></div><div class="comment-text"><p>(I converted Graham's comment to an answer because, generically, it is an answer: decryption has likely failed. To know the specific reason we'd need to see the capture file.)</p></div><div id="comment-58488-info" class="comment-info"><span class="comment-age">(03 Jan '17, 15:16)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-58255" class="comment-tools"></div><div class="clear"></div><div id="comment-58255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

