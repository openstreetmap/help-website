+++
type = "question"
title = "remote capture"
description = '''I currently have wireshark installed on my windowsXP box; I want to do a capture between a remote laptop and a remote file server on the same subnet. How can I set that up? thanks! '''
date = "2010-10-19T10:27:00Z"
lastmod = "2010-10-19T15:43:00Z"
weight = 536
keywords = [ "remote" ]
aliases = [ "/questions/536" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [remote capture](/questions/536/remote-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-536-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I currently have wireshark installed on my windowsXP box; I want to do a capture between a remote laptop and a remote file server on the same subnet. How can I set that up? thanks!</p></div><div id="question-tags" class="tags-container tags">remote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '10, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/90e1fac28a2a807e76893a152d908b38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="will_sj&#39;s gravatar image" /><p>will_sj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="will_sj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Oct '10, 10:28</p></div></div><div id="comments-container-536" class="comments-container"></div><div id="comment-tools-536" class="comment-tools"></div><div class="clear"></div><div id="comment-536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="544"></span>

<div id="answer-container-544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-544-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think what you want to do is capture the traffic between the laptop and the file server with the help of your XP box, which would be a pretty standard setup. I wouldn't call that a remote capture, because for me that would imply doing a rcapd capture, which is a little more complicated.</p><p>What you have to do is to attach your XP box to the same switch either server or laptop (or both) are physically attached to, and then setup a monitoring (a.k.a SPAN) session to forward their packets towards the switch port your XP box is attached to. For this you will need a manageable switch and access to the CLI or Web front end where the monitoring settings can be configured. If you don't have that kind of switch you can try using a hub that you put inline, or go for a low cost switch tap sold by Dual-Comm.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '10, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-544" class="comments-container"><span id="565"></span><div id="comment-565" class="comment"><div id="post-565-score" class="comment-score"></div><div class="comment-text"><p>Okay thanks, this is doable as I use Cisco Catalyst switches. I have just one other question, the file server is at another location, it's on my WAN but a different subnet, I can access it just not physically. Would I be able to config the server in the SPAN session?</p></div><div id="comment-565-info" class="comment-info"><span class="comment-age">(20 Oct '10, 12:30)</span> will_sj</div></div><span id="566"></span><div id="comment-566" class="comment"><div id="post-566-score" class="comment-score"></div><div class="comment-text"><p>Well... maybe. Usually you should be able to attach the capture box directly to the switch where you are doing the monitoring session, so you need physical access. There are some options like doing a remote span where the capture data will be transferred to your location via special transport VLAN, but that is problematic as you might lose packets and the times get distorted. I would advise against doing that. If the remote server is not accessable just capture the client, very often you can tell enough from that kind of trace anyway.</p></div><div id="comment-566-info" class="comment-info"><span class="comment-age">(20 Oct '10, 13:16)</span> Jasper ♦♦</div></div><span id="574"></span><div id="comment-574" class="comment"><div id="post-574-score" class="comment-score"></div><div class="comment-text"><p>thanks for your help!</p></div><div id="comment-574-info" class="comment-info"><span class="comment-age">(21 Oct '10, 08:06)</span> will_sj</div></div></div><div id="comment-tools-544" class="comment-tools"></div><div class="clear"></div><div id="comment-544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

