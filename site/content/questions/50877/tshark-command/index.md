+++
type = "question"
title = "Tshark command"
description = '''Hi All, How to disable/enable the protocols using tshark commands? Could you tell me the ASAP. Regards, Swathi.'''
date = "2016-03-14T02:26:00Z"
lastmod = "2016-03-14T03:29:00Z"
weight = 50877
keywords = [ "tshark" ]
aliases = [ "/questions/50877" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark command](/questions/50877/tshark-command)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50877-score" class="post-score" title="current number of votes">0</div><span id="post-50877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>How to disable/enable the protocols using tshark commands? Could you tell me the ASAP.</p><p>Regards, Swathi.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '16, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/a34282ab2b31d84bc63d5ea83c15d775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swathi%20jakkam&#39;s gravatar image" /><p><span>swathi jakkam</span><br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swathi jakkam has no accepted answers">0%</span></p></div></div><div id="comments-container-50877" class="comments-container"><span id="50885"></span><div id="comment-50885" class="comment"><div id="post-50885-score" class="comment-score"></div><div class="comment-text"><p>In the context of your other recent questions, I suspect you are actually seeking ways to reduce the amount of data which Tshark has to process so that you would be able to handle longer (in terms of time) captures. Is this suspicion correct?</p></div><div id="comment-50885-info" class="comment-info"><span class="comment-age">(14 Mar '16, 03:29)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50877" class="comment-tools"></div><div class="clear"></div><div id="comment-50877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50884"></span>

<div id="answer-container-50884" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50884-score" class="post-score" title="current number of votes">0</div><span id="post-50884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you use Wireshark 2.0.x, you can use the --disable-protocol option as found in the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">man page</a>.</p><p>You can also manually edit the disabled_protos file as described in the same man page. It is applicable fro all Wireshark releases as far as I know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '16, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Mar '16, 06:50</strong> </span></p></div></div><div id="comments-container-50884" class="comments-container"></div><div id="comment-tools-50884" class="comment-tools"></div><div class="clear"></div><div id="comment-50884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

