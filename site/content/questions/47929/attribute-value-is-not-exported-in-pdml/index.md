+++
type = "question"
title = "Attribute value is not exported in PDML"
description = '''Hello every body, I wonder why in the PDML the attribute value is not exported when I do the following thing in the lua dissector: subtree:add(f_sil, bit.band(buffer(3,1):uint(), 0x0F)) =&amp;gt; no attribute value is exported in PDML for field f_sil. When I do this, this works well (but not what I want...'''
date = "2015-11-24T06:21:00Z"
lastmod = "2015-11-24T06:21:00Z"
weight = 47929
keywords = [ "pdml", "export" ]
aliases = [ "/questions/47929" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Attribute value is not exported in PDML](/questions/47929/attribute-value-is-not-exported-in-pdml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47929-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello every body,</p><p>I wonder why in the PDML the attribute value is not exported when I do the following thing in the lua dissector:</p><p>subtree:add(f_sil, bit.band(buffer(3,1):uint(), 0x0F)) =&gt; no attribute value is exported in PDML for field f_sil.</p><p>When I do this, this works well (but not what I want): subtree:add(f_sil, buffer(3,1)) =&gt; atribute value is present in PDML.</p><p>Thanks in advance for any help.</p><p>Best regards.</p></div><div id="question-tags" class="tags-container tags">pdml export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '15, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/53788167c9f9406f36b429ed9d9546af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sedor36&#39;s gravatar image" /><p>sedor36<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sedor36 has no accepted answers">0%</span></p></div></div><div id="comments-container-47929" class="comments-container"></div><div id="comment-tools-47929" class="comment-tools"></div><div class="clear"></div><div id="comment-47929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

