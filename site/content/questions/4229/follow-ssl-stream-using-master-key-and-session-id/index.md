+++
type = "question"
title = "Follow SSL stream using Master-key and Session-ID"
description = '''Hello I&#x27;m debugging my SSL application and would be great if I could capture SSL stream using Wireshark and then follow it decrypted. It is not possible to obtain server&#x27;s private key in my case But as a client application I can read the whole stream fine and can dump all needed information for decr...'''
date = "2011-05-25T03:22:00Z"
lastmod = "2013-09-14T10:57:00Z"
weight = 4229
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/4229" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Follow SSL stream using Master-key and Session-ID](/questions/4229/follow-ssl-stream-using-master-key-and-session-id)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4229-score" class="post-score" title="current number of votes">5</div><span id="post-4229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">3</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I'm debugging my SSL application and would be great if I could capture SSL stream using Wireshark and then follow it decrypted. It is not possible to obtain server's private key in my case</p><p>But as a client application I can read the whole stream fine and can dump all needed information for decryption, like Session-ID and Master-key, ex:</p><pre><code>&gt; openssl s_client -connect mail.google.com:443 -ssl3

Loading &#39;screen&#39; into random state - done
CONNECTED(00000180)
depth=1 /C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
verify error:num=20:unable to get local issuer certificate
verify return:0
---
Certificate chain
 0 s:/C=US/ST=California/L=Mountain View/O=Google Inc/CN=mail.google.com
   i:/C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
 1 s:/C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
   i:/C=US/O=VeriSign, Inc./OU=Class 3 Public Primary Certification Authority
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDIjCCAougAwIBAgIQHxn23jXdY6FCkYrVLMCrEjANBgkqhkiG9w0BAQUFADBM
MQswCQYDVQQGEwJaQTElMCMGA1UEChMcVGhhd3RlIENvbnN1bHRpbmcgKFB0eSkg
THRkLjEWMBQGA1UEAxMNVGhhd3RlIFNHQyBDQTAeFw0wOTEyMTgwMDAwMDBaFw0x
MTEyMTgyMzU5NTlaMGkxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlh
MRYwFAYDVQQHFA1Nb3VudGFpbiBWaWV3MRMwEQYDVQQKFApHb29nbGUgSW5jMRgw
FgYDVQQDFA9tYWlsLmdvb2dsZS5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJ
AoGBANknyBHye+RFyUa2Y3WDsXd+F0GJgDjxRSegPNnoqABL2QfQut7t9CymrNwn
E+wMwaaZF0LmjSfSgRSwS4L6ssXQuyBZYiijlrVh9nbBbUbS/brGDz3RyXeaWDP2
BnYyrVFfKV9u+BKLrebFCDmzQ0OpW5Ed1+PPUd91WY6NgKtTAgMBAAGjgecwgeQw
DAYDVR0TAQH/BAIwADA2BgNVHR8ELzAtMCugKaAnhiVodHRwOi8vY3JsLnRoYXd0
ZS5jb20vVGhhd3RlU0dDQ0EuY3JsMCgGA1UdJQQhMB8GCCsGAQUFBwMBBggrBgEF
BQcDAgYJYIZIAYb4QgQBMHIGCCsGAQUFBwEBBGYwZDAiBggrBgEFBQcwAYYWaHR0
cDovL29jc3AudGhhd3RlLmNvbTA+BggrBgEFBQcwAoYyaHR0cDovL3d3dy50aGF3
dGUuY29tL3JlcG9zaXRvcnkvVGhhd3RlX1NHQ19DQS5jcnQwDQYJKoZIhvcNAQEF
BQADgYEAicju7fexy+yRP2drx57Tcqo+BElR1CiHNZ1nhPmS9QSZaudDA8jy25IP
VWvjEgaq13Hro0Hg32ZNVK53qcXwjWtnCAReojvNwj6/x1Ciq5B6D7E6eiYDSfXJ
8/a2vR5IbgY89nq+wuHaA6vspH6vNR848xO3z1PQ7BrIjnYQ1A0=
-----END CERTIFICATE-----
subject=/C=US/ST=California/L=Mountain View/O=Google Inc/CN=mail.google.com
issuer=/C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
---
No client certificate CA names sent
---
SSL handshake has read 1797 bytes and written 296 bytes
---
New, TLSv1/SSLv3, Cipher is RC4-SHA
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : SSLv3
    Cipher    : RC4-SHA
    Session-ID: B5AEB800F43F96A9BAD007A5D26423E43479B904166FA72A4789DEA15A830E26
    Session-ID-ctx:
    Master-Key: 454AD3030F0AE8234508DF959EF533675E225BBB388EE5F80A20A007BAB63E1ABB972F39401796FB02F27AF95AB083A4
    Key-Arg   : None
    Start Time: 1306318364
    Timeout   : 7200 (sec)
    Verify return code: 20 (unable to get local issuer certificate)
---</code></pre><p>Is it possible somehow to follow decrypted stream in Wireshark without server's private key but having client's Master-Key and Session-ID?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '11, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/a2752a013d4ecddfaab3e4d7c43a464c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tosiara&#39;s gravatar image" /><p><span>tosiara</span><br />
<span class="score" title="81 reputation points">81</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tosiara has no accepted answers">0%</span></p></div></div><div id="comments-container-4229" class="comments-container"></div><div id="comment-tools-4229" class="comment-tools"></div><div class="clear"></div><div id="comment-4229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4238"></span>

