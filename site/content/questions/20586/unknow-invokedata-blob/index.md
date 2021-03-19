+++
type = "question"
title = "unknow invokedata blob"
description = '''hello  i make a trace when a platform sent a invoke data messages in MAP 1 (sendparameters- UTU), but everytime when i see the GSM mobile application part , the package cant decode - i always have InvokeData blob. Do you know how i can solve this? maybe i have a wrong configuration in the wireshark?...'''
date = "2013-04-18T11:22:00Z"
lastmod = "2013-04-18T14:58:00Z"
weight = 20586
keywords = [ "invokedatablob" ]
aliases = [ "/questions/20586" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [unknow invokedata blob](/questions/20586/unknow-invokedata-blob)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20586-score" class="post-score" title="current number of votes">0</div><span id="post-20586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello</p><p>i make a trace when a platform sent a invoke data messages in MAP 1 (sendparameters- UTU), but everytime when i see the GSM mobile application part , the package cant decode - i always have InvokeData blob. Do you know how i can solve this? maybe i have a wrong configuration in the wireshark?</p><p>Thanks a lot</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-invokedatablob" rel="tag" title="see questions tagged &#39;invokedatablob&#39;">invokedatablob</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '13, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/91037fd6fd0ba4053905b5cc369d0a13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ray&#39;s gravatar image" /><p><span>Ray</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ray has no accepted answers">0%</span></p></div></div><div id="comments-container-20586" class="comments-container"><span id="20593"></span><div id="comment-20593" class="comment"><div id="post-20593-score" class="comment-score"></div><div class="comment-text"><p>Is sendparameters-UTU the message sent? What operation code does that message have?</p></div><div id="comment-20593-info" class="comment-info"><span class="comment-age">(18 Apr '13, 14:08)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="20594"></span><div id="comment-20594" class="comment"><div id="post-20594-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders</p><p>yes is sendparameters-UTU Opcode: localValue (0) localvalue: 9</p><p>down is a capture from my wireshark</p><p><img src="http://s23.postimg.org/3v6u46hwb/Capture.jpg" alt="alt text" /></p><p>Thanks a lot for the help I really appreciate</p><p>Brgs</p><p>Ray</p></div><div id="comment-20594-info" class="comment-info"><span class="comment-age">(18 Apr '13, 14:27)</span> <span class="comment-user userinfo">Ray</span></div></div><span id="20595"></span><div id="comment-20595" class="comment"><div id="post-20595-score" class="comment-score"></div><div class="comment-text"><p>Hi Andres , I put another answer with the information you ask, and this time i include a screen shot</p><p>Thanks a lot Ray</p></div><div id="comment-20595-info" class="comment-info"><span class="comment-age">(18 Apr '13, 14:28)</span> <span class="comment-user userinfo">Ray</span></div></div></div><div id="comment-tools-20586" class="comment-tools"></div><div class="clear"></div><div id="comment-20586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20596"></span>

<div id="answer-container-20596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20596-score" class="post-score" title="current number of votes">0</div><span id="post-20596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In packet-gsm_map-template.c there is this comment / <em>TODO find out why this isn't in the ASN1 file</em> / / <em>reserved sendParameters (9)</em> / So it looks like we have no code to dissect that data, if you have a reference to a standard document where there is a discription of this op code you could rasise a bug report to have it added.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 14:58</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></img></div></div><div id="comments-container-20596" class="comments-container"></div><div id="comment-tools-20596" class="comment-tools"></div><div class="clear"></div><div id="comment-20596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

