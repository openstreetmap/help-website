+++
type = "question"
title = "I see some red lines about some TCP connections and not sure what they mean"
description = '''I&#x27;m new to Wireshark. I&#x27;m using it to detect if my pc was hacked or not. I open it up first time today, and I can see some red lines which has these info: 36 15.728607 128.199.176.14 192.168.1.4 TCP 60 443 → 50207 [RST] Seq=1 Win=0 Len=0 425 52.346648 192.168.1.3 192.168.1.4 TCP 60 8009 → 50234 [RST...'''
date = "2017-06-01T16:38:00Z"
lastmod = "2017-06-02T01:33:00Z"
weight = 61734
keywords = [ "reset", "attack", "tcp" ]
aliases = [ "/questions/61734" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I see some red lines about some TCP connections and not sure what they mean](/questions/61734/i-see-some-red-lines-about-some-tcp-connections-and-not-sure-what-they-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61734-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to Wireshark. I'm using it to detect if my pc was hacked or not.</p><p>I open it up first time today, and I can see some red lines which has these info:</p><pre><code>36  15.728607   128.199.176.14  192.168.1.4 TCP 60  443 → 50207 [RST] Seq=1 Win=0 Len=0
425 52.346648   192.168.1.3 192.168.1.4 TCP 60  8009 → 50234 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</code></pre><p>I'm not sure how to interpret these information.</p><p>Is it possible I'm under TCP Reset Attack?</p></div><div id="question-tags" class="tags-container tags">reset attack tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '17, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/c65f5f9dde12f21e334b78a490ef0dfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kekehuang&#39;s gravatar image" /><p>kekehuang<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kekehuang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jun '17, 02:00</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61734" class="comments-container"></div><div id="comment-tools-61734" class="comment-tools"></div><div class="clear"></div><div id="comment-61734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61742"></span>

<div id="answer-container-61742" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61742-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is highly unlikely. Resets are connection terminations that can happen for a number of reasons, but hacking is very rarely using those. Especially a RST/ACK combination is usually not critical, but used as a faster way of shutting down a data transfer that is complete.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '17, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61742" class="comments-container"></div><div id="comment-tools-61742" class="comment-tools"></div><div class="clear"></div><div id="comment-61742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