<div id="answer-container-4238" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4238-score" class="post-score" title="current number of votes">6</div><span id="post-4238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tosiara has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, forget my last answer... as of today, it <strong>is</strong> possible to use the "openssl s_client" output to do decryption. I added this to the keylog option that was already there. You can now use the format:</p><pre><code>RSA Session-ID:xxxx Master-Key:xxxx</code></pre><p>In the key log file to decrypt the session. In your case that would be:</p><pre><code>RSA Session-ID:B5AEB800F43F96A9BAD007A5D26423E43479B904166FA72A4789DEA15A830E26 Master-Key:454AD3030F0AE8234508DF959EF533675E225BBB388EE5F80A20A007BAB63E1ABB972F39401796FB02F27AF95AB083A4</code></pre><p>You will need to build your own version from "trunk" or use an <a href="http://www.wireshark.org/download/automated/">automated build</a> which will be available in a couple of hours. Please use a version with a number higher or equal to 37401.</p><p>I hope this works for you :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '11, 14:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4238" class="comments-container"><span id="4243"></span><div id="comment-4243" class="comment"><div id="post-4243-score" class="comment-score"></div><div class="comment-text"><p>Great, that works!!! Thank you very much!</p><p>Only one small note: if keylog file does not contain trailing CRLF I receive this error:</p><p><code>trying to use SSL keylog in c:\rsa.log   checking keylog line: RSA Session-ID:451C00005EC950112D2156C2FDC29BB71A3CA320CEE28FC2DA786AD6F5E5102E Master-Key:DD81A0D7D526740CDEB1AB6DE421102F52C781547A06F6A6480D6055846BB7FFB8CCBCB09FC1A38CC4610135F0F17C4     line contains non-hex chars in master secret</code></p><p>But after adding CRLF at the end - all works perfect!</p></div><div id="comment-4243-info" class="comment-info"><span class="comment-age">(26 May '11, 03:22)</span> <span class="comment-user userinfo">tosiara</span></div></div><span id="4244"></span><div id="comment-4244" class="comment"><div id="post-4244-score" class="comment-score"></div><div class="comment-text"><p>I'm glad it works for you too :-)</p><p>Indeed the code requires all lines to be terminated with a newline character.</p></div><div id="comment-4244-info" class="comment-info"><span class="comment-age">(26 May '11, 04:59)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="24687"></span><div id="comment-24687" class="comment"><div id="post-24687-score" class="comment-score"></div><div class="comment-text"><p>Although the <code>s_client</code> shows a Session-ID, this will be useless if it is not sent to the server (<code>Session-ID 0</code> in the capture). You can still try to match a known master key with a request using <code>CLIENT_RANDOM</code> by looking at the traffic. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9144#c5">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9144#c5</a> for parsing <code>s_client</code> output to generate a <code>CLIENT_RANDOM</code> line.</p></div><div id="comment-24687-info" class="comment-info"><span class="comment-age">(14 Sep '13, 10:57)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-4238" class="comment-tools"></div><div class="clear"></div><div id="comment-4238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4230"></span>

<div id="answer-container-4230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4230-score" class="post-score" title="current number of votes">2</div><span id="post-4230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>At the moment "No, not directly". There has been code added that reads in a file with a list of decrypted PreMasterSecrets, indexed by the first 8 bytes (IIRC) of the Encrypted PreMasterSecret. It has been added by a developer that also added a debug option to the SSL library of Firefox/Chrome to export this data (see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4349">Bug 4349</a>)</p><p>So at the moment, you might be able to fabricate the file yourself based on the tracefile and the "openssl s_client" output. In the future there might be more options added to import/export session keys to make decryption possible without obtaining (or exposing) the private key.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '11, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4230" class="comments-container"><span id="4231"></span><div id="comment-4231" class="comment"><div id="post-4231-score" class="comment-score"></div><div class="comment-text"><p>I'm glad you knew this SYN..my knee-jerk reaction to this question was "No - never". It makes sense that this would be possible, but considering the work necessary on the user end I figured it would never be an option.</p></div><div id="comment-4231-info" class="comment-info"><span class="comment-age">(25 May '11, 08:16)</span> <span class="comment-user userinfo">GeonJay</span></div></div><span id="4234"></span><div id="comment-4234" class="comment"><div id="post-4234-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, the route of creating a keylog file yourself based on the openssl s_client output won't work. I just tried it myself, but the input from the key-log file is a PreMasterSecret, while the output of openssl s_cient is the MasterSecret.</p><p>I need to dig into SSL some more again to see whether the MasterSecret contains enough information to decrypt the session. If it does, then it is possible to extend the decryption engine to also take the MasterSecret from the s_client output. But someone needs to find the time to code it...</p></div><div id="comment-4234-info" class="comment-info"><span class="comment-age">(25 May '11, 09:28)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-4230" class="comment-tools"></div><div class="clear"></div><div id="comment-4230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

