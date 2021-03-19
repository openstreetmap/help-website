+++
type = "question"
title = "Unable to see Voip calls with Polycom phones"
description = '''When I plug my PC into Polycom phones and try to analyze the data from the phones I&#x27;m not able to see any data. No RTP stream, no Voip calls, nothing. When I plug my computer into a Cisco phone and analyze the data everything shows up perfectly, just not with the Soundpoint IP 430 and 330 Polycom ph...'''
date = "2012-07-26T16:42:00Z"
lastmod = "2012-08-06T06:13:00Z"
weight = 13041
keywords = [ "430", "polycom", "rtp", "voip", "330" ]
aliases = [ "/questions/13041" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to see Voip calls with Polycom phones](/questions/13041/unable-to-see-voip-calls-with-polycom-phones)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13041-score" class="post-score" title="current number of votes">0</div><span id="post-13041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I plug my PC into Polycom phones and try to analyze the data from the phones I'm not able to see any data. No RTP stream, no Voip calls, nothing. When I plug my computer into a Cisco phone and analyze the data everything shows up perfectly, just not with the Soundpoint IP 430 and 330 Polycom phones we use. Cisco has an option called "span to PC port" but it doesn't appear Polycom phones have that same option so I'm not sure why it's not working. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-430" rel="tag" title="see questions tagged &#39;430&#39;">430</span> <span class="post-tag tag-link-polycom" rel="tag" title="see questions tagged &#39;polycom&#39;">polycom</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-330" rel="tag" title="see questions tagged &#39;330&#39;">330</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '12, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/734d7e93ff663063245efb719c58a157?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cyprusg&#39;s gravatar image" /><p><span>Cyprusg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cyprusg has no accepted answers">0%</span></p></div></div><div id="comments-container-13041" class="comments-container"></div><div id="comment-tools-13041" class="comment-tools"></div><div class="clear"></div><div id="comment-13041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13055"></span>

<div id="answer-container-13055" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13055-score" class="post-score" title="current number of votes">0</div><span id="post-13055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Cisco has an option called "span to PC port"</p></blockquote><p>That's the reason why you don't see anything when your PC is hooked to the Polcyom.</p><blockquote><p><code>PC -- [PC]Polcycom[LAN/NET] --- switch ---</code></p></blockquote><p>VoIP Packets come in on the [LAN/NET] port of the Poloycom. If the phone does not copy those packets to the [PC] port, there is no way to capture the VoIP traffic on the attached PC. Cisco's option "span to PC port" does exactly that.</p><p>If Polycom does not have such an option, you can only capture on a mirror/span/monitor port of the switch.</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Ethernet</code><br />
</p></blockquote><p>There is a nice animated explanation of Port mirroring on the following website. At the bottom: "How Port Mirroring function is used for VoIP call recording" (requires flash).</p><blockquote><p><code>http://www.miarec.com/faq/what-is-port-mirroring</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jul '12, 03:21</strong> </span></p></div></div><div id="comments-container-13055" class="comments-container"></div><div id="comment-tools-13055" class="comment-tools"></div><div class="clear"></div><div id="comment-13055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13394"></span>

<div id="answer-container-13394" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13394-score" class="post-score" title="current number of votes">0</div><span id="post-13394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try Synety's full <a href="https://www.synety.com/callrecording/">call recording</a> system and see if it helps</p><p><a href="https://www.synety.com/callrecording/">https://www.synety.com/callrecording/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '12, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/15f9bbf8d08786304a6b6c7c5ee627de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunnycoin&#39;s gravatar image" /><p><span>sunnycoin</span><br />
<span class="score" title="-1 reputation points">-1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunnycoin has no accepted answers">0%</span></p></div></div><div id="comments-container-13394" class="comments-container"></div><div id="comment-tools-13394" class="comment-tools"></div><div class="clear"></div><div id="comment-13394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

