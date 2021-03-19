+++
type = "question"
title = "How can a dissector or tap recognize if data is from live capture or loading a file?"
description = '''I am writing a tap in Lua, but could also write it in C if necessary. I would like to know in the tap.packet was called as a result of a live capture or file load. I know that in the main Wireshark code, it uses capture_opts-&amp;gt;real_time_mode, but I can&#x27;t seem to find how to access this in a tap.'''
date = "2016-02-01T13:51:00Z"
lastmod = "2016-02-02T12:03:00Z"
weight = 49699
keywords = [ "capture", "live", "tap", "options" ]
aliases = [ "/questions/49699" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can a dissector or tap recognize if data is from live capture or loading a file?](/questions/49699/how-can-a-dissector-or-tap-recognize-if-data-is-from-live-capture-or-loading-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49699-score" class="post-score" title="current number of votes">0</div><span id="post-49699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a tap in Lua, but could also write it in C if necessary. I would like to know in the tap.packet was called as a result of a live capture or file load. I know that in the main Wireshark code, it uses capture_opts-&gt;real_time_mode, but I can't seem to find how to access this in a tap.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-live" rel="tag" title="see questions tagged &#39;live&#39;">live</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-options" rel="tag" title="see questions tagged &#39;options&#39;">options</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '16, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/96d66ec4a4b71e2cc5cb819045bd6393?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SonomaDave&#39;s gravatar image" /><p><span>SonomaDave</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SonomaDave has no accepted answers">0%</span></p></div></div><div id="comments-container-49699" class="comments-container"></div><div id="comment-tools-49699" class="comment-tools"></div><div class="clear"></div><div id="comment-49699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49703"></span>

<div id="answer-container-49703" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49703-score" class="post-score" title="current number of votes">0</div><span id="post-49703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It can't.</p><p>What is it that your tap would do differently in those two cases?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '16, 18:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49703" class="comments-container"><span id="49737"></span><div id="comment-49737" class="comment"><div id="post-49737-score" class="comment-score"></div><div class="comment-text"><p>I am sending data to an external program to calculate response times. It works slightly different for real time data versus the load of previously captured data. It present results in time slices, (e.g. response time for 10 minute slices). If traffic is sparse, then there may be no data at the end of the next time slice, which means the user would not see the complete picture. So, if the data is in real time, and no traffic is seen for a few seconds, the program initiates a cut-off. I do not want to do this for the load of a previously captured file.</p></div><div id="comment-49737-info" class="comment-info"><span class="comment-age">(02 Feb '16, 12:03)</span> <span class="comment-user userinfo">SonomaDave</span></div></div></div><div id="comment-tools-49703" class="comment-tools"></div><div class="clear"></div><div id="comment-49703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

