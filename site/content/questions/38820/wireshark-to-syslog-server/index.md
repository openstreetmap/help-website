+++
type = "question"
title = "Wireshark to syslog server"
description = '''Is there a way to send the Wireshark (dumpcap) captures directly to a syslog server? Or send them to a custom Windows event log?'''
date = "2014-12-31T05:43:00Z"
lastmod = "2014-12-31T08:39:00Z"
weight = 38820
keywords = [ "syslog", "dumpcap" ]
aliases = [ "/questions/38820" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark to syslog server](/questions/38820/wireshark-to-syslog-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38820-score" class="post-score" title="current number of votes">0</div><span id="post-38820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to send the Wireshark (dumpcap) captures directly to a syslog server? Or send them to a custom Windows event log?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syslog" rel="tag" title="see questions tagged &#39;syslog&#39;">syslog</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '14, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/b826fc435a80f6b2fe75d4bf4789022a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark_r&#39;s gravatar image" /><p><span>wireshark_r</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark_r has no accepted answers">0%</span></p></div></div><div id="comments-container-38820" class="comments-container"></div><div id="comment-tools-38820" class="comment-tools"></div><div class="clear"></div><div id="comment-38820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38830"></span>

<div id="answer-container-38830" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38830-score" class="post-score" title="current number of votes">1</div><span id="post-38830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Neither syslog nor Windows eventlog makes much sense in this context, as the capture files taken with dumpcap, are in binary format and you won't be able to do anything usefull with that data on the syslog server.</p><p>Maybe I don't understand what you are trying to achive. Can you please add some words about what you are trying to do and mabye a sample log line you want to see on the syslog server?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '14, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38830" class="comments-container"><span id="38831"></span><div id="comment-38831" class="comment"><div id="post-38831-score" class="comment-score"></div><div class="comment-text"><p>I am trying to send my Cisco SPAN port stream from my NIC to my SIEM device.</p></div><div id="comment-38831-info" class="comment-info"><span class="comment-age">(31 Dec '14, 08:33)</span> <span class="comment-user userinfo">wireshark_r</span></div></div><span id="38832"></span><div id="comment-38832" class="comment"><div id="post-38832-score" class="comment-score">1</div><div class="comment-text"><p>The SIEM (most certainly) won't be able to read/decode the binary pcap data. So, again: What are you actually trying to do?</p><p>If your SIEM is able to listen to network traffic, you should take a look at <a href="https://supportforums.cisco.com/document/139236/understanding-spanrspanand-erspan">RSPAN or ERPSAN</a>.</p></div><div id="comment-38832-info" class="comment-info"><span class="comment-age">(31 Dec '14, 08:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-38830" class="comment-tools"></div><div class="clear"></div><div id="comment-38830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

