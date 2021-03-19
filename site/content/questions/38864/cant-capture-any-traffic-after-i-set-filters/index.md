+++
type = "question"
title = "Can&#x27;t capture any traffic after i set filters"
description = '''Before I set filters,I can capture traffics ,such as:  But after I set a TCP filters,I capture nothing,such as:   Does anyone know what happened and how to fix it? Thanks a lot'''
date = "2015-01-03T02:18:00Z"
lastmod = "2015-01-03T09:42:00Z"
weight = 38864
keywords = [ "capture-filter" ]
aliases = [ "/questions/38864" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can't capture any traffic after i set filters](/questions/38864/cant-capture-any-traffic-after-i-set-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38864-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>Before</strong> I set filters,I can capture traffics ,such as:<br />
<img src="http://ww4.sinaimg.cn/large/005yyi5Jjw1enwhs2k094j311y0ich2i.jpg" alt="alt text" /></p><p>But <strong>after</strong> I set a <strong>TCP</strong> filters,I capture nothing,such as:<br />
<img src="http://ww4.sinaimg.cn/large/005yyi5Jjw1enwhv3wzyfj30us0h379c.jpg" alt="alt text" /> <img src="http://ww1.sinaimg.cn/large/005yyi5Jjw1enwhwx5a4dj311s0jeaci.jpg" alt="alt text" /></p><p>Does anyone know what happened and how to fix it? Thanks a lot</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '15, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/820929fa9194146a9ef6cbaa8fadb0d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="obo&#39;s gravatar image" /><p>obo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="obo has no accepted answers">0%</span> </br></br></p></img></div></div><div id="comments-container-38864" class="comments-container"></div><div id="comment-tools-38864" class="comment-tools"></div><div class="clear"></div><div id="comment-38864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38866"></span>

<div id="answer-container-38866" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38866-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filters are fairly simple compared to display filters, due to the need for performance. They're really BPF filters. When you use a capture filter of "tcp", the resultant filter logic expects to see that transport type at specific offsets in packets - for example it expects to see the IP header at a specific offset relative to the Ethernet header, and the IP header's protocol field at a specific offset to determine tcp vs. udp and so on.</p><p>In your case you're not running "normal" IP over Ethernet - you're running PPP over Ethernet. So I believe you need to tell the capture filter to account for that change in offsets due to PPPoE, by using the filter "<code>pppoes and tcp</code>".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '15, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></img></div></div><div id="comments-container-38866" class="comments-container"><span id="38870"></span><div id="comment-38870" class="comment"><div id="post-38870-score" class="comment-score"></div><div class="comment-text"><p>Yes,I'm running PPP over Ethernet.Your method works.thank you.</p></div><div id="comment-38870-info" class="comment-info"><span class="comment-age">(04 Jan '15, 01:22)</span> obo</div></div></div><div id="comment-tools-38866" class="comment-tools"></div><div class="clear"></div><div id="comment-38866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

