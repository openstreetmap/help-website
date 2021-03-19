+++
type = "question"
title = "Deleting files after live capture"
description = '''Hi, How do I get rid of those temporarily files wireshark writes onto my hard disk after a live capture. I don&#x27;t want to run out of space. Can you guys give me some ways to clear up the files to free up some? Thank you in advance for your help!'''
date = "2015-09-07T07:26:00Z"
lastmod = "2015-09-07T10:02:00Z"
weight = 45663
keywords = [ "files", "capture", "live", "after", "deleting" ]
aliases = [ "/questions/45663" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Deleting files after live capture](/questions/45663/deleting-files-after-live-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45663-score" class="post-score" title="current number of votes">0</div><span id="post-45663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>How do I get rid of those temporarily files wireshark writes onto my hard disk after a live capture. I don't want to run out of space. Can you guys give me some ways to clear up the files to free up some?</p><p>Thank you in advance for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-live" rel="tag" title="see questions tagged &#39;live&#39;">live</span> <span class="post-tag tag-link-after" rel="tag" title="see questions tagged &#39;after&#39;">after</span> <span class="post-tag tag-link-deleting" rel="tag" title="see questions tagged &#39;deleting&#39;">deleting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '15, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/cf4be01b061a5afaa89a0ede264563b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karanza&#39;s gravatar image" /><p><span>Karanza</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karanza has no accepted answers">0%</span></p></div></div><div id="comments-container-45663" class="comments-container"></div><div id="comment-tools-45663" class="comment-tools"></div><div class="clear"></div><div id="comment-45663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45664"></span>

<div id="answer-container-45664" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45664-score" class="post-score" title="current number of votes">0</div><span id="post-45664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The temporary file should be automatically removed when you either close the capture, or save it to a named file. What version of Wireshark and which OS are you using?</p><p>However, testing (1.12.7 on Windows 8.1) shows that if the capture is saved to a named file, then the temporary file is not removed. This looks like a bug to me and should be reported on the Wireshark <a href="https://bugs.wireshark.org">Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45664" class="comments-container"><span id="45670"></span><div id="comment-45670" class="comment"><div id="post-45670-score" class="comment-score"></div><div class="comment-text"><p>I'm using a windows 7 64bit computer. I have the same version of wireshark like you've mentioned earlier.</p></div><div id="comment-45670-info" class="comment-info"><span class="comment-age">(07 Sep '15, 10:02)</span> <span class="comment-user userinfo">Karanza</span></div></div></div><div id="comment-tools-45664" class="comment-tools"></div><div class="clear"></div><div id="comment-45664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

