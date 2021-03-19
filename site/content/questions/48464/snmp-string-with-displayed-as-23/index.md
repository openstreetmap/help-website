+++
type = "question"
title = "SNMP string with # displayed as %23"
description = '''Hi,  I am troubleshooting an issue with a vendor of ours. We are using an SNMP tool to scan our network and keep running into failures. I used wireshark to determine that the snmp string sent out over the wire is incorrect.  I am typing my SNMP string into a webserver which then takes that string an...'''
date = "2015-12-11T15:11:00Z"
lastmod = "2015-12-12T02:22:00Z"
weight = 48464
keywords = [ "snmpwireshark", "snmp" ]
aliases = [ "/questions/48464" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SNMP string with \# displayed as %23](/questions/48464/snmp-string-with-displayed-as-23)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48464-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am troubleshooting an issue with a vendor of ours. We are using an SNMP tool to scan our network and keep running into failures. I used wireshark to determine that the snmp string sent out over the wire is incorrect.</p><p>I am typing my SNMP string into a webserver which then takes that string and attempts to query the device. When I see the community string in wireshark, I notice that the "#" is now missing from my string and replaced with "%23"</p><p>The vendor has told us this is just wireshark displaying the # as the hex value. This does not make sense to me as I am asking myself, why wouldn't wireshark convert the rest of that value to hex? Can anyone help me validate or correct what this vendor has told me?</p></div><div id="question-tags" class="tags-container tags">snmpwireshark snmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '15, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/238d0902a59854cdc5e2bf4c42377512?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crknipe123&#39;s gravatar image" /><p>crknipe123<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crknipe123 has no accepted answers">0%</span></p></div></div><div id="comments-container-48464" class="comments-container"><span id="48466"></span><div id="comment-48466" class="comment"><div id="post-48466-score" class="comment-score"></div><div class="comment-text"><p>Do you have a screenshot of the packet bytes pane, or better yet a trace you can share? Share by cloudshark, dropbox, drive, etc...</p></div><div id="comment-48466-info" class="comment-info"><span class="comment-age">(11 Dec '15, 17:30)</span> Rooster_50</div></div></div><div id="comment-tools-48464" class="comment-tools"></div><div class="clear"></div><div id="comment-48464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48467"></span>

<div id="answer-container-48467" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48467-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Many text-based protocols (not sure that it is the case of SNMP, but I <em>am</em> sure about SIP and I am <em>almost</em> sure about HTTP) use escaping of special characters in address (uri, url) strings because these characters have a special meaning for the text-based protocol itself.</p><p>I can imagine that Wireshark would translate (unescape) <code>%23</code> (three characters) into a single <code>#</code> when displaying the value in dissection pane, as dissectors are written by different people and someone might prefer to be bit-verbatim while someone else might prefer readability, but it would definitely not do the reverse, i.e. to escape a received <code>#</code> into <code>%23</code>.</p><p>Luckily, there is the packet bytes pane below the dissection pane, so click at the string value in the dissection pane and see the corresponding bytes highlighted in the packed bytes pane. If you find there, in the ASCII (rightmost) part, the <code>%23</code>, you can be sure it is what the web-fed machine has sent in the SNMP message.</p><p>My own guess is that your browser translates the <code>#</code> into <code>%23</code> before sending the data using http GET, because in case of GET, the data filled in to the form are used as parameters of url so they have to be escaped, and the vendor's machine does not translate <code>%23</code> back into <code>#</code> when processing the received parameters.</p><p>If you can use plain http rather than https to access the web interface, capture also the http communication and look into it, you should see whether your browser sends <code>#</code> or <code>%23</code> in the request url if you use <code>#</code> inside the form fields, something like</p><p><code>GET /?field1=%23one HTTP/1.1\r\n</code></p><p>if you've filled one of the fields with <code>#one</code>.</p><p>If they are using POST instead of GET, the parameters are part of the body rather than the url but the same encoding rules are intentionally applied.</p><p>The <code>#</code> has a specific meaning in an url because it is normally used to separate an identifier of a certain position on the web page to which the browser should focus the display of the page, so it is normally not sent from the browser to the server. So I dare to speculate further and say that the application vendor improperly handles url-encoded strings at reception, unescaping only % HEX HEX sequences which it has on some list, and the <code>%23</code> is missing on that list for the above reason and therefore they forward it transparently. The correct way is to escape only what is necessary (to save place) when sending, but to unescape everything received, as the <code>%</code> character is always a leading one of an escape sequence; if it is to be sent itself, it is escaped as <code>%25</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '15, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '15, 04:13</p></div></div><div id="comments-container-48467" class="comments-container"><span id="48474"></span><div id="comment-48474" class="comment"><div id="post-48474-score" class="comment-score"></div><div class="comment-text"><p>I had a 2nd look and it seems as if it is also incorrect in the dissection pane as well. So I am now confident it is the web browser/web server. Thanks for the explanation.</p><p>Screenshot of pcap <a href="https://www.dropbox.com/s/5ksm7zl3dnlr5ox/snmp.PNG?dl=0">https://www.dropbox.com/s/5ksm7zl3dnlr5ox/snmp.PNG?dl=0</a></p></div><div id="comment-48474-info" class="comment-info"><span class="comment-age">(12 Dec '15, 06:35)</span> crknipe123</div></div></div><div id="comment-tools-48467" class="comment-tools"></div><div class="clear"></div><div id="comment-48467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

