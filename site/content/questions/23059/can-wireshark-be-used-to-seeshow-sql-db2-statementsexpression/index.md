+++
type = "question"
title = "Can Wireshark be used to see/show SQL (DB2) statements/expression?"
description = '''I am trying to analyze SQL statements/expressions being sent from a client machine to a DB2 server. I can successfully get a general capture [from Wireshark app] but I have been unable to get any useful output (&#x27;readable&#x27; info). I figured that after HOURS of &#x27;google-ing&#x27; this issue, I would have stu...'''
date = "2013-07-16T17:58:00Z"
lastmod = "2013-07-22T01:34:00Z"
weight = 23059
keywords = [ "db2" ]
aliases = [ "/questions/23059" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark be used to see/show SQL (DB2) statements/expression?](/questions/23059/can-wireshark-be-used-to-seeshow-sql-db2-statementsexpression)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23059-score" class="post-score" title="current number of votes">0</div><span id="post-23059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to analyze SQL statements/expressions being sent from a client machine to a DB2 server. I can successfully get a general capture [from Wireshark app] but I have been unable to get any useful output ('readable' info). I figured that after HOURS of 'google-ing' this issue, I would have stumbled upon a YouTube vid or a forum entry that explains this wireshark-related process. However, coming up emtpy, it is becoming apparent that either Wireshark is not the tool to do this OR not a lot of people know HOW to accomplish this task with Wireshark. Any one have any suggestions on best tool to use for this task?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-db2" rel="tag" title="see questions tagged &#39;db2&#39;">db2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '13, 17:58</strong></p><img src="https://secure.gravatar.com/avatar/a5b54cd180fdffc99cc49439da933823?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mem5449&#39;s gravatar image" /><p><span>mem5449</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mem5449 has no accepted answers">0%</span></p></div></div><div id="comments-container-23059" class="comments-container"></div><div id="comment-tools-23059" class="comment-tools"></div><div class="clear"></div><div id="comment-23059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23065"></span>

<div id="answer-container-23065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23065-score" class="post-score" title="current number of votes">0</div><span id="post-23065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is almost certainly the best tool for this task.</p><p>A quick Google search found two articles (<a href="https://www.ibm.com/developerworks/community/blogs/dylanskillsharing/entry/understanding_the_drda_protocol_in_db2_using_wireshark?lang=en">here</a> and <a href="http://thenetworkguy.typepad.com/nau/2009/06/drda-unraveling-the-db2-decodes.html">here</a>) showing Wireshark being used to examine DB2 traffic, so it would seem to be a local issue on your end, unless your DB2 instances are not using DRDA.</p><p>Can you explain what you do see in your capture, and if possible post the capture somewhere so we can examine it, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '13, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23065" class="comments-container"><span id="23212"></span><div id="comment-23212" class="comment"><div id="post-23212-score" class="comment-score"></div><div class="comment-text"><p>Graham,</p><p>Thanks for your reply. I would love to post the capture so maybe someone could assist. However, since the DB2 results (from queries) contain customers phone numbers, my client is not willing to let me put that out on the web.</p><p>I had already seen those 2 links you provided. In fact I emailed the gent in the second link but have not heard back. After FURTHER Google searches, I learned that I will probably need to install a DB2 specific DISSECTOR into Wireshark to actually see the SQL statements in the packet capture.</p><p>Mike</p></div><div id="comment-23212-info" class="comment-info"><span class="comment-age">(21 Jul '13, 11:35)</span> <span class="comment-user userinfo">mem5449</span></div></div><span id="23219"></span><div id="comment-23219" class="comment"><div id="post-23219-score" class="comment-score"></div><div class="comment-text"><p>Wireshark has had a dissector for DRDA since 2007. Apparently this is the protocol used by DB2 since version 8. The DRDA dissector is heuristic so DRDA traffic (as long as it's not encrypted e.g. by using SSL) should be visible in your capture.</p><p>As you are unable to post the capture, are you able to identify traffic to the port the server is listening on, and the protocols used on traffic to that port?</p></div><div id="comment-23219-info" class="comment-info"><span class="comment-age">(22 Jul '13, 01:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23065" class="comment-tools"></div><div class="clear"></div><div id="comment-23065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

