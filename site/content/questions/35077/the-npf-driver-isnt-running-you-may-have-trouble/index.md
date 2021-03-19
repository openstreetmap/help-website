+++
type = "question"
title = "The NPF driver isn&#x27;t running.  You may have trouble"
description = '''I am getting this message even though I attempted to install WinPcap with Wireshark. The install program tells me WinPcap is already running but how can that be? I&#x27;ve never installed this program before today. Also, program manager doesn&#x27;t find any instances of it running. I cannot capture any calls...'''
date = "2014-08-01T14:14:00Z"
lastmod = "2014-09-16T13:38:00Z"
weight = 35077
keywords = [ "drivers", "npf" ]
aliases = [ "/questions/35077" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The NPF driver isn't running. You may have trouble](/questions/35077/the-npf-driver-isnt-running-you-may-have-trouble)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35077-score" class="post-score" title="current number of votes">0</div><span id="post-35077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting this message even though I attempted to install WinPcap with Wireshark. The install program tells me WinPcap is already running but how can that be? I've never installed this program before today. Also, program manager doesn't find any instances of it running. I cannot capture any calls until I get this resolved. Please help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-drivers" rel="tag" title="see questions tagged &#39;drivers&#39;">drivers</span> <span class="post-tag tag-link-npf" rel="tag" title="see questions tagged &#39;npf&#39;">npf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '14, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/cb79e77452b1128bb6b3d187230d98ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brian&#39;s gravatar image" /><p><span>Brian</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brian has no accepted answers">0%</span></p></div></div><div id="comments-container-35077" class="comments-container"></div><div id="comment-tools-35077" class="comment-tools"></div><div class="clear"></div><div id="comment-35077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35088"></span>

<div id="answer-container-35088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35088-score" class="post-score" title="current number of votes">0</div><span id="post-35088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>There are programs and services, NPF is a service</li><li>WinPcap / NPF is used by other programs as well, might have already come in that way</li><li>WinPcap 'already running' is probably 'already installed', as found through registry keys</li></ol><p>To find NPF go to your services control panel and look for it there. It also shows its running state, and if it is started at boot time.</p><p>Start the service launch Wireshark again and see.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '14, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-35088" class="comments-container"><span id="35089"></span><div id="comment-35089" class="comment"><div id="post-35089-score" class="comment-score"></div><div class="comment-text"><p>Also see the answers to <a href="http://ask.wireshark.org/questions/1281/npf-driver-problem-in-windows-7">this</a> question, possibly the most viewed on the site.</p></div><div id="comment-35089-info" class="comment-info"><span class="comment-age">(02 Aug '14, 07:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="36376"></span><div id="comment-36376" class="comment"><div id="post-36376-score" class="comment-score"></div><div class="comment-text"><p>npf is not in my service list</p></div><div id="comment-36376-info" class="comment-info"><span class="comment-age">(16 Sep '14, 13:38)</span> <span class="comment-user userinfo">richards</span></div></div></div><div id="comment-tools-35088" class="comment-tools"></div><div class="clear"></div><div id="comment-35088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

