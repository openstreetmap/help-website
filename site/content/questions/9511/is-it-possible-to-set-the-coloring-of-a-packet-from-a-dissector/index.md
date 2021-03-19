+++
type = "question"
title = "Is it possible to set the coloring of a packet from a dissector?"
description = '''Is there any way to set the packet colors through dissector (or any other file), but through code only?'''
date = "2012-03-13T09:32:00Z"
lastmod = "2012-03-13T09:55:00Z"
weight = 9511
keywords = [ "coloring", "dissector", "packet-display" ]
aliases = [ "/questions/9511" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to set the coloring of a packet from a dissector?](/questions/9511/is-it-possible-to-set-the-coloring-of-a-packet-from-a-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9511-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to set the packet colors through dissector (or any other file), but through code only?</p></div><div id="question-tags" class="tags-container tags">coloring dissector packet-display</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '12, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p>ashish_goel<br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '12, 09:57</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9511" class="comments-container"></div><div id="comment-tools-9511" class="comment-tools"></div><div class="clear"></div><div id="comment-9511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9512"></span>

<div id="answer-container-9512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9512-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packet coloring rules are defined by the user via the <code>View -&gt; Coloring Rules</code> dialog. Rules are defined with a name, a background color, a foreground color, and a display filter. They are ordered such that rules higher in the list are tried first, and the first rule to match a packet determines its color. Once these rules are in place, coloring is automatic. The only way to "set the packet colors" is to dissect the packet using the header fields defined for your protocol and hope the user has appropriate coloring rules.<br />
You may be able to <em>influence</em> this behavior by supplying coloring rules with your version of Wireshark, but there is no exposed mechanism at the dissector level to influence the color of a packet in the packet list view (and why should there be, since the user could be running <code>tshark</code> in stead, which must run dissector code but cannot color packets at all).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '12, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></p></div></div><div id="comments-container-9512" class="comments-container"><span id="9513"></span><div id="comment-9513" class="comment"><div id="post-9513-score" class="comment-score"></div><div class="comment-text"><p>thnx for the quick reply.</p><p>by supplying the coloring rules do you mean to write a coloring rule file similar to file "colorfilters" present in your personal configuration of wireshark.</p></div><div id="comment-9513-info" class="comment-info"><span class="comment-age">(13 Mar '12, 10:23)</span> ashish_goel</div></div><span id="9515"></span><div id="comment-9515" class="comment"><div id="post-9515-score" class="comment-score"></div><div class="comment-text"><p>Yes, but I do not know where the default set is provided off hand. Keep in mind that your users could ultimately change any coloring rules you provided, so you should not assume that your specific coloring rules will always be available.</p></div><div id="comment-9515-info" class="comment-info"><span class="comment-age">(13 Mar '12, 10:39)</span> multipleinte...</div></div><span id="9516"></span><div id="comment-9516" class="comment"><div id="post-9516-score" class="comment-score"></div><div class="comment-text"><p>The default set of color rules is in a file that's part of the Wireshark installation.</p><p>As multipleinterfaces noted, Wireshark allows the user to change coloring rules, so it does not and will not ever have a mechanism to allow a dissector to force a particular color to be used - the developer will not be allowed to force a particular color to be used without the user being allowed to override it.</p></div><div id="comment-9516-info" class="comment-info"><span class="comment-age">(13 Mar '12, 11:01)</span> Guy Harris ♦♦</div></div><span id="9529"></span><div id="comment-9529" class="comment"><div id="post-9529-score" class="comment-score"></div><div class="comment-text"><p>thanks for all your help.</p></div><div id="comment-9529-info" class="comment-info"><span class="comment-age">(13 Mar '12, 21:14)</span> ashish_goel</div></div><span id="9556"></span><div id="comment-9556" class="comment"><div id="post-9556-score" class="comment-score"></div><div class="comment-text"><p>@ guy harris. Even if there was a possibility of setting the color codes through dissector code, it won't have meant forcing the scheme user. In such a case user could have overwrite the rules by specifying its own rules through Wireshark GUI.</p><p>Wireshark has already such kind of mechanism for preferences settings then why can't for color scheme?</p></div><div id="comment-9556-info" class="comment-info"><span class="comment-age">(15 Mar '12, 07:43)</span> ashish_goel</div></div></div><div id="comment-tools-9512" class="comment-tools"></div><div class="clear"></div><div id="comment-9512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

