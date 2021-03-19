+++
type = "question"
title = "not able to decrypt ssl traffic in wireshark using SessionID and MasterKey"
description = '''Hi, I am trying to decrypt SSL traffic in wireshark . I dont have server given private key but instead I am trying with SessionID and Master key. I have exported the key file under Edit-&amp;gt;Preferences-&amp;gt;Protocols-&amp;gt;SSL -&amp;gt; (Pre)-Master-Secret log filename option. Still Wireshark is not able t...'''
date = "2014-01-17T02:30:00Z"
lastmod = "2014-06-30T10:40:00Z"
weight = 28989
keywords = [ "ssl" ]
aliases = [ "/questions/28989" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [not able to decrypt ssl traffic in wireshark using SessionID and MasterKey](/questions/28989/not-able-to-decrypt-ssl-traffic-in-wireshark-using-sessionid-and-masterkey)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28989-score" class="post-score" title="current number of votes">1</div><span id="post-28989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to decrypt SSL traffic in wireshark . I dont have server given private key but instead I am trying with SessionID and Master key. I have exported the key file under Edit-&gt;Preferences-&gt;Protocols-&gt;SSL -&gt; (Pre)-Master-Secret log filename option. Still Wireshark is not able to decrypt SSL traffic. Need help on this. I am using wireshark 1.10.5. Below is the configuration I have used. Running openssl server on linux box. openssl client on windows xp. Using self signed certificate.</p><h2 id="linux">Linux:</h2><p>openssl req -new -x509 -out server.cert -keyout server.pem ..... openssl s_server -www -cipher AES256-SHA -cert server.cert -key server.pem ......</p><h2 id="windows-xp">Windows xp:</h2><p>openssl s_client -connect &lt;ipaddress: 4443=""&gt; ...... GET / HTTP/1.0 .......</p><p>Example session_key.key file</p><p>RSA Session-ID:0E1A3AAD99A68936E242D4BB2A2F66197F466FD7883D5AA604B9EF5EFC6EF5EE Master-Key:8186F7C4137167EFD92298F01FC07C0236DDC016BD1C3B559F17C87F63270945C975B37CBE24D29A44B0ED9643D59D1F</p><p>Appreciate any help.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '14, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/5d2712bfddd1a234a320326af07e34da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Phani&#39;s gravatar image" /><p><span>Phani</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Phani has no accepted answers">0%</span></p></div></div><div id="comments-container-28989" class="comments-container"><span id="34296"></span><div id="comment-34296" class="comment"><div id="post-34296-score" class="comment-score"></div><div class="comment-text"><p>Still having this problem with Wireshark 1.11.x or 1.12.x?</p></div><div id="comment-34296-info" class="comment-info"><span class="comment-age">(30 Jun '14, 10:40)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-28989" class="comment-tools"></div><div class="clear"></div><div id="comment-28989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

