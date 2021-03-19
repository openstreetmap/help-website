+++
type = "question"
title = "updating windows plugin from wireshark 1.6 to 2.2"
description = '''Hello dear Wireshark Exprets, after trying to update the plugin by myself and removing as much error as I can, I am stuck with These Errors and don&#x27;t know what to do with These. I&#x27;d really appreciate your help. Thanks in advance  &quot;C:&#92;Temp&#92;_temp_setupFiles&#92;Development&#92;wsbuild32&#92;plugins&#92;myPlugin&#92;myPlu...'''
date = "2016-11-28T06:27:00Z"
lastmod = "2017-03-01T01:13:00Z"
weight = 57681
keywords = [ "windows", "apichange", "dissector", "updateplugin", "plugin" ]
aliases = [ "/questions/57681" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [updating windows plugin from wireshark 1.6 to 2.2](/questions/57681/updating-windows-plugin-from-wireshark-16-to-22)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57681-score" class="post-score" title="current number of votes">0</div><span id="post-57681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello dear Wireshark Exprets,</p><p>after trying to update the plugin by myself and removing as much error as I can, I am stuck with These Errors and don't know what to do with These. I'd really appreciate your help. Thanks in advance</p><pre><code>   &quot;C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj&quot; (Standardziel) (140) -&gt;
   (Link Ziel) -&gt; 
     packet-myPlugin.obj : error LNK2005: _plugin_reg_handoff already defined in plugin.obj [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     packet-myPlugin.obj : error LNK2005: _plugin_register already defined in plugin.obj [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     plugin.obj : error LNK2019: unresolved external symbol _proto_register_myPlugin referenced in function _plugin_register [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     plugin.obj : error LNK2019: unresolved external symbol _proto_reg_handoff_myPlugin referenced in function _plugin_reg_handoff [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     packet-myPlugin.obj : error LNK2019: unresolved external symbol _match_strval referenced in function _dissector_ife [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     packet-myPlugin.obj : error LNK2019: unresolved external symbol _ADDRESSES_EQUAL referenced in function _dissector_ife [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     packet-myPlugin.obj : error LNK2019: unresolved external symbol _se_alloc referenced in function _dissector_ife [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     packet-myPlugin.obj : error LNK2019: unresolved external symbol _proto_tree_add_text referenced in function _dissector_ife [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     packet-myPlugin.obj : error LNK2019: unresolved external symbol _snprintf referenced in function _dissector_ife [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     packet-myPlugin.obj : error LNK2019: unresolved external symbol _ep_strdup_printf referenced in function _dissector_ife [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     packet-myPlugin.obj : error LNK2019: unresolved external symbol _tvb_get_ephemeral_string referenced in function _dissector_ife [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     packet-myPlugin.obj : error LNK2019: unresolved external symbol _tvb_get_string referenced in function _dissector_ife [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]
     C:\Temp\_temp_setupFiles\Development\wsbuild32\run\RelWithDebInfo\plugins\myPlugin.dll : fatal error LNK1120: 10 unresolved externals [C:\Temp\_temp_setupFiles\Development\wsbuild32\plugins\myPlugin\myPlugin.vcxproj]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-apichange" rel="tag" title="see questions tagged &#39;apichange&#39;">apichange</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-updateplugin" rel="tag" title="see questions tagged &#39;updateplugin&#39;">updateplugin</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '16, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p><span>xaheen</span><br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Nov '16, 18:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-57681" class="comments-container"><span id="57684"></span><div id="comment-57684" class="comment"><div id="post-57684-score" class="comment-score">1</div><div class="comment-text"><p>So you are looking at the following functions:</p><pre><code>match_strval()
ADDRESSES_EQUAL()
se_alloc()
proto_tree_add_text()
snprintf()
ep_strdup_printf()
tvb_get_ephemeral_string()
tvb_get_string()</code></pre></div><div id="comment-57684-info" class="comment-info"><span class="comment-age">(28 Nov '16, 11:16)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="57696"></span><div id="comment-57696" class="comment"><div id="post-57696-score" class="comment-score"></div><div class="comment-text"><p><span>@jaap</span> thanks for your reply. Which functions should I use instead of these functions?</p></div><div id="comment-57696-info" class="comment-info"><span class="comment-age">(29 Nov '16, 04:09)</span> <span class="comment-user userinfo">xaheen</span></div></div><span id="57699"></span><div id="comment-57699" class="comment"><div id="post-57699-score" class="comment-score">1</div><div class="comment-text"><p>In addition to the above you need to change the plugin_reg_handoff() to proto_reg_handof_foo. eg the same handoff and register functions are used in plugins as in regular dissectors. You should probably look at the(c)make files of plugin in the current code base. ep and se memory has been replaced by wmem you can look up the usage of those funktions in the docs and or the code base.</p></div><div id="comment-57699-info" class="comment-info"><span class="comment-age">(29 Nov '16, 05:16)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="57701"></span><div id="comment-57701" class="comment"><div id="post-57701-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys :)</p></div><div id="comment-57701-info" class="comment-info"><span class="comment-age">(29 Nov '16, 05:22)</span> <span class="comment-user userinfo">xaheen</span></div></div></div><div id="comment-tools-57681" class="comment-tools"></div><div class="clear"></div><div id="comment-57681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57698"></span>

<div id="answer-container-57698" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57698-score" class="post-score" title="current number of votes">1</div><span id="post-57698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xaheen has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code>match_strval -&gt; try_val_to_str
ADDRESSES_EQUAL -&gt; addresses_equal
se_alloc(XXX) -&gt; wmem_alloc(wmem_file_scope(), XXX)
proto_tree_add_text -&gt; must be replaced by the proper proto_tree_add_XXX function depending on your use case
ep_strdup_printf(XXX) -&gt; wmem_strdup(wmem_packet_scope(), XXX)
tvb_get_ephemeral_string(XXX) -&gt; tvb_get_string_enc(wmem_packet_scope(), XXX, ENC_UTF_8|ENC_NA)
tvb_get_string(XXX) -&gt; tvb_get_string_enc(NULL, XXX, ENC_UTF_8|ENC_NA)</code></pre><p>As for snprintf(), this is a standard C function and not a Wireshark API.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '16, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-57698" class="comments-container"><span id="57700"></span><div id="comment-57700" class="comment"><div id="post-57700-score" class="comment-score"></div><div class="comment-text"><p>Thanks a bunch for saving my day :D</p></div><div id="comment-57700-info" class="comment-info"><span class="comment-age">(29 Nov '16, 05:21)</span> <span class="comment-user userinfo">xaheen</span></div></div><span id="57714"></span><div id="comment-57714" class="comment"><div id="post-57714-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>As for snprintf(), this is a standard C function</p></blockquote><p>It's a standard C99 function, but not a standard C89 function, and older versions of Microsoft Visual Studio don't provide it.</p><p>In Wireshark 2.2 and later, you can include <code>&lt;wsutil/ws_printf.h&gt;</code> and use <code>ws_snprintf()</code> instead of <code>snprintf()</code>; it should work on UN*X and it should also work on Windows with all versions of Visual Studio that we support.</p></div><div id="comment-57714-info" class="comment-info"><span class="comment-age">(29 Nov '16, 14:52)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="59755"></span><div id="comment-59755" class="comment"><div id="post-59755-score" class="comment-score"></div><div class="comment-text"><p>ep_strdup_printf(XXX) -&gt; wmem_strdup(wmem_packet_scope(), XXX) didnt work for me.</p><p>wmem_strdup_printf(wmem_packet_scope(), XXX) worked perfectly</p></div><div id="comment-59755-info" class="comment-info"><span class="comment-age">(01 Mar '17, 01:13)</span> <span class="comment-user userinfo">xaheen</span></div></div></div><div id="comment-tools-57698" class="comment-tools"></div><div class="clear"></div><div id="comment-57698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

