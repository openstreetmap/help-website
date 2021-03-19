+++
type = "question"
title = "mb&#x27;s vs gb&#x27;s"
description = '''we r trying to run wireshark on our network and we have heard wireshark cannot run on a 1gb network line/switch, is that true and if it is, is there anyway around this? Basically we do not have a sniffer available and we r seeing spikes in network traffic and we need to determine where the increase ...'''
date = "2011-11-28T11:54:00Z"
lastmod = "2011-11-28T14:41:00Z"
weight = 7688
keywords = [ "network" ]
aliases = [ "/questions/7688" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [mb's vs gb's](/questions/7688/mbs-vs-gbs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7688-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>we r trying to run wireshark on our network and we have heard wireshark cannot run on a 1gb network line/switch, is that true and if it is, is there anyway around this? Basically we do not have a sniffer available and we r seeing spikes in network traffic and we need to determine where the increase in network traffic is coming from.<br />
Thanks, Scott Kobel [email protected]</p></div><div id="question-tags" class="tags-container tags">network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '11, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/6dbca94b9b0b2a1e7892acd176e8c051?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skobel&#39;s gravatar image" /><p>skobel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skobel has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-7688" class="comments-container"></div><div id="comment-tools-7688" class="comment-tools"></div><div class="clear"></div><div id="comment-7688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7689"></span>

<div id="answer-container-7689" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7689-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can capture 1GB/s link and even faster links as long as you have a network card that is supported (which they usually are). The question is (and I guess that's where the hearsay comes from) if the capturing PC/Notebook can write the captured data fast enough to do it without "drops". Drops are frames that have been on the wire but could not be saved due to performance reasons.</p><p>For a statistical analysis (which seems to be enough for starters in your case) you can even live with drops if the ratio is not too high - you're only trying to get an idea what's happening, so you don't need every frame.</p><p>As soon as you see something unusual you can then capture that device specifically, which usually gives you less traffic than a full 1gb network link.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '11, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7689" class="comments-container"></div><div id="comment-tools-7689" class="comment-tools"></div><div class="clear"></div><div id="comment-7689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

