+++
type = "question"
title = "why multiple FIDs for the same folder"
description = '''Hi, when i try to read files in a folder in a network share(windows 7 client), i see multiple SMB CREATE ANDX requests with different FIDs for the same folder. In some instances, there are multiple searches going on for the same folder.  Can someone please help me understand what is really going on ...'''
date = "2015-03-08T10:24:00Z"
lastmod = "2015-03-11T03:27:00Z"
weight = 40367
keywords = [ "samba", "cifs", "wireshark" ]
aliases = [ "/questions/40367" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [why multiple FIDs for the same folder](/questions/40367/why-multiple-fids-for-the-same-folder)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40367-score" class="post-score" title="current number of votes">0</div><span id="post-40367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, when i try to read files in a folder in a network share(windows 7 client), i see multiple SMB CREATE ANDX requests with different FIDs for the same folder. In some instances, there are multiple searches going on for the same folder. Can someone please help me understand what is really going on here?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-samba" rel="tag" title="see questions tagged &#39;samba&#39;">samba</span> <span class="post-tag tag-link-cifs" rel="tag" title="see questions tagged &#39;cifs&#39;">cifs</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '15, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/bc1e7422b9e06f3c3d9d6f68a870c202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xerocool&#39;s gravatar image" /><p><span>xerocool</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xerocool has no accepted answers">0%</span></p></div></div><div id="comments-container-40367" class="comments-container"><span id="40370"></span><div id="comment-40370" class="comment"><div id="post-40370-score" class="comment-score"></div><div class="comment-text"><p>Are you reading them in a program that you wrote or are you viewing them in somebody else's program, such as Windows Explorer?</p></div><div id="comment-40370-info" class="comment-info"><span class="comment-age">(08 Mar '15, 17:02)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="40373"></span><div id="comment-40373" class="comment"><div id="post-40373-score" class="comment-score"></div><div class="comment-text"><p>am viewing them in windows explorer.</p></div><div id="comment-40373-info" class="comment-info"><span class="comment-age">(08 Mar '15, 20:20)</span> <span class="comment-user userinfo">xerocool</span></div></div></div><div id="comment-tools-40367" class="comment-tools"></div><div class="clear"></div><div id="comment-40367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40374"></span>

<div id="answer-container-40374" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40374-score" class="post-score" title="current number of votes">1</div><span id="post-40374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The most likely "someone" would be somebody from the Windows Explorer team at Microsoft.</p><p>The different FIDs either result from opens of the folder being done while other opens are still active, so that a new FID has to be assigned for each new open, or from the SMB server not immediately reusing FIDs.</p><p>If there are multiple searches in parallel being done by Windows Explorer, those would, when accessing an SMB-mounted folder, translate into multiple opens (SMB CreateAndX requests) going over the wire.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '15, 22:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40374" class="comments-container"><span id="40375"></span><div id="comment-40375" class="comment"><div id="post-40375-score" class="comment-score"></div><div class="comment-text"><p>There are no multiple searches being done and my machine is the only client opening that particular share. I took the trace when I opened the folder just once and that's it. So there are no other opens still active.</p><p>Can you please explain the "SMB server not immediately reusing FIDs" part a little more? I am new to CIFS/SMB.</p></div><div id="comment-40375-info" class="comment-info"><span class="comment-age">(09 Mar '15, 01:32)</span> <span class="comment-user userinfo">xerocool</span></div></div><span id="40377"></span><div id="comment-40377" class="comment"><div id="post-40377-score" class="comment-score"></div><div class="comment-text"><blockquote><p>There are no multiple searches being done</p></blockquote><p>Have you run some tracing program against the Windows Explorer to be certain that it does not, for example, have multiple threads making <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa364418(v=vs.85).aspx">FindFirstFile</a> and <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa364428(v=vs.85).aspx">FindNextFile</a> calls? If not, then you don't know for certain whether multiple searches are being done.</p><blockquote><p>Can you please explain the "SMB server not immediately reusing FIDs" part a little more?</p></blockquote><p>Section 2.2.1.6.1 "FID Generation" of the [MS-CIFS] specification says that:</p><ul><li><p>The <strong>FID</strong> MUST be unique within a specified client/server SMB connection.</p></li><li><p>The <strong>FID</strong> MUST remain valid for the lifetime of the SMB connection on which the open request is performed, or until the client sends a request to the server to close the <strong>FID</strong>.</p></li><li><p>Once a <strong>FID</strong> has been closed, the value can be reused for another create or open request.</p></li></ul><p>so FIDs can't be reused as long as they're open; they <em>can</em> be reused once closed, but the server isn't <em>obliged</em> to reuse them immediately. It may eventually have to reuse them, as they're only 16 bits wide, but, for whatever reason, it might choose not to do so.</p></div><div id="comment-40377-info" class="comment-info"><span class="comment-age">(09 Mar '15, 01:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="40462"></span><div id="comment-40462" class="comment"><div id="post-40462-score" class="comment-score"></div><div class="comment-text"><p>You are right. The simultaneous searches occurred just once. I guess there was an active search opened from before.</p><p>The part regarding the FID reuse makes sense too. Thanks!</p><p>However, now the the client sends a createAndx request, partial listing of the files in the folder is done before it sends a close2 request to stop that. It then resends the CreateAndX request(with FID incremeted by 1) and the listing begins again. This time, its successful.</p><p>Could this be due to the fact that the request asked for oplocks and none were granted? So it keeps trying to open the folder, do some operation and close it afterwards repeatedly?</p></div><div id="comment-40462-info" class="comment-info"><span class="comment-age">(11 Mar '15, 03:27)</span> <span class="comment-user userinfo">xerocool</span></div></div></div><div id="comment-tools-40374" class="comment-tools"></div><div class="clear"></div><div id="comment-40374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

