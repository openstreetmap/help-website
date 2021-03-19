+++
type = "question"
title = "Why is Wireshark using Dell Latitude E6400 not capturing all data ?"
description = '''Running various versions of Wireshark on a Dell Latitude E6400 only displays some TCPIP data in one direction and IP traffic etc. from laptop in the other when monitoring the link in the other direction. We are using a Copper Tap A &amp;amp; B outputs. All other models of Dell laptop e.g E4300, D630 etc...'''
date = "2012-06-13T10:56:00Z"
lastmod = "2012-06-13T23:56:00Z"
weight = 11877
keywords = [ "not", "e6400", "displaying", "dell", "correctly" ]
aliases = [ "/questions/11877" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is Wireshark using Dell Latitude E6400 not capturing all data ?](/questions/11877/why-is-wireshark-using-dell-latitude-e6400-not-capturing-all-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11877-score" class="post-score" title="current number of votes">0</div><span id="post-11877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running various versions of Wireshark on a Dell Latitude E6400 only displays some TCPIP data in one direction and IP traffic etc. from laptop in the other when monitoring the link in the other direction. We are using a Copper Tap A &amp; B outputs.<br />
All other models of Dell laptop e.g E4300, D630 etc. work ok. All are using XP and have exactly the same build and configuration. All setups appear to be identical, could this be a Dell driver issue ? The Dell E4300 and E6400 appear to have the same net hardware implemented yet one model works and the other doesn't. I have tried this on three of each model with consistant results.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-e6400" rel="tag" title="see questions tagged &#39;e6400&#39;">e6400</span> <span class="post-tag tag-link-displaying" rel="tag" title="see questions tagged &#39;displaying&#39;">displaying</span> <span class="post-tag tag-link-dell" rel="tag" title="see questions tagged &#39;dell&#39;">dell</span> <span class="post-tag tag-link-correctly" rel="tag" title="see questions tagged &#39;correctly&#39;">correctly</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '12, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/af58f24a8f2e513a3e3be8c046edf645?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TR%20shark&#39;s gravatar image" /><p><span>TR shark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TR shark has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-11877" class="comments-container"></div><div id="comment-tools-11877" class="comment-tools"></div><div class="clear"></div><div id="comment-11877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11890"></span>

<div id="answer-container-11890" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11890-score" class="post-score" title="current number of votes">1</div><span id="post-11890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could be a driver problem or a problem with <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a>. To eliminate the driver problem, I suggest to use a live image of BackTrack 5R2 (Linux / contains Wireshark) and run it on your sniffer PC.</p><blockquote><p><code>http://www.backtrack-linux.org/tutorials/usb-live-install/</code><br />
</p></blockquote><p>Regarding the <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a>, please check similar problems:</p><blockquote><p><code>http://ask.wireshark.org/questions/11714/only-inbound-traffic</code><br />
<code>http://ask.wireshark.org/questions/11560/unable-to-capture-or-display-incoming-tcpip-packets-with-port-8100</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '12, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '12, 00:19</strong> </span></p></div></div><div id="comments-container-11890" class="comments-container"></div><div id="comment-tools-11890" class="comment-tools"></div><div class="clear"></div><div id="comment-11890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

