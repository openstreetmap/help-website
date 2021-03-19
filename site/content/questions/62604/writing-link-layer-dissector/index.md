+++
type = "question"
title = "Writing Link Layer dissector"
description = '''I want to write my own LINK_LAYER dissector, which using DLT_USER13. I tried to use function  void dissector_add_for_decode_as(const char *name, dissector_handle_t handle); but i can&#x27;t understand the value of name for link_layer protocol.'''
date = "2017-07-07T06:32:00Z"
lastmod = "2017-07-11T19:16:00Z"
weight = 62604
keywords = [ "link_layer", "dlt_user" ]
aliases = [ "/questions/62604" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Writing Link Layer dissector](/questions/62604/writing-link-layer-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62604-score" class="post-score" title="current number of votes">0</div><span id="post-62604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I want to write my own LINK_LAYER dissector, which using DLT_USER13. I tried to use function <code>void dissector_add_for_decode_as(const char *name, dissector_handle_t handle);</code> but i can't understand the value of <strong>name</strong> for link_layer protocol.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-link_layer" rel="tag" title="see questions tagged &#39;link_layer&#39;">link_layer</span> <span class="post-tag tag-link-dlt_user" rel="tag" title="see questions tagged &#39;dlt_user&#39;">dlt_user</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '17, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/5f52a68bc7c3007b89b6d13df27d4184?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nomad&#39;s gravatar image" /><p><span>Nomad</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nomad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '17, 14:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-62604" class="comments-container"></div><div id="comment-tools-62604" class="comment-tools"></div><div class="clear"></div><div id="comment-62604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62688"></span>

<div id="answer-container-62688" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62688-score" class="post-score" title="current number of votes">0</div><span id="post-62688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "name" is the name of the dissector table; for a pcap/pcapng link layer, the name would be <code>"wtap.encap"</code>.</p><p>Alternatively, you can make sure your dissector has a name, and edit the "Encapsulations Table" list for the preferences for the "DLT_USER" protocol, and put in an entry with "User 13" as the DLT, your protocol as the "Payload protocol", and 0 as the header and trailer lengths.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '17, 19:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jul '17, 22:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-62688" class="comments-container"></div><div id="comment-tools-62688" class="comment-tools"></div><div class="clear"></div><div id="comment-62688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

