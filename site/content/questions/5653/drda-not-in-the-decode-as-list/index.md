+++
type = "question"
title = "DRDA not in the &quot;Decode As&quot; list?"
description = '''Hello, I&#x27;m trying to decode some DB2 traffic, but I&#x27;m not finding a decode. It looks like there used to be a DRDA entry, but I don&#x27;t see it on 1.6.1 (windows). Thanks for any info.'''
date = "2011-08-11T10:11:00Z"
lastmod = "2011-08-11T20:36:00Z"
weight = 5653
keywords = [ "db2" ]
aliases = [ "/questions/5653" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DRDA not in the "Decode As" list?](/questions/5653/drda-not-in-the-decode-as-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5653-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm trying to decode some DB2 traffic, but I'm not finding a decode. It looks like there used to be a DRDA entry, but I don't see it on 1.6.1 (windows). Thanks for any info.</p></div><div id="question-tags" class="tags-container tags">db2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '11, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/204826a40764946ae1f19e386a7e8f54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RickE&#39;s gravatar image" /><p>RickE<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RickE has no accepted answers">0%</span></p></div></div><div id="comments-container-5653" class="comments-container"></div><div id="comment-tools-5653" class="comment-tools"></div><div class="clear"></div><div id="comment-5653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5665"></span>

<div id="answer-container-5665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5665-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure what you mean by "used to be a DRDA entry". Where ?</p><p>The DRDA dissector is a heuristic dissector riding on top of TCP. This means that it is in the list of heuristic dissectors called in turn by the TCP dissector. Each dissector does a heuristic test of the TCP payload data to see if the dissector considers the payload to be valid for that dissector. The TCP dissector can call the heuristic dissectors before or after checking for TCP port protocol mappings.</p><p>So: One possibility: The TCP payload is being dissected as something other than DRDA because of a TCP port mapping to a protocol. If the TCP preference "try heuristic dissectors first" is not set, you might try setting that preference and see what happens.</p><p>Another possibility: another dissector in the TCP heuristic dissector list before the DRDA dissector "accepts" the data for dissection.</p><p>If this is the case, try disabling the other protocol (Analyze ! Enabled Protocols)</p><p>Another possibility: The TCP payload data doesn't match the heuristic used by the DRDA dissector. If you're convinced that the data should be dissected as DRDA, you can file a bug report at bugs.wireshark.org attaching a (small) capture file showing the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '11, 20:36</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Aug '11, 20:40</p></div></div><div id="comments-container-5665" class="comments-container"><span id="5684"></span><div id="comment-5684" class="comment"><div id="post-5684-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. I enabled heuristic dissectors, but it didn't change - the Protocol classified as TCP. The traffic is from a MS SQL Server to DB2 on a mainframe. When I google those terms, they lead to pages that describe how to decode DRDA with Wireshark to analyze the traffic. In those, they show DRDA listed as the protocol. I can see DRDA listed under Preferences-&gt;Protocols, but I don't see it listed when I try to force a "Decode As".</p></div><div id="comment-5684-info" class="comment-info"><span class="comment-age">(12 Aug '11, 08:57)</span> RickE</div></div><span id="5685"></span><div id="comment-5685" class="comment"><div id="post-5685-score" class="comment-score"></div><div class="comment-text"><p>(I converted your answer to a comment to conform to the way ask.wireshark.org is intended to be used. See the FAQ).</p></div><div id="comment-5685-info" class="comment-info"><span class="comment-age">(12 Aug '11, 09:23)</span> Bill Meier ♦♦</div></div><span id="5686"></span><div id="comment-5686" class="comment"><div id="post-5686-score" class="comment-score"></div><div class="comment-text"><p>ask.wireshark.org is not really suited for a discussion. (FAQ) This is a discussion forum, right? "No. This is a Q&amp;A site. Answers move up and down depending on votes. If you treat it like a traditional time-descending web forum things can get very confusing."</p><p>Maybe the best way to resolve this issue is for you to submit a bug at bugs.wireshark.org attaching a (small) capture file which shows the issue. If needed, you can mark the file as "private" so that only the Wireshark core developers have access.</p><p>Otherwise please use the mail list [email protected] for further discussion.</p></div><div id="comment-5686-info" class="comment-info"><span class="comment-age">(12 Aug '11, 09:32)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-5665" class="comment-tools"></div><div class="clear"></div><div id="comment-5665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

