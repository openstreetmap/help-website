+++
type = "question"
title = "SSL : Decrypt servers&#x27; Application Data"
description = '''In order to decode the SSL application data, I set the &#x27;RSA Keys List&#x27; with right server key file along with its port and IP addresses.  What I see is that the only the client&#x27;s application data(HTTP) got decoded successfully but not the servers&#x27;s response to it.  What is that I could be missing? -P...'''
date = "2014-03-24T04:37:00Z"
lastmod = "2014-03-25T01:45:00Z"
weight = 31109
keywords = [ "tlsv1" ]
aliases = [ "/questions/31109" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL : Decrypt servers' Application Data](/questions/31109/ssl-decrypt-servers-application-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31109-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In order to decode the SSL application data, I set the 'RSA Keys List' with right server key file along with its port and IP addresses.</p><p>What I see is that the only the client's application data(HTTP) got decoded successfully but not the servers's response to it.</p><p>What is that I could be missing?</p><p>-Prabhu</p></div><div id="question-tags" class="tags-container tags">tlsv1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '14, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/bee5774ed7754b58092719339bb1a549?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sp87&#39;s gravatar image" /><p>Sp87<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sp87 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Mar '14, 04:39</p></div></div><div id="comments-container-31109" class="comments-container"></div><div id="comment-tools-31109" class="comment-tools"></div><div class="clear"></div><div id="comment-31109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31141"></span>

<div id="answer-container-31141" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31141-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>What cipher suite is being used? Check the Server Hello packet.</p><p>You cannot decrypt ephemeral cipher suites.</p><p>If the above does not apply you can try to decrypt the session using the Pre-Master Secret.</p><ol><li>Remove the RSA key you just added in Wireshark.</li><li>In Windows create a System Variable named SSLKEYLOGFILE with the value C:\premaster.txt</li><li>In Wireshark go to Edit &gt; Preferences &gt; Protocols &gt; SSL and type the path to the file above under (Pre)Master-Secret log file name.</li><li>Start your packet capture.</li><li>Open Chrome or Firefox and make sure the cache is cleared, then go to the desired webpage.</li><li>Stop the packet capture and follow the SSL Stream to check if the session was decrypted.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '14, 01:45</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-31141" class="comments-container"><span id="31158"></span><div id="comment-31158" class="comment"><div id="post-31158-score" class="comment-score"></div><div class="comment-text"><p>@Roland, thanks for your reply. I am not sure the steps that you mention can be carried out. The test is being done at a customer location trials. The cipher suites seem to be OK for the application data from the client is decrypted successfully. It is the server response to it that is not decrypted..</p></div><div id="comment-31158-info" class="comment-info"><span class="comment-age">(25 Mar '14, 12:29)</span> Sp87</div></div></div><div id="comment-tools-31141" class="comment-tools"></div><div class="clear"></div><div id="comment-31141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

