+++
type = "question"
title = "TCP Window Scaling option"
description = '''I keep seeing what seems to be conflicting explanation for how to interpret TCP Window Scaling option in WS. I am writing a report on the what appears to be poor TCP performance. I need a warm fuzzy... My questions is this...  Scenario:  During TCP session establishment I typically see Win=8192 ** W...'''
date = "2015-08-27T05:01:00Z"
lastmod = "2015-08-27T05:01:00Z"
weight = 45397
keywords = [ "scaling", "window", "tcp" ]
aliases = [ "/questions/45397" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Window Scaling option](/questions/45397/tcp-window-scaling-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45397-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I keep seeing what seems to be conflicting explanation for how to interpret TCP Window Scaling option in WS. I am writing a report on the what appears to be poor TCP performance. I need a warm fuzzy...</p><p>My questions is this...</p><p>Scenario: During TCP session establishment I typically see Win=8192 ** WS=256.</p><p>1). Which is the correct way to interpret this? NOTE: Sometimes I will see small values vice 256 [8] WS=4 WRT (-1, 0 - 14) <strong>8192 * 8 = 65536 or</strong> 8192 * 256 = 2,097,152?</p><p>It would seem that the standard 64k Windows TCP Window size fit known conventions...however the purpose of TCP Windows Scaling it to allow window sizes to open up for large bandwidth segments up to 1Gbits</p><p>The confusing part is for example, I am looking at a file upload on our organizational intranet and what I see an average windows size of 920,951 Bytes; this includes sizes ranging from 138,752 to 953344. The majority of TCP window Updates indicate 953344.</p><p>Thanks in advance, Fritz</p><p>A few Refs:</p><p><a href="http://slaptijack.com/system-administration/what-is-tcp-window-scaling/">http://slaptijack.com/system-administration/what-is-tcp-window-scaling/</a> <a href="http://kb.pert.geant.net/PERTKB/WindowScalingOption">http://kb.pert.geant.net/PERTKB/WindowScalingOption</a></p></div><div id="question-tags" class="tags-container tags">scaling window tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '15, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/6e0fda2a5c8d02515d88f004b33a9998?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fritzbied&#39;s gravatar image" /><p>fritzbied<br />
<span class="score" title="6 reputation points">6</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fritzbied has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 27 Aug '15, 05:36</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-45397" class="comments-container"><span id="45471"></span><div id="comment-45471" class="comment"><div id="post-45471-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>The confusing part is for example,</p></blockquote><p>O.K. and what exactly does confuse you in that example? Looks totally normal to me.</p></div><div id="comment-45471-info" class="comment-info"><span class="comment-age">(28 Aug '15, 08:19)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-45397" class="comment-tools"></div><div class="clear"></div><div id="comment-45397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

