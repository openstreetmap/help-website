+++
type = "question"
title = "Removing headers during live capture"
description = '''Is there a method in which I can remove or filter headers keeping only the payload during a live capture via wireshark or tshark? I know that I can modify an existing capture using editcap.'''
date = "2015-08-18T13:07:00Z"
lastmod = "2015-08-20T14:14:00Z"
weight = 45214
keywords = [ "filter", "header", "remove", "headers" ]
aliases = [ "/questions/45214" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Removing headers during live capture](/questions/45214/removing-headers-during-live-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45214-score" class="post-score" title="current number of votes">0</div><span id="post-45214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a method in which I can remove or filter headers keeping only the payload during a live capture via wireshark or tshark? I know that I can modify an existing capture using editcap.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span> <span class="post-tag tag-link-headers" rel="tag" title="see questions tagged &#39;headers&#39;">headers</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '15, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/7fa32aa16ce4137617bcee250f37805a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NiCe85&#39;s gravatar image" /><p><span>NiCe85</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NiCe85 has no accepted answers">0%</span></p></div></div><div id="comments-container-45214" class="comments-container"></div><div id="comment-tools-45214" class="comment-tools"></div><div class="clear"></div><div id="comment-45214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45223"></span>

<div id="answer-container-45223" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45223-score" class="post-score" title="current number of votes">1</div><span id="post-45223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, this isn't possible. dumpcap (the tool which both Wireshark and tshark start to do the capture) does not process frames before writing them to disk.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '15, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-45223" class="comments-container"><span id="45279"></span><div id="comment-45279" class="comment"><div id="post-45279-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, when I run tshark with the following options "tshark -i -T fields -e data" I am able to get the output that I want. Is there an equivalent wireshark display filter</p></div><div id="comment-45279-info" class="comment-info"><span class="comment-age">(20 Aug '15, 13:21)</span> <span class="comment-user userinfo">NiCe85</span></div></div><span id="45280"></span><div id="comment-45280" class="comment"><div id="post-45280-score" class="comment-score"></div><div class="comment-text"><p>Well, you can filter on "data" but Wireshark will always show the full packet - that's because the "-T fields -e data" is a feature that selectively prints just the fields mentioned (it' not a "display filter" as such), while Wireshark always shows all fields.</p></div><div id="comment-45280-info" class="comment-info"><span class="comment-age">(20 Aug '15, 14:14)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-45223" class="comment-tools"></div><div class="clear"></div><div id="comment-45223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

