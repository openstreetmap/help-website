+++
type = "question"
title = "Is there a command line parameter for &quot;tshark&quot; command to show raw bytes in addition to decoded stuff?"
description = '''The following command will output all the decoded fields which is nice. I can pipe it to other program for more processing.  tshark -r temp.pcap -P -V  Wonder if there is a command parameter to make it output raw bytes (like in the wireshark, the pane for raw bytes). Thanks.'''
date = "2015-04-11T18:44:00Z"
lastmod = "2015-04-11T20:40:00Z"
weight = 41386
keywords = [ "tshark" ]
aliases = [ "/questions/41386" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a command line parameter for "tshark" command to show raw bytes in addition to decoded stuff?](/questions/41386/is-there-a-command-line-parameter-for-tshark-command-to-show-raw-bytes-in-addition-to-decoded-stuff)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41386-score" class="post-score" title="current number of votes">0</div><span id="post-41386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The following command will output all the decoded fields which is nice. I can pipe it to other program for more processing.<br />
</p><pre><code>tshark -r temp.pcap -P -V</code></pre><p>Wonder if there is a command parameter to make it output raw bytes (like in the wireshark, the pane for raw bytes).</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '15, 18:44</strong></p><img src="https://secure.gravatar.com/avatar/0228802baecfa9b8d8764a043fea883b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharkfun&#39;s gravatar image" /><p><span>sharkfun</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharkfun has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-41386" class="comments-container"></div><div id="comment-tools-41386" class="comment-tools"></div><div class="clear"></div><div id="comment-41386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41387"></span>

<div id="answer-container-41387" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41387-score" class="post-score" title="current number of votes">2</div><span id="post-41387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sharkfun has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>tshark -r temp.pcap -P -V -x</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '15, 20:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41387" class="comments-container"><span id="41388"></span><div id="comment-41388" class="comment"><div id="post-41388-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick answer! It feels so obvious now that you pointed it out :-)</p></div><div id="comment-41388-info" class="comment-info"><span class="comment-age">(11 Apr '15, 20:40)</span> <span class="comment-user userinfo">sharkfun</span></div></div></div><div id="comment-tools-41387" class="comment-tools"></div><div class="clear"></div><div id="comment-41387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

