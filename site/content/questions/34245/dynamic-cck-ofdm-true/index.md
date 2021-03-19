+++
type = "question"
title = "Dynamic CCK-OFDM - True"
description = ''' So generell CCK and OFDM is off. But what does the Line &quot;Dynamic CCK-OFDM: True&quot; mean? CCK and OFDM ist switched dynamically, for the case one is better in a specific Situation? I can&#x27;t find an Answer, pleae Help.'''
date = "2014-06-27T10:03:00Z"
lastmod = "2014-06-29T10:30:00Z"
weight = 34245
keywords = [ "modulation" ]
aliases = [ "/questions/34245" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dynamic CCK-OFDM - True](/questions/34245/dynamic-cck-ofdm-true)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34245-score" class="post-score" title="current number of votes">0</div><span id="post-34245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://www.bilder-upload.eu/upload/1a2198-1403888177.png" alt="alt text" /></p><p>So generell CCK and OFDM is off.</p><p>But what does the Line "Dynamic CCK-OFDM: True" mean?</p><p>CCK and OFDM ist switched dynamically, for the case one is better in a specific Situation?</p><p>I can't find an Answer, pleae Help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modulation" rel="tag" title="see questions tagged &#39;modulation&#39;">modulation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '14, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/766b4dbec818886d2eee9bec52edc460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jan%20Hermanns&#39;s gravatar image" /><p><span>Jan Hermanns</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jan Hermanns has no accepted answers">0%</span></p></img></div></div><div id="comments-container-34245" class="comments-container"></div><div id="comment-tools-34245" class="comment-tools"></div><div class="clear"></div><div id="comment-34245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34252"></span>

<div id="answer-container-34252" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34252-score" class="post-score" title="current number of votes">0</div><span id="post-34252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think it means "uses OFDM if it can, reverts to CCK if it can't". <a href="https://en.wikipedia.org/wiki/802.11g">The Wikipedia article on 802.11g</a> says</p><blockquote><p>802.11g hardware is fully backwards compatible with 802.11b hardware. Details of making b and g work well together occupied much of the lingering technical process. In an 802.11g network, however, the presence of a legacy 802.11b participant will significantly reduce the speed of the overall 802.11g network. Some 802.11g routers employ a back-compatible mode for 802.11b clients called 54g LRS (Limited Rate Support).</p><p>The modulation scheme used in 802.11g is orthogonal frequency-division multiplexing (OFDM) copied from 802.11a with data rates of 6, 9, 12, 18, 24, 36, 48, and 54 Mbit/s, and reverts to CCK (like the 802.11b standard) for 5.5 and 11 Mbit/s and DBPSK/DQPSK+DSSS for 1 and 2 Mbit/s. Even though 802.11g operates in the same frequency band as 802.11b, it can achieve higher data rates because of its heritage to 802.11a.</p></blockquote><p>IEEE Std 802.11g-2003 says</p><blockquote><p>For example, a BSS could operate in an ERP-OFDM-only mode, a mixed mode of ERP-OFDM and ERP-DSSS/CCK, or a mixed mode of ERP-DSSS/CCK and Non-ERP.</p></blockquote><p>and "Dynamic CCK-OFDM" is probably "a mixed mode of ERP-OFDM and ERP-DSSS/CCK", whereas just "OFDM" would probably be "an ERP-OFDM-only mode" and just "CCK" would presumably be "a mixed mode of ERP-DSSS/CCK and Non-ERP".</p><p>(Note that the "channel type" field describes the channel, not the way the particular packet was transmitted.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '14, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jun '14, 14:48</strong> </span></p></div></div><div id="comments-container-34252" class="comments-container"><span id="34269"></span><div id="comment-34269" class="comment"><div id="post-34269-score" class="comment-score"></div><div class="comment-text"><p>I got it!</p><p>As the name implies, CCK/OFDM is a hybrid. It is included as an optional part of the IEEE 802.11g Draft Proposal. As shown in Figure 7, CCK/OFDM uses CCK modulation to transmit the Preamble/Header and OFDM to transmit the Payload. Note that the CCK and OFDM modulation formats remain separate and distinct. A transition from CCK modulation to OFDM modulation is made between the Preamble/Header and the Payload.</p></div><div id="comment-34269-info" class="comment-info"><span class="comment-age">(29 Jun '14, 10:30)</span> <span class="comment-user userinfo">Jan Hermanns</span></div></div></div><div id="comment-tools-34252" class="comment-tools"></div><div class="clear"></div><div id="comment-34252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

