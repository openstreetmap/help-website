+++
type = "question"
title = "tshark -G doesn&#x27;t work with profiles?"
description = '''Hi all, I&#x27;m not sure if that&#x27;s a bug or something I&#x27;m doing wrong, and will appreciate your help. I&#x27;m trying to get the list of ports which are decoded as http under the profile &quot;myprofile&quot;. If I try doing: tshark.exe -G decodes -C myprofile | grep http  I get the default profile&#x27;s decoding list. If...'''
date = "2011-02-10T00:42:00Z"
lastmod = "2011-02-14T12:57:00Z"
weight = 2263
keywords = [ "decode", "tshark" ]
aliases = [ "/questions/2263" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark -G doesn't work with profiles?](/questions/2263/tshark-g-doesnt-work-with-profiles)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2263-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm not sure if that's a bug or something I'm doing wrong, and will appreciate your help. I'm trying to get the list of ports which are decoded as http under the profile "myprofile". If I try doing:</p><pre><code>tshark.exe -G decodes -C myprofile | grep http</code></pre><p>I get the default profile's decoding list. If however I try</p><pre><code>tshark.exe -C myprofile -G decodes | grep http</code></pre><p>I get tshark's help page. Any idea how to get the list of ports I'm looking for?</p></div><div id="question-tags" class="tags-container tags">decode tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '11, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/9b7b5e633f7836289c2fc6c3934bffaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r0u1i&#39;s gravatar image" /><p>r0u1i<br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r0u1i has no accepted answers">0%</span></p></div></div><div id="comments-container-2263" class="comments-container"></div><div id="comment-tools-2263" class="comment-tools"></div><div class="clear"></div><div id="comment-2263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2330"></span>

<div id="answer-container-2330" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2330-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you are trying to do is not currently supported. As far as I can tell, only the default profile's decoding list will be returned regardless of a profile being specified or not.</p><p>Moreover, at present, it is expected that if the <code>-G</code> option is specified, then it must be the very first option; otherwise it will appear as an invalid option, which is what you encountered in your second attempt as:</p><pre><code>tshark.exe -C myprofile -G decodes | grep http</code></pre><p>... and because it's treated as an invalid option, you are <em>"treated"</em> to the tshark usage output.</p><p>Anyway, if you desire this functionality, I would suggest filing a bug report for it <a href="https://bugs.wireshark.org/bugzilla/">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '11, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-2330" class="comments-container"></div><div id="comment-tools-2330" class="comment-tools"></div><div class="clear"></div><div id="comment-2330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

