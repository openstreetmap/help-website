+++
type = "question"
title = "Capturing headers only"
description = '''Does anyone have a simple filter for capturing headers only.'''
date = "2011-05-19T05:37:00Z"
lastmod = "2012-11-09T07:59:00Z"
weight = 4137
keywords = [ "capture-filter" ]
aliases = [ "/questions/4137" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing headers only](/questions/4137/capturing-headers-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4137-score" class="post-score" title="current number of votes">1</div><span id="post-4137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anyone have a simple filter for capturing headers only.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '11, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/5763d40ca936c0414018982172082747?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mooseman&#39;s gravatar image" /><p><span>mooseman</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mooseman has no accepted answers">0%</span></p></div></div><div id="comments-container-4137" class="comments-container"></div><div id="comment-tools-4137" class="comment-tools"></div><div class="clear"></div><div id="comment-4137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4139"></span>

<div id="answer-container-4139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4139-score" class="post-score" title="current number of votes">5</div><span id="post-4139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try to go with slicing the frames to the first # of bytes, but there is no simple filter that will exactly capture certain headers only afaik.</p><p>Just open the capture options and put a check mark next to "Limit each packet to" and put in the number of bytes you want to capture. Usually you should go for at least 54 bytes (14 bytes Ethernet header, 20 IP, 20 TCP, unless IP or TCP are using a lot of optional "Option" headers). For SMB and other higher protocol header you'll need to go for 128 or even more bytes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '11, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4139" class="comments-container"><span id="4143"></span><div id="comment-4143" class="comment"><div id="post-4143-score" class="comment-score"></div><div class="comment-text"><p>Wireshark filters (both capture and display filters) only select which packets to capture or display, they do not select which information <strong>within</strong> a packet to display. So it is not possible to use a filter to only <strong>show</strong> certain headers. The only way to limit this is to actually cut the extra data of as Jasper has explained.</p></div><div id="comment-4143-info" class="comment-info"><span class="comment-age">(19 May '11, 06:06)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="15773"></span><div id="comment-15773" class="comment"><div id="post-15773-score" class="comment-score"></div><div class="comment-text"><p>I am using the 1.8.3 version and I am having the same problem, I want to capture only the headers not the payload. I am having a hard time finding the option to limit each packet in this new version of Wireshark. Can anyone help me with that?</p></div><div id="comment-15773-info" class="comment-info"><span class="comment-age">(09 Nov '12, 07:54)</span> <span class="comment-user userinfo">mikidi</span></div></div><span id="15774"></span><div id="comment-15774" class="comment"><div id="post-15774-score" class="comment-score"></div><div class="comment-text"><p>open the capture options dialog and double click on the network card row of the card you want to use.</p></div><div id="comment-15774-info" class="comment-info"><span class="comment-age">(09 Nov '12, 07:59)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-4139" class="comment-tools"></div><div class="clear"></div><div id="comment-4139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

