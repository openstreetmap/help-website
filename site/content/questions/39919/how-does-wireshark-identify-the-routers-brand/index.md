+++
type = "question"
title = "How does Wireshark identify the Router&#x27;s brand?"
description = '''I started a packet capture on my PC. Wireshark shows as packets coming from NetGear something.I was curious as to how Wireshark identifies the Router&#x27;s brand?'''
date = "2015-02-17T18:55:00Z"
lastmod = "2015-02-17T19:37:00Z"
weight = 39919
keywords = [ "wireshark" ]
aliases = [ "/questions/39919" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does Wireshark identify the Router's brand?](/questions/39919/how-does-wireshark-identify-the-routers-brand)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39919-score" class="post-score" title="current number of votes">0</div><span id="post-39919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I started a packet capture on my PC. Wireshark shows as packets coming from NetGear something.I was curious as to how Wireshark identifies the Router's brand?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '15, 18:55</strong></p><img src="https://secure.gravatar.com/avatar/2fef2471b4b8f38706edb26660de1c3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user0912&#39;s gravatar image" /><p><span>user0912</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user0912 has no accepted answers">0%</span></p></div></div><div id="comments-container-39919" class="comments-container"></div><div id="comment-tools-39919" class="comment-tools"></div><div class="clear"></div><div id="comment-39919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39920"></span>

<div id="answer-container-39920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39920-score" class="post-score" title="current number of votes">2</div><span id="post-39920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I imagine you are seeing the manufacturer's name as part of the Ethernet MAC (src/dst) addresses in a packet.</p><p>Every Ethernet hardware port has a unique MAC address with the first 3 bytes being a specific value assigned to a manufacturer and the last 3 bytes being assigned by the manufacturer.</p><p>Wireshark looks up the first 3 bytes of the Ethernet address in a table to determine the manufacturer.</p><p>This can be disabled in the Edit ! Preferences ! Name Resolution screen in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '15, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '15, 19:47</strong> </span></p></div></div><div id="comments-container-39920" class="comments-container"></div><div id="comment-tools-39920" class="comment-tools"></div><div class="clear"></div><div id="comment-39920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

