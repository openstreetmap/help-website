+++
type = "question"
title = "prot_register_field_array error"
description = '''Hello all, i just updated a custom plugin to wireshark version 1.12. This plugin worked fine until version 1.11. So I compiled wireshark version 1.12 and used the new sources to build the plugin. But when I try to start Wireshark with this plugin, it always crashes at startup. It seems to be a probl...'''
date = "2014-09-04T00:24:00Z"
lastmod = "2014-09-04T00:24:00Z"
weight = 35987
keywords = [ "startup", "crash" ]
aliases = [ "/questions/35987" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [prot\_register\_field\_array error](/questions/35987/prot_register_field_array-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35987-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>i just updated a custom plugin to wireshark version 1.12. This plugin worked fine until version 1.11. So I compiled wireshark version 1.12 and used the new sources to build the plugin.</p><p>But when I try to start Wireshark with this plugin, it always crashes at startup. It seems to be a problem with proto_register_field_array. When I remove this function from the code, wireshark starts.</p><p>The code looks like that:</p><pre><code>static hf\_register\_info hf[] = {
{ &amp;hf\_prio,
{   &quot;PRIO-Bit&quot; , &quot;iec104.prio&quot;, FT\_UINT8,BASE\_DEC,NULL,0x0,
     &quot;&quot;, HFILL}},  
{ &amp;hf_serial2,
{   &quot;Serial&quot; , &quot;iec104.serial2&quot;, FT\_UINT32,BASE\_DEC,NULL,0x0,
     &quot;&quot;, HFILL}},
}

proto_iec104 = proto_register_protocol(DECODERNAME, DECODERNAMEPREFS, DECODERKURZNAME);
proto_register_field_array(proto_iec104, hf, array_length(hf));</code></pre><p>I am using Windows 7 64-bit.</p><p>Do I have to use another function instead of proto_register_field_array? Or maybe is there a known bug with this function?</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags">startup crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '14, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/128b142c3a9292444f555b1aad741960?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dranigl&#39;s gravatar image" /><p>dranigl<br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dranigl has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Sep '14, 06:29</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-35987" class="comments-container"><span id="35994"></span><div id="comment-35994" class="comment"><div id="post-35994-score" class="comment-score"></div><div class="comment-text"><p>Try replacing the empty string "" with null.</p></div><div id="comment-35994-info" class="comment-info"><span class="comment-age">(04 Sep '14, 02:25)</span> Anders ♦</div></div><span id="36002"></span><div id="comment-36002" class="comment"><div id="post-36002-score" class="comment-score"></div><div class="comment-text"><p>You might also want to try running tools/checkhf.pl and tools/checkAPIs.pl on your code: they might point out what's wrong with your hf array.</p></div><div id="comment-36002-info" class="comment-info"><span class="comment-age">(04 Sep '14, 06:31)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-35987" class="comment-tools"></div><div class="clear"></div><div id="comment-35987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

