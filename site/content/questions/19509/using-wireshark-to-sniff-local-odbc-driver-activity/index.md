+++
type = "question"
title = "Using Wireshark to sniff local ODBC driver activity"
description = '''Hello I am not satisfied with the ODBC driver embedded tracing tool in the ODBC manager of Windows 7 and was wondering how I could use Wireshark to monitor the activity over ODBC drivers? I read that some of you did use it but I was not able to monitor anything related to this kind of traffic. I am ...'''
date = "2013-03-14T08:03:00Z"
lastmod = "2013-03-14T08:18:00Z"
weight = 19509
keywords = [ "express", "sql", "odbc", "server", "mysql" ]
aliases = [ "/questions/19509" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using Wireshark to sniff local ODBC driver activity](/questions/19509/using-wireshark-to-sniff-local-odbc-driver-activity)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19509-score" class="post-score" title="current number of votes">0</div><span id="post-19509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I am not satisfied with the ODBC driver embedded tracing tool in the ODBC manager of Windows 7 and was wondering how I could use Wireshark to monitor the activity over ODBC drivers? I read that some of you did use it but I was not able to monitor anything related to this kind of traffic. I am using Windows 7 and my ODBC client and database (Mysql or SQLserver Express) are on the same PC. Thanks for any hint, details much appreciated... Christophe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-express" rel="tag" title="see questions tagged &#39;express&#39;">express</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span> <span class="post-tag tag-link-odbc" rel="tag" title="see questions tagged &#39;odbc&#39;">odbc</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '13, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/0b2eeccf42bae093a93fef3e877ab7d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christ0phe&#39;s gravatar image" /><p><span>Christ0phe</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christ0phe has no accepted answers">0%</span></p></div></div><div id="comments-container-19509" class="comments-container"></div><div id="comment-tools-19509" class="comment-tools"></div><div class="clear"></div><div id="comment-19509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19510"></span>

<div id="answer-container-19510" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19510-score" class="post-score" title="current number of votes">0</div><span id="post-19510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For a db on the same machine I don't think the drivers send data anywhere near the network so Wireshark won't be much help. Even if the mysql driver does, it will be "short-circuited" by the OS so won't get near the NIC so WinPCap (the library that Wireshark uses to make captures) won't see the traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '13, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Mar '13, 08:19</strong> </span></p></div></div><div id="comments-container-19510" class="comments-container"></div><div id="comment-tools-19510" class="comment-tools"></div><div class="clear"></div><div id="comment-19510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

