+++
type = "question"
title = "Https traffic can not be decrypted"
description = '''Hi, I&#x27;m sorry , my English is not good defense .  I have a problem in decoding htpps pages. I have tested the following page . http://www.foteviken.de/?p=2227 I have the address 78.47.216.236 , port 443 and http protocol , key file in text format . ( Key File is https://test.foteviken.de/ on the tes...'''
date = "2015-02-05T00:56:00Z"
lastmod = "2015-02-10T02:16:00Z"
weight = 39657
keywords = [ "https" ]
aliases = [ "/questions/39657" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Https traffic can not be decrypted](/questions/39657/https-traffic-can-not-be-decrypted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39657-score" class="post-score" title="current number of votes">0</div><span id="post-39657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm sorry , my English is not good defense . I have a problem in decoding htpps pages. I have tested the following page . <a href="http://www.foteviken.de/?p=2227">http://www.foteviken.de/?p=2227</a> I have the address 78.47.216.236 , port 443 and http protocol , key file in text format . ( Key File is <a href="https://test.foteviken.de/">https://test.foteviken.de/</a> on the test page)<br />
The log file is plain text , which is not any but . The plaintext is still encrypted. What am I doing wrong ? Can Wiresahrk ever decrypt https traffic?</p><p>My system : Win 8.1, Wireshark 1.12.3 , Firefox 35.0.1</p><p>... With a man in the middle proxy test page can be decrypted.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '15, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/5446c7bc71a648d1fa12429c56c7147e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="melli&#39;s gravatar image" /><p><span>melli</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="melli has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-39657" class="comments-container"><span id="39665"></span><div id="comment-39665" class="comment"><div id="post-39665-score" class="comment-score"></div><div class="comment-text"><p>umm the cipher being used is tls_dhe_rsa which according to my research wireshark doesnt support(?) in your https data..U can check in server hello for the cipher suite..It must be tls_rsa_some_algo.I think thats the problem.</p></div><div id="comment-39665-info" class="comment-info"><span class="comment-age">(05 Feb '15, 06:22)</span> <span class="comment-user userinfo">koundi</span></div></div><span id="39672"></span><div id="comment-39672" class="comment"><div id="post-39672-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your quick response. The Diffie-Hellman algorithm can not Wireshark I know. But I have my browser (Firefox) in the about: config set all ... ssl3.dhe_rsa_ .... to false.</p><p>Still do not understand why this does not work.</p></div><div id="comment-39672-info" class="comment-info"><span class="comment-age">(05 Feb '15, 10:53)</span> <span class="comment-user userinfo">melli</span></div></div><span id="39749"></span><div id="comment-39749" class="comment"><div id="post-39749-score" class="comment-score"></div><div class="comment-text"><p>so in wireshark capture what is the cipher suite that is being displayed in the server hello?? if it is tls_rsa only then it can be done...because when i tried doing the same thing from my pc ..my wireshark capture server hello had dhe_rsa as the cipher suite!!</p></div><div id="comment-39749-info" class="comment-info"><span class="comment-age">(10 Feb '15, 02:16)</span> <span class="comment-user userinfo">koundi</span></div></div></div><div id="comment-tools-39657" class="comment-tools"></div><div class="clear"></div><div id="comment-39657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

