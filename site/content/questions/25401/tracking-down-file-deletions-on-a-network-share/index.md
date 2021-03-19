+++
type = "question"
title = "Tracking down file deletions on a network share"
description = '''I need to track down who marked what files for deletion when. This is on a network shared drive on a Windows server. If someone can help me set up a capture that will only look for SMB requests and tell me how to crunch that data that would be great!'''
date = "2013-09-30T10:12:00Z"
lastmod = "2013-09-30T11:46:00Z"
weight = 25401
keywords = [ "auditing", "samba", "smb", "deletion" ]
aliases = [ "/questions/25401" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tracking down file deletions on a network share](/questions/25401/tracking-down-file-deletions-on-a-network-share)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25401-score" class="post-score" title="current number of votes">0</div><span id="post-25401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to track down who marked what files for deletion when. This is on a network shared drive on a Windows server. If someone can help me set up a capture that will only look for SMB requests and tell me how to crunch that data that would be great!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-auditing" rel="tag" title="see questions tagged &#39;auditing&#39;">auditing</span> <span class="post-tag tag-link-samba" rel="tag" title="see questions tagged &#39;samba&#39;">samba</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span> <span class="post-tag tag-link-deletion" rel="tag" title="see questions tagged &#39;deletion&#39;">deletion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '13, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/b5ee883976d91bd6cfceb588c700707a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trogdor3000&#39;s gravatar image" /><p><span>trogdor3000</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trogdor3000 has no accepted answers">0%</span></p></div></div><div id="comments-container-25401" class="comments-container"></div><div id="comment-tools-25401" class="comment-tools"></div><div class="clear"></div><div id="comment-25401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25405"></span>

<div id="answer-container-25405" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25405-score" class="post-score" title="current number of votes">0</div><span id="post-25405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you're much more likely to solve your issue by using the built-in Windows auditing tools to track file deletions. A little Googling came up with <a href="http://sogeeky.blogspot.co.uk/2006/07/how-to-audit-and-track-file-deletions.html">this</a>, I have no idea if it works though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '13, 10:38</strong> </span></p></div></div><div id="comments-container-25405" class="comments-container"><span id="25406"></span><div id="comment-25406" class="comment"><div id="post-25406-score" class="comment-score"></div><div class="comment-text"><p>This does not give the IP of the machines that the username of the user making the requests. I know there is a request being sent tat is marking files for deletion.</p></div><div id="comment-25406-info" class="comment-info"><span class="comment-age">(30 Sep '13, 10:39)</span> <span class="comment-user userinfo">trogdor3000</span></div></div></div><div id="comment-tools-25405" class="comment-tools"></div><div class="clear"></div><div id="comment-25405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25408"></span>

<div id="answer-container-25408" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25408-score" class="post-score" title="current number of votes">0</div><span id="post-25408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A brief test with my own SMB system (a run of the mill SMB sharing NAS appliance) shows that windows will delete files using the "delete on close" disposition status. You can filter for this using "smb.disposition.delete_on_close == 1" however there might be other states used that cause a file to be deleted. To best diagnose the issue you will probably want to look at all SMB traffic, filter for each IP host (roughly sorting out your users so you know who is doing what) and then look for file info sets with the filter "smb.trans2.cmd == 0x0008". Hope this helps!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/9ee282b379860571958ec7b61855d7d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ipchains1&#39;s gravatar image" /><p><span>ipchains1</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ipchains1 has no accepted answers">0%</span></p></div></div><div id="comments-container-25408" class="comments-container"></div><div id="comment-tools-25408" class="comment-tools"></div><div class="clear"></div><div id="comment-25408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

