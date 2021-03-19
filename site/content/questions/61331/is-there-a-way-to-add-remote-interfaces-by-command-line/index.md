+++
type = "question"
title = "is there a way to Add remote interfaces by command line?"
description = '''As the remote interfaces do not save in the configuration, is there a way to add them via command line? Thanks,'''
date = "2017-05-10T05:57:00Z"
lastmod = "2017-05-11T08:21:00Z"
weight = 61331
keywords = [ "capture-options", "capture" ]
aliases = [ "/questions/61331" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [is there a way to Add remote interfaces by command line?](/questions/61331/is-there-a-way-to-add-remote-interfaces-by-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61331-score" class="post-score" title="current number of votes">0</div><span id="post-61331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As the remote interfaces do not save in the configuration, is there a way to add them via command line?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-options" rel="tag" title="see questions tagged &#39;capture-options&#39;">capture-options</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '17, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/a4a1b2f45befcae1bf9964af228be737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="solutionsville&#39;s gravatar image" /><p><span>solutionsville</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="solutionsville has no accepted answers">0%</span></p></div></div><div id="comments-container-61331" class="comments-container"></div><div id="comment-tools-61331" class="comment-tools"></div><div class="clear"></div><div id="comment-61331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61347"></span>

<div id="answer-container-61347" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61347-score" class="post-score" title="current number of votes">0</div><span id="post-61347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To add them on the command line in TShark or dumpcap, use an rpcap URL as an argument to the <code>-i</code> flag.</p><p>For example, to capture on interface eth0 on machine example.com, use the option <code>-i rpcap://example.com/eth0</code> to TShark or dumpcap.</p><p>There's no good option to do that with Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '17, 14:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61347" class="comments-container"><span id="61352"></span><div id="comment-61352" class="comment"><div id="post-61352-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that is what I thought I would have to do.</p></div><div id="comment-61352-info" class="comment-info"><span class="comment-age">(11 May '17, 05:35)</span> <span class="comment-user userinfo">solutionsville</span></div></div><span id="61353"></span><div id="comment-61353" class="comment"><div id="post-61353-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-61353-info" class="comment-info"><span class="comment-age">(11 May '17, 08:21)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-61347" class="comment-tools"></div><div class="clear"></div><div id="comment-61347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

