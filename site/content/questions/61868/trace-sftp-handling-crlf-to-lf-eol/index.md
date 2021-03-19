+++
type = "question"
title = "Trace SFTP handling CRLF to LF EOL"
description = '''Hi, We are using Jcraft java library and it is using SFTP to transfer the our own shell script file name &quot;A&quot; from windows to Linux OS. Sometimes it was showing up as DOS format at Linux machine since copied at Linux, due to this reason we are not able to execute this shell script. So, do we have any...'''
date = "2017-06-08T08:10:00Z"
lastmod = "2017-06-08T14:18:00Z"
weight = 61868
keywords = [ "handling", "crlf_to_lf_eol", "trace", "sftp" ]
aliases = [ "/questions/61868" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trace SFTP handling CRLF to LF EOL](/questions/61868/trace-sftp-handling-crlf-to-lf-eol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61868-score" class="post-score" title="current number of votes">0</div><span id="post-61868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, We are using Jcraft java library and it is using SFTP to transfer the our own shell script file name "A" from windows to Linux OS. Sometimes it was showing up as DOS format at Linux machine since copied at Linux, due to this reason we are not able to execute this shell script. So, do we have any option/flags/something in wire shark? Does this wire shark indicate us "it changes from CRLF to LF" ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-handling" rel="tag" title="see questions tagged &#39;handling&#39;">handling</span> <span class="post-tag tag-link-crlf_to_lf_eol" rel="tag" title="see questions tagged &#39;crlf_to_lf_eol&#39;">crlf_to_lf_eol</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span> <span class="post-tag tag-link-sftp" rel="tag" title="see questions tagged &#39;sftp&#39;">sftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '17, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/a8b61416fae5662658f43a1b4a867214?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kalyanasundaram&#39;s gravatar image" /><p><span>kalyanasundaram</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kalyanasundaram has no accepted answers">0%</span></p></div></div><div id="comments-container-61868" class="comments-container"></div><div id="comment-tools-61868" class="comment-tools"></div><div class="clear"></div><div id="comment-61868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61880"></span>

<div id="answer-container-61880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61880-score" class="post-score" title="current number of votes">0</div><span id="post-61880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>FTP services work with so called modes for transport of files. These modes are 'text' and 'binary'. In the former any transcoding may take place to create a file conforming to local formatting. In the latter no transcoding is applied at all. I can assume that you'll have to make sure the transport mode is text so that local EOL encoding is applied.</p><p>In Wireshark you may be able to find the mode setting in packets exchanged across the command channel, but it could also be that the default is used, and that this may not always be the state you require.</p><p>And then you're talking about SFTP, so you'll have to decrypt first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '17, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61880" class="comments-container"></div><div id="comment-tools-61880" class="comment-tools"></div><div class="clear"></div><div id="comment-61880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

