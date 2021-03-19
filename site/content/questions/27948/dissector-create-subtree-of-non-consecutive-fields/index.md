+++
type = "question"
title = "Dissector / Create subtree of non-consecutive fields"
description = '''Hi all, I&#x27;m writing a dissector (over UDP) which has header fields (32 bytes) but also footer fields (padding of 8 bytes). The remaining data (between my protocol header and protocol footer) are passed to the usual &quot;data&quot; dissector. When creating my dissector subtree I do not success to highlight ju...'''
date = "2013-12-09T06:08:00Z"
lastmod = "2013-12-09T06:08:00Z"
weight = 27948
keywords = [ "proto_tree_add_item", "dissector" ]
aliases = [ "/questions/27948" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector / Create subtree of non-consecutive fields](/questions/27948/dissector-create-subtree-of-non-consecutive-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27948-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm writing a dissector (over UDP) which has header fields (32 bytes) but also footer fields (padding of 8 bytes). The remaining data (between my protocol header and protocol footer) are passed to the usual "data" dissector.</p><p>When creating my dissector subtree I do not success to highlight just the header and the footer.</p><p>With the following code I highlight the full UDP payload (my protocol header + the data + my protocol footer): amin_item = proto_tree_add_item(tree, proto_amin, tvb, 0, -1, FALSE); amin_tree = proto_item_add_subtree(amin_item, ett_amin);</p><p>Besides, with the following code I only highlight my protocol header: amin_item = proto_tree_add_item(tree, proto_amin, tvb, 0, 32, FALSE); amin_tree = proto_item_add_subtree(amin_item, ett_amin);</p><p>How could I create my subtree and only highlight my protocol header + my protocol footer?</p><p>Thanks.</p><p>PS: In the Ethernet frame with padding, when clicking to the Ethernet subtree, Ethernet header fields and padding are highlighted (the data between is not highlighted). I would like to do the same.</p></div><div id="question-tags" class="tags-container tags">proto_tree_add_item dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '13, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/997774ebe8215d18e07d84e29b1c5996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wolfy_21&#39;s gravatar image" /><p>Wolfy_21<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wolfy_21 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Dec '13, 06:17</p></div></div><div id="comments-container-27948" class="comments-container"></div><div id="comment-tools-27948" class="comment-tools"></div><div class="clear"></div><div id="comment-27948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

