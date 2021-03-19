+++
type = "question"
title = "DIS PDU filtering"
description = '''Does anyone know how to load the latest DIS PDU updates in order for Wireshark to be able to filter on DIS PDUs being transmitted over the network? It would have to be compatible with 64-bit Windows 7. I&#x27;m new to this system and my protocol preferences state that DIS is available, but I wasn&#x27;t sure ...'''
date = "2011-04-19T07:43:00Z"
lastmod = "2012-04-20T07:41:00Z"
weight = 3609
keywords = [ "pdu", "dis" ]
aliases = [ "/questions/3609" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [DIS PDU filtering](/questions/3609/dis-pdu-filtering)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3609-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone know how to load the latest DIS PDU updates in order for Wireshark to be able to filter on DIS PDUs being transmitted over the network? It would have to be compatible with 64-bit Windows 7. I'm new to this system and my protocol preferences state that DIS is available, but I wasn't sure if I need to download additional code for DIS PDUs as well to make this work.</p><p>The version of Wireshark that I have is vers. 1.4.5</p></div><div id="question-tags" class="tags-container tags">pdu dis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '11, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/5e53a2ed447dbe2c0915a656d0eaaba5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="native020&#39;s gravatar image" /><p>native020<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="native020 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '11, 18:28</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3609" class="comments-container"></div><div id="comment-tools-3609" class="comment-tools"></div><div class="clear"></div><div id="comment-3609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4011"></span>

<div id="answer-container-4011" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4011-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Distributed Interactive Simulation (DIS) dissector has been included with Wireshark since July 11, 2005. As long as the DIS traffic is being transported over UDP/3000, you don't have to do anything special to get DIS PDU's to be dissected. If it's being transported over another port, then just change the port preference via Edit -&gt; Preferences -&gt; Protocols -&gt; DIS -&gt; DIS UDP Port.</p><p>By the way, if you're still using 1.4.5, you should upgrade to <a href="http://www.wireshark.org/download.html">1.4.6</a> immediately due to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5837">bug 5837</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '11, 18:41</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4011" class="comments-container"></div><div id="comment-tools-4011" class="comment-tools"></div><div class="clear"></div><div id="comment-4011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10350"></span>

<div id="answer-container-10350" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10350-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This feature amounts to a bug with Aastra IP phones: They send RTP data on port 3000, and wireshark interprets it as DIS. To get Wireshark to recognize RTP stream of this kind as RTP, I had to set the preference above to something other than 3000 (I used 0). After that, the datastream was correctly interpreted as RTP by wireshark. Reference: <a href="http://www.pbxinaflash.com/community/index.php?threads/dis-pdu-types.8521">http://www.pbxinaflash.com/community/index.php?threads/dis-pdu-types.8521</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '12, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/7d7f91bf11cbf8b7b39d0c6acb50033f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephen%20J%20Alexander&#39;s gravatar image" /><p>Stephen J Al...<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephen J Alexander has no accepted answers">0%</span></p></div></div><div id="comments-container-10350" class="comments-container"></div><div id="comment-tools-10350" class="comment-tools"></div><div class="clear"></div><div id="comment-10350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

