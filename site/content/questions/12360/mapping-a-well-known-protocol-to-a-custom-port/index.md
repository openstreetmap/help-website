+++
type = "question"
title = "Mapping a well known protocol to a custom port"
description = '''I have an http server that listens on port XXXX where XXXX is not 80 or 8080. Wireshark does not recognize the traffic to the server as http. What can I do to map port XXXX to http.'''
date = "2012-07-01T14:52:00Z"
lastmod = "2013-05-15T22:24:00Z"
weight = 12360
keywords = [ "http", "mapping", "port" ]
aliases = [ "/questions/12360" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping a well known protocol to a custom port](/questions/12360/mapping-a-well-known-protocol-to-a-custom-port)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12360-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an http server that listens on port XXXX where XXXX is not 80 or 8080. Wireshark does not recognize the traffic to the server as http. What can I do to map port XXXX to http.</p></div><div id="question-tags" class="tags-container tags">http mapping port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '12, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/d7b878d29423f0ed231924e63723bc96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dheerajrs&#39;s gravatar image" /><p>dheerajrs<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dheerajrs has no accepted answers">0%</span></p></div></div><div id="comments-container-12360" class="comments-container"><span id="21097"></span><div id="comment-21097" class="comment"><div id="post-21097-score" class="comment-score"></div><div class="comment-text"><p>Maybe a patch is required to automatically do this?</p></div><div id="comment-21097-info" class="comment-info"><span class="comment-age">(12 May '13, 15:38)</span> gak</div></div></div><div id="comment-tools-12360" class="comment-tools"></div><div class="clear"></div><div id="comment-12360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="12361"></span>

<div id="answer-container-12361" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12361-score" class="post-score" title="current number of votes">6</div></div></td><td><div class="item-right"><div class="answer-body"><p>The non-standard http port can be specified by setting one of the HTTP preferences</p><p>In Wireshark do:</p><p><code>Edit ! Preferences ! Protocols ! HTTP</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '12, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-12361" class="comments-container"><span id="21096"></span><div id="comment-21096" class="comment"><div id="post-21096-score" class="comment-score"></div><div class="comment-text"><p>This works but only with HTTP and SSL.</p></div><div id="comment-21096-info" class="comment-info"><span class="comment-age">(12 May '13, 15:38)</span> gak</div></div><span id="24643"></span><div id="comment-24643" class="comment"><div id="post-24643-score" class="comment-score"></div><div class="comment-text"><p>In order to specify this on the command line, you can use: <code>wireshark -o http.ssl.port:4433</code> (port 4433 for HTTPS) and <code>wireshark -o http.tcp.port:8080</code> (port 8080 for HTTP). It should also be possible to specify range (<code>8080-8082,8084</code>), but I haven't tested that.</p></div><div id="comment-24643-info" class="comment-info"><span class="comment-age">(13 Sep '13, 05:17)</span> Lekensteyn</div></div></div><div id="comment-tools-12361" class="comment-tools"></div><div class="clear"></div><div id="comment-12361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12362"></span>

<div id="answer-container-12362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12362-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>For HTTP, you can add additional ports in the HTTP preferences as Bill explained. In a more general manner you can always use "Decode As..." to specifically decode some traffic as a certain protocol. You can rightclick on a packet and choose "Decode As...".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '12, 22:25</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-12362" class="comments-container"></div><div id="comment-tools-12362" class="comment-tools"></div><div class="clear"></div><div id="comment-12362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21165"></span>

<div id="answer-container-21165" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21165-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>do edit the preferences file, add the specified port no in the list of pre-configured port nos list.That will solve the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '13, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p>Sanny_D<br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-21165" class="comments-container"></div><div id="comment-tools-21165" class="comment-tools"></div><div class="clear"></div><div id="comment-21165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

