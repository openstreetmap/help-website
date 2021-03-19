+++
type = "question"
title = "Using a Lua Script to Unbundle SCTP Multi-Chunk Packets and Generate Custom One-Line Summaries for Each Chunk"
description = '''Hello everyone. I&#x27;ve got some question(s) regarding the usage of Lua to unbundle SCTP multi-chunk packets and create custom one-line summaries for each chunk. The Question(s) 1) Is it possible to use a Lua script to retrieve specific fields within the dissection tree? I&#x27;m thinking of a Lua script be...'''
date = "2013-04-11T08:36:00Z"
lastmod = "2013-04-23T00:59:00Z"
weight = 20340
keywords = [ "unbundle", "sctp", "lua", "chunk", "summary" ]
aliases = [ "/questions/20340" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using a Lua Script to Unbundle SCTP Multi-Chunk Packets and Generate Custom One-Line Summaries for Each Chunk](/questions/20340/using-a-lua-script-to-unbundle-sctp-multi-chunk-packets-and-generate-custom-one-line-summaries-for-each-chunk)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20340-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone.</p><p>I've got some question(s) regarding the usage of Lua to unbundle SCTP multi-chunk packets and create custom one-line summaries for each chunk.</p><p><strong>The Question(s)</strong></p><p>1) Is it possible to use a Lua script to retrieve specific fields within the dissection tree?</p><p>I'm thinking of a Lua script because I've seen that it is passed a reference to the dissection tree in some methods.</p><p>2a) If no, what other solution do you suggest to navigate the dissection tree?</p><p>2b) If yes, should I use a listener, a dissector, a post-dissector, or what else?</p><p>For instance, I read on the Wireshark Lua documentation and elsewhere that the dissection tree may not be fully populated the first time a listener is notified.</p><p>3) What are the Lua methods to navigate the tree, check the field names, and retrieve their values?</p><p>I need to navigate the tree so that I can tell which SCTP chunk (i.e., subtree) a given field (e.g., tcap.tid) belongs to, and assign its value(s) in the one-line summary for that SCTP chunk.</p><p>In the rest of the post, I describe the situation I'm in and which led me to ask these questions.</p><p><strong>The environment</strong></p><p>I'm analyzing SS7 traffic over IP such that the protocol stack for each packet usually looks like this (bottom up):</p><pre><code>GSM SMS
GSM MAP
TCAP
SCCP
MTP3 UA
SCTP
IP
Ethernet
Frame</code></pre><p>Of course, not all captured packets feature the whole protocol stack listed above. Some of them are just SCTP control packets, while others feature payloads for (some of) the protocols on top of SCTP as well.</p><p>Most importantly, each packet usually features multiple SCTP chunks, so that there are multiple entries on top of SCTP (each one containing payload for some out of M3UA, SCCP, TCAP, GSM MAP, and GSM SMS) for most of the captured packets.</p><p>I am working with Tshark 1.8.2 compiled with Lua 5.1. This is the standard Tshark package in Ubuntu 12.10.</p><p><strong>The Objective</strong></p><p>As part of a project, I need to dissect this SS7 traffic and save to a file a one-line summary for each M3UA, SCCP, TCAP, GSM MAP, and GSM SMS packet with the values of selected fields in their payloads.</p><p>The one-line summaries should be tab-separated and contain entries for OPC and DPC, SSNs, TCAP TIDs, IMSIs, and a few other fields.</p><p><strong>The Problem</strong></p><p>Unfortunately, Wireshark/Tshark does not provide a one-line summary for each SCTP chunk in an SCTP multi-chunk packet.</p><p>Consequently, the M3UA, SCCP, TCAP, GSM MAP, and GSM SMS fields of different SCTP chunks in a packet get all listed together when one accesses them using the -T fields and -e options.</p><p>At first sight, this makes it impossible to match the values of these fields to the respective SCTP chunk.</p><p><strong>A Partial Solution</strong></p><p>I developed a partial solution to this problem by using some of the structure in the protocols to infer if a given chunk features a given field, and thus read it off the list of entries for that field returned by the Tshark-generated one-line summaries.</p><p>However, this method can get me only so far as it fails if there isn't a (simple) structure in the protocol. For instance, it's impossible to infer which chunk the TCAP transaction IDs belong to, because a chunk can feature one or two transaction IDs, which are both output with the tcap.tid field. Therefore, if I see a packet with two SCTP chunks and three values in tcap.tid, it's impossible to tell which one of the two chunks had two TCAP IDs.</p><p><strong>An Alternative Solution</strong></p><p>Given the shortcomings of the partial solution described above, I went back to the drawing board and tried to find another solution.</p><p>Then I noticed that there is a place where the SCTP chunks are unbundled: The Packet Details Pane. In the packet details, the field values are listed under their respective SCTP chunks. Therefore, by looking at the packet details I can tell which SCTP chunk the TCAP transaction IDs refer to.</p><p>I then considered parsing the output generated by Tshark with options -T text and -V (the packet details) to retrieve the required fields for each SCTP chunk and output my own one-line summary for each SCTP chunk.</p><p>However, this doesn't sound like good software engineering for several reasons:</p><ol><li>It's very time expensive for Tshark to output the packet details even if I use the -O protocols option to select which protocols (e.g., only M3UA, SCCP, TCAP, GSM MAP, and GSM SMS) to generate the details for; and</li><li>The output packet details format could change anytime, thus breaking my parser.</li></ol><p>With these remarks in mind, I then started looking into Lua scripts, which prompted me to ask the questions above.</p><p>Thank you in advance for your help.</p></div><div id="question-tags" class="tags-container tags">unbundle sctp lua chunk summary</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '13, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/23b5d693d82939faf272e4319afc0d13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tshark-user&#39;s gravatar image" /><p>tshark-user<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tshark-user has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Apr '13, 07:14</p></div></div><div id="comments-container-20340" class="comments-container"></div><div id="comment-tools-20340" class="comment-tools"></div><div class="clear"></div><div id="comment-20340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20732"></span>

