+++
type = "question"
title = "Is it possible to filter SNMP packets looking for specific text in the values?"
description = '''I am looking at a large number of SNMP packets and want to be able to search them all for specific strings of human readable text. Here are some examples: &quot;Loss&quot; &quot;LOS&quot; &quot;Loss Of Signal&quot; &quot;Loss of Enet link from Controller&quot; If anyone has done anything similar, your feedback would be most welcome.  Than...'''
date = "2016-07-15T14:13:00Z"
lastmod = "2016-07-15T16:27:00Z"
weight = 54084
keywords = [ "snmp" ]
aliases = [ "/questions/54084" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to filter SNMP packets looking for specific text in the values?](/questions/54084/is-it-possible-to-filter-snmp-packets-looking-for-specific-text-in-the-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54084-score" class="post-score" title="current number of votes">0</div><span id="post-54084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking at a large number of SNMP packets and want to be able to search them all for specific strings of human readable text. Here are some examples: "Loss" "LOS" "Loss Of Signal" "Loss of Enet link from Controller" If anyone has done anything similar, your feedback would be most welcome.</p><p>Thank you</p><p>Lars</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '16, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/ed1276dd1840b5936f0e463eb18ea659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lars&#39;s gravatar image" /><p><span>Lars</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lars has no accepted answers">0%</span></p></div></div><div id="comments-container-54084" class="comments-container"></div><div id="comment-tools-54084" class="comment-tools"></div><div class="clear"></div><div id="comment-54084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54085"></span>

<div id="answer-container-54085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54085-score" class="post-score" title="current number of votes">0</div><span id="post-54085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try using a <a href="https://www.wireshark.org/docs/man-pages/wireshark-filter.html">Wireshark Display Filter</a> incorporating the "matches" (or "contains") operator.</p><p>An example:</p><pre><code>snmp.var-bind_str matches &quot;(?i)Los&quot;</code></pre><p>Replace <code>snmp.var-bind_str</code> with the appropriate field or fields if that's not the right one for your needs, or you could use a more generic filter, such as:</p><pre><code>snmp and frame matches &quot;(?i)Los&quot;</code></pre><p>If a case-insensitive match of "Los" is not restrictive enough, then you could always <em><code>or</code></em> together filters that meet your needs.</p><p>For example:</p><pre><code>snmp.var-bind_str matches &quot;^Loss&quot; or snmp.var-bind_str contains &quot;LOS&quot;</code></pre><p>Experiment a bit to find the filter that best meets your exact needs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '16, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54085" class="comments-container"></div><div id="comment-tools-54085" class="comment-tools"></div><div class="clear"></div><div id="comment-54085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54086"></span>

<div id="answer-container-54086" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54086-score" class="post-score" title="current number of votes">0</div><span id="post-54086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to use: snmp.value.octets contains "Loss"</p><p>I think with this type of string I can search the SNMP contents for any type of message now.</p><p>Thanks!</p><p>Lars</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '16, 16:27</strong></p><img src="https://secure.gravatar.com/avatar/ed1276dd1840b5936f0e463eb18ea659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lars&#39;s gravatar image" /><p><span>Lars</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lars has no accepted answers">0%</span></p></div></div><div id="comments-container-54086" class="comments-container"></div><div id="comment-tools-54086" class="comment-tools"></div><div class="clear"></div><div id="comment-54086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

