+++
type = "question"
title = "Get full NFS path/filename for object"
description = '''When analyzing wireshark data, none of the NFS path/filenames are available even after selecting  the option to show full path and file name. How can I see the full NFS path and file name that was accessed? Please advise. Additional data. NFS v3, source data is on NetApp running Ontap 7.1.x; wiresha...'''
date = "2010-10-09T09:53:00Z"
lastmod = "2010-10-10T13:50:00Z"
weight = 467
keywords = [ "path", "nfs" ]
aliases = [ "/questions/467" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Get full NFS path/filename for object](/questions/467/get-full-nfs-pathfilename-for-object)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-467-score" class="post-score" title="current number of votes">0</div><span id="post-467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When analyzing wireshark data, none of the NFS path/filenames are available even after selecting the option to show full path and file name. How can I see the full NFS path and file name that was accessed? Please advise.</p><p>Additional data. NFS v3, source data is on NetApp running Ontap 7.1.x; wireshark capturing NFS data on port 2049 from Linux SLES10 client (autofs). I can see all access,getattr,setattr, etc. i need to figure out how to see each NFS path/filename (full path &amp; file name)</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-nfs" rel="tag" title="see questions tagged &#39;nfs&#39;">nfs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '10, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/80ec40e1e7b5c00d1bdfa2f15021dc3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="debugme&#39;s gravatar image" /><p><span>debugme</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="debugme has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Oct '10, 09:57</strong> </span></p></div></div><div id="comments-container-467" class="comments-container"></div><div id="comment-tools-467" class="comment-tools"></div><div class="clear"></div><div id="comment-467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="472"></span>

<div id="answer-container-472" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-472-score" class="post-score" title="current number of votes">1</div><span id="post-472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="debugme has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can only see the full pathname for a file if:</p><ul><li><p>for a request that includes a file name (LOOKUP, REMOVE, RENAME, CREATE, etc.), replies that provide the file names of all directories in the path of the directory in which that request was done appear in the capture before the request in question;</p></li><li><p>for a request that includes only a file handle (ACCESS, GETATTR, SETATTR, etc.), replies that provide the file names of all those directories <em>and</em> the file to which the file handle refers appear in the capture appear in the capture before the request in question.</p></li></ul><p>In general, there's no guarantee that you <em>can</em> see the full path name - or even just the file name - corresponding to a given file handle in an arbitrary capture. That's just how NFS works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '10, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Oct '10, 13:51</strong> </span></p></div></div><div id="comments-container-472" class="comments-container"></div><div id="comment-tools-472" class="comment-tools"></div><div class="clear"></div><div id="comment-472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

