+++
type = "question"
title = "Capture Multiple Files"
description = '''Hi guys, I have a problem with wireshark creating multiple files. I try to capture the network trafic for several days on a system with the following options: -use multiple files -next file every 2 megabytes -ring buffer with 9999 files unfortunaly this doesn&#x27;t work! There are two different things h...'''
date = "2013-09-16T04:46:00Z"
lastmod = "2013-09-18T01:37:00Z"
weight = 24745
keywords = [ "files", "capture", "ring", "multiple", "buffer" ]
aliases = [ "/questions/24745" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Multiple Files](/questions/24745/capture-multiple-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24745-score" class="post-score" title="current number of votes">0</div><span id="post-24745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I have a problem with wireshark creating multiple files. I try to capture the network trafic for several days on a system with the following options: -use multiple files -next file every 2 megabytes -ring buffer with 9999 files</p><p>unfortunaly this doesn't work! There are two different things happening. 1. the system opens several wiresharkwindows which all tell me "closing files" but nothing happens. 2. the wireshark application crashes with an Application error Event ID 1000. The system had already created 800 capture files saved at this time, but then it stops with this application error....</p><p>wireshark version is 1.8.2.44520 and it runs on Windows 2008 Server</p><p>Sorry for my bad english, but I'm from Germany and still learning....</p><p>I would be happy to hear from you. Any help will be appreciated! Please let me know if further information or data is required!</p><p>Thanks &amp; Regards Wolfgang</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-ring" rel="tag" title="see questions tagged &#39;ring&#39;">ring</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-buffer" rel="tag" title="see questions tagged &#39;buffer&#39;">buffer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '13, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/00b79d2922d04a1c82b5a601e0359761?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wolfy&#39;s gravatar image" /><p><span>Wolfy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wolfy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Sep '13, 04:47</strong> </span></p></div></div><div id="comments-container-24745" class="comments-container"><span id="24761"></span><div id="comment-24761" class="comment"><div id="post-24761-score" class="comment-score"></div><div class="comment-text"><p>When you experienced the <em>"Closing File"</em> problem, was it the same as what is described in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3046">bug 3046</a>? That bug was closed as fixed for releases after 1.6.x, but perhaps it's not truly fixed and should be reopened. If you do reopen it, if you any have more information that might help someone recreate/test/fix it, please provide it.</p></div><div id="comment-24761-info" class="comment-info"><span class="comment-age">(16 Sep '13, 07:23)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-24745" class="comment-tools"></div><div class="clear"></div><div id="comment-24745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24746"></span>

<div id="answer-container-24746" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24746-score" class="post-score" title="current number of votes">0</div><span id="post-24746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at this: <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '13, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24746" class="comments-container"><span id="24748"></span><div id="comment-24748" class="comment"><div id="post-24748-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>thanks a lot for your quick answer. I'm going to try this "dumpcap" thing and let you know if it won't work, too ;-)</p><p>Regards Wolfgang</p></div><div id="comment-24748-info" class="comment-info"><span class="comment-age">(16 Sep '13, 05:22)</span> <span class="comment-user userinfo">Wolfy</span></div></div><span id="24770"></span><div id="comment-24770" class="comment"><div id="post-24770-score" class="comment-score"></div><div class="comment-text"><p>As Jasper said, dumpcap is certainly the way to go for this type of capturing.</p><p>But it's also interesting that you're hitting this problem. It sounds like <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3046">bug 3046</a> which is supposed to be fixed in the 1.8.x versions.</p></div><div id="comment-24770-info" class="comment-info"><span class="comment-age">(16 Sep '13, 08:28)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="24885"></span><div id="comment-24885" class="comment"><div id="post-24885-score" class="comment-score"></div><div class="comment-text"><p>Hi cmaynard, Hi Jeff,</p><p>thanks a lot for your answers!</p><p>I think you are right. It sounds like the ""Closing File!" Dialog Hangs - Bug" and I'm already running wireshark version 1.8.2.44520 on Windows 2008 Server, so I'm not sure if bug 3046 is realy fixed... I tried several different settings and found that it is working if I limit the size of the file to 1MB. With a file size of 2 MB this "closing file" Error happens after a while.</p><p>Unfortunately I have no experience how to "reopen a bug" or what data or information might be relevant to do this....</p><p>Again, thanks a lot Wolfgang</p></div><div id="comment-24885-info" class="comment-info"><span class="comment-age">(18 Sep '13, 01:37)</span> <span class="comment-user userinfo">Wolfy</span></div></div></div><div id="comment-tools-24746" class="comment-tools"></div><div class="clear"></div><div id="comment-24746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24747"></span>

<div id="answer-container-24747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24747-score" class="post-score" title="current number of votes">0</div><span id="post-24747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See also <a href="http://ask.wireshark.org/questions/23891/wireshark-wont-run-with-multiple-capture-files">this</a> question and note the answer from <span>@cmaynard</span>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '13, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24747" class="comments-container"></div><div id="comment-tools-24747" class="comment-tools"></div><div class="clear"></div><div id="comment-24747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

