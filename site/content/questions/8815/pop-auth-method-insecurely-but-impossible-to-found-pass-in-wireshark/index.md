+++
type = "question"
title = "POP auth method insecurely but impossible to found PASS in Wireshark!"
description = '''Hello, When I analyze POP packets with Wireshark, when I receive emails with Outlook, I can see USER and PASS commands with username and password transmitted unecrypted. But if I try to get my emails with Thunderbird (without encryption), I CANNOT see in Wireshark USER and PASS commands, and for sur...'''
date = "2012-02-03T13:56:00Z"
lastmod = "2012-02-06T07:19:00Z"
weight = 8815
keywords = [ "encrypted", "outlook", "password", "thunderbird", "pop" ]
aliases = [ "/questions/8815" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [POP auth method insecurely but impossible to found PASS in Wireshark!](/questions/8815/pop-auth-method-insecurely-but-impossible-to-found-pass-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8815-score" class="post-score" title="current number of votes">0</div><span id="post-8815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>When I analyze POP packets with Wireshark, when I receive emails with Outlook, I can see USER and PASS commands with username and password transmitted unecrypted.</p><p>But if I try to get my emails with Thunderbird (without encryption), I CANNOT see in Wireshark USER and PASS commands, and for sure, no username and password !!</p><p>But there are new commands :</p><ul><li>AUTH : PLAIN</li><li>Request command : AGNsZW1lbnQuYm9ubmFsADJ4cgt0OQ==</li></ul><p>I don't understand why, is there a way to get them ??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encrypted" rel="tag" title="see questions tagged &#39;encrypted&#39;">encrypted</span> <span class="post-tag tag-link-outlook" rel="tag" title="see questions tagged &#39;outlook&#39;">outlook</span> <span class="post-tag tag-link-password" rel="tag" title="see questions tagged &#39;password&#39;">password</span> <span class="post-tag tag-link-thunderbird" rel="tag" title="see questions tagged &#39;thunderbird&#39;">thunderbird</span> <span class="post-tag tag-link-pop" rel="tag" title="see questions tagged &#39;pop&#39;">pop</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '12, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/5cb9dd3678bfab432157941dc1222b4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cl%C3%A9ment%20Bonnal&#39;s gravatar image" /><p><span>Clément Bonnal</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clément Bonnal has no accepted answers">0%</span></p></div></div><div id="comments-container-8815" class="comments-container"></div><div id="comment-tools-8815" class="comment-tools"></div><div class="clear"></div><div id="comment-8815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8833"></span>

<div id="answer-container-8833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8833-score" class="post-score" title="current number of votes">1</div><span id="post-8833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Clément,</p><p>the information is Base 64 encoded and can be decoded easily (but Wireshark does not do that for you). The strange output is due to null bytes being present in the decoded string. See RFC 2595 [2] for more information.</p><pre><code>echo &quot;AGNsZW1lbnQuYm9ubmFsADJ4cgt0OQ==&quot; | base64 -d
clement.bonnal2xr
                 t9</code></pre><p>The plain authentication method only uses one command to transmit the credentials, unlike the login method which uses two commands(user,pass).</p><p>[1] http://www.fehcom.de/qmail/smtpauth.html [2] http://tools.ietf.org/html/rfc2595[2]</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '12, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/ecde384d426d858745b3fcb0d497cd97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="otr&#39;s gravatar image" /><p><span>otr</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="otr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Feb '12, 05:30</strong> </span></p></div></div><div id="comments-container-8833" class="comments-container"><span id="8847"></span><div id="comment-8847" class="comment"><div id="post-8847-score" class="comment-score"></div><div class="comment-text"><p>As the question refers to Outlook, it's likely that the user is on windows without access to the usual Unix utils. A PowerShell equivalent is shown below:</p><pre><code>[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(&quot;AGNsZW1lbnQuYm9ubmFsADJ4cgt0OQ==&quot;))</code></pre></div><div id="comment-8847-info" class="comment-info"><span class="comment-age">(06 Feb '12, 07:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-8833" class="comment-tools"></div><div class="clear"></div><div id="comment-8833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

