+++
type = "question"
title = "After upgrading to 2.0.5 IP DSCP Value column shows in hex"
description = '''I updated to 2.0.5 and now the IP DSCP Value is showing EF instead of 46 as example. It appears to be broke in 2.0.5 as 2.0.4 and below work just fine. Anyone else or can this be redefined in custom?'''
date = "2016-08-02T11:51:00Z"
lastmod = "2016-08-02T12:58:00Z"
weight = 54524
keywords = [ "dscp" ]
aliases = [ "/questions/54524" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [After upgrading to 2.0.5 IP DSCP Value column shows in hex](/questions/54524/after-upgrading-to-205-ip-dscp-value-column-shows-in-hex)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54524-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I updated to 2.0.5 and now the IP DSCP Value is showing EF instead of 46 as example. It appears to be broke in 2.0.5 as 2.0.4 and below work just fine.</p><p>Anyone else or can this be redefined in custom?</p></div><div id="question-tags" class="tags-container tags">dscp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '16, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/314d0fd3405183279133c3d208abe35e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r1limited&#39;s gravatar image" /><p>r1limited<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r1limited has no accepted answers">0%</span></p></div></div><div id="comments-container-54524" class="comments-container"></div><div id="comment-tools-54524" class="comment-tools"></div><div class="clear"></div><div id="comment-54524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54525"></span>

<div id="answer-container-54525" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54525-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "new" display shows the function, not just the raw code. The code 46 stands for "Expedited Forwarding" or EF for short. The actual function code (46) can be seen if the field is expanded as shown below:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/dscp-ef.PNG" alt="DiffServ field expanded" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '16, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-54525" class="comments-container"><span id="54526"></span><div id="comment-54526" class="comment"><div id="post-54526-score" class="comment-score"></div><div class="comment-text"><p>And if the DSCP field is added as a column it shows up as "Expedited Forwarding", similarly for tshark output:</p><pre><code>Differentiated Services Field: 0xb8 (DSCP: EF PHB, ECN: Not-ECT)               
    1011 10.. = Differentiated Services Codepoint: Expedited Forwarding (46)   
    .... ..00 = Explicit Congestion Notification: Not ECN-Capable Transport (0)</code></pre></div><div id="comment-54526-info" class="comment-info"><span class="comment-age">(02 Aug '16, 13:53)</span> grahamb ♦</div></div><span id="54527"></span><div id="comment-54527" class="comment"><div id="post-54527-score" class="comment-score"></div><div class="comment-text"><p>Yes, I get that, I understand that, my point is it changed and now displays that value in the column field instead of the actual number. EF can be ef 46 ef 48 etc I want the honored value to show. I use this as a column to quick check that value</p></div><div id="comment-54527-info" class="comment-info"><span class="comment-age">(02 Aug '16, 13:55)</span> r1limited</div></div><span id="54528"></span><div id="comment-54528" class="comment"><div id="post-54528-score" class="comment-score"></div><div class="comment-text"><p>This was done in response to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12429">bug 12429</a></p></div><div id="comment-54528-info" class="comment-info"><span class="comment-age">(02 Aug '16, 14:02)</span> Jaap ♦</div></div><span id="54936"></span><div id="comment-54936" class="comment"><div id="post-54936-score" class="comment-score"></div><div class="comment-text"><p>Same here, I'm using 2 columns IP DSCP value and ip.dscp.field, but now it has no added value</p></div><div id="comment-54936-info" class="comment-info"><span class="comment-age">(18 Aug '16, 01:15)</span> kosz</div></div><span id="54966"></span><div id="comment-54966" class="comment"><div id="post-54966-score" class="comment-score"></div><div class="comment-text"><p>If this is a problem, <a href="https://bugs.wireshark.org/bugzilla/">file a bug</a></p></div><div id="comment-54966-info" class="comment-info"><span class="comment-age">(18 Aug '16, 21:40)</span> Jaap ♦</div></div><span id="54977"></span><div id="comment-54977" class="comment not_top_scorer"><div id="post-54977-score" class="comment-score"></div><div class="comment-text"><p>Ya its a bloody problem</p></div><div id="comment-54977-info" class="comment-info"><span class="comment-age">(19 Aug '16, 07:57)</span> r1limited</div></div><span id="54993"></span><div id="comment-54993" class="comment not_top_scorer"><div id="post-54993-score" class="comment-score"></div><div class="comment-text"><p>Then file a bloody bug ;)</p></div><div id="comment-54993-info" class="comment-info"><span class="comment-age">(19 Aug '16, 14:37)</span> Jaap ♦</div></div></div><div id="comment-tools-54525" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-54525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

