+++
type = "question"
title = "Format of s1ap.m_TMSI"
description = '''I&#x27;m trying to filter s1ap communication for a certain M-TMSI. So a1ap.m_TMSI looks like what I&#x27;m searching for. M-TMSI format is a hex 4Byte number .... (i.e.: 0x21de4747)  How can I search for this or do I misunderstand m_TMSI in wireshark....? Error: &quot;s1ap.m_TMSI==0x021de4747&quot; isn&#x27;t a valid displa...'''
date = "2015-02-12T23:24:00Z"
lastmod = "2015-02-13T05:25:00Z"
weight = 39843
keywords = [ "s1ap" ]
aliases = [ "/questions/39843" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Format of s1ap.m\_TMSI](/questions/39843/format-of-s1apm_tmsi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39843-score" class="post-score" title="current number of votes">0</div><span id="post-39843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to filter s1ap communication for a certain M-TMSI. So a1ap.m_TMSI looks like what I'm searching for.</p><p>M-TMSI format is a hex 4Byte number .... (i.e.: 0x21de4747)</p><p>How can I search for this or do I misunderstand m_TMSI in wireshark....?</p><p>Error: "s1ap.m_TMSI==0x021de4747" isn't a valid display filter: "0x021de4747" is not a valid byte string.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-s1ap" rel="tag" title="see questions tagged &#39;s1ap&#39;">s1ap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '15, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/8dfb58db2c8903a1e1083f1291265733?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dibu&#39;s gravatar image" /><p><span>dibu</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dibu has no accepted answers">0%</span></p></div></div><div id="comments-container-39843" class="comments-container"></div><div id="comment-tools-39843" class="comment-tools"></div><div class="clear"></div><div id="comment-39843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39845"></span>

<div id="answer-container-39845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39845-score" class="post-score" title="current number of votes">1</div><span id="post-39845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try instead:</p><pre><code>s1ap.m_TMSI == 21:de:47:47</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '15, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-39845" class="comments-container"><span id="39846"></span><div id="comment-39846" class="comment"><div id="post-39846-score" class="comment-score"></div><div class="comment-text"><p>sometimes solutions are real simple ....</p><p>Thanks</p><p>... confusing: filter notation of technical parameter M-TMSI depends on packet you want to get the information from.....</p><p>s1ap.m_TMSI==21:de:47:47 --&gt; thats's what I've been looking for ...</p><p>nas_eps.emm.m_tmsi == 0x21de4747 --&gt; when I realized that I didn't see all of the packets .....</p></div><div id="comment-39846-info" class="comment-info"><span class="comment-age">(13 Feb '15, 03:41)</span> <span class="comment-user userinfo">dibu</span></div></div><span id="39848"></span><div id="comment-39848" class="comment"><div id="post-39848-score" class="comment-score"></div><div class="comment-text"><p>This is a side effect of the S1AP dissector being automatically generated from the ASN.1 specification where M-TMSI is defined as OCTET STRING (SIZE (4)). This could be easily fixed but would break backward compatibility.</p></div><div id="comment-39848-info" class="comment-info"><span class="comment-age">(13 Feb '15, 05:25)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-39845" class="comment-tools"></div><div class="clear"></div><div id="comment-39845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

