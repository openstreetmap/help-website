+++
type = "question"
title = "Verify a password is not sent in clear text"
description = '''I&#x27;m totally new to wireshark so I need help in checking out, to verify a password is not sent in clear text. In the process of testing a powershell script which uses an AD account and password to connect to a vsphere server and carry out some tasks. I have used a powershell method which uses a secur...'''
date = "2015-01-08T05:04:00Z"
lastmod = "2015-01-08T07:04:00Z"
weight = 38947
keywords = [ "password" ]
aliases = [ "/questions/38947" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Verify a password is not sent in clear text](/questions/38947/verify-a-password-is-not-sent-in-clear-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38947-score" class="post-score" title="current number of votes">0</div><span id="post-38947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm totally new to wireshark so I need help in checking out, to verify a password is not sent in clear text. In the process of testing a powershell script which uses an AD account and password to connect to a vsphere server and carry out some tasks. I have used a powershell method which uses a secured way to protect the password but want to check and make sure it is working correctly in a test environment. Do I install wireshark on the computer which runs the powershell script? How do I search the entire capture to try and find the password of the account used in the powershell script? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '15, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/7392cd11ff5cb6775a0a18e0478471ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dvenner&#39;s gravatar image" /><p><span>dvenner</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dvenner has no accepted answers">0%</span></p></div></div><div id="comments-container-38947" class="comments-container"></div><div id="comment-tools-38947" class="comment-tools"></div><div class="clear"></div><div id="comment-38947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38948"></span>

<div id="answer-container-38948" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38948-score" class="post-score" title="current number of votes">0</div><span id="post-38948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For tasks like that it's acceptable to install Wireshark on the PC you run the Powershell script on. Easiest way to check for clear text passwords would be to start the capture, run the script and stop the capture after a while.</p><p>Then use the Statistics -&gt; Conversation Statistics to filter on each conversation that talks to the vSphere server. Finally, use "Follow TCP stream" on each of them to see if there is plain ASCII anywhere.</p><p>You could also use the "find" dialog in string search mode to find the password directly - if you find nothing you can assume the password to be encrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '15, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38948" class="comments-container"><span id="38958"></span><div id="comment-38958" class="comment"><div id="post-38958-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick response and very useful. Just one further question on your last point use "find" in string search, how do I access this search feature?</p></div><div id="comment-38958-info" class="comment-info"><span class="comment-age">(08 Jan '15, 06:57)</span> <span class="comment-user userinfo">dvenner</span></div></div><span id="38959"></span><div id="comment-38959" class="comment"><div id="post-38959-score" class="comment-score"></div><div class="comment-text"><p>You can find the dialog for that choosing "Edit" -&gt; "Find Packet" (or pressing CTRL-F). Make sure you select "by string".</p></div><div id="comment-38959-info" class="comment-info"><span class="comment-age">(08 Jan '15, 07:04)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-38948" class="comment-tools"></div><div class="clear"></div><div id="comment-38948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

