+++
type = "question"
title = "Active Directory User Account Capture"
description = '''How to trace an AD account lockout issue using wireshark.How to trace the caller computer inside my network'''
date = "2013-11-20T20:22:00Z"
lastmod = "2013-11-21T06:12:00Z"
weight = 27192
keywords = [ "active", "directory", "rogue", "password" ]
aliases = [ "/questions/27192" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Active Directory User Account Capture](/questions/27192/active-directory-user-account-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27192-score" class="post-score" title="current number of votes">0</div><span id="post-27192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to trace an AD account lockout issue using wireshark.How to trace the caller computer inside my network</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-active" rel="tag" title="see questions tagged &#39;active&#39;">active</span> <span class="post-tag tag-link-directory" rel="tag" title="see questions tagged &#39;directory&#39;">directory</span> <span class="post-tag tag-link-rogue" rel="tag" title="see questions tagged &#39;rogue&#39;">rogue</span> <span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 20:22</strong></p><img src="https://secure.gravatar.com/avatar/ba527fc823d8f95e1811ae5326d3b3ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anand%20Giri&#39;s gravatar image" /><p><span>Anand Giri</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anand Giri has no accepted answers">0%</span></p></div></div><div id="comments-container-27192" class="comments-container"></div><div id="comment-tools-27192" class="comment-tools"></div><div class="clear"></div><div id="comment-27192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27217"></span>

<div id="answer-container-27217" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27217-score" class="post-score" title="current number of votes">0</div><span id="post-27217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How to trace an AD account lockout issue using wireshark.How to trace the caller computer inside my network</p></blockquote><p>Well, that's not really easy with a network trace, as the account lockout could have a range of possible reasons and the offending system could use LDAP (plaintext) or LDAPS (encrypted via TLS) or Kerberos. As soon as encryption is part of the game (LDAPS or Kerberos), the effort to figure out the problem via a network capture tool, raises fairly fast.</p><p>If I had to analyze that kind of problem, I would use built in tools of Windows, like Security Eventlogs, or the 'new' <a href="http://technet.microsoft.com/en-us/library/jj649776.aspx">Windows Message Analyzer</a>, rather than a network capture tool.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '13, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '13, 06:13</strong> </span></p></div></div><div id="comments-container-27217" class="comments-container"></div><div id="comment-tools-27217" class="comment-tools"></div><div class="clear"></div><div id="comment-27217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

