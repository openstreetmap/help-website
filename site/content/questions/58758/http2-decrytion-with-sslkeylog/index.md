+++
type = "question"
title = "HTTP/2 decrytion with sslkeylog"
description = '''Hi I hope this should be the right way to ask the related question. These days, I tried to use the wireshark to decrypt the SSL data and analysis the HTTP/2 traffic. I tried win64-1.99.2. win64-1.12.6,win 64-2.2.3. I also tried the same version on ubuntu 14.04 and MacOS. I followed the steps below t...'''
date = "2017-01-14T03:35:00Z"
lastmod = "2017-01-14T03:35:00Z"
weight = 58758
keywords = [ "ssl_decrypt" ]
aliases = [ "/questions/58758" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP/2 decrytion with sslkeylog](/questions/58758/http2-decrytion-with-sslkeylog)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58758-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I hope this should be the right way to ask the related question.</p><p>These days, I tried to use the wireshark to decrypt the SSL data and analysis the HTTP/2 traffic. I tried win64-1.99.2. win64-1.12.6,win 64-2.2.3. I also tried the same version on ubuntu 14.04 and MacOS. I followed the steps below to try to decrypt the traffic</p><ol><li>add the SSLKEYLOGFILE and the corresponding path to the environment variable 2.I set the SSL of preference in wireshark and set the corresponding path in the (Pre)-Master-Secret log filename. 3.Then I restart the browser(firefox and chrome) and the wireshark to capture the corresponding packets</li></ol><p>The results I observe: Sometimes, the ssllogkey file is empty, I think this might be the reason of chrome or firefox, after waiting for sometime, there is the session key inside the ssllogkey file Sometimes,when there is content inside the ssllogkey file and I can still not decrypt the frames completely. I can only see the content of some js or css file. But I cannot see the specific frames type of http2 like push promise, settings, data etc.</p><p>I tried to solve this problem for three whole days but failed. And my target website includes google, twitter some public sites and some sites I set in the testbed. But I can not get a satisfied result. I searched and visited many sites introducing the way to decrypting the ssl traffic but I failed at last. I also tried the way to set the private key in wireshark and do the test on my testbed, still no results.</p><p>I really need you guys help if any of you ever used wireshark to decrypt the HTTP/2 traffic completely, could you please tell me your platform, your wireshark version, your browser version, your test site or your testbed server version(better with configuration if available) and the cipher suite. I want to repeat your test. I am completely confused and don't trust myself, I don't know which step is wrong or I just miss some important thing.</p><p>If you need more information of my test, please let me know and I can provide more information and the pcap files. Many Thanks and really need your help.</p><p>Regards</p><p>Muhui</p></div><div id="question-tags" class="tags-container tags">ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '17, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/e71bbde48e924a45bf0717f8fb803940?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muhui&#39;s gravatar image" /><p>Muhui<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muhui has no accepted answers">0%</span></p></div></div><div id="comments-container-58758" class="comments-container"></div><div id="comment-tools-58758" class="comment-tools"></div><div class="clear"></div><div id="comment-58758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

