+++
type = "question"
title = "Does Wireshark Version 1.10.6 STUN dissector comply with rfc 6062?"
description = '''Hi Does Wireshark Version 1.10.6 complies with rfc 6062. As i get message method 0*000b AS UNKNOWN.'''
date = "2015-02-26T02:22:00Z"
lastmod = "2015-02-26T03:07:00Z"
weight = 40088
keywords = [ "rfc", "stun", "6062" ]
aliases = [ "/questions/40088" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark Version 1.10.6 STUN dissector comply with rfc 6062?](/questions/40088/does-wireshark-version-1106-stun-dissector-comply-with-rfc-6062)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40088-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Does Wireshark Version 1.10.6 complies with rfc 6062.</p><p>As i get message method 0*000b AS UNKNOWN.</p></div><div id="question-tags" class="tags-container tags">rfc stun 6062</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '15, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/1bb7dd4334a15adf12a27a3abd4dd5d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shaggy&#39;s gravatar image" /><p>shaggy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shaggy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '15, 14:37</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-40088" class="comments-container"></div><div id="comment-tools-40088" class="comment-tools"></div><div class="clear"></div><div id="comment-40088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40090"></span>

<div id="answer-container-40090" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40090-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently not. Even the current master code for the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-stun.c;hb=HEAD">STUN dissector</a> has the following in the comments:</p><pre><code> * - RFC 5389, formerly draft-ietf-behave-rfc3489bis-18
 * - RFC 5245, formerly draft-ietf-mmusic-ice-19
 * - RFC 5780, formerly draft-ietf-behave-nat-behavior-discovery-08
 * - RFC 5766, formerly draft-ietf-behave-turn-16
 * - draft-ietf-behave-turn-ipv6-11
 * - RFC 3489, http://www.faqs.org/rfcs/rfc3489.html  (Addition of deprecated attributes for diagnostics purpose)</code></pre><p>And the following methods:</p><pre><code>/* Methods */
#define BINDING                 0x0001 /* draft-ietf-behave-rfc3489bis-17 */
#define ALLOCATE                0x0003 /* draft-ietf-behave-turn-10*/
#define REFRESH                 0x0004 /* draft-ietf-behave-turn-10*/
#define CHANNELBIND             0x0009 /* draft-ietf-behave-turn-10*/
#define CREATE_PERMISSION       0x0008 /* draft-ietf-behave-turn-10 */
/* Indications */
#define SEND                    0x0006 /* draft-ietf-behave-turn-10*/
#define DATA_IND                0x0007 /* draft-ietf-behave-turn-10*/</code></pre><p>Please check at the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> if there is a item already already open for this issue, and if not create a new one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '15, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '15, 09:21</p></div></div><div id="comments-container-40090" class="comments-container"><span id="40103"></span><div id="comment-40103" class="comment"><div id="post-40103-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb,</p><p>Does any higher version of wireshark compiles with rfc 6062?</p></div><div id="comment-40103-info" class="comment-info"><span class="comment-age">(26 Feb '15, 08:58)</span> shaggy</div></div><span id="40105"></span><div id="comment-40105" class="comment"><div id="post-40105-score" class="comment-score"></div><div class="comment-text"><p>Nope, the excerpts above are from the current latest version of the file.</p></div><div id="comment-40105-info" class="comment-info"><span class="comment-age">(26 Feb '15, 09:17)</span> grahamb ♦</div></div></div><div id="comment-tools-40090" class="comment-tools"></div><div class="clear"></div><div id="comment-40090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

