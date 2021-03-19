+++
type = "question"
title = "Private PC - need to decipher data"
description = '''Hi, need help. I&#x27;ve been capturing data for a while now and need to analyse it but need to decrypt it. Could someone please show me where or explain the procedure step by step (dummy style) so that I will be able to read the data in a more english format. Is this possible? Have had IT experience but...'''
date = "2014-12-04T11:59:00Z"
lastmod = "2014-12-06T12:04:00Z"
weight = 38337
keywords = [ "decipher", "decrypt", "help" ]
aliases = [ "/questions/38337" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Private PC - need to decipher data](/questions/38337/private-pc-need-to-decipher-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38337-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, need help. I've been capturing data for a while now and need to analyse it but need to decrypt it. Could someone please show me where or explain the procedure step by step (dummy style) so that I will be able to read the data in a more english format. Is this possible? Have had IT experience but more in software development rather than this side. My internet activity shot up and that is why I am investigating.</p><p>TIA</p></div><div id="question-tags" class="tags-container tags">decipher decrypt help</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '14, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/9e84f6c1cdd827e7848d8176bf78325a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Der&#39;s gravatar image" /><p>Der<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Der has no accepted answers">0%</span></p></div></div><div id="comments-container-38337" class="comments-container"><span id="38341"></span><div id="comment-38341" class="comment"><div id="post-38341-score" class="comment-score"></div><div class="comment-text"><p>There are several protocols that encrypt data: 802.11 encrypts it on "protected" networks (networks using WEP or WPA/WPA2), SSL encrypts it when used for services such as HTTP ("https") and mail, and so on. What form of encryption are you seeing?</p></div><div id="comment-38341-info" class="comment-info"><span class="comment-age">(04 Dec '14, 17:34)</span> Guy Harris ♦♦</div></div><span id="38389"></span><div id="comment-38389" class="comment"><div id="post-38389-score" class="comment-score"></div><div class="comment-text"><p>will answer tomorrow with an example thanks</p></div><div id="comment-38389-info" class="comment-info"><span class="comment-age">(06 Dec '14, 03:01)</span> Der</div></div><span id="38397"></span><div id="comment-38397" class="comment"><div id="post-38397-score" class="comment-score"></div><div class="comment-text"><p>can't upload image but this is typed copy TLSV1.2 Record layer: Handshake protocol: Encryted handshake message . . then follows a lot of hex chars on the left and other characters on right the only understandable characters on the right are http in this case. Many other examples as well including "application data". What I'd like is for all that data (left / right to be decoded if possible.</p><p>Basically if possible I'd like to see as much of my normal internet activity decoded and readable as I seem to have much more activity going on than I should have! Plain PC via wireless modem to a few web pages and a few product updates. In my IP stats I see sites that as far as my activity is concerned I shouldn't have gone near so I want to see what is happening if I can... Thinking of just blocking all these sites via host but would like to investigate if possible. Thanks, hope this help you help me :)</p></div><div id="comment-38397-info" class="comment-info"><span class="comment-age">(06 Dec '14, 11:12)</span> Der</div></div></div><div id="comment-tools-38337" class="comment-tools"></div><div class="clear"></div><div id="comment-38337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38398"></span>

<div id="answer-container-38398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38398-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, that's SSL/TLS encryption.</p><p>Wireshark can, in some cases, decrypt that; see <a href="http://wiki.wireshark.org/SSL">the SSL page in the Wireshark Wiki</a> for some information on how to do that.</p><p>It cannot, however, <em>always</em> decrypt it. You may have to use a proxy tool, such as <a href="http://www.telerik.com/fiddler">Fiddler</a>, to see some of it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '14, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-38398" class="comments-container"><span id="38401"></span><div id="comment-38401" class="comment"><div id="post-38401-score" class="comment-score"></div><div class="comment-text"><p>much appreciated thanks</p></div><div id="comment-38401-info" class="comment-info"><span class="comment-age">(06 Dec '14, 16:33)</span> Der</div></div></div><div id="comment-tools-38398" class="comment-tools"></div><div class="clear"></div><div id="comment-38398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

