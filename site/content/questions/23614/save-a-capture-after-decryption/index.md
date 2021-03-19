+++
type = "question"
title = "save a capture after decryption?"
description = '''I know you&#x27;ve been asked this before and said no, but are there plans to implement this feature? I have several clients that use SSL and while decrypting captures are not a problem, the inability to save it as decrypted is a genuine headache.'''
date = "2013-08-07T09:35:00Z"
lastmod = "2013-08-07T11:40:00Z"
weight = 23614
keywords = [ "ssl" ]
aliases = [ "/questions/23614" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [save a capture after decryption?](/questions/23614/save-a-capture-after-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23614-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know you've been asked this before and said no, but are there plans to implement this feature? I have several clients that use SSL and while decrypting captures are not a problem, the inability to save it as decrypted is a genuine headache.</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '13, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/7894f23047523148cfd593bc2916c5f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ken%20Cohen&#39;s gravatar image" /><p>Ken Cohen<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ken Cohen has no accepted answers">0%</span></p></div></div><div id="comments-container-23614" class="comments-container"><span id="39474"></span><div id="comment-39474" class="comment"><div id="post-39474-score" class="comment-score"></div><div class="comment-text"><p>Hi guys!</p><p>This thread seem to have gone "cold"? I´m searching for same function as we need to send some dumps for review of external support at Citrix.</p><p>Any chance that this has been implemented yet? Cheers Marksu Korhonen</p></div><div id="comment-39474-info" class="comment-info"><span class="comment-age">(29 Jan '15, 04:22)</span> Markus Korhonen</div></div><span id="39478"></span><div id="comment-39478" class="comment"><div id="post-39478-score" class="comment-score"></div><div class="comment-text"><p>Well you can save it as a .txt file using export packet dissection..doesnt that work??</p></div><div id="comment-39478-info" class="comment-info"><span class="comment-age">(29 Jan '15, 05:58)</span> koundi</div></div><span id="39479"></span><div id="comment-39479" class="comment"><div id="post-39479-score" class="comment-score"></div><div class="comment-text"><p>What was an experimental feature in August of 2013 was released in the 1.12.0 release about 6 months ago. So now the feature is there (File-&gt;Export PDUs to file).</p><p>Note that this function is only available in the GUI for now (see <a href="https://ask.wireshark.org/questions/39344/save-decrypted-wpa-packets-to-file-using-tshark">this question</a> for what's happening on the tshark front).</p></div><div id="comment-39479-info" class="comment-info"><span class="comment-age">(29 Jan '15, 06:03)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-23614" class="comment-tools"></div><div class="clear"></div><div id="comment-23614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23619"></span>

<div id="answer-container-23619" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23619-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The current trunk (development builds) of Wireshark also have a new (I'd guess still "experimental") "export PDUs" functionality that allows one to export PDUs. This can be used, for example, to export decrypted PDUs which can be read in with another copy of Wireshark that does not have any knowledge of the SSL configuration needed/used by the PDU exporter.</p><p>It's still a work in progress but it looks as if it's passed the "proof of concept" phase. AFAICR it already supports exporting TLS/DTLS PDUs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '13, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-23619" class="comments-container"></div><div id="comment-tools-23619" class="comment-tools"></div><div class="clear"></div><div id="comment-23619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23618"></span>

<div id="answer-container-23618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23618-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can export the SSL session keys, which makes it possible to share the tracefile and provide only the keys necessary to decrypt the SSL sessions in the tracefile. This way someone else does not need the private key of the server to decrypt the traffic. It is on the wishlist to be able to save the session keys in the pcapng file, but for now you'll have to do with exporting the session keys to a text file.</p><p>Go to "File -&gt; Export SSL Session Keys..." to export the session keys.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '13, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23618" class="comments-container"></div><div id="comment-tools-23618" class="comment-tools"></div><div class="clear"></div><div id="comment-23618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

