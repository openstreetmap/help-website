+++
type = "question"
title = "RTP Plugin | Possible to create |"
description = '''Hello, I have a question to write a Plugin in Wireshark. I have a RTP Protkoll, where I have Header Extensions. Now I have download and build Wireshark. I have add to this Wireshark Version with my RTP Extensions. Now the RTP Header are really good shown my Extensions. I can build an Installer and s...'''
date = "2014-04-17T01:18:00Z"
lastmod = "2014-04-17T06:42:00Z"
weight = 31913
keywords = [ "rtp", "plugin" ]
aliases = [ "/questions/31913" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RTP Plugin | Possible to create |](/questions/31913/rtp-plugin-possible-to-create)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31913-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a question to write a Plugin in Wireshark. I have a RTP Protkoll, where I have Header Extensions. Now I have download and build Wireshark. I have add to this Wireshark Version with my RTP Extensions. Now the RTP Header are really good shown my Extensions. I can build an Installer and so on.</p><p>Now I would like to create a Plugin. So that I can use every Wireshark Version with my RTP- Extensions. The problem is. I have not found an example how I can create a Plugin to an existing Protokoll. Is that Possible ? When yes, can you show me an example to start.</p><p>Thanks a lot.</p></div><div id="question-tags" class="tags-container tags">rtp plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '14, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/3378e4af34b02834b98e8a896efe303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alias_alias&#39;s gravatar image" /><p>Alias_alias<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alias_alias has no accepted answers">0%</span></p></div></div><div id="comments-container-31913" class="comments-container"></div><div id="comment-tools-31913" class="comment-tools"></div><div class="clear"></div><div id="comment-31913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31927"></span>

<div id="answer-container-31927" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31927-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're not creating a plugin replacing an existing protocol, you're trying to extend/build on top of an existing protocol. This is something very normal, heck the core principle of how dissectors are stacked.</p><p>What you need to find out is how a dissector exports a hook to which you can register for your specific protocol. If you look in <code>packet-rtp</code> you'll see that when an RTP extension is found (in <code>rtp_hdr_ext_dissector_table</code>) it tries to call any registered subdissector for that extension. It uses the dissectors registered at table <code>rtp.hdr_ext</code>. This is basically not different from the HTML dissector registering itself for tcp.port 80.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '14, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-31927" class="comments-container"><span id="31930"></span><div id="comment-31930" class="comment"><div id="post-31930-score" class="comment-score"></div><div class="comment-text"><p>I should have looked in the code ;-)</p></div><div id="comment-31930-info" class="comment-info"><span class="comment-age">(17 Apr '14, 07:08)</span> Anders ♦</div></div><span id="32063"></span><div id="comment-32063" class="comment"><div id="post-32063-score" class="comment-score"></div><div class="comment-text"><p>First thanks. You understand what I would like to do.</p><p>The Problem for me is that i don't have any Idea how to do that. I would like that my extensions only start when the Protokoll is : static const value_string rtp_payload_type_vals[] = { PT_UNDF_100, "DynamicRTP-Type-100" },</p><p>So what i have make ....</p><p>.... if( rtp_info-&gt;info_payload_type == 0x100 ) { ... proto_tree_add_item(rtp_tree, hf_rtp_hdr_exts, tvb, hdrext_offset_rd, (hdr_extension_len * 4 - 4), ENC_NA) } ...</p><p>how now can i make a plugin please give me a example for any protokoll</p></div><div id="comment-32063-info" class="comment-info"><span class="comment-age">(22 Apr '14, 09:16)</span> Alias_alias</div></div><span id="32143"></span><div id="comment-32143" class="comment"><div id="post-32143-score" class="comment-score"></div><div class="comment-text"><p>There is a significant difference in RTP header extensions and RTP payload types. From what I read here I assume that your header extension is only applicable when the RTP payload type is 100 (=0x64 !!). Currently I don't have an example protocol at hand. I would have to fake one.</p></div><div id="comment-32143-info" class="comment-info"><span class="comment-age">(24 Apr '14, 04:23)</span> Jaap ♦</div></div></div><div id="comment-tools-31927" class="comment-tools"></div><div class="clear"></div><div id="comment-31927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31914"></span>

<div id="answer-container-31914" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31914-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.plugins">README.plugins</a> in the doc directory of the source?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '14, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-31914" class="comments-container"><span id="31919"></span><div id="comment-31919" class="comment"><div id="post-31919-score" class="comment-score"></div><div class="comment-text"><p>yes but i don't find my problem there.</p></div><div id="comment-31919-info" class="comment-info"><span class="comment-age">(17 Apr '14, 03:27)</span> Alias_alias</div></div><span id="31920"></span><div id="comment-31920" class="comment"><div id="post-31920-score" class="comment-score"></div><div class="comment-text"><p>So what have you tried, and what is your problem?</p><p>README.plugin tells you exactly what you need to do to take your built-in dissector and make a plugin dissector.</p><p>Are you also aware that your plugin is unlikely to work across different versions of Wireshark. You may end up having to make multiple versions of your plugin.</p><p>Are you also aware that if you distribute your modified version of Wireshark or your plugin to others then as per the GPL licence you must offer the source code for your changes?</p></div><div id="comment-31920-info" class="comment-info"><span class="comment-age">(17 Apr '14, 03:47)</span> grahamb ♦</div></div><span id="31924"></span><div id="comment-31924" class="comment"><div id="post-31924-score" class="comment-score"></div><div class="comment-text"><p>As you ar replacing the existing RTP dissector with yours you are probably better off building a custom installer and use that. I suppose your extensions are non standard ones otherwise you should offer your code to the Wireshark project. If they need to be private you might want to look into the posibillities of hooking into the existing dissector rather than replacing it. As it stands you will have to reapply your changes every time packet-rtp.c is updated if you want to stay current.</p></div><div id="comment-31924-info" class="comment-info"><span class="comment-age">(17 Apr '14, 04:31)</span> Anders ♦</div></div></div><div id="comment-tools-31914" class="comment-tools"></div><div class="clear"></div><div id="comment-31914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

