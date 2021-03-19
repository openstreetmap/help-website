+++
type = "question"
title = "VOIP QoS in monitoring??"
description = '''Hello WireShark.org I have a small experiment on voice over ip, I &#x27;ve done it by asterisk. I have a question about monitoring packets of VoIP when the Qos 802.11e is activated. How can I detect the quality of service is running?? the DSCP(0x00) is not changed when I activet it or don&#x27;t. Thanks very ...'''
date = "2013-07-19T19:05:00Z"
lastmod = "2013-07-22T19:10:00Z"
weight = 23188
keywords = [ "802.11e", "voip" ]
aliases = [ "/questions/23188" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [VOIP QoS in monitoring??](/questions/23188/voip-qos-in-monitoring)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23188-score" class="post-score" title="current number of votes">0</div><span id="post-23188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello WireShark.org I have a small experiment on voice over ip, I 've done it by asterisk. I have a question about monitoring packets of VoIP when the Qos 802.11e is activated. How can I detect the quality of service is running?? the DSCP(0x00) is not changed when I activet it or don't.</p><p>Thanks very much</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.11e" rel="tag" title="see questions tagged &#39;802.11e&#39;">802.11e</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '13, 19:05</strong></p><img src="https://secure.gravatar.com/avatar/c82b04c7fd1edfdf465212f48079fdf7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hamad&#39;s gravatar image" /><p><span>hamad</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hamad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jul '13, 19:08</strong> </span></p></div></div><div id="comments-container-23188" class="comments-container"></div><div id="comment-tools-23188" class="comment-tools"></div><div class="clear"></div><div id="comment-23188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23259"></span>

<div id="answer-container-23259" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23259-score" class="post-score" title="current number of votes">0</div><span id="post-23259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The QoS mechanisms of 802.11e are <strong>totally different</strong> from the DiffServ mechanism (DSCP flags).</p><p>As you did not say how you configured your systems, I ask you to read the following overview of 802.11e and then rethink what you did and what you expected to see.</p><blockquote><p><a href="http://www.networkworld.com/news/tech/2003/0623techupdate.html">http://www.networkworld.com/news/tech/2003/0623techupdate.html</a></p></blockquote><p>BTW: I'm not sure if asterisk is able to have an influence on 802.11e. Can you please add some information how you configured asterisk?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23259" class="comments-container"></div><div id="comment-tools-23259" class="comment-tools"></div><div class="clear"></div><div id="comment-23259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23276"></span>

<div id="answer-container-23276" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23276-score" class="post-score" title="current number of votes">0</div><span id="post-23276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To confirm, this is wireless VoIP? When you "activated" 802.11e, I assume this was at your wireless access point? Did you configure the access point to also map the 802.11e classes with DSCP code points and mark the IP headers accordingly?</p><p>Really to the heart of your question, if the DSCP markings are all best-effort, ask yourself "In this network design, what device is responsible for marking the IP header with DSCP values that map to these 802.11e classes that I've defined?". If Wireshark is showing you best-effort packets, either that device is not marking the packets correctly, the traffic is being misclassified or marked closer to the source, or the DSCP markings are getting stripped closer to the destination (this would depend on where you're tapping into the network).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 19:10</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jul '13, 19:12</strong> </span></p></div></div><div id="comments-container-23276" class="comments-container"></div><div id="comment-tools-23276" class="comment-tools"></div><div class="clear"></div><div id="comment-23276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

