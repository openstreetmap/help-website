+++
type = "question"
title = "troubleshooting &quot;Bogus IP length&quot;. Causes?"
description = '''I have two identical win7x64 machines on different drops - one of them gets numerous &quot;Bogus IP length&quot; packets in the capture. About every 10 seconds there will appear 7 or 8 of these all at once. The other machine gets none. What can be the problem here? is it layer 1, as I suspect? Or could it be ...'''
date = "2011-03-04T11:41:00Z"
lastmod = "2011-03-05T16:40:00Z"
weight = 2667
keywords = [ "length", "bogus", "bogusiplength", "windows7" ]
aliases = [ "/questions/2667" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [troubleshooting "Bogus IP length". Causes?](/questions/2667/troubleshooting-bogus-ip-length-causes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2667-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two identical win7x64 machines on different drops - one of them gets numerous "Bogus IP length" packets in the capture. About every 10 seconds there will appear 7 or 8 of these all at once. The other machine gets none. What can be the problem here? is it layer 1, as I suspect? Or could it be software layer?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">length bogus bogusiplength windows7</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '11, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/debbec791e8c495049db26aefbcc40b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peakbagger66&#39;s gravatar image" /><p>Peakbagger66<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peakbagger66 has no accepted answers">0%</span></p></div></div><div id="comments-container-2667" class="comments-container"></div><div id="comment-tools-2667" class="comment-tools"></div><div class="clear"></div><div id="comment-2667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2679"></span>

<div id="answer-container-2679" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2679-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are saying these are incoming, so I'm curious what they look like on the wire just before the pc receives them. So I'd bring up a pc on a span port of a switch and look at the packets in both locations. My initial guess is that it is something that the network card on the receiving pc is doing. Maybe some type of hardware offloading or something.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '11, 16:40</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-2679" class="comments-container"><span id="2706"></span><div id="comment-2706" class="comment"><div id="post-2706-score" class="comment-score"></div><div class="comment-text"><p>Or perhaps the offloading is being done on the <em>sending</em> PC, i.e. on the machine running Wireshark; are the packets in question being sent by that machine?</p></div><div id="comment-2706-info" class="comment-info"><span class="comment-age">(07 Mar '11, 18:37)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-2679" class="comment-tools"></div><div class="clear"></div><div id="comment-2679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

