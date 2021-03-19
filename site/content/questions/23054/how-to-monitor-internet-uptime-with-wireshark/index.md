+++
type = "question"
title = "How to monitor internet uptime with Wireshark?"
description = '''Hi everyone,  I was told that I could use Wireshark to monitor internet uptime. I&#x27;m trying to determine if our internet connection is dropping out sporadically, causing our Verizon network extenders to continuously go down.  Can Wireshark help me with this solution?  Thank you for your time! Ben '''
date = "2013-07-16T12:07:00Z"
lastmod = "2013-08-09T03:04:00Z"
weight = 23054
keywords = [ "uptime", "internet" ]
aliases = [ "/questions/23054" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to monitor internet uptime with Wireshark?](/questions/23054/how-to-monitor-internet-uptime-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23054-score" class="post-score" title="current number of votes">0</div><span id="post-23054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I was told that I could use Wireshark to monitor internet uptime. I'm trying to determine if our internet connection is dropping out sporadically, causing our Verizon network extenders to continuously go down.</p><p>Can Wireshark help me with this solution?</p><p>Thank you for your time! Ben</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-uptime" rel="tag" title="see questions tagged &#39;uptime&#39;">uptime</span> <span class="post-tag tag-link-internet" rel="tag" title="see questions tagged &#39;internet&#39;">internet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '13, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/87a6ba6fb3c362e211133f57f0c32ee5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ben%20Bolduc&#39;s gravatar image" /><p><span>Ben Bolduc</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ben Bolduc has no accepted answers">0%</span></p></div></div><div id="comments-container-23054" class="comments-container"></div><div id="comment-tools-23054" class="comment-tools"></div><div class="clear"></div><div id="comment-23054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23057"></span>

<div id="answer-container-23057" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23057-score" class="post-score" title="current number of votes">1</div><span id="post-23057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ben Bolduc has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFAIK Wireshark is not designed for monitoring but for Packet/Protocol analysis.Few vendors like (Gigamon,Endace,Netoptics) are exclusively in that monitoring space.Monitoring requires lot of memory and processing power.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '13, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-23057" class="comments-container"><span id="23069"></span><div id="comment-23069" class="comment"><div id="post-23069-score" class="comment-score"></div><div class="comment-text"><p>Fair enough, that was very helpful, thank you much!</p></div><div id="comment-23069-info" class="comment-info"><span class="comment-age">(17 Jul '13, 05:17)</span> <span class="comment-user userinfo">Ben Bolduc</span></div></div><span id="23083"></span><div id="comment-23083" class="comment"><div id="post-23083-score" class="comment-score"></div><div class="comment-text"><p>A good solution to monitor internet 'uptime' would be SmokePing</p><blockquote><p><a href="http://oss.oetiker.ch/smokeping/">http://oss.oetiker.ch/smokeping/</a></p></blockquote></div><div id="comment-23083-info" class="comment-info"><span class="comment-age">(17 Jul '13, 15:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-23057" class="comment-tools"></div><div class="clear"></div><div id="comment-23057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23673"></span>

<div id="answer-container-23673" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23673-score" class="post-score" title="current number of votes">0</div><span id="post-23673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Such tools Wireshark or Anturis were not designed to help in these matters. It is even better to contact Internet providers and ask for help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '13, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/afbf87a3b2046e5967c940e733c825c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marykaichini&#39;s gravatar image" /><p><span>marykaichini</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marykaichini has no accepted answers">0%</span></p></div></div><div id="comments-container-23673" class="comments-container"></div><div id="comment-tools-23673" class="comment-tools"></div><div class="clear"></div><div id="comment-23673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

