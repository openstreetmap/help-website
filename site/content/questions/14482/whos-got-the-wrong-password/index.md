+++
type = "question"
title = "Who&#x27;s got the wrong password?"
description = '''Hi (wireshark newbee here), I work in a school where we occasionally have to update client software from an external local education authority source. This means we have to use a mapped drive to a server on a different subnet thus requiring a different domain&#92;username and password. As this update ap...'''
date = "2012-09-24T08:19:00Z"
lastmod = "2012-09-26T03:27:00Z"
weight = 14482
keywords = [ "capture", "window" ]
aliases = [ "/questions/14482" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Who's got the wrong password?](/questions/14482/whos-got-the-wrong-password)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14482-score" class="post-score" title="current number of votes">0</div><span id="post-14482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi (wireshark newbee here), I work in a school where we occasionally have to update client software from an external local education authority source. This means we have to use a mapped drive to a server on a different subnet thus requiring a different domain\username and password. As this update applies to more than 30 members of staff the mapped drive is connected via batch script with one username and password. The problem occurs after 30days when the password is due for renewal. Some of the pc's seem to have cached the login details thus giving the wrong passord after the 30days. Three tries of the wrong password and it's a lockout resulting in multiple phone calls to our LEA!! I can use wireshark to find all the source ip addresses contacting the destination ip but is there a way of using the capture window to see when the password is failing so that I can identify the ip address (therefore hostname)of the rogue pc's?</p><p>Thanks in advance for any suggestions</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '12, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/c160b8d4d634984a852546919917b489?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xenolith5&#39;s gravatar image" /><p><span>xenolith5</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xenolith5 has no accepted answers">0%</span></p></div></div><div id="comments-container-14482" class="comments-container"></div><div id="comment-tools-14482" class="comment-tools"></div><div class="clear"></div><div id="comment-14482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14501"></span>

<div id="answer-container-14501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14501-score" class="post-score" title="current number of votes">0</div><span id="post-14501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm guessing you're using SMB for your folder sharing, if not then please specify which protocol your looking at.</p><p>If it is SMB you're using then then you could try putting this in the Filter command box smb.nt_status != STATUS_SUCCESS for a general view of what's going wrong or smb.nt_status == STATUS_WRONG_PASSWORD for the packets you really want.</p><p>Cheers,</p><p>Craig.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '12, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/7f557535084abef24cd30661f9daefad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CTNOBLE&#39;s gravatar image" /><p><span>CTNOBLE</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CTNOBLE has no accepted answers">0%</span></p></div></div><div id="comments-container-14501" class="comments-container"><span id="14536"></span><div id="comment-14536" class="comment"><div id="post-14536-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the filters and sorry for the slow reply. I've been off site so couldn't test. Will see how it goes asap</p></div><div id="comment-14536-info" class="comment-info"><span class="comment-age">(26 Sep '12, 03:27)</span> <span class="comment-user userinfo">xenolith5</span></div></div></div><div id="comment-tools-14501" class="comment-tools"></div><div class="clear"></div><div id="comment-14501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

