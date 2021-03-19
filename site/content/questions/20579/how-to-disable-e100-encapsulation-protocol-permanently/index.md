+++
type = "question"
title = "How to disable E100 Encapsulation protocol permanently?"
description = '''The dissector is attempting to apply a E100 protocol to my proprietary UDP packets and displaying &quot;Malformed Packet&quot; when it does that. I found that I can right click that line in the display and select &quot;Temporarily disable this protocol&quot; to prevent this during the rest of the session but I&#x27;d like t...'''
date = "2013-04-18T08:36:00Z"
lastmod = "2013-04-18T08:59:00Z"
weight = 20579
keywords = [ "e100", "disable" ]
aliases = [ "/questions/20579" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to disable E100 Encapsulation protocol permanently?](/questions/20579/how-to-disable-e100-encapsulation-protocol-permanently)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20579-score" class="post-score" title="current number of votes">0</div><span id="post-20579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The dissector is attempting to apply a E100 protocol to my proprietary UDP packets and displaying "Malformed Packet" when it does that. I found that I can right click that line in the display and select "Temporarily disable this protocol" to prevent this during the rest of the session but I'd like to disable this protocol permanently. Unfortunately I don't see "E100" in the protocol list anywhere. How can I disable this from the start? I'm using Version 1.6.11 (SVN Rev 45257 from /trunk-1.6) with Windows 7.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-e100" rel="tag" title="see questions tagged &#39;e100&#39;">e100</span> <span class="post-tag tag-link-disable" rel="tag" title="see questions tagged &#39;disable&#39;">disable</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '13, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/f00433cd3f4d686395b091a36b834a1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gismo&#39;s gravatar image" /><p><span>gismo</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gismo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '13, 08:37</strong> </span></p></div></div><div id="comments-container-20579" class="comments-container"></div><div id="comment-tools-20579" class="comment-tools"></div><div class="clear"></div><div id="comment-20579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20581"></span>

<div id="answer-container-20581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20581-score" class="post-score" title="current number of votes">0</div><span id="post-20581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can go to "Analyze -&gt; Enabled Protocols" to disable E100 dissection. If you use multiple configuration profiles, you need to disable it separately in each configuration profile.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20581" class="comments-container"></div><div id="comment-tools-20581" class="comment-tools"></div><div class="clear"></div><div id="comment-20581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

