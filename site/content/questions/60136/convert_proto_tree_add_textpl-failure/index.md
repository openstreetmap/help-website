+++
type = "question"
title = "convert_proto_tree_add_text.pl failure"
description = ''' I am trying to use convert_proto_tree_add_text.pl for a dissector that has:   proto_tree_add_text(tl_tree, tvb, offset, -1,  &quot;Data (%d bytes)&quot;, tvb_reported_length_remaining(tvb, offset)); generate gave me: 1;1;tl_tree;hf_tl_data_(%d_bytes)&quot;;tvb;offset;-1;encoding;Data (%d bytes)&quot;;fieldtype;tl.data...'''
date = "2017-03-16T21:27:00Z"
lastmod = "2017-03-16T21:27:00Z"
weight = 60136
keywords = [ "conversion" ]
aliases = [ "/questions/60136" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [convert\_proto\_tree\_add\_text.pl failure](/questions/60136/convert_proto_tree_add_textpl-failure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60136-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><ol><li>I am trying to use convert_proto_tree_add_text.pl for a dissector that has:<br />
</li></ol><p>proto_tree_add_text(tl_tree, tvb, offset, -1, "Data (%d bytes)", tvb_reported_length_remaining(tvb, offset));</p><p>generate gave me:</p><p>1;1;tl_tree;hf_tl_data_(%d_bytes)";tvb;offset;-1;encoding;Data (%d bytes)";fieldtype;tl.data_(%d_bytes)";BASE_DEC;NULL;0x0</p><p>however fixall fails:</p><p>C:\Development\wireshark\tools&gt;convert_proto_tree_add_text.pl ../epan/dissectors /packet-tl.c --action=fix-all --encoding=ENC_BIG_ENDIAN</p><p>1: Encoding value 'encoding' unknown!</p><p>1: Field type 'fieldtype' unknown! Aborting conversion.</p><p>Should the replacement be like: proto_tree_add_item(tl_tree, hf_tl_data, tvb, offset, -1, ENC_BIG_ENDIAN);</p><pre><code>{&amp;hf_tl_data,
{ &quot;Data&quot;, &quot;tl.data&quot;,  
FT_UINT16, BASE_DEC, NULL, 0x0,
&quot;Data&quot;, HFILL } }</code></pre><p>I am not sure what the FT value should be here.</p><p>2.When debugging using printf, how to I get the console when using windows interface. In 2.x wireshark version I am not seeing the "open console" option.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">conversion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '17, 21:27</strong></p><img src="https://secure.gravatar.com/avatar/93a0fe758f88fad43c2ac5d1528f4ec9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erin&#39;s gravatar image" /><p>erin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-60136" class="comments-container"><span id="60137"></span><div id="comment-60137" class="comment"><div id="post-60137-score" class="comment-score"></div><div class="comment-text"><p>Under advanced , found the gui.console_open and updated it to Always. However console level log is set to 28 by default. Will prints show up on console with this logging level?</p></div><div id="comment-60137-info" class="comment-info"><span class="comment-age">(16 Mar '17, 22:06)</span> erin</div></div></div><div id="comment-tools-60136" class="comment-tools"></div><div class="clear"></div><div id="comment-60136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

