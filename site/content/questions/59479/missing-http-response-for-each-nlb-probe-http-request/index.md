+++
type = "question"
title = "Missing HTTP response for each NLB probe HTTP Request"
description = '''Hi, I need help to find if there is any missing HTTP response (Http 401 status code) from IIS server for the HTTP requests received from NLB probes. This way we can diagnose whether the issue is with NLB or IIS? The problem faced by us is that at certain time NLB is down because it does not receive ...'''
date = "2017-02-16T09:50:00Z"
lastmod = "2017-02-16T09:50:00Z"
weight = 59479
keywords = [ "proberesponse", "http", "misssing" ]
aliases = [ "/questions/59479" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing HTTP response for each NLB probe HTTP Request](/questions/59479/missing-http-response-for-each-nlb-probe-http-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59479-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I need help to find if there is any missing HTTP response (Http 401 status code) from IIS server for the HTTP requests received from NLB probes.</p><p>This way we can diagnose whether the issue is with NLB or IIS? The problem faced by us is that at certain time NLB is down because it does not receive the response but at the same time we are able to browse the site in IIS. So if we know missing packets or missing responses we can figure out where the problem is.</p><p>Also is there any way in Wireshark to figure out packet loss? Regards Rajaniesh</p></div><div id="question-tags" class="tags-container tags">proberesponse http misssing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '17, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/e4f9940127b9da7dd8687b7b748ddab3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rajaniesh&#39;s gravatar image" /><p>rajaniesh<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rajaniesh has no accepted answers">0%</span></p></div></div><div id="comments-container-59479" class="comments-container"><span id="59661"></span><div id="comment-59661" class="comment"><div id="post-59661-score" class="comment-score"></div><div class="comment-text"><p>Yes, Wireshark can help to figure out if there is packet loss.</p><p>However if you call NLB or IIS into question it would help to take a capture of the traffic with a port mirror or a TAP.</p></div><div id="comment-59661-info" class="comment-info"><span class="comment-age">(24 Feb '17, 07:19)</span> Uli</div></div><span id="59680"></span><div id="comment-59680" class="comment"><div id="post-59680-score" class="comment-score"></div><div class="comment-text"><p>How do we do port mirror or TAP?</p></div><div id="comment-59680-info" class="comment-info"><span class="comment-age">(25 Feb '17, 07:07)</span> rajaniesh</div></div><span id="59681"></span><div id="comment-59681" class="comment"><div id="post-59681-score" class="comment-score"></div><div class="comment-text"><p>see <a href="https://blog.packet-foo.com/2016/11/the-network-capture-playbook-part-4-span-port-in-depth/">https://blog.packet-foo.com/2016/11/the-network-capture-playbook-part-4-span-port-in-depth/</a> and <a href="https://blog.packet-foo.com/2016/12/the-network-capture-playbook-part-5-network-tap-basics/">https://blog.packet-foo.com/2016/12/the-network-capture-playbook-part-5-network-tap-basics/</a></p></div><div id="comment-59681-info" class="comment-info"><span class="comment-age">(25 Feb '17, 07:19)</span> Uli</div></div></div><div id="comment-tools-59479" class="comment-tools"></div><div class="clear"></div><div id="comment-59479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

