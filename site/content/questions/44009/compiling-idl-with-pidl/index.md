+++
type = "question"
title = "Compiling IDL with PIDL"
description = '''As a followup to https://ask.wireshark.org/questions/43940/lua-dissector-for-extended-mapi-over-dcerpc Related to https://ask.wireshark.org/questions/27244/mapi-unknown-operation-10-11-request-response I found the IDL file provided by microsoft here: https://msdn.microsoft.com/en-us/library/ee217991...'''
date = "2015-07-09T07:18:00Z"
lastmod = "2015-07-09T07:18:00Z"
weight = 44009
keywords = [ "wireshark", "pidl", "dcerpc" ]
aliases = [ "/questions/44009" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Compiling IDL with PIDL](/questions/44009/compiling-idl-with-pidl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As a followup to <a href="https://ask.wireshark.org/questions/43940/lua-dissector-for-extended-mapi-over-dcerpc">https://ask.wireshark.org/questions/43940/lua-dissector-for-extended-mapi-over-dcerpc</a><br />
Related to <a href="https://ask.wireshark.org/questions/27244/mapi-unknown-operation-10-11-request-response">https://ask.wireshark.org/questions/27244/mapi-unknown-operation-10-11-request-response</a></p><p>I found the IDL file provided by microsoft here:<br />
<a href="https://msdn.microsoft.com/en-us/library/ee217991(v=exchg.80).aspx">https://msdn.microsoft.com/en-us/library/ee217991(v=exchg.80).aspx</a><br />
The needed import IDL (ms-rpce.idl) is here:<br />
<a href="https://msdn.microsoft.com/en-us/library/cc243865.aspx">https://msdn.microsoft.com/en-us/library/cc243865.aspx</a></p><p>I had to slightly modify the IDL files in order for PIDL to compile them, here are the modified versions: <a href="https://gist.github.com/TechplexEngineer/a993f55fe1587b7642cd">https://gist.github.com/TechplexEngineer/a993f55fe1587b7642cd</a></p><p>I have combined them and attempted to compile them with the pidl tool in the Wireshark source. With this command:<br />
<code>../../../tools/pidl/pidl --includedir . --ws-parser -- ms-oxcrpc.idl</code></p><p>The result of the above command is an error: <code>Can't use an undefined value as a subroutine reference at /wireshark/tools/pidl/lib/Parse/Pidl/Wireshark/NDR.pm line 868.</code></p><p>Any ideas?</p><p>What goes in the conformance files? Is there documentation I am not finding on this?</p></div><div id="question-tags" class="tags-container tags">wireshark pidl dcerpc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '15, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/1eb79f4883fab86171d353463aed2332?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="techplex&#39;s gravatar image" /><p>techplex<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="techplex has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '15, 07:18</p></div></div><div id="comments-container-44009" class="comments-container"></div><div id="comment-tools-44009" class="comment-tools"></div><div class="clear"></div><div id="comment-44009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

