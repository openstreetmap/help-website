+++
type = "question"
title = "TCP data transmission stops for a second and I can&#x27;t interpret the data. Can someone help?"
description = ''' This happens multiple times, dependent on how large the file is that I&#x27;m sending. This file is 1MB and takes around 8 seconds to trasmit.  What might be causing this?'''
date = "2015-06-17T09:04:00Z"
lastmod = "2015-06-17T13:10:00Z"
weight = 43272
keywords = [ "tcp" ]
aliases = [ "/questions/43272" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP data transmission stops for a second and I can't interpret the data. Can someone help?](/questions/43272/tcp-data-transmission-stops-for-a-second-and-i-cant-interpret-the-data-can-someone-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43272-score" class="post-score" title="current number of votes">0</div><span id="post-43272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://i.imgur.com/2UVgF0j.png" alt="alt text" /></p><p>This happens multiple times, dependent on how large the file is that I'm sending. This file is 1MB and takes around 8 seconds to trasmit.</p><p><img src="http://i.imgur.com/TmPl3KC.png" alt="alt text" /></p><p>What might be causing this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '15, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/1859c55fc7c2a69f6a0531a4d0dbbea4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breau&#39;s gravatar image" /><p><span>Breau</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breau has no accepted answers">0%</span></p></img></div></div><div id="comments-container-43272" class="comments-container"></div><div id="comment-tools-43272" class="comment-tools"></div><div class="clear"></div><div id="comment-43272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43280"></span>

<div id="answer-container-43280" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43280-score" class="post-score" title="current number of votes">0</div><span id="post-43280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you have packet loss. But by the fact that multiple packets in a row seem to get lost and that there is a repeating pattern, I think there might be a device between these two systems that is applying a bandwidth limit.</p><p>That however would be strange as the systems might be in the same IP subnet (are they?). Since you are capturing on one of the hosts (192.168.14.10), could you try making a capture on a span port on the switch to see what exactly is being sent to the system? It could be that something on your system is interfering....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></img></div></div><div id="comments-container-43280" class="comments-container"></div><div id="comment-tools-43280" class="comment-tools"></div><div class="clear"></div><div id="comment-43280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

