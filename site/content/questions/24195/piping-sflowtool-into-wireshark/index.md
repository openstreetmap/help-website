+++
type = "question"
title = "Piping sflowtool into WireShark"
description = '''From the elevated cmd prompt, I have tried &quot;wireshark -k -i (sflowtool)&quot; and receive error that capture session could not be created: error opening adapter...system cannot find specified file. How can I get sflowtool piped into WireShark?'''
date = "2013-08-30T06:59:00Z"
lastmod = "2013-08-30T07:59:00Z"
weight = 24195
keywords = [ "piping" ]
aliases = [ "/questions/24195" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Piping sflowtool into WireShark](/questions/24195/piping-sflowtool-into-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24195-score" class="post-score" title="current number of votes">0</div><span id="post-24195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From the elevated cmd prompt, I have tried "wireshark -k -i (sflowtool)" and receive error that capture session could not be created: error opening adapter...system cannot find specified file.</p><p>How can I get sflowtool piped into WireShark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-piping" rel="tag" title="see questions tagged &#39;piping&#39;">piping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '13, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/2ae74f7ca0d39f7f20081c6246f8ccad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jrupert&#39;s gravatar image" /><p><span>jrupert</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jrupert has no accepted answers">0%</span></p></div></div><div id="comments-container-24195" class="comments-container"></div><div id="comment-tools-24195" class="comment-tools"></div><div class="clear"></div><div id="comment-24195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24197"></span>

<div id="answer-container-24197" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24197-score" class="post-score" title="current number of votes">1</div><span id="post-24197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you set up the named pipe sflowtool as per the Wireshark Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Pipes">capturing over pipes</a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24197" class="comments-container"><span id="24199"></span><div id="comment-24199" class="comment"><div id="post-24199-score" class="comment-score"></div><div class="comment-text"><p>Also, you may want to read <a href="http://blog.sflow.com/2011/11/wireshark.html">this</a> sflow blog article, although the article indicates capturing as, <code>wireshark -k -i &lt;(sflowtool -t)</code>, but I think <code>sflowtool -t | wireshark -k -i -</code> <em>might</em> be needed.</p></div><div id="comment-24199-info" class="comment-info"><span class="comment-age">(30 Aug '13, 07:59)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-24197" class="comment-tools"></div><div class="clear"></div><div id="comment-24197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

