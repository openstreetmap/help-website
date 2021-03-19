+++
type = "question"
title = "how to calculate UL throughput on the MAC level?"
description = '''how to calculate UL throughput on the MAC level?'''
date = "2014-04-18T18:32:00Z"
lastmod = "2014-04-19T14:20:00Z"
weight = 31980
keywords = [ "ul", "mac", "throughput" ]
aliases = [ "/questions/31980" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to calculate UL throughput on the MAC level?](/questions/31980/how-to-calculate-ul-throughput-on-the-mac-level)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31980-score" class="post-score" title="current number of votes">0</div><span id="post-31980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to calculate UL throughput on the MAC level?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ul" rel="tag" title="see questions tagged &#39;ul&#39;">ul</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '14, 18:32</strong></p><img src="https://secure.gravatar.com/avatar/f06f6b3ad79b8afedef1058c188cc863?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lte007&#39;s gravatar image" /><p><span>lte007</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lte007 has one accepted answer">100%</span></p></div></div><div id="comments-container-31980" class="comments-container"><span id="31982"></span><div id="comment-31982" class="comment"><div id="post-31982-score" class="comment-score"></div><div class="comment-text"><p>What is UL ?</p></div><div id="comment-31982-info" class="comment-info"><span class="comment-age">(18 Apr '14, 19:45)</span> <span class="comment-user userinfo">hardshah4</span></div></div><span id="31985"></span><div id="comment-31985" class="comment"><div id="post-31985-score" class="comment-score"></div><div class="comment-text"><p>From the "lte" in the asker's name, I'm guessing it's "uplink" (and that MAC is the <a href="https://en.wikipedia.org/wiki/LTE_(telecommunication)">LTE</a> MAC layer).</p></div><div id="comment-31985-info" class="comment-info"><span class="comment-age">(18 Apr '14, 20:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-31980" class="comment-tools"></div><div class="clear"></div><div id="comment-31980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31991"></span>

<div id="answer-container-31991" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31991-score" class="post-score" title="current number of votes">0</div><span id="post-31991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are a few different ways I could take that question, with the most on-point probably being to look at the UL-SCH channel, and read 3GPP TS 36.321 as it relates to uplink data transfer by the UE.</p><p>In any case, I think something like this is better-asked in more mobile-centric message boards. There are a lot of strong protocol analysts on this site, and plenty of people who can answer virtually any question you'd have on Wireshark itself, but if you have a theory question on SC-FDMA you're not likely to find many mobile/RF experts here to answer it.</p><p>I would suggest checking out some of the 3GPP-related groups on Linkedin, as there's no shortage of radio experts there. eventhelix.com is a fairly good resource if you don't like navigating the 3GPP whitepapers; I wrote some of the EPC material they use, but I'm more of an authority on the core side and am definitely not an FDMA expert.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '14, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Apr '14, 10:29</strong> </span></p></div></div><div id="comments-container-31991" class="comments-container"></div><div id="comment-tools-31991" class="comment-tools"></div><div class="clear"></div><div id="comment-31991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31993"></span>

<div id="answer-container-31993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31993-score" class="post-score" title="current number of votes">0</div><span id="post-31993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you have access to logged LTE MAC PDUs (and you are asking on a Wireshark site), there are a couple of ways you can see the UL throughput. Depending upon your setup, it may be possible to query the eNodeB or test equipment for such statistics.</p><p>Assuming you have MAC PDUs, one way is to open the MAC Stats (Telephony | LTE | MAC) where there is a UL MBits/sec column. The time used is the time between first and last logged PDUs. There is also a tshark option to get the same information.</p><p>Another way is to plot an IO graph, which would let you see how it changes over time. With the Y Axis Units set to Advanced..., you can filter by mac-lte.ulsch (all UEs) or a specific UE (e.g. mac-lte.ueid == 10). The calculation would be SUM, and you probably want mac-lte.ulgrant-size (which is in bytes) as the field to plot. Note that this includes padding, which, depending upon how the MAC PDUs are logged, may not actually be present in the logged frame. Setting a long enough tick interval (say, 1 second) should give you a usable average.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '14, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/4b31b42b2960269c605715bae6547459?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinM&#39;s gravatar image" /><p><span>MartinM</span><br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinM has 3 accepted answers">33%</span></p></div></div><div id="comments-container-31993" class="comments-container"></div><div id="comment-tools-31993" class="comment-tools"></div><div class="clear"></div><div id="comment-31993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

