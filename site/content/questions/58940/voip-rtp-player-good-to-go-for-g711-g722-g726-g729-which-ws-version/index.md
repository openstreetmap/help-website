+++
type = "question"
title = "VoIP RTP Player Good to Go for g711, g722, G726, G729? Which WS version?"
description = '''I was reading Peter Wu&#x27;s release on the update in Dec 2016 that WS playback ability for codecs other than g711 was &quot;merged&quot;. see https://code.wireshark.org/review/18939. I downloaded the test files but the only one that worked was the g711 still. My WS version is 2.2.3 (v2.2.3-0-g57531cd) downloaded...'''
date = "2017-01-21T17:22:00Z"
lastmod = "2017-01-23T03:40:00Z"
weight = 58940
keywords = [ "g711a", "g729", "g722", "voip" ]
aliases = [ "/questions/58940" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VoIP RTP Player Good to Go for g711, g722, G726, G729? Which WS version?](/questions/58940/voip-rtp-player-good-to-go-for-g711-g722-g726-g729-which-ws-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58940-score" class="post-score" title="current number of votes">0</div><span id="post-58940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was reading Peter Wu's release on the update in Dec 2016 that WS playback ability for codecs other than g711 was "merged". see <a href="https://code.wireshark.org/review/18939.">https://code.wireshark.org/review/18939.</a></p><p>I downloaded the test files but the only one that worked was the g711 still. My WS version is 2.2.3 (v2.2.3-0-g57531cd) downloaded 12-20-17).</p><p>Is this in the "bleeding edge" version or is it still coming? I know A LOT of voip guys are dying to get this functionality.</p><p>Thanks Eric</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-g711a" rel="tag" title="see questions tagged &#39;g711a&#39;">g711a</span> <span class="post-tag tag-link-g729" rel="tag" title="see questions tagged &#39;g729&#39;">g729</span> <span class="post-tag tag-link-g722" rel="tag" title="see questions tagged &#39;g722&#39;">g722</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '17, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jan '17, 17:23</strong> </span></p></div></div><div id="comments-container-58940" class="comments-container"></div><div id="comment-tools-58940" class="comment-tools"></div><div class="clear"></div><div id="comment-58940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58941"></span>

<div id="answer-container-58941" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58941-score" class="post-score" title="current number of votes">1</div><span id="post-58941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to download the Wireshark 2.3 development nightly builds that can be found <a href="https://www.wireshark.org/download/automated/">here</a>. G.722 and G.726 playback will be part of Wireshark 2.4 release that will be out sometime around summer. Note that G.729 (and AMR) playback is not supported due to patents.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '17, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-58941" class="comments-container"><span id="58971"></span><div id="comment-58971" class="comment"><div id="post-58971-score" class="comment-score"></div><div class="comment-text"><p>YaaaaaY!!!!!</p></div><div id="comment-58971-info" class="comment-info"><span class="comment-age">(23 Jan '17, 03:26)</span> <span class="comment-user userinfo">EricKnaus</span></div></div><span id="58972"></span><div id="comment-58972" class="comment"><div id="post-58972-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-58972-info" class="comment-info"><span class="comment-age">(23 Jan '17, 03:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-58941" class="comment-tools"></div><div class="clear"></div><div id="comment-58941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

