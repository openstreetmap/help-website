+++
type = "question"
title = "Reproducing the HTTP Post Call to a webservice based on a Wireshark log"
description = '''Hi, Im trying to use Wireshark to dissect the communication between two an application and a webservice, with the goal to implement the same call to the webservice in my own application. When I filter out the request it looks like this in TCP Stream : POST Call HTTP/1.1 Content-Type: application/x-t...'''
date = "2012-04-19T07:29:00Z"
lastmod = "2012-04-19T07:29:00Z"
weight = 10281
keywords = [ "dissect", "http", "post", "webservice" ]
aliases = [ "/questions/10281" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reproducing the HTTP Post Call to a webservice based on a Wireshark log](/questions/10281/reproducing-the-http-post-call-to-a-webservice-based-on-a-wireshark-log)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10281-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Im trying to use Wireshark to dissect the communication between two an application and a webservice, with the goal to implement the same call to the webservice in my own application.</p><p>When I filter out the request it looks like this in TCP Stream :</p><p>POST Call HTTP/1.1 Content-Type: application/x-tpnet-package Content-Length: 254 x-tpnet-msgid: 382</p><p>CTPNET$$..............TSM-KS-OS03......MMSW.TestUsr.....ATRowSet2.1.........DataSource...........MmsData1_11_SL.SchId...............Request...........SetEvent.EvId...............SchedStatus............EstTime...........H...ActualDepartTime...........H...HTTP/1.1 200 OK</p><p>My question is how can I reverse engineer the datastructure that's beeing posted here, so I can reproduse it in my own code?</p><p>brgs, Tor</p></div><div id="question-tags" class="tags-container tags">dissect http post webservice</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '12, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/1606104ad09b59b13af8d6e0ffaaffcc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tor&#39;s gravatar image" /><p>Tor<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tor has no accepted answers">0%</span></p></div></div><div id="comments-container-10281" class="comments-container"></div><div id="comment-tools-10281" class="comment-tools"></div><div class="clear"></div><div id="comment-10281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

