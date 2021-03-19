+++
type = "question"
title = "Kovter infection, can anybody help me track it down?"
description = '''Hi I have been informed of a Kovter infection here at work, but im struggling to track it down. I have the folllwing information:  2015-01-27 08:40:09 ip OUREXTERNALIP port 43533 hostname mail.OURDOMAIN infection Kovter url /w1/form.php cc_asn 1101 cc_dns final9a.biz  I tried filter by port:  tcp.po...'''
date = "2015-01-29T03:22:00Z"
lastmod = "2015-02-05T13:30:00Z"
weight = 39473
keywords = [ "kovter", "help", "infection" ]
aliases = [ "/questions/39473" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Kovter infection, can anybody help me track it down?](/questions/39473/kovter-infection-can-anybody-help-me-track-it-down)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39473-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have been informed of a Kovter infection here at work, but im struggling to track it down. I have the folllwing information:</p><blockquote><p>2015-01-27 08:40:09</p><p>ip OUREXTERNALIP</p><p>port 43533</p><p>hostname mail.OURDOMAIN</p><p>infection Kovter</p><p>url /w1/form.php</p><p>cc_asn 1101</p><p>cc_dns final9a.biz</p></blockquote><p>I tried filter by port:</p><blockquote><p>tcp.port eq 43533</p></blockquote><p>But nothing shows up. Can any suggest something else to track this down?</p><p>Thanks in advance</p><p>EDIT: I did find this site that goes into detail about this infection, but alas...I'm not 100% sure where to start with WireShark.</p><p><a href="http://www.cyphort.com/kovter-ad-fraud-trojan/">http://www.cyphort.com/kovter-ad-fraud-trojan/</a></p></div><div id="question-tags" class="tags-container tags">kovter help infection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '15, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/9ee6ce020149c87a43ab2dac61a7467f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="F2000&#39;s gravatar image" /><p>F2000<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="F2000 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '15, 08:04</p></div></div><div id="comments-container-39473" class="comments-container"></div><div id="comment-tools-39473" class="comment-tools"></div><div class="clear"></div><div id="comment-39473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39518"></span>

<div id="answer-container-39518" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39518-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not familiar with this malware, but based on the link you provided, you may want to try editing/adding a coloring rule(s) for some extensions that might be in use, such as: .exe .pl .py .pw .biz</p><p>Eg. frame matches ".(?i)exe"<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '15, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/ad02d2c94bb362339b32ac9e2ca8468e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qwert&#39;s gravatar image" /><p>Qwert<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qwert has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39518" class="comments-container"><span id="39668"></span><div id="comment-39668" class="comment"><div id="post-39668-score" class="comment-score"></div><div class="comment-text"><p>Qwert</p><p>First, thank you for replying and sorry its taken so long for me to reply. I had given up hope. Sorry to bug you again, but would ".(?i)biz" be enough...or any of the following?</p><p>http.request.uri matches ".(?i)biz"</p><p>http contains "final9a.biz"</p><p>Thanks again, really appreciate you taking time to reply.</p></div><div id="comment-39668-info" class="comment-info"><span class="comment-age">(05 Feb '15, 07:40)</span> F2000</div></div></div><div id="comment-tools-39518" class="comment-tools"></div><div class="clear"></div><div id="comment-39518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39675"></span>

<div id="answer-container-39675" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39675-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First, it seems that they either updated their analysis, or I didn't read it well enough the first time (more likely the latter). The .py/.pl extensions are not relevant (so my apologies on the misinformation).</p><p>With regard to the coloring rule, I like 'frame matches' because the protocol needs to be recognized as http in order for an 'http' coloring rule to find a match. That being said, an http-specific rule may work just fine so the syntax of the rule here may be a non-issue in that one respect.</p><p>In addition to 'final9a.biz,' it looks like the following names should also be looked for:</p><p>a16-car.biz resolveasy.com a16-kite.pw (I <em>think</em> this is a locally run request on an infected host, so this may not show up in traffic)</p><p>Also ... 'resolveasy.com' doesn't resolve but resolveeasy.com does. Both domains are registered, but only the latter currently has a DNS record. Regardless, rules for both will cover those bases.</p><p>HTH</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '15, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/ad02d2c94bb362339b32ac9e2ca8468e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qwert&#39;s gravatar image" /><p>Qwert<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qwert has no accepted answers">0%</span></p></div></div><div id="comments-container-39675" class="comments-container"></div><div id="comment-tools-39675" class="comment-tools"></div><div class="clear"></div><div id="comment-39675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

