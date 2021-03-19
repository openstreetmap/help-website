+++
type = "question"
title = "jumbo frame mtu setting"
description = '''Once If I set jumbo frame on a specific interface like: ifconfig eth0 mtu 9000 what will be the minimum and maximum packet size ? Say for example, if I send a 1 byte packet, whether padding happens till 64 byte frame size(minimum required) will be done (OR) some other minimum size ? Also, If I set p...'''
date = "2014-01-07T04:37:00Z"
lastmod = "2014-01-07T04:56:00Z"
weight = 28624
keywords = [ "jumbo", "mtu" ]
aliases = [ "/questions/28624" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [jumbo frame mtu setting](/questions/28624/jumbo-frame-mtu-setting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28624-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Once If I set jumbo frame on a specific interface like:</p><p>ifconfig eth0 mtu 9000</p><p>what will be the minimum and maximum packet size ?</p><p>Say for example, if I send a 1 byte packet, whether padding happens till 64 byte frame size(minimum required) will be done (OR) some other minimum size ?</p><p>Also, If I set packet size as 100, what will be the frame size ? Is it 1500 (OR) 9000 ? How the padding happens in this case ?</p><p>OS: linux 2.6.32 Thanks.</p></div><div id="question-tags" class="tags-container tags">jumbo mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '14, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/03741fde046267f91ecf3e1989f88cc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saro&#39;s gravatar image" /><p>saro<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saro has no accepted answers">0%</span></p></div></div><div id="comments-container-28624" class="comments-container"></div><div id="comment-tools-28624" class="comment-tools"></div><div class="clear"></div><div id="comment-28624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28625"></span>

<div id="answer-container-28625" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28625-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Minimum frame size is always 64 bytes, so if you send 1 byte you'll be padded up to 64 bytes. If you send 100 bytes the frame size is still 100 bytes. Maximum is only the size a frame cannot exceed. It doesn't mean that all frames need to be that big.</p><p>I'm not sure if you use the terms "packet size" and "frame size" as it is meant. "Packet Size" would be the IP part of the frame, while frame is the whole data including ethernet headers and FCS being sent. So if you send an IP "packet" of 100 bytes you'll end up with 118 bytes "frame" size (14 bytes ethernet header and 4 bytes FCS).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '14, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28625" class="comments-container"><span id="28659"></span><div id="comment-28659" class="comment"><div id="post-28659-score" class="comment-score"></div><div class="comment-text"><p>And the MTU is "the IP part of the frame", so the maximum IP packet size, with an MTU of 9000, is 9000, but a 9000-byte IP packet would be 9018 bytes "on the wire", with a 14-byte header and a 4-byte FCS).</p></div><div id="comment-28659-info" class="comment-info"><span class="comment-age">(07 Jan '14, 19:25)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-28625" class="comment-tools"></div><div class="clear"></div><div id="comment-28625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

