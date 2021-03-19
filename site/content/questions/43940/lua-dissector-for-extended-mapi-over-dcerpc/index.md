+++
type = "question"
title = "Lua Dissector for Extended MAPI over DCE/RPC"
description = '''I&#x27;m trying to write a dissector to decode &quot;MAPI Extended&quot; over DCE/RPC. From my reading I believe that I need to register my dissector with the &quot;dcerpc&quot; DissectorTable. I found in the dcerpc code a comment reading &quot;XXX - DCE/RPC doesn&#x27;t have a true (sub)dissector table, so provide a &quot;fake&quot; one to fi...'''
date = "2015-07-07T13:45:00Z"
lastmod = "2015-07-07T14:57:00Z"
weight = 43940
keywords = [ "lua", "dcerpc", "dissector", "wireshark" ]
aliases = [ "/questions/43940" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Lua Dissector for Extended MAPI over DCE/RPC](/questions/43940/lua-dissector-for-extended-mapi-over-dcerpc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43940-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to write a dissector to decode "MAPI Extended" over DCE/RPC.</p><p>From my reading I believe that I need to register my dissector with the "dcerpc" DissectorTable.</p><p>I found in the dcerpc code a comment reading "XXX - DCE/RPC doesn't have a true (sub)dissector table, so provide a "fake" one to fit the Decode As algorithm". This leads me to believe that I register my dissector like this:</p><pre><code>local dis_table = DissectorTable.get(&quot;dcerpc.fake&quot;)</code></pre><p>However when launching tshark or wireshark I get the error:</p><pre><code>dis.lua:30: bad argument #1 to &#39;get&#39; (DissectorTable_get: no such dissector_table)</code></pre><p>Any Recommendations?</p></div><div id="question-tags" class="tags-container tags">lua dcerpc dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '15, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/1eb79f4883fab86171d353463aed2332?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="techplex&#39;s gravatar image" /><p>techplex<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="techplex has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jul '15, 14:58</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-43940" class="comments-container"></div><div id="comment-tools-43940" class="comment-tools"></div><div class="clear"></div><div id="comment-43940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43943"></span>

<div id="answer-container-43943" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43943-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>My recommendation is that you don't try to write it in Lua.</p><p>The types of "true" dissector tables in Wireshark either switch off of an integral value or a string value. DCE/RPC protocols must register using a UUID, <em>and</em> they require a bunch of individual operation dissectors to be registered, not just a single dissector.</p><p>So DCE/RPC dissectors (and ONC RPC dissectors) are <em>quite</em> different, when it comes to registration, from "regular" dissectors, and we don't have support for Lua DCE/RPC (or ONC RPC) dissectors, and are unlikely to have them in the near future (it'd be a significant amount of work).</p><p>The <em>good</em> news is that <a href="http://www.samba.org/">Samba</a> has a DCE/RPC IDL (I think it's more like Microsoft's IDL than the OSF's IDL, although Microsoft's might have been at least influenced by OSF's) and <a href="https://wiki.wireshark.org/Pidl">a tool to generate Samba code and Wireshark dissectors from it</a>. You should look at getting an IDL description of Extended MAPI, converting it to PIDL form, and using the PIDL tool to generate the dissector. The bad news is that you'll need to compile code; the good news is that you probably won't have to <em>write</em> most of that code - the PIDL tool should do that for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '15, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-43943" class="comments-container"><span id="43946"></span><div id="comment-43946" class="comment"><div id="post-43946-score" class="comment-score"></div><div class="comment-text"><p>Sweet, sounds good. I think this is the IDL I need: <a href="https://msdn.microsoft.com/en-us/library/ee217991(v=exchg.80).aspx">https://msdn.microsoft.com/en-us/library/ee217991(v=exchg.80).aspx</a> Do you think this is something that should be sent in as a patch? MAPI Extended is what Exchange/Outlook use today(if they aren't using MAPI/HTTP).</p></div><div id="comment-43946-info" class="comment-info"><span class="comment-age">(07 Jul '15, 15:08)</span> techplex</div></div><span id="43947"></span><div id="comment-43947" class="comment"><div id="post-43947-score" class="comment-score"></div><div class="comment-text"><p>It's probably the right place to start, although you might have to modify it to make it a valid PIDL IDL file. See epan/dissectors/pidl for examples of PIDL files and the corresponding "conformance" files (the .cnf files).</p><p>If you get this working, please do submit it for inclusion in Wireshark. See the <a href="https://wiki.wireshark.org/Development/SubmittingPatches">SubmittingPatches</a> page for information on how to do so. If you have captures with which to test the page, file an enhancement request on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a> for your new dissector, attach your captures to it, and, at the end of the commit message, put "Bug: {the bug number}", on a line by itself, after a blank line.</p></div><div id="comment-43947-info" class="comment-info"><span class="comment-age">(07 Jul '15, 15:48)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-43943" class="comment-tools"></div><div class="clear"></div><div id="comment-43943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

