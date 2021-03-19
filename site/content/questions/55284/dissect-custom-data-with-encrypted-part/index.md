+++
type = "question"
title = "dissect custom data with encrypted part"
description = '''Hello, I&#x27;m developing a custom packet dissector. Lets say we have a 64 byte packet to dissect and bytes 16 to 32 are encrypted, what is the right way to display this data ? Today I have something working like that but I want to have a clean code proto_tree_add_item( //the encrypted data displayed as...'''
date = "2016-09-02T04:41:00Z"
lastmod = "2016-09-02T04:41:00Z"
weight = 55284
keywords = [ "dissector", "wireshark2.2", "display", "custom" ]
aliases = [ "/questions/55284" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dissect custom data with encrypted part](/questions/55284/dissect-custom-data-with-encrypted-part)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55284-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm developing a custom packet dissector. Lets say we have a 64 byte packet to dissect and bytes 16 to 32 are encrypted, what is the right way to display this data ?</p><p>Today I have something working like that but I want to have a clean code</p><pre><code>proto_tree_add_item( //the encrypted data displayed as is 
offset += 16
dec_buffer = decryptData() //decrypted data are in a buffer 
payload_tvb = tvb_new_child_real_data(tvb, dec_buffer, 16, 16);
add_new_data_source(pinfo, payload_tvb, &quot;Decrypted Data&quot;);</code></pre><p>What protocol dissector may I use as example ?</p></div><div id="question-tags" class="tags-container tags">dissector wireshark2.2 display custom</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '16, 04:41</strong></p><img src="https://secure.gravatar.com/avatar/195c8bfd4768041efdfdd094508cc2bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="atsju2&#39;s gravatar image" /><p>atsju2<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="atsju2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Sep '16, 04:42</p></div></div><div id="comments-container-55284" class="comments-container"></div><div id="comment-tools-55284" class="comment-tools"></div><div class="clear"></div><div id="comment-55284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

