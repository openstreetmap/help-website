+++
type = "question"
title = "how to write a wireshark  dissector to write a amf packet to a file"
description = '''I want to write a wireshark dissector in ubuntu to write an amf packet to a file.'''
date = "2012-10-15T22:59:00Z"
lastmod = "2012-10-15T22:59:00Z"
weight = 15025
keywords = [ "dissector" ]
aliases = [ "/questions/15025" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to write a wireshark dissector to write a amf packet to a file](/questions/15025/how-to-write-a-wireshark-dissector-to-write-a-amf-packet-to-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15025-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to write a wireshark dissector in ubuntu to write an amf packet to a file.</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '12, 22:59</strong></p><img src="https://secure.gravatar.com/avatar/b0ed262c234b0aa9fae2e5b2d51b14c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akhil&#39;s gravatar image" /><p>Akhil<br />
<span class="score" title="53 reputation points">53</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akhil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Oct '12, 23:00</p></div></div><div id="comments-container-15025" class="comments-container"><span id="15028"></span><div id="comment-15028" class="comment"><div id="post-15028-score" class="comment-score"></div><div class="comment-text"><p>There already is a dissector: RTMPT</p></div><div id="comment-15028-info" class="comment-info"><span class="comment-age">(15 Oct '12, 23:28)</span> Jaap ♦</div></div><span id="15038"></span><div id="comment-15038" class="comment"><div id="post-15038-score" class="comment-score"></div><div class="comment-text"><p>Dissectors don't write stuff to files, they just dissect packets and construct a tree of fields and subfields. Other parts of Wireshark can write stuff to files, including a "printed-out" version of that tree.</p><p>If a Wireshark dissector is dissecting an AMF packet, the packet is already <em>in</em> a file - the file that Wireshark read.</p><p>What <em>exactly</em> do you want to do here?</p></div><div id="comment-15038-info" class="comment-info"><span class="comment-age">(16 Oct '12, 16:43)</span> Guy Harris ♦♦</div></div><span id="15053"></span><div id="comment-15053" class="comment"><div id="post-15053-score" class="comment-score"></div><div class="comment-text"><p>And if you want to write AMF objects to a file, then you'll need to implement a tap. So what <em>do</em> you want to do?</p></div><div id="comment-15053-info" class="comment-info"><span class="comment-age">(17 Oct '12, 04:05)</span> Jaap ♦</div></div></div><div id="comment-tools-15025" class="comment-tools"></div><div class="clear"></div><div id="comment-15025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

