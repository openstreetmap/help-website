+++
type = "question"
title = "Find bad password attempt in capture file"
description = '''How and where do I find an incorrect password was provided in a capture file? I do not need to know the password, but just what to look for to know for sure an incorrect password was given. '''
date = "2017-03-08T12:43:00Z"
lastmod = "2017-03-08T13:20:00Z"
weight = 59932
keywords = [ "password" ]
aliases = [ "/questions/59932" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find bad password attempt in capture file](/questions/59932/find-bad-password-attempt-in-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59932-score" class="post-score" title="current number of votes">0</div><span id="post-59932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How and where do I find an incorrect password was provided in a capture file? I do not need to know the password, but just what to look for to know for sure an incorrect password was given.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '17, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/d93efca3dee12e9f3df6283c38ba36d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neilinpa&#39;s gravatar image" /><p><span>neilinpa</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neilinpa has no accepted answers">0%</span></p></div></div><div id="comments-container-59932" class="comments-container"></div><div id="comment-tools-59932" class="comment-tools"></div><div class="clear"></div><div id="comment-59932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59933"></span>

<div id="answer-container-59933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59933-score" class="post-score" title="current number of votes">2</div><span id="post-59933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That totally depends on the protocol and the application. So you need to find out how the protocol transports the password, and then try to find it. These days, chances are that the protocol is using some sort of encryption to transfer passwords, in which case you won't be able to see it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '17, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-59933" class="comments-container"><span id="59934"></span><div id="comment-59934" class="comment"><div id="post-59934-score" class="comment-score"></div><div class="comment-text"><p>The only protocols (there is a heading in the capture file) listed are TCP and SMB. I do not necessarily want to see what the password actually is, just where it failed in the capture.</p></div><div id="comment-59934-info" class="comment-info"><span class="comment-age">(08 Mar '17, 12:55)</span> <span class="comment-user userinfo">neilinpa</span></div></div><span id="59935"></span><div id="comment-59935" class="comment"><div id="post-59935-score" class="comment-score"></div><div class="comment-text"><p>SMB doesn't transfer readable passwords, it uses password hashes. You need to look for SMB return codes telling you that a request failed, e.g. by looking at the "NT Status" fields in the SMB header.</p></div><div id="comment-59935-info" class="comment-info"><span class="comment-age">(08 Mar '17, 12:59)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="59936"></span><div id="comment-59936" class="comment"><div id="post-59936-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I found the line: NT Status: STATUS_LOGON_FAILURE (0XC000006D)<br />
Then I googled that and found: The potential causes for this</p><ol><li>An invalid username and/or password was used</li></ol><p>a. Verify you are using the correct username or password</p><p>So my question has been answered. Thanks for help Jasper.</p></div><div id="comment-59936-info" class="comment-info"><span class="comment-age">(08 Mar '17, 13:16)</span> <span class="comment-user userinfo">neilinpa</span></div></div><span id="59937"></span><div id="comment-59937" class="comment"><div id="post-59937-score" class="comment-score"></div><div class="comment-text"><p>Great, glad to be of help. You could accept the answer using the checkmark button to the left of it, so others can see it was the one that helped ;-)</p></div><div id="comment-59937-info" class="comment-info"><span class="comment-age">(08 Mar '17, 13:20)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-59933" class="comment-tools"></div><div class="clear"></div><div id="comment-59933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

