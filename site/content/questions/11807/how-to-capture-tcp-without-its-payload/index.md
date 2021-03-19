+++
type = "question"
title = "How to capture TCP without its payload?"
description = '''During sending a large amount of data (~1 TB) there are some kind of connection errors which I want to track out. If I capture the whole tcp traffic, than the final pcap file will be more likely about ~1TB. How to capture my tcp traffic to a file not writing its payload. I am not interested in conte...'''
date = "2012-06-11T05:30:00Z"
lastmod = "2012-06-11T05:38:00Z"
weight = 11807
keywords = [ "exclusion", "tcp" ]
aliases = [ "/questions/11807" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture TCP without its payload?](/questions/11807/how-to-capture-tcp-without-its-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11807-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>During sending a large amount of data (~1 TB) there are some kind of connection errors which I want to track out. If I capture the whole <code>tcp</code> traffic, than the final <code>pcap</code> file will be more likely about ~1TB.</p><p>How to capture my <code>tcp</code> traffic to a file not writing its payload. I am not interested in contents I send, I am much interested in tcp conversation instead. Is it possible?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">exclusion tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '12, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/379c9b0fdbc1951a677438075fe5bd12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baranovdmi&#39;s gravatar image" /><p>baranovdmi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baranovdmi has no accepted answers">0%</span></p></div></div><div id="comments-container-11807" class="comments-container"></div><div id="comment-tools-11807" class="comment-tools"></div><div class="clear"></div><div id="comment-11807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11808"></span>

<div id="answer-container-11808" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11808-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could capture the traffic with a packet size limitation (for example 64 bytes) if you do not need the payload. The size should be selected based on the length of the headers you need to keep when capturing. For an ethernet based tcp/ip packet 64 bytes is usually enough if all you need to see is up to the TCP layer.</p><p>You can set this limit at the capture interface settings. There is a checkmark called "Limit each packet to" which is usually not checked and has a default size of 65535 bytes. Activate the checkbox and set the limit to whatever suits you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '12, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-11808" class="comments-container"></div><div id="comment-tools-11808" class="comment-tools"></div><div class="clear"></div><div id="comment-11808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

