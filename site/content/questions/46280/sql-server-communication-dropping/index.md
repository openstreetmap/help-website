+++
type = "question"
title = "SQL Server Communication dropping"
description = '''We have this application that we use to grab information from one SQL Server and do some calculations and so on, then put information into another SQL Server. We have been having some issues with it lately where it just stops working. Originally I had found duplicate SPNs and removed the dups and th...'''
date = "2015-09-30T07:45:00Z"
lastmod = "2015-09-30T13:37:00Z"
weight = 46280
keywords = [ "sql", "tcp", "server" ]
aliases = [ "/questions/46280" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SQL Server Communication dropping](/questions/46280/sql-server-communication-dropping)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46280-score" class="post-score" title="current number of votes">0</div><span id="post-46280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have this application that we use to grab information from one SQL Server and do some calculations and so on, then put information into another SQL Server. We have been having some issues with it lately where it just stops working. Originally I had found duplicate SPNs and removed the dups and the application started working. now it stopped again. I ran wireshark on the workstation that uses this application and I'm seeing a lot of bad TCP. can someone help me figure out what all this means?</p><p><a href="https://drive.google.com/open?id=0B3aXFCKzXbMZOW50ajFsWHFhQm8">Capture File</a></p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_Nvhuldt.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '15, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/91882b009050e665f425043c1f7f33ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThompsonAdmin&#39;s gravatar image" /><p><span>ThompsonAdmin</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThompsonAdmin has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '15, 13:09</strong> </span></p></div></div><div id="comments-container-46280" class="comments-container"><span id="46287"></span><div id="comment-46287" class="comment"><div id="post-46287-score" class="comment-score"></div><div class="comment-text"><p>What do you exactly mean with <code>"bad TCPs"</code></p><p>Do you mean the TCP Keep alive packets?</p></div><div id="comment-46287-info" class="comment-info"><span class="comment-age">(30 Sep '15, 12:28)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46290"></span><div id="comment-46290" class="comment"><div id="post-46290-score" class="comment-score"></div><div class="comment-text"><p>i mean its highlighted with black background and red text by keep alive i guess i'm refering to this... tcp.analysis.keep_alive</p></div><div id="comment-46290-info" class="comment-info"><span class="comment-age">(30 Sep '15, 13:08)</span> <span class="comment-user userinfo">ThompsonAdmin</span></div></div></div><div id="comment-tools-46280" class="comment-tools"></div><div class="clear"></div><div id="comment-46280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46291"></span>

<div id="answer-container-46291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46291-score" class="post-score" title="current number of votes">0</div><span id="post-46291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ok. That is no real error. If for a defined period (could be mostly configured and this case 30 sec.) no segements had beeen received then the stacks probes if the session is still alive with so called "TCP-KEEP-ALLIVES" You can identify the frames by their SEQ number, because it is <code>"SEQ Number of TCP-KEEP-ALLIVE = Expected SEQ Number - 1" </code>.</p><p>So it will tell the system 192.168.0.23 that it is still waiting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '15, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-46291" class="comments-container"></div><div id="comment-tools-46291" class="comment-tools"></div><div class="clear"></div><div id="comment-46291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

