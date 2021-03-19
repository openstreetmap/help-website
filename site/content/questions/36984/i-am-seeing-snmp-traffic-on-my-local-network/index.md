+++
type = "question"
title = "I am seeing SNMP traffic on my local network"
description = '''I am not too sure if this should be happening but I don&#x27;t think SNMP on a home network is the type of network traffic one should be seeing on their Local LAN.  A lot of Get requests seem to be made from what I am seeing an epson device. Correct me if I&#x27;m wrong. Is this a cause for concern to see SNM...'''
date = "2014-10-12T10:57:00Z"
lastmod = "2014-10-12T11:19:00Z"
weight = 36984
keywords = [ "snmpwireshark", "snmp" ]
aliases = [ "/questions/36984" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [I am seeing SNMP traffic on my local network](/questions/36984/i-am-seeing-snmp-traffic-on-my-local-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am not too sure if this should be happening but I don't think SNMP on a home network is the type of network traffic one should be seeing on their Local LAN.</p><p>A lot of Get requests seem to be made from what I am seeing an epson device. Correct me if I'm wrong. Is this a cause for concern to see SNMP. I know that typically speaking it's not a UDP protocol I want to see since SNMP is not even configured on my network.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/snmptraffic.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">snmpwireshark snmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '14, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p>Beldum<br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></img></div></div><div id="comments-container-36984" class="comments-container"></div><div id="comment-tools-36984" class="comment-tools"></div><div class="clear"></div><div id="comment-36984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36985"></span>

<div id="answer-container-36985" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36985-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you any Epson devices in your network? Printer, Router, scanner etc. SNMP is used by pretty much anything on your network to communicate its preferences (I may have translated that badly..) Epsonnet Setup manager springs to mind</p><p>Basically if you have ANY epson devices, then no, it is nothing to worry about.</p><p>Oh, and for FJHADS sake Admins, get rid of this captcha.. I can't read it half the time..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '14, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-36985" class="comments-container"><span id="36986"></span><div id="comment-36986" class="comment"><div id="post-36986-score" class="comment-score"></div><div class="comment-text"><p>Thank you, I understood what you were saying clearly. What do all the get next request messages mean?</p></div><div id="comment-36986-info" class="comment-info"><span class="comment-age">(12 Oct '14, 11:21)</span> Beldum</div></div><span id="36987"></span><div id="comment-36987" class="comment"><div id="post-36987-score" class="comment-score"></div><div class="comment-text"><blockquote>Oh, and for FJHADS sake Admins, get rid of this captcha.. I can't read it half the time..</blockquote><p>Unfortunately all the bottom-feeding scammers that like to post here make that impossible at this time, sorry for the inconvenience.</p></div><div id="comment-36987-info" class="comment-info"><span class="comment-age">(12 Oct '14, 11:25)</span> grahamb ♦</div></div><span id="37116"></span><div id="comment-37116" class="comment"><div id="post-37116-score" class="comment-score"></div><div class="comment-text"><p>In that case, I need new glasses :/</p><p>ähm.. Think of snmp data as a kind of XML file. A get-next-request basically means, thanks, got that one , now tell me the next line. It is pretty innefficient (my personal belief), I assume it can, but I have never seen an address lookup, just a tree search with get-next.</p><p>Or the technical explanation: get-next-request is just like get-request, except it returns the item in the MIB just after the specified item (the “first lexicographic successor” in RFC terms). This operation comes into play most often when you are attempting to find all of the items in a logical table object. For instance, you might send a set of repeated get-next-requests to query for each line of a workstation’s ARP table. We’ll see an example of this in practice in a moment.</p><p>Quoted from: <a href="http://oreilly.com/perl/excerpts/system-admin-with-perl/twenty-minute-snmp-tutorial.html">http://oreilly.com/perl/excerpts/system-admin-with-perl/twenty-minute-snmp-tutorial.html</a></p></div><div id="comment-37116-info" class="comment-info"><span class="comment-age">(16 Oct '14, 12:02)</span> DarrenWright</div></div></div><div id="comment-tools-36985" class="comment-tools"></div><div class="clear"></div><div id="comment-36985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

