+++
type = "question"
title = "libxml2 in dessector - string encoding"
description = '''Hi, I&#x27;m using libxml2 to read an xml-file (in utf-8) and set the tree-items in wireshark. My problem is that I only see unreadable text in wireshark. I used  xmlNodeGetContent(node-&amp;gt;xmlChildrenNode);  to get the content and than  proto_item_append_text(ti,ts);  to set text text to a tree-item and...'''
date = "2012-02-06T05:28:00Z"
lastmod = "2012-02-06T05:28:00Z"
weight = 8845
keywords = [ "libxml2", "dissector", "encoding" ]
aliases = [ "/questions/8845" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [libxml2 in dessector - string encoding](/questions/8845/libxml2-in-dessector-string-encoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8845-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using libxml2 to read an xml-file (in utf-8) and set the tree-items in wireshark. My problem is that I only see unreadable text in wireshark. I used xmlNodeGetContent(node-&gt;xmlChildrenNode); to get the content and than proto_item_append_text(ti,ts); to set text text to a tree-item and I get something like ð§Derungsanhang What should I call to get a readable string?</p></div><div id="question-tags" class="tags-container tags">libxml2 dissector encoding</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '12, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/ce79034142dc613a1a30949664b84723?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic&#39;s gravatar image" /><p>Nic<br />
<span class="score" title="14 reputation points">14</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic has no accepted answers">0%</span></p></div></div><div id="comments-container-8845" class="comments-container"></div><div id="comment-tools-8845" class="comment-tools"></div><div class="clear"></div><div id="comment-8845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

