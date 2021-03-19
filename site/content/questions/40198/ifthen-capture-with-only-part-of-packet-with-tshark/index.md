+++
type = "question"
title = "IF/THEN capture with only part of packet with tshark"
description = '''Hi, Would like to capture packets into a file based on if I find for example a specific address in the Ethernet header. Once I find a packet with say mac.src=XX:XX:XX:XX:XX:XX I don&#x27;t want the entire packet, just some fields or maybe only the Ethernet + IP headers (don&#x27;t want to store the entire IP ...'''
date = "2015-03-02T18:11:00Z"
lastmod = "2015-03-05T05:55:00Z"
weight = 40198
keywords = [ "capture-filter", "tshark" ]
aliases = [ "/questions/40198" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IF/THEN capture with only part of packet with tshark](/questions/40198/ifthen-capture-with-only-part-of-packet-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40198-score" class="post-score" title="current number of votes">0</div><span id="post-40198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Would like to capture packets into a file based on if I find for example a specific address in the Ethernet header. Once I find a packet with say mac.src=XX:XX:XX:XX:XX:XX I don't want the entire packet, just some fields or maybe only the Ethernet + IP headers (don't want to store the entire IP payload).</p><p>So my capture would look something like:</p><p>WHILE (criteria is met) IF (mac.srx=XX:XX:XX:XX:XX:XX OR mac.dest=XX:XX:XX:XX:XX:XX) THEN #save first Y octets in raw data OR MAC+IP headers if that option is possible</p><p>I know this syntax doesn't make sense for a script, but as for the concept, could anyone suggest a capture filter that would do the trick?</p><p>Thanks! /Sam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '15, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/c19324dc35615378dc81ba8a3d71b0b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SamA&#39;s gravatar image" /><p><span>SamA</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SamA has no accepted answers">0%</span></p></div></div><div id="comments-container-40198" class="comments-container"></div><div id="comment-tools-40198" class="comment-tools"></div><div class="clear"></div><div id="comment-40198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40202"></span>

<div id="answer-container-40202" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40202-score" class="post-score" title="current number of votes">1</div><span id="post-40202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This can't be done. dumpcap (the process that does the capture for tshark/Wireshark) always writes full packet bytes to file. Also, a capture filter like you want can't work because it would take way too much time to inspect/filter packets before writing them, which would make the capture process so slow that it would lose too many packets for performance reasons.</p><p>Why don't you just specify a capture filter for the MAC addresses you want, and limit the captured bytes to a certain amount, e.g. 64 bytes? This can be done with dumpcap using the "-f" and "-s" parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '15, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40202" class="comments-container"><span id="40282"></span><div id="comment-40282" class="comment"><div id="post-40282-score" class="comment-score"></div><div class="comment-text"><p>dumpcap -i eth0 -s 32 -f "ether host XX:XX:XX:XX:XX:XX" -w dump.pcap</p></div><div id="comment-40282-info" class="comment-info"><span class="comment-age">(05 Mar '15, 05:55)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-40202" class="comment-tools"></div><div class="clear"></div><div id="comment-40202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

