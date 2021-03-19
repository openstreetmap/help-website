+++
type = "question"
title = "Unpacking sub-packets (recursive dissection?)"
description = '''I&#x27;m looking at a protocol which may &quot;glue together&quot; multiple packets in arbitrary ways... So in essence a single &quot;frame&quot; of data has a 1:N relationship to packets it contains. Is it possible to attack something like this in a recursive type fashion by re-starting dissection on any remaining data aft...'''
date = "2017-06-13T14:44:00Z"
lastmod = "2017-06-14T06:54:00Z"
weight = 61994
keywords = [ "dissector", "post-dissector", "dissection" ]
aliases = [ "/questions/61994" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Unpacking sub-packets (recursive dissection?)](/questions/61994/unpacking-sub-packets-recursive-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61994-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking at a protocol which may "glue together" multiple packets in arbitrary ways... So in essence a single "frame" of data has a 1:N relationship to packets it contains. Is it possible to attack something like this in a recursive type fashion by re-starting dissection on any remaining data after dissection of the first packet is complete? Ideally this would include segmenting the frame into new instances so that each packet would be uniquely identifiable for filtering purposes....</p></div><div id="question-tags" class="tags-container tags">dissector post-dissector dissection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '17, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/f5a6a32440657fdf63b9db18f3922c70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wittynickname&#39;s gravatar image" /><p>wittynickname<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wittynickname has one accepted answer">50%</span></p></div></div><div id="comments-container-61994" class="comments-container"></div><div id="comment-tools-61994" class="comment-tools"></div><div class="clear"></div><div id="comment-61994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62011"></span>

<div id="answer-container-62011" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62011-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Recursive dissection is fairly standard: there are a lot of protocols where a single (e.g., Ethernet) frame may contain multiple upper-layer PDUs. In Telco circles a good example is SCTP which frequently bundles many PDUs into a single SCTP packet.</p><p>Programmatically this is as simple as having a for() or while() loop in your "glue" protocol dissector to dissect all the protocol packets that in that frame. You can choose whether to make these PDUs top-level tree items or subtree items (in the Packet-Details pane) by choosing which tree/subtree parameter you pass to the sub-dissection function.</p><p>However, in Wireshark 1 frame is 1 frame is 1 frame. There isn't currently a way to "segment" a single (e.g., Ethernet) frame into multiple frames (in the Packet List pane). It's something we've talked about on and off for a long time but nothing has come of it.</p><p>If you want to see an example of this with SCTP traffic you can check out the <code>sctp-addip.cap</code> capture on the <a href="https://wiki.wireshark.org/SampleCaptures">SampleCaptures</a> page (unfortunately there the bundled chunks are just DATA--not upper layer protocol PDUs).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '17, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jun '17, 06:54</p></div></div><div id="comments-container-62011" class="comments-container"><span id="62015"></span><div id="comment-62015" class="comment"><div id="post-62015-score" class="comment-score"></div><div class="comment-text"><p>So does the inability to segment frames mean that it's also not possible to represent multiple instances of common data for each sub packet?</p><p>Goal being that a filter run searching for a certain type of packet would highlight the frame even if it's not the first instance of a packet in a given frame.</p></div><div id="comment-62015-info" class="comment-info"><span class="comment-age">(14 Jun '17, 07:14)</span> wittynickname</div></div><span id="62017"></span><div id="comment-62017" class="comment"><div id="post-62017-score" class="comment-score">1</div><div class="comment-text"><p>I'm not sure what you are saying, if you have a frame with PDU1, PDU2 and PDU3 and you program your dissector to show the PDUs in the "frame tree" a filter of pdu.fieldx would match the frame if any of the PDUs have that filter set, unfortuatly if you have a filter of pdu.fieldxx &amp;&amp; pdu.fieldyy it would match if pdu.fieldxx is in PDU1 and pdu.fieldyy is in PDU2 or PDU3.</p><p>The export PDU functionality can be used as a workaround to create a new pcap-ng with each PDU in a separate manufactured frame including meta information from the original trace.</p></div><div id="comment-62017-info" class="comment-info"><span class="comment-age">(14 Jun '17, 07:35)</span> Anders ♦</div></div><span id="62018"></span><div id="comment-62018" class="comment"><div id="post-62018-score" class="comment-score">1</div><div class="comment-text"><p>As Anders said filtering will work but there are some gotchas.</p><p>Fundamentally it's useful to remember that a filter like <code>ip.addr == 1.2.3.4</code> means "there exists a field in the frame named <code>ip.addr</code> whose value is <code>1.2.3.4</code>" So the <code>ip.addr</code> filter field can be anywhere in the frame: at the top-level or embedded in one or more PDUs within the frame. The trouble comes when you want to filter on the Nth instance of that field.</p></div><div id="comment-62018-info" class="comment-info"><span class="comment-age">(14 Jun '17, 07:59)</span> JeffMorriss ♦</div></div><span id="62020"></span><div id="comment-62020" class="comment"><div id="post-62020-score" class="comment-score"></div><div class="comment-text"><p>Just the ability to do filtering is probably good enough for my needs, I've tested with some basic support for iterative processing and the results are looking good. Thanks for the help!</p></div><div id="comment-62020-info" class="comment-info"><span class="comment-age">(14 Jun '17, 09:16)</span> wittynickname</div></div></div><div id="comment-tools-62011" class="comment-tools"></div><div class="clear"></div><div id="comment-62011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

