+++
type = "question"
title = "ERR (inst 3) MAC:    Number of BAT entries not set correctly (written 0, 0 RARs 1 grants (0 HARQs))"
description = '''Hi Experts, We are running lte test and we are getting this error. Is there anyone who had faced that error before? We could not be able to find it at the source code. Thanks, regards.'''
date = "2016-01-20T05:56:00Z"
lastmod = "2016-01-20T13:18:00Z"
weight = 49402
keywords = [ "mac-lte" ]
aliases = [ "/questions/49402" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ERR (inst 3) MAC: Number of BAT entries not set correctly (written 0, 0 RARs 1 grants (0 HARQs))](/questions/49402/err-inst-3-mac-number-of-bat-entries-not-set-correctly-written-0-0-rars-1-grants-0-harqs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49402-score" class="post-score" title="current number of votes">0</div><span id="post-49402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>We are running lte test and we are getting this error. Is there anyone who had faced that error before? We could not be able to find it at the source code.</p><p>Thanks, regards.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac-lte" rel="tag" title="see questions tagged &#39;mac-lte&#39;">mac-lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '16, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/240115732c28fd444597e0ce50e83203?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrtkrgz&#39;s gravatar image" /><p><span>mrtkrgz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrtkrgz has no accepted answers">0%</span></p></div></div><div id="comments-container-49402" class="comments-container"></div><div id="comment-tools-49402" class="comment-tools"></div><div class="clear"></div><div id="comment-49402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49403"></span>

<div id="answer-container-49403" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49403-score" class="post-score" title="current number of votes">0</div><span id="post-49403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This does not seem to be a log from the default Wireshark source code.</p><p>Which Wireshark version are you using? Does it have any proprietary plugin / builtin dissector?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '16, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-49403" class="comments-container"></div><div id="comment-tools-49403" class="comment-tools"></div><div class="clear"></div><div id="comment-49403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49411"></span>

<div id="answer-container-49411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49411-score" class="post-score" title="current number of votes">0</div><span id="post-49411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I recognise this error as an internal message reported by Ixia's LTE test product. It would have been logged as a comment/trace message (although it does relate to the operation of MAC). Best contact Ixia for details/resolution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '16, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/4b31b42b2960269c605715bae6547459?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinM&#39;s gravatar image" /><p><span>MartinM</span><br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinM has 3 accepted answers">33%</span></p></div></div><div id="comments-container-49411" class="comments-container"></div><div id="comment-tools-49411" class="comment-tools"></div><div class="clear"></div><div id="comment-49411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

