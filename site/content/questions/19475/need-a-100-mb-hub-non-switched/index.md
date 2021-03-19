+++
type = "question"
title = "Need a 100 mb hub non switched"
description = '''I need to monitor a PBX for SIP traffic and do not have a monitor port. The switch will only run at 100 mb. Netgear makes a 10/100 hub the ds104 or ds108. Will this work? It appears to be un switched? Has anyone else found a 100 mb hub that did work?'''
date = "2013-03-13T14:30:00Z"
lastmod = "2013-03-13T15:17:00Z"
weight = 19475
keywords = [ "sip" ]
aliases = [ "/questions/19475" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need a 100 mb hub non switched](/questions/19475/need-a-100-mb-hub-non-switched)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19475-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to monitor a PBX for SIP traffic and do not have a monitor port. The switch will only run at 100 mb. Netgear makes a 10/100 hub the ds104 or ds108. Will this work? It appears to be un switched? Has anyone else found a 100 mb hub that did work?</p></div><div id="question-tags" class="tags-container tags">sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '13, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/ddb1621d607db50275e5299fab372bbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mserino&#39;s gravatar image" /><p>mserino<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mserino has no accepted answers">0%</span></p></div></div><div id="comments-container-19475" class="comments-container"></div><div id="comment-tools-19475" class="comment-tools"></div><div class="clear"></div><div id="comment-19475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19476"></span>

<div id="answer-container-19476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19476-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I really think we should get away from using hubs for network analysis. How about the Netgear GS105E? This is a 10/100/1000 MB switch with port mirroring capability. Use this in place of the hub. The port mirroring capability will let you mirror the PBX traffic to the port that your Wireshark system is plugged into, but since it's not a hub, it won't blast all traffic out all ports. It's inexpensive, although not as cheap as a DS104, and small enough to be easily carried around. Also, you'll be able to use this same switch later when you want to monitor a Gigabit link, which you can't do with the 10/100 MB DS104/108.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19476" class="comments-container"><span id="19479"></span><div id="comment-19479" class="comment"><div id="post-19479-score" class="comment-score">1</div><div class="comment-text"><p>Make sure you get the 105e. They also make a plain 105 that doesn't do port mirroring.</p></div><div id="comment-19479-info" class="comment-info"><span class="comment-age">(13 Mar '13, 16:14)</span> grahamb ♦</div></div><span id="19487"></span><div id="comment-19487" class="comment"><div id="post-19487-score" class="comment-score"></div><div class="comment-text"><p>And that's just one of over 20 options to choose from. They're all <a href="http://wiki.wireshark.org/SwitchReference">listed on the Wiki</a>.</p></div><div id="comment-19487-info" class="comment-info"><span class="comment-age">(14 Mar '13, 00:08)</span> Jaap ♦</div></div></div><div id="comment-tools-19476" class="comment-tools"></div><div class="clear"></div><div id="comment-19476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

