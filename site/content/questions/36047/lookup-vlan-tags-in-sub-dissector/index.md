+++
type = "question"
title = "Lookup VLAN tags in sub-dissector"
description = '''Hi, I am currently writing a dissector which handles a registered ethertype, and I have a requirement to reassemble a subtype from multiple fragments. The key/uniqueness for these fragments is held in the vlan tag/ID and so I need to access this information from a sub-dissector. I think I am missing...'''
date = "2014-09-06T19:18:00Z"
lastmod = "2014-09-06T19:18:00Z"
weight = 36047
keywords = [ "development", "dissector", "subdissector", "vlan" ]
aliases = [ "/questions/36047" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lookup VLAN tags in sub-dissector](/questions/36047/lookup-vlan-tags-in-sub-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36047-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am currently writing a dissector which handles a registered ethertype, and I have a requirement to reassemble a subtype from multiple fragments. The key/uniqueness for these fragments is held in the vlan tag/ID and so I need to access this information from a sub-dissector.</p><p>I think I am missing something fundamental, but some guidance on how to access the vlan information would be great. Currently I am looking at the column info for QinQ VLAN tags, but I assume this is a hack and not an appropriate way to ascertain this information. Perhaps tapping or some other construct is required?</p><p>Regards</p><p>John</p></div><div id="question-tags" class="tags-container tags">development dissector subdissector vlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '14, 19:18</strong></p><img src="https://secure.gravatar.com/avatar/a57776c478b7160f88e7deb83c5b0fcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crumble68&#39;s gravatar image" /><p>crumble68<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crumble68 has no accepted answers">0%</span></p></div></div><div id="comments-container-36047" class="comments-container"></div><div id="comment-tools-36047" class="comment-tools"></div><div class="clear"></div><div id="comment-36047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

