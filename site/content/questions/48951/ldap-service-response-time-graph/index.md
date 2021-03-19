+++
type = "question"
title = "LDAP Service Response Time Graph"
description = '''I am having problems graphing LDAP Service Response Time in Wireshark 2.0.1. The Y-axis especially does not seem to be accurate. Has anyone been able to accurately graph LDAP response time? I&#x27;d like to see the spikes, etc in graph format. The field occurrence does not matter to me at the moment. Her...'''
date = "2016-01-07T11:38:00Z"
lastmod = "2017-02-14T10:22:00Z"
weight = 48951
keywords = [ "graph", "srt", "ldap" ]
aliases = [ "/questions/48951" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LDAP Service Response Time Graph](/questions/48951/ldap-service-response-time-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48951-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having problems graphing LDAP Service Response Time in Wireshark 2.0.1. The Y-axis especially does not seem to be accurate. Has anyone been able to accurately graph LDAP response time? I'd like to see the spikes, etc in graph format. The field occurrence does not matter to me at the moment.</p><p>Here is a screen shot of the graph. I've tried several options and attempts at graphing it correctly. Essentially, I'm seeing a Max SRT of 11.85 seconds from Wireshark's LDAP SRT statistics window (forefront). However, when attempting to graph those values, I can't seem to get the Y-axis to reflect the correct scale/numbers.</p><p>Unfortunately, due to the capture containing LDAP/account information I can't upload the actual capture file itself.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ldap_M1b8YHT.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">graph srt ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '16, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/37aeac42341cc42e5d10656094aa9139?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csereno&#39;s gravatar image" /><p>csereno<br />
<span class="score" title="69 reputation points">69</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csereno has one accepted answer">25%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '16, 08:33</p></div></div><div id="comments-container-48951" class="comments-container"><span id="49024"></span><div id="comment-49024" class="comment"><div id="post-49024-score" class="comment-score"></div><div class="comment-text"><p>can you please provide a screenshot and (if possible) the pcap file?</p></div><div id="comment-49024-info" class="comment-info"><span class="comment-age">(09 Jan '16, 12:17)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-48951" class="comment-tools"></div><div class="clear"></div><div id="comment-48951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59416"></span>

<div id="answer-container-59416" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59416-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I stumbled back across my question, and it seems the later versions of Wireshark have improved the graphing. It seems to line up a little more. I still have a little learning to do around the graphing (particularly with LDAP and timing), but it seems Wireshark is graphing more appropriately now.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ldap_maxtime_0uxXdT1.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '17, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/37aeac42341cc42e5d10656094aa9139?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csereno&#39;s gravatar image" /><p>csereno<br />
<span class="score" title="69 reputation points">69</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csereno has one accepted answer">25%</span></p></img></div></div><div id="comments-container-59416" class="comments-container"></div><div id="comment-tools-59416" class="comment-tools"></div><div class="clear"></div><div id="comment-59416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

