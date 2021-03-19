+++
type = "question"
title = "How to capture the data sent from forms on websites?"
description = '''Hi! Is it possible to capture the data that is sent from forms on websites? If I use Firebug I can see what data that was sent from all the fields in a form, but I should see the same data in Wireshark, but I cannot. Isn´t it possible or am I doing something wrong?'''
date = "2010-12-28T01:45:00Z"
lastmod = "2010-12-29T05:17:00Z"
weight = 1494
keywords = [ "forms", "data", "http" ]
aliases = [ "/questions/1494" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture the data sent from forms on websites?](/questions/1494/how-to-capture-the-data-sent-from-forms-on-websites)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1494-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! Is it possible to capture the data that is sent from forms on websites?</p><p>If I use Firebug I can see what data that was sent from all the fields in a form, but I should see the same data in Wireshark, but I cannot. Isn´t it possible or am I doing something wrong?</p></div><div id="question-tags" class="tags-container tags">forms data http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '10, 01:45</strong></p><img src="https://secure.gravatar.com/avatar/b40d415d5a5ed5142e38ad841b2e176a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rox&#39;s gravatar image" /><p>Rox<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rox has no accepted answers">0%</span></p></div></div><div id="comments-container-1494" class="comments-container"></div><div id="comment-tools-1494" class="comment-tools"></div><div class="clear"></div><div id="comment-1494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1506"></span>

<div id="answer-container-1506" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1506-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is possible to have a https action on an http page. The action must simply fully identify the action with a complete uri including 'https'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '10, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1506" class="comments-container"></div><div id="comment-tools-1506" class="comment-tools"></div><div class="clear"></div><div id="comment-1506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1495"></span>

<div id="answer-container-1495" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1495-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Rox, forms datas are also displayed in wireshark but it's less user-friendly than Firebug !</p><p>GET method datas are displayed in the http.request.uri field whereas POST method datas are displayed as Line-based text data.</p><p>P.S. : HttpFox is a very good http analyzer on Firefox (<a href="https://addons.mozilla.org/en-US/firefox/addon/6647/">https://addons.mozilla.org/en-US/firefox/addon/6647/</a> )</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '10, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/2282d6ca42253cbf6aa80c00be6af1b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manux&#39;s gravatar image" /><p>manux<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manux has no accepted answers">0%</span></p></div></div><div id="comments-container-1495" class="comments-container"></div><div id="comment-tools-1495" class="comment-tools"></div><div class="clear"></div><div id="comment-1495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1500"></span>

<div id="answer-container-1500" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1500-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for your answer!</p><p>I found the text in this post with Wireshark, but not when I log in into services that´s not using SSL, for instance Facebook (I am using their non-SSL-login). I am just getting the cookies sent from Facebook and some other stuff, but I cannot see the POST data that was sent from my computer. How come?</p><p>EDIT: Now I see that the POST action is to a HTTPS server. But http://www.facebook.com is not HTTPS, so how is it possible to send encrypted data from HTTP to HTTPS? I thought both ends would have to be HTTPS?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '10, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/b40d415d5a5ed5142e38ad841b2e176a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rox&#39;s gravatar image" /><p>Rox<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rox has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Dec '10, 08:37</p></div></div><div id="comments-container-1500" class="comments-container"></div><div id="comment-tools-1500" class="comment-tools"></div><div class="clear"></div><div id="comment-1500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

