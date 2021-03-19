+++
type = "question"
title = "How to iterating though a bundled SS7 SCTP packet in Lua"
description = '''Hi, I wonder if there is someone that have been able to iterate thourgh a bundled SS7 SCTP packet with tshark and a Lua script. Example of my packet:  Frame IP  SCTP  M3UA  SCCP  TCAP  GSM-MAP  SCTP  M3UA  SCCP  TCAP  SCTP  M3UA  SCCP  TCAP  GSM-MAP  So I want to be able to evaluate each M3UA pcaket...'''
date = "2015-06-25T07:00:00Z"
lastmod = "2015-06-25T15:28:00Z"
weight = 43543
keywords = [ "lua", "sctp", "ss7" ]
aliases = [ "/questions/43543" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to iterating though a bundled SS7 SCTP packet in Lua](/questions/43543/how-to-iterating-though-a-bundled-ss7-sctp-packet-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43543-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I wonder if there is someone that have been able to iterate thourgh a bundled SS7 SCTP packet with tshark and a Lua script.</p><p>Example of my packet:</p><hr /><p>Frame IP</p><hr /><p>SCTP M3UA SCCP TCAP GSM-MAP</p><hr /><p>SCTP M3UA SCCP TCAP</p><hr /><p>SCTP M3UA SCCP TCAP GSM-MAP</p><hr /><p>So I want to be able to evaluate each M3UA pcaket at the time and be able to get out data from MTP3,SCCP,TCAP and GSM-MAP layer as I can do with a unbundled M3UA packet.</p><p>For example e212.imsi and tcap.tid I have hard time to match to a particular M3UA packet when analysing a frame with bundled M3UA packets.</p><p>I have seen some QA on the forum but I can not find any solution that works for me.</p><p>Thanks</p><p>/Mattias</p></div><div id="question-tags" class="tags-container tags">lua sctp ss7</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '15, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/594b884dee890a5bd1cf58797ce53243?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lunken&#39;s gravatar image" /><p>Lunken<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lunken has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '15, 14:50</p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-43543" class="comments-container"></div><div id="comment-tools-43543" class="comment-tools"></div><div class="clear"></div><div id="comment-43543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43573"></span>

<div id="answer-container-43573" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43573-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think there's any easy/simple answer to this, but there I can think of a way to do it that's fairly complicated...</p><p>First, are you using a Listener tap or a dissector? It can probably be done either way, but the answer changes slightly depending on which one you do.</p><p>If you're doing this with a Listener tap, you can tap the M3UA layer, so that your Lua-defined tap.packet() function gets called for each separate M3UA message. So for a given IP packet, let's say IP packet #1, the first time your tap.packet() runs for IP packet #1, you'll only get the various Fields you're interested in for the first M3UA; but unfortunately the second time the tap.packet() is called it will get the Fields from both the first and second M3UA message; and the third time tap.packet() is invoked it will get the Fields from all three messages.</p><p>So the brute-force way to "fix" that is to keep state information about what Fields tap.packet() has already seen/retrieved for a given IP packet. For example, create a Lua table outside of the tap.packet() function, and within the tap.packet() function add an entry in that table using the frame number as an index of the table, and the value as another sub-table with indexes being the field names, and the value of those field names would be a number representing how many you've already seen. Or if all fields only appear once in a given M3UA message, then you don't need the sub-table of fields names but can instead just have the frame number entry be a number for how many M3UA messages have been processed in this frame.</p><p>So for example, for IP packet #1 when tap.packet() gets invoked there would be no entry for index "1" in the table so you create it with a value "1", and then use all the Fields you get. The second time tap.packet() is invoked it finds an existing index entry for packet # "1", with a value count of "1", so it updates the value to "2", and it knows to skip the first Field it gets and only use the second. And the third time tap.packet() is called it finds the index packet # "1" entry with a value of "2", which it increments to "3", and knows to skip the first 2 Fields it gets, etc.</p><p>Just make sure to clear/destroy that table at the end of the file, by defining a tap.reset() function which clears it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '15, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43573" class="comments-container"></div><div id="comment-tools-43573" class="comment-tools"></div><div class="clear"></div><div id="comment-43573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

