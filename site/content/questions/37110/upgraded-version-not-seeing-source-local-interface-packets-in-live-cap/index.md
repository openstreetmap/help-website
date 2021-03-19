+++
type = "question"
title = "Upgraded version - not seeing source local interface packets in live cap"
description = '''I upgraded to v1.12.1, yesterday, and the first thing I noticed is that I no longer see my local interface IP (or mac, name, etc) in the source column on the capture. It&#x27;s showing up in the destination side, but I&#x27;m not sure why it&#x27;s not on the originating side. Ideas? I normally run promiscuous mod...'''
date = "2014-10-16T07:13:00Z"
lastmod = "2014-10-17T05:50:00Z"
weight = 37110
keywords = [ "wireshark" ]
aliases = [ "/questions/37110" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Upgraded version - not seeing source local interface packets in live cap](/questions/37110/upgraded-version-not-seeing-source-local-interface-packets-in-live-cap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37110-score" class="post-score" title="current number of votes">0</div><span id="post-37110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I upgraded to v1.12.1, yesterday, and the first thing I noticed is that I no longer see my local interface IP (or mac, name, etc) in the source column on the capture. It's showing up in the destination side, but I'm not sure why it's not on the originating side. Ideas? I normally run promiscuous mode, but have tried both ways. There is no filter applied.</p><p>For example, if I ping google, I only see the replies. Also, only one interface is active on my machine.<br />
</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '14, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/ffdeb6cfddd61b02a3e929a28aaffdcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ribby24&#39;s gravatar image" /><p><span>ribby24</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ribby24 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-37110" class="comments-container"><span id="37127"></span><div id="comment-37127" class="comment"><div id="post-37127-score" class="comment-score"></div><div class="comment-text"><p>Then what is shown in the source column? Is there another address, or is it empty? Or is it that the complete outgoing packet is missing? Does it still fail if you downgrade to wherever you came from? Also: context. What platform, OS and version are you using?</p></div><div id="comment-37127-info" class="comment-info"><span class="comment-age">(17 Oct '14, 03:45)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="37131"></span><div id="comment-37131" class="comment"><div id="post-37131-score" class="comment-score"></div><div class="comment-text"><p>It seems to only be showing incoming packets. So, I see the source/dest, but just for incoming. I don't see any outgoing packets. I'll look at uninstalling and reinstalling the older version and make sure it still works.</p><p>I'll report back...</p></div><div id="comment-37131-info" class="comment-info"><span class="comment-age">(17 Oct '14, 05:50)</span> <span class="comment-user userinfo">ribby24</span></div></div></div><div id="comment-tools-37110" class="comment-tools"></div><div class="clear"></div><div id="comment-37110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

