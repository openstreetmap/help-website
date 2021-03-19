+++
type = "question"
title = "Capture Filter for Just SOAP and a Specific Port"
description = '''I am trying to capture just SOAP interactions through a specific port. There are multiple processes running on the server so I need to be as specific as possible. I have managed to capture data when a SOAP conversation takes place but there is far too much detail. Can someone please tell me what Cap...'''
date = "2014-10-01T21:17:00Z"
lastmod = "2014-10-02T02:12:00Z"
weight = 36769
keywords = [ "capture-filter", "soap" ]
aliases = [ "/questions/36769" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filter for Just SOAP and a Specific Port](/questions/36769/capture-filter-for-just-soap-and-a-specific-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36769-score" class="post-score" title="current number of votes">0</div><span id="post-36769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture just SOAP interactions through a specific port. There are multiple processes running on the server so I need to be as specific as possible.</p><p>I have managed to capture data when a SOAP conversation takes place but there is far too much detail.</p><p>Can someone please tell me what Capture Filter to use to limit the data to a specific port and to SOAP.</p><p>Thanks,</p><p>Alan Eth</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-soap" rel="tag" title="see questions tagged &#39;soap&#39;">soap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '14, 21:17</strong></p><img src="https://secure.gravatar.com/avatar/92842ce17eefb295c4cc52fe99ffc086?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan%20Eth&#39;s gravatar image" /><p><span>Alan Eth</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan Eth has no accepted answers">0%</span></p></div></div><div id="comments-container-36769" class="comments-container"></div><div id="comment-tools-36769" class="comment-tools"></div><div class="clear"></div><div id="comment-36769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36779"></span>

<div id="answer-container-36779" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36779-score" class="post-score" title="current number of votes">1</div><span id="post-36779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A capture filter for SOAP is somewhat difficult as it's at a layer above what the capture filters handle well. You can certainly create a capture filter for a specific port, e.g. <code>tcp port 1234</code>. Once you have captured the traffic you can then use a display filter (which can handle filtering for SOAP) to reduce the displayed packets, and then you can export those packets to a new capture file so you can look at just the traffic of interest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '14, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36779" class="comments-container"></div><div id="comment-tools-36779" class="comment-tools"></div><div class="clear"></div><div id="comment-36779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

