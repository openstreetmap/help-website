+++
type = "question"
title = "Capture filter - how to NOT capture ip range?"
description = '''Example of my filter: &quot;not broadcast and not multicast and not src net 192.168.1.0/24&quot;  and don&#x27;t want to capture data from IP range: 146.170.1.1 - 146.170.255.255 and 226.111.1.1 - 226.111.255.255'''
date = "2016-04-27T04:14:00Z"
lastmod = "2016-04-27T05:16:00Z"
weight = 51999
keywords = [ "filter", "capture" ]
aliases = [ "/questions/51999" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter - how to NOT capture ip range?](/questions/51999/capture-filter-how-to-not-capture-ip-range)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51999-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Example of my filter: "not broadcast and not multicast and not src net 192.168.1.0/24"</p><p>and don't want to capture data from IP range: 146.170.1.1 - 146.170.255.255 and 226.111.1.1 - 226.111.255.255</p></div><div id="question-tags" class="tags-container tags">filter capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '16, 04:14</strong></p><img src="https://secure.gravatar.com/avatar/3d9c606d7d9a99d49fcecb150f9f72c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="myszoor&#39;s gravatar image" /><p>myszoor<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="myszoor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Apr '16, 04:16</p></div></div><div id="comments-container-51999" class="comments-container"></div><div id="comment-tools-51999" class="comment-tools"></div><div class="clear"></div><div id="comment-51999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="52000"></span>

<div id="answer-container-52000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52000-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to exclude subnet ranges completely you'll need to explicitly exclude both source and destination IP ranges, e.g.:</p><p><code>not (ip.src==146.170.0.0/16 or ip.dst==146.170.0.0/16) and not (ip.src==226.111.0.0/16 or ip.dst==226.111.0.0/16)</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '16, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-52000" class="comments-container"><span id="52001"></span><div id="comment-52001" class="comment"><div id="post-52001-score" class="comment-score"></div><div class="comment-text"><p>@Jasper,</p><ul><li><p>the OP asks for a capture filter so the syntax is not the correct one; in capture filter, <code>not net 146.170.0.0/16</code> would cover both <code>src</code> and <code>dst</code> but he's asked for <code>src</code> only (data <strong>from</strong> IP range)</p></li><li><p>the OP has specially asked for a <strong>range</strong> so 146.170.0.0/16 won't do as 146.170.0.0/24, 146.170.1.0/32 and 146.170.1.1/32 should be let through unless he's made a mistake.</p></li></ul></div><div id="comment-52001-info" class="comment-info"><span class="comment-age">(27 Apr '16, 04:39)</span> sindy</div></div><span id="52004"></span><div id="comment-52004" class="comment"><div id="post-52004-score" class="comment-score"></div><div class="comment-text"><p>right... my bad about the capture filter syntax, I read the question too fast I guess. :-)</p><p>The question wording is a bit unspecific - he gives an example with broadcast and multicast and a src range and say "AND don't want to..." which lead me to assume that he want's to expand the example. I assumed also that the ranges should not appear at all, so a src filter only wouldn't do.</p><p>And yes, I assumed the full range was in question as it makes almost no sense at all to leave two /32 in there, especially the .0.0 which is the net address and should never been seen anyway for that range.</p></div><div id="comment-52004-info" class="comment-info"><span class="comment-age">(27 Apr '16, 04:54)</span> Jasper ♦♦</div></div></div><div id="comment-tools-52000" class="comment-tools"></div><div class="clear"></div><div id="comment-52000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52003"></span>

<div id="answer-container-52003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52003-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The simple answer would be <code>not net 146.170.0.0/16 and not net 226.111.0.0/16</code> but that would also exclude the ranges 146.170.0.0 - 146.170.0.255 and 226.111.0.0 - 226.111.0.255.</p><p>If you do want to see traffic in the x.x.0.0/24 subnets, then you'll have to "or" in those networks, e.g. <code>... or net 142.170.0.0/24 or net 226.111.0.0/24</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '16, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52003" class="comments-container"><span id="52008"></span><div id="comment-52008" class="comment"><div id="post-52008-score" class="comment-score"></div><div class="comment-text"><p>This</p><blockquote><blockquote><p>The simple answer would be not net 146.170.0.0/16 and not net 226.111.0.0/16 but that would also exclude the ranges 146.170.0.0 - 146.170.0.255 and 226.111.0.0 - 226.111.0.255.</p></blockquote></blockquote><p>works fine - thanks :)</p><p>Have one more question - how add to this filter: "not broadcast and not multicast and not src net 192.168.1.0/24" exception "192.168.1.111".</p><p>Overall idea is: want ignore all local network traffic with exception of traffic beetwen IP "192.168.1.111" (on 192.168.1.111 is working WS) and Internet. In Internet traffic want ignore IP from range 146.170.0.0/16 and 226.111.0.0/16 (beacuse hosts from this IP ranges are trusted for me).</p></div><div id="comment-52008-info" class="comment-info"><span class="comment-age">(27 Apr '16, 05:34)</span> myszoor</div></div><span id="52009"></span><div id="comment-52009" class="comment"><div id="post-52009-score" class="comment-score"></div><div class="comment-text"><p><code>not broadcast and not multicast and (not src net 192.168.1.0/24 or src host 192.168.1.111)</code></p></div><div id="comment-52009-info" class="comment-info"><span class="comment-age">(27 Apr '16, 05:36)</span> sindy</div></div></div><div id="comment-tools-52003" class="comment-tools"></div><div class="clear"></div><div id="comment-52003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52006"></span>

<div id="answer-container-52006" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52006-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi all, is it correct the below filter for his aim in your opinion ?</p><p>(not broadcast and not multicast and not ip src net 192.168.1.0/24) or (not ip net 146.170.0.0/16 or not ip net 226.111.0.0/16)</p><p>Have a nice day</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '16, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/bba638c3a54975c52c98530defa199af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ValerioItaly&#39;s gravatar image" /><p>ValerioItaly<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ValerioItaly has no accepted answers">0%</span></p></div></div><div id="comments-container-52006" class="comments-container"><span id="52007"></span><div id="comment-52007" class="comment"><div id="post-52007-score" class="comment-score"></div><div class="comment-text"><p>It is not correct at least because <code>not ip net 146.170.0.0/16</code> is true also for e.g. broadcast packets, and <code>not broadcast</code> is true for any non-broadcast packet including one from/to 146.170.0.0/16, so (simplified for illustration) <code>not broadcast or not ip net 146.170.0.0/16</code> would cause both broadcast packets and packets to/from 146.170.0.0/16 to be captured. For similar reason, <code>not net X or not net Y</code> would let through everything (unless networks X and Y overlap in some way).</p><p>@grahamb's answer is the closest one so far. Let's wait for OP's update and eventually adjust that one accordingly. But basically <code>((not src net 146.170.0.0/16) or src net 146.170.0.0/24)</code> is a way to exclude packets whose src ip is in range 146.170.1.0 to 146.170.255.255 from the capture.</p></div><div id="comment-52007-info" class="comment-info"><span class="comment-age">(27 Apr '16, 05:34)</span> sindy</div></div></div><div id="comment-tools-52006" class="comment-tools"></div><div class="clear"></div><div id="comment-52006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

