+++
type = "question"
title = "export PDUs?"
description = '''Hi all:  My wireshark version 1.12.5, I captured DTLS packets(pre-shared-key), Wireshark is able to show decrypted payload, but since the payload is another protocol, i&#x27;d like to export it into another pcap and use wireshark to analyze it. I&#x27;ve learned that i could use &quot;Export PDUs&quot; functionality to...'''
date = "2015-06-18T21:20:00Z"
lastmod = "2015-06-24T17:27:00Z"
weight = 43354
keywords = [ "pdu" ]
aliases = [ "/questions/43354" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [export PDUs?](/questions/43354/export-pdus)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43354-score" class="post-score" title="current number of votes">0</div><span id="post-43354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all: My wireshark version 1.12.5, I captured DTLS packets(pre-shared-key), Wireshark is able to show decrypted payload, but since the payload is another protocol, i'd like to export it into another pcap and use wireshark to analyze it. I've learned that i could use "Export PDUs" functionality to do that. as explained in here: <a href="https://www.wireshark.org/lists/wireshark-users/201407/msg00038.html">https://www.wireshark.org/lists/wireshark-users/201407/msg00038.html</a> However, after I select "export PDUs" ,with OSI Layer 7 option, no packets showing up. Does anyone knows why?</p><p>Thanks Lei</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pdu" rel="tag" title="see questions tagged &#39;pdu&#39;">pdu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '15, 21:20</strong></p><img src="https://secure.gravatar.com/avatar/6c39cdd586a6e713b4457ee65309c4cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lei%20Sun&#39;s gravatar image" /><p><span>Lei Sun</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lei Sun has no accepted answers">0%</span></p></div></div><div id="comments-container-43354" class="comments-container"><span id="43355"></span><div id="comment-43355" class="comment"><div id="post-43355-score" class="comment-score"></div><div class="comment-text"><p>I just tested the functionality with Wireshark 1.12.5 and the DTLS sample pcap found on the wiki <a href="https://wiki.wireshark.org/DTLS">https://wiki.wireshark.org/DTLS</a> and it works fine. COuld you give a try with this example and confirms it works for you?</p></div><div id="comment-43355-info" class="comment-info"><span class="comment-age">(18 Jun '15, 22:19)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="43356"></span><div id="comment-43356" class="comment"><div id="post-43356-score" class="comment-score"></div><div class="comment-text"><p>I tried it and didn't work with snakeoil-dtls.pcap. The procedure is: open snakeoid-dtls.pcap. select "File-&gt;export PDUs to file", and then select "OSI layer 7" in dialog box. Wirehshark shows no packet afterward.</p><p>Wireshark version: Version 1.12.5 (v1.12.5-0-g5819e5b from master-1.12)</p></div><div id="comment-43356-info" class="comment-info"><span class="comment-age">(18 Jun '15, 22:51)</span> <span class="comment-user userinfo">Lei Sun</span></div></div><span id="43358"></span><div id="comment-43358" class="comment"><div id="post-43358-score" class="comment-score"></div><div class="comment-text"><p>Well, it definitely does work for me as long as I configure the decryption properly: you end up with 4 data packets in the new window.</p><p>Did you set RSA configuration to IP address:127.0.0.1, Port:4433, Protocol:data, Key File:/path/to/snakeoil-rsa.key as explained in the wiki?</p></div><div id="comment-43358-info" class="comment-info"><span class="comment-age">(19 Jun '15, 03:02)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="43377"></span><div id="comment-43377" class="comment"><div id="post-43377-score" class="comment-score"></div><div class="comment-text"><p>Sorry I forgot to configure the decryption, I did and it worked with the sample capture. However it still doesn't work with my capture, which is pre-shared-key instead of RSA. I mean i can see the decrypted packet content in "decrypt DTLS record" tab of the wireshark, but exporting PDUs still gives me no packets.</p></div><div id="comment-43377-info" class="comment-info"><span class="comment-age">(19 Jun '15, 09:07)</span> <span class="comment-user userinfo">Lei Sun</span></div></div></div><div id="comment-tools-43354" class="comment-tools"></div><div class="clear"></div><div id="comment-43354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43530"></span>

<div id="answer-container-43530" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43530-score" class="post-score" title="current number of votes">0</div><span id="post-43530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark 1.12 can only export deciphered packets for which a sub dissector handle (protocol in preference window) is configured. Presumable you did not fill any.</p><p>Wireshark v1.99.8rc0-121-gcdc7d25 and later now also supports the export of captures using heuristic sub dissectors. It can be downloaded from <a href="https://www.wireshark.org/download/automated/">https://www.wireshark.org/download/automated/</a></p><p>If your payload is for a protocol not currently supported by Wireshark, ensure to configure the "data" dissector as protocol so as to have the payload exported.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '15, 17:27</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43530" class="comments-container"></div><div id="comment-tools-43530" class="comment-tools"></div><div class="clear"></div><div id="comment-43530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

