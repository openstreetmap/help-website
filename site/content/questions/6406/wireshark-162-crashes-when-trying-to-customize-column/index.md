+++
type = "question"
title = "Wireshark 1.6.2 crashes when trying to customize column"
description = '''Version 1.6.2 (SVN Rev 38931 from /trunk-1.6) Windows 7, 64-bit Wireshark crashes when trying to customize a column as eth.vlan.id, instance 1. This when the 802.1Q VLAN id column is visible and then selected for customization.  The capture does include packets from q-in-q trunk. The standard 802.1Q...'''
date = "2011-09-15T13:10:00Z"
lastmod = "2011-09-15T13:10:00Z"
weight = 6406
keywords = [ "column", "custom" ]
aliases = [ "/questions/6406" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.6.2 crashes when trying to customize column](/questions/6406/wireshark-162-crashes-when-trying-to-customize-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6406-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Version 1.6.2 (SVN Rev 38931 from /trunk-1.6) Windows 7, 64-bit</p><p>Wireshark crashes when trying to customize a column as eth.vlan.id, instance 1. This when the 802.1Q VLAN id column is visible and then selected for customization.</p><p>The capture does include packets from q-in-q trunk. The standard 802.1Q VLAN id only displays the innermost (instance 2) VLAN tag.</p><p>Creating the custom column from Edit/Pref/Columns does seem to work. Once created, the column is editable by selecting the column.</p><p>Jason</p></div><div id="question-tags" class="tags-container tags">column custom</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '11, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/32cb5681d46462bf751ad6880773796f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JasonF&#39;s gravatar image" /><p>JasonF<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JasonF has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Sep '11, 13:11</p></div></div><div id="comments-container-6406" class="comments-container"><span id="6409"></span><div id="comment-6409" class="comment"><div id="post-6409-score" class="comment-score">1</div><div class="comment-text"><p>You should file a <a href="http://bugzilla.wireshark.org">bug report</a>. Attach to the report a sample packet capture (scrubbed of any private info if necessary) that exercises the bug. Most importantly, describe your exact steps to reproduce the problem. In particular, "selected for customization" here needs clarification:</p><blockquote><p>This when the 802.1Q VLAN id column is visible and then selected for customization.</p></blockquote></div><div id="comment-6409-info" class="comment-info"><span class="comment-age">(15 Sep '11, 19:59)</span> helloworld</div></div></div><div id="comment-tools-6406" class="comment-tools"></div><div class="clear"></div><div id="comment-6406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