<div id="answer-container-20732" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20732-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>Short answers:</p><p>Re: 1) Yes</p><p>Re: 2) Use a tap</p><p>Re: 3) Field extractors in some cases as tables</p><p>Longer answer:</p><p>I've actually did very similar thing to what you've described there.</p><p>I've created in lua what was in fact an SCCP/RANAP/ALCAP analyzer that would track UMTS/GSM events calls, SMS'es, PS sessions etc and then rather than printing it out as you are thinking about doing I used luasql and dumped transactions to a database with a little web interface which allowed me to do loads of statistical analysis.</p><p>It is was a bit tricky as you basically need to do session tracking ending etc but nonetheless doable.</p><p>The problem you've described with multiple tcap.tids is very common</p><p><a href="http://ask.wireshark.org/questions/4225/lua-how-to-get-multiple-values-from-faststart-items-h225-h245?page=1&amp;focusedAnswerId=4236#4236">How to get multiple values from items</a></p><p><a href="http://ask.wireshark.org/questions/11000/lua-tap-and-multiple-instances-of-a-protocol-in-one-frame">Multiple instances of a protocol in one frame</a></p><p>Best advise I could give you is to study lua examples on this website.</p><p>I'd especially recommend reading answers posted by <a href="http://ask.wireshark.org/users/817/helloworld">helloworld</a> his code examples were great help although not directly related to the problem I was trying to solve.</p><p>Have fun</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '13, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-20732" class="comments-container"><span id="20745"></span><div id="comment-20745" class="comment"><div id="post-20745-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer, izopizo. I'll look into the links you provided.</p><p>What are the field extractors you're referring to? The all_field_infos() method seems to return all fields, while the Field.new() selects a specific field. However, none of the them seems to support navigation of the dissection tree.</p><p>I would like to be able to navigate the dissection tree just like you can navigate an XML document, so as to read and process fields knowing their relative position in the tree. Among other things, this would enable me to tell between TCAP transaction IDs of different chunks in the same multi-chunk SCTP packet, or distinguish whether an MSISDN in a GSM MAP operation is the device phone number or the network element (say HLR).</p><p>Are there any methods in the Lua API that I can use to navigate the dissection tree (starting from the root)?</p><p>In the meantime since I asked the question, I developed a solution to my problem using an existing Perl script (also mentioned in this question <a href="http://ask.wireshark.org/questions/12845/sctp-unbundle">http://ask.wireshark.org/questions/12845/sctp-unbundle</a> ) to split multi-chunk SCTP packets into multiple packets, and then process the output of -T fields with my own Python script to reconstruct the TCAP transactions.</p><p>If there are indeed methods to navigate the dissection tree in Lua, I'd be glad to port my Python script for TCAP transaction reconstruction to Lua and make it available to the Wireshark community.</p><p>Thank you again for your help.</p></div><div id="comment-20745-info" class="comment-info"><span class="comment-age">(23 Apr '13, 14:23)</span> tshark-user</div></div></div><div id="comment-tools-20732" class="comment-tools"></div><div class="clear"></div><div id="comment-20732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

