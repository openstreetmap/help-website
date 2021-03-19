+++
type = "question"
title = "Custom dissector for LLC Payload in Lua"
description = '''Hi, I&#x27;d like to preface this by stating that this is my first time making a dissector in Lua (or really working in Wireshark for that matter) so if anything is unclear I&#x27;d be more than happy to clarify. My goal is to make a custom dissector for a protocol on top of SNAP LLC frames. Since the protoco...'''
date = "2017-02-10T07:12:00Z"
lastmod = "2017-02-10T07:12:00Z"
weight = 59326
keywords = [ "chained-dissector", "lua", "dissector", "llc" ]
aliases = [ "/questions/59326" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Custom dissector for LLC Payload in Lua](/questions/59326/custom-dissector-for-llc-payload-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59326-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'd like to preface this by stating that this is my first time making a dissector in Lua (or really working in Wireshark for that matter) so if anything is unclear I'd be more than happy to clarify. My goal is to make a custom dissector for a protocol on top of SNAP LLC frames. Since the protocol info is currently dissected as "data," it seems that a chained dissector is appropriate. Using <a href="https://delog.wordpress.com/2010/09/27/create-a-wireshark-dissector-in-lua/">https://delog.wordpress.com/2010/09/27/create-a-wireshark-dissector-in-lua/</a> as a guide, I have created the following:</p><pre><code>iiot = Proto(&quot;myproto&quot;, &quot;My Protocol&quot;)

local f_type = ProtoField.new(&quot;Type Value&quot;, &quot;myproto.type&quot;,  ftypes.UINT16, nil, base.HEX)
local f_data = ProtoField.string(&quot;Data&quot;, &quot;myproto.data&quot;, FT_STRING)

iiot.fields = { f_type, f_data }

function iiot.dissector(buf, pkt, root)

     pkt.cols.protocol:set(&quot;IIOT&quot;)

     local pktlen_remaining = buf:reported_length_remaining()

     local tree = root:add(iiot, buf:range(0, pktlen_remaining))

     tree:add(f_type, buf:range(0, 2))

     local typeid = buf:range(0, 2)
     pkt.cols.info:set(&quot;(&quot;.. typeid ..&quot;)&quot;)

     pktlen_remaining = pktlen_remaining - 2

     tree:add(f_data, buf:range(2, pktlen_remaining))

     local data = buf:range(2, pktlen_remaining)
     pkt.cols.info:set(&quot;(&quot;.. data ..&quot;)&quot;)

end

local llc_dissector_table = DissectorTable.get(&quot;llc.dsap&quot;)
dissector = llc_dissector_table:get_dissector(170)
llc_dissector_table:add(170, iiot)</code></pre><p>I suppose my question is two-fold. At present, my dissector loads and I can filter by "myiiot". However, I am unable to dissect my packets using the "Decode As..." window. Since my packets are 0xaa SNAP, shouldn't they automatically be dissected by my script? Is there a way to do this manually assuming the code is correct? Apologies if I am missing something obvious.</p><p><img src="http://i.imgur.com/qGojiaL.png" alt="alt text" /></p><p>edit: Here is a CloudShark link for the capture <a href="https://www.cloudshark.org/captures/fef0e7fd73d3">https://www.cloudshark.org/captures/fef0e7fd73d3</a></p></div><div id="question-tags" class="tags-container tags">chained-dissector lua dissector llc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '17, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/134bbb4fd9687f9718bb94d36c4b75fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brownfox&#39;s gravatar image" /><p>brownfox<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brownfox has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '17, 11:44</p></div></div><div id="comments-container-59326" class="comments-container"><span id="59330"></span><div id="comment-59330" class="comment"><div id="post-59330-score" class="comment-score"></div><div class="comment-text"><p>Can you share the capture that generated the screenshot in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc. so others can test the script?</p></div><div id="comment-59330-info" class="comment-info"><span class="comment-age">(10 Feb '17, 07:37)</span> grahamb ♦</div></div><span id="60582"></span><div id="comment-60582" class="comment"><div id="post-60582-score" class="comment-score"></div><div class="comment-text"><p>did you find a solution? I am currently working on something similar</p></div><div id="comment-60582-info" class="comment-info"><span class="comment-age">(05 Apr '17, 00:50)</span> nikdubois</div></div></div><div id="comment-tools-59326" class="comment-tools"></div><div class="clear"></div><div id="comment-59326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

