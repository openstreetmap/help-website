+++
type = "question"
title = "Skinny protocol problem"
description = '''Wireshark 1.4.1 cannot decode Skinny message . I believe it is last version on Skinny protocol. It is a full call and believe on of the message which wireshark cannot regognize  0x000014a - is CallInfoMessage message .  Is it any workaround to read all Skinny messages or is any fix for this will be ...'''
date = "2010-10-20T07:19:00Z"
lastmod = "2010-10-20T17:51:00Z"
weight = 558
keywords = [ "skinny", "sccp" ]
aliases = [ "/questions/558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Skinny protocol problem](/questions/558/skinny-protocol-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-558-score" class="post-score" title="current number of votes">0</div><span id="post-558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark 1.4.1 cannot decode Skinny message . I believe it is last version on Skinny protocol.</p><p>It is a full call and believe on of the message which wireshark cannot regognize</p><p>0x000014a - is CallInfoMessage message .</p><p>Is it any workaround to read all Skinny messages or is any fix for this will be available anytime soon ?</p><p>Thank you,</p><p><img src="http://img840.imageshack.us/img840/2418/skinnyr.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-skinny" rel="tag" title="see questions tagged &#39;skinny&#39;">skinny</span> <span class="post-tag tag-link-sccp" rel="tag" title="see questions tagged &#39;sccp&#39;">sccp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '10, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/7013184a5cec8d3de0d5b09064501b3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dan&#39;s gravatar image" /><p><span>Dan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dan has no accepted answers">0%</span></p></img></div></div><div id="comments-container-558" class="comments-container"></div><div id="comment-tools-558" class="comment-tools"></div><div class="clear"></div><div id="comment-558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="560"></span>

<div id="answer-container-560" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-560-score" class="post-score" title="current number of votes">0</div><span id="post-560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to the <a href="http://chan-sccp-b.sourceforge.net/doc/sccp__protocol_8h_source.html">Asterisk chan_sccp driver source</a> this is a CallInfoDynamicMessage. This will have to be added to Wireshark's Skinny dissector. I'm not sure when that will happen.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '10, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-560" class="comments-container"><span id="571"></span><div id="comment-571" class="comment"><div id="post-571-score" class="comment-score"></div><div class="comment-text"><p>If you will take a look on the picture it actually much more messages like - 0x000014a 0x0000154 ( StartMediaTransmissionAck ) 0x0000049 ( AccessoryStatusMessage )<br />
</p></div><div id="comment-571-info" class="comment-info"><span class="comment-age">(20 Oct '10, 17:51)</span> <span class="comment-user userinfo">Dan</span></div></div></div><div id="comment-tools-560" class="comment-tools"></div><div class="clear"></div><div id="comment-560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

