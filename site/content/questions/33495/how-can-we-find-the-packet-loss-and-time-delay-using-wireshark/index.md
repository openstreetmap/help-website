+++
type = "question"
title = "how can we find the packet loss and time delay using wireshark"
description = '''how can we find the packet loss and time delay using wireshark'''
date = "2014-06-06T03:10:00Z"
lastmod = "2014-06-09T10:25:00Z"
weight = 33495
keywords = [ "wireshark" ]
aliases = [ "/questions/33495" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how can we find the packet loss and time delay using wireshark](/questions/33495/how-can-we-find-the-packet-loss-and-time-delay-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33495-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can we find the packet loss and time delay using wireshark</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '14, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/84a759b8584868e51394ec196d6ed4af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teju&#39;s gravatar image" /><p>teju<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teju has no accepted answers">0%</span></p></div></div><div id="comments-container-33495" class="comments-container"></div><div id="comment-tools-33495" class="comment-tools"></div><div class="clear"></div><div id="comment-33495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33587"></span>

<div id="answer-container-33587" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33587-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>By capturing at two places, one near the client and one near the server.</p><p>Then compare the two capture files. Unfortunately there is no functionality in Wireshark that does that kind of comparison in a fully automatic way. So, you'll have to do it manually or use a script.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '14, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33587" class="comments-container"><span id="33603"></span><div id="comment-33603" class="comment"><div id="post-33603-score" class="comment-score"></div><div class="comment-text"><p>script means on what way we have to develop that.</p></div><div id="comment-33603-info" class="comment-info"><span class="comment-age">(09 Jun '14, 22:29)</span> teju</div></div><span id="33609"></span><div id="comment-33609" class="comment"><div id="post-33609-score" class="comment-score"></div><div class="comment-text"><p>script means, you will print the content of the two capture files with tshark (see man page of tshark - option <strong>-e</strong>) and then you will process the output with a script in your preferred scripting language (perl, python, etc..).</p></div><div id="comment-33609-info" class="comment-info"><span class="comment-age">(10 Jun '14, 03:30)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33587" class="comment-tools"></div><div class="clear"></div><div id="comment-33587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

