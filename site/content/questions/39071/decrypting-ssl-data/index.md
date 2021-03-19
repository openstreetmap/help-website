+++
type = "question"
title = "Decrypting SSL data"
description = '''Hey, i want to sniff packets coming from a mobile device and i&#x27;m gonna use tcpdump to sniff them, so i need to know if there&#x27;s there any way to get the RSA key for decryption.'''
date = "2015-01-12T02:17:00Z"
lastmod = "2015-01-13T04:28:00Z"
weight = 39071
keywords = [ "ssl", "rsa", "decryption" ]
aliases = [ "/questions/39071" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypting SSL data](/questions/39071/decrypting-ssl-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39071-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, i want to sniff packets coming from a mobile device and i'm gonna use tcpdump to sniff them, so i need to know if there's there any way to get the RSA key for decryption.</p></div><div id="question-tags" class="tags-container tags">ssl rsa decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '15, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/57a346c51606f30cffeaf3ea7bf48656?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LGMan&#39;s gravatar image" /><p>LGMan<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LGMan has one accepted answer">100%</span></p></div></div><div id="comments-container-39071" class="comments-container"></div><div id="comment-tools-39071" class="comment-tools"></div><div class="clear"></div><div id="comment-39071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39089"></span>

<div id="answer-container-39089" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39089-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes there is (assuming you're in a controlled environment where you are allowed to receive the private key), talk to the server administrator and ask him to give you the private key.</p><p>It it is a public website you want to decrypt the traffic from, you will need to proxy the traffic through an SSL termination proxy and do the decryption with the key of your proxy. An example of such a proxy is fiddler2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '15, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39089" class="comments-container"><span id="39151"></span><div id="comment-39151" class="comment"><div id="post-39151-score" class="comment-score"></div><div class="comment-text"><p>Thanks, but is there a way to decrypt https from a pcap file? I usually make a hotspot for some coworkers and i want to keep track of what they're browsing and make sure they don't do anything bad [or illegal]. I have a jailbroken idevice and i used tcpdump to collect data.</p></div><div id="comment-39151-info" class="comment-info"><span class="comment-age">(15 Jan '15, 02:29)</span> LGMan</div></div><span id="39173"></span><div id="comment-39173" class="comment"><div id="post-39173-score" class="comment-score"></div><div class="comment-text"><p>Since the whole purpose of SSL is to make the contents of a transmission private between the client and the server, just capturing the traffic will not enable you to decrypt the traffic. You will need the session keys used (known only to the clients and the servers) or the private keys (only known to the servers) to decrypt the traffic.</p></div><div id="comment-39173-info" class="comment-info"><span class="comment-age">(15 Jan '15, 12:45)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-39089" class="comment-tools"></div><div class="clear"></div><div id="comment-39089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

