+++
type = "question"
title = "Crash in custom plugin"
description = '''I added the following to my dissector to make use of wireshark&#x27;s xml dissector: static dissector_handle_t xml_handle; xml_handle = find_dissector(&quot;xml&quot;); call_dissector_only(xml_handle, xml_tvb, pinfo, tree, NULL);  But now I am getting the following error whenever I capture a packet that makes the ...'''
date = "2015-05-26T11:47:00Z"
lastmod = "2015-05-26T11:47:00Z"
weight = 42668
keywords = [ "xml", "error", "wirehsark", "bug" ]
aliases = [ "/questions/42668" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Crash in custom plugin](/questions/42668/crash-in-custom-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42668-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I added the following to my dissector to make use of wireshark's xml dissector:</p><pre><code>static dissector_handle_t xml_handle;
xml_handle = find_dissector(&quot;xml&quot;);
call_dissector_only(xml_handle, xml_tvb, pinfo, tree, NULL);</code></pre><p>But now I am getting the following error whenever I capture a packet that makes the code execute:</p><p><strong>"This application has requested the Runtime to terminate it in an unusal way."</strong></p></div><div id="question-tags" class="tags-container tags">xml error wirehsark bug</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '15, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/42f084d62348c04d00bd67b129116cc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XQW1123&#39;s gravatar image" /><p>XQW1123<br />
<span class="score" title="46 reputation points">46</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XQW1123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 May '15, 01:08</p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span></p></div></div><div id="comments-container-42668" class="comments-container"><span id="42692"></span><div id="comment-42692" class="comment"><div id="post-42692-score" class="comment-score"></div><div class="comment-text"><p>It depends on where you've placed these calls. Can you elaborate on that? Whats the value of xml_handle after the function call?</p></div><div id="comment-42692-info" class="comment-info"><span class="comment-age">(27 May '15, 00:10)</span> Jaap ♦</div></div></div><div id="comment-tools-42668" class="comment-tools"></div><div class="clear"></div><div id="comment-42668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

