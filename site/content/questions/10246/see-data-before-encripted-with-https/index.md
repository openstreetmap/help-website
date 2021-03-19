+++
type = "question"
title = "See Data before encripted with HTTPS"
description = '''Can I, with WireShark, see what data is being sent via HTTPS before it has been encripted?'''
date = "2012-04-18T09:49:00Z"
lastmod = "2012-04-19T11:38:00Z"
weight = 10246
keywords = [ "encripted", "https" ]
aliases = [ "/questions/10246" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [See Data before encripted with HTTPS](/questions/10246/see-data-before-encripted-with-https)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10246-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I, with WireShark, see what data is being sent via HTTPS before it has been encripted?</p></div><div id="question-tags" class="tags-container tags">encripted https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '12, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/37dea0fbe37c2a62551e7235c11eba3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IraH&#39;s gravatar image" /><p>IraH<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IraH has no accepted answers">0%</span></p></div></div><div id="comments-container-10246" class="comments-container"></div><div id="comment-tools-10246" class="comment-tools"></div><div class="clear"></div><div id="comment-10246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10249"></span>

<div id="answer-container-10249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10249-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can, in some cases, if you have enough information, <em>decrypt</em> the data <em>after</em> it has been encrypted and transmitted; see <a href="http://wiki.wireshark.org/SSL">the Wireshark Wiki page about SSL</a>. There's no place for Wireshark to connect to your Web browser to see the data <em>before</em> it's encrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '12, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10249" class="comments-container"></div><div id="comment-tools-10249" class="comment-tools"></div><div class="clear"></div><div id="comment-10249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10296"></span>

<div id="answer-container-10296" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10296-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That (seeing the data from a browser hook before it is encrypted (outbound) and after it is decrypted (inbound)) can be done with a variety of <em>browser</em> accessories, such as TamperData and Firebug. You can also insert a man-in-the-middle HTTPS proxy such as Charles Proxy. But for more information on any of those options, go to their respective discussion sites.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-10296" class="comments-container"></div><div id="comment-tools-10296" class="comment-tools"></div><div class="clear"></div><div id="comment-10296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

