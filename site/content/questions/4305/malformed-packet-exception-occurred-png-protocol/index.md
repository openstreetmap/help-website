+++
type = "question"
title = "malformed packet (exception occurred) PNG Protocol"
description = '''Hello friends, I got the following error while capturing our hosting mail server, which is malformed packet (exception occurred) PNG Protocol, I was using version 1.4.4 and I thought it was a software bug, but then I uninstalled this version and I&#x27;m now using version 1.4.7 and still see this error. ...'''
date = "2011-05-31T23:17:00Z"
lastmod = "2011-06-01T01:52:00Z"
weight = 4305
keywords = [ "malformed", "protocol", "packet", "png" ]
aliases = [ "/questions/4305" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [malformed packet (exception occurred) PNG Protocol](/questions/4305/malformed-packet-exception-occurred-png-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4305-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello friends, I got the following error while capturing our hosting mail server, which is malformed packet (exception occurred) PNG Protocol, I was using version 1.4.4 and I thought it was a software bug, but then I uninstalled this version and I'm now using version 1.4.7 and still see this error. Does this mean there is a critical situation we have to check deeply with it or is it normal?</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">malformed protocol packet png</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '11, 23:17</strong></p><img src="https://secure.gravatar.com/avatar/78a1fd7e0db832efc378a0009d83cd6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abood&#39;s gravatar image" /><p>Abood<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abood has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '11, 08:34</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4305" class="comments-container"></div><div id="comment-tools-4305" class="comment-tools"></div><div class="clear"></div><div id="comment-4305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4308"></span>

<div id="answer-container-4308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4308-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd say this is normal. It just means that the dissector for PNG failed when trying to work through the data, which often happens if TCP reassembly is turned off and the payload is stretched over multiple packets.</p><p>I don't think it is critical unless someone uses the PNG dissector flaw to write attack code that utilizes it to inject malicious code (if that is possible at all in this case). Afterwards he needs to send you packets containing the malicious PNG payload and you need to analyze it. Chances for something like that aren't high, but you never know :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '11, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '11, 08:34</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4308" class="comments-container"><span id="4310"></span><div id="comment-4310" class="comment"><div id="post-4310-score" class="comment-score"></div><div class="comment-text"><p>Thanks. the TCP reassembly is turned on. what shall we do in order to see it is not an attack?</p></div><div id="comment-4310-info" class="comment-info"><span class="comment-age">(01 Jun '11, 01:59)</span> Abood</div></div><span id="4311"></span><div id="comment-4311" class="comment"><div id="post-4311-score" class="comment-score"></div><div class="comment-text"><p>Determining if binary content contains attack code is a science in itself, called reversing/reverse engineering. It is not something you can learn without weeks, months and sometimes years of practicing.</p><p>But you might be able to look for the consequences of an attack - capture the device that had the exception (preferable with a 3rd, passive Wireshark) and see if the device is trying to communicate with other nodes outside your net that it shouldn't. This can be difficult, too, unless you have full knowledge of what that device should or shouldn't do.</p></div><div id="comment-4311-info" class="comment-info"><span class="comment-age">(01 Jun '11, 02:05)</span> Jasper ♦♦</div></div></div><div id="comment-tools-4308" class="comment-tools"></div><div class="clear"></div><div id="comment-4308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

