+++
type = "question"
title = "Capture IP filter"
description = '''Hello all, Setting the capture filter in wireshark and restarting the capture still shows other IP network traffic....what went south? Here is what I did: started WS went into capture -&amp;gt; Capture Filters -&amp;gt; Cliked New -&amp;gt; filtername = 192.168.2.12 filter string = host 192.168.2.12. then resta...'''
date = "2012-06-01T12:24:00Z"
lastmod = "2012-06-01T13:34:00Z"
weight = 11547
keywords = [ "filter", "ip", "capture" ]
aliases = [ "/questions/11547" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture IP filter](/questions/11547/capture-ip-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11547-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>Setting the capture filter in wireshark and restarting the capture still shows other IP network traffic....what went south? Here is what I did: started WS went into capture -&gt; Capture Filters -&gt; Cliked New -&gt; filtername = 192.168.2.12 filter string = host 192.168.2.12. then restarted capture but I still see all the other traffic being displayed; Does this mean that the capture only collects data in the log file for x.x.x.12 address but the display continues to show all other traffic or did I do something wrong.</p><p>Thanks,</p><p>Adrian</p></div><div id="question-tags" class="tags-container tags">filter ip capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '12, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/a372519bafc417d6fc1817b6895e89d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kv7d-data&#39;s gravatar image" /><p>kv7d-data<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kv7d-data has no accepted answers">0%</span></p></div></div><div id="comments-container-11547" class="comments-container"></div><div id="comment-tools-11547" class="comment-tools"></div><div class="clear"></div><div id="comment-11547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11549"></span>

<div id="answer-container-11549" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11549-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have only created a capture filter for later use. You must apply the filter in the capture options dialog.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '12, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-11549" class="comments-container"></div><div id="comment-tools-11549" class="comment-tools"></div><div class="clear"></div><div id="comment-11549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

