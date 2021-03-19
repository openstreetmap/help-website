+++
type = "question"
title = "Trouble getting Exported PFX file to Import and Decrypt HTTPS Traffic"
description = '''I&#x27;m getting the following error from Wireshark: error in column &#x27;Password&#x27;: Could not load PKCS#12 key file: could not load PKCS#12 in PEM format: Base64 unexpected header error.  Do I need to convert this? I tried using openssl with the following: C:&#92;Projects&#92;openssl&amp;gt;C:&#92;OpenSSL-Win32&#92;bin&#92;openssl...'''
date = "2015-11-02T09:21:00Z"
lastmod = "2015-11-05T12:39:00Z"
weight = 47162
keywords = [ "pfx", "https", "ssl" ]
aliases = [ "/questions/47162" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trouble getting Exported PFX file to Import and Decrypt HTTPS Traffic](/questions/47162/trouble-getting-exported-pfx-file-to-import-and-decrypt-https-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47162-score" class="post-score" title="current number of votes">0</div><span id="post-47162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting the following error from Wireshark:</p><pre><code>error in column &#39;Password&#39;: Could not
load PKCS#12 key file: could not load
PKCS#12 in PEM format: Base64
unexpected header error.</code></pre><p>Do I need to convert this? I tried using openssl with the following:</p><pre><code>C:\Projects\openssl&gt;C:\OpenSSL-Win32\bin\openssl.exe pkcs12 -in ExportedCert.pfx -nocerts -out key.pem -nodes
7736:error:0D0680A8:asn1 encoding routines:ASN1_CHECK_TLEN:wrong tag:.\crypto\asn1\tasn_dec.c:1198:
7736:error:0D07803A:asn1 encoding routines:ASN1_ITEM_EX_D2I:nested asn1 error:.\crypto\asn1\tasn_dec.c:372:Type=PKCS12</code></pre><p>I also tried converting it to a Base64 encoded binary format, but had trouble:</p><pre><code>C:\Projects\openssl&gt;C:\OpenSSL-Win32\bin\openssl.exe pkcs12 -in DEVexportcert1.pfx -out Devexportcert1.pem -nodes
7676:error:0D0680A8:asn1 encoding routines:ASN1_CHECK_TLEN:wrong tag:.\crypto\asn1\tasn_dec.c:1198:
7676:error:0D07803A:asn1 encoding routines:ASN1_ITEM_EX_D2I:nested asn1 error:.\crypto\asn1\tasn_dec.c:372:Type=PKCS12</code></pre><p>Is there a specific format Wireshark requires? What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pfx" rel="tag" title="see questions tagged &#39;pfx&#39;">pfx</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '15, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/cbd494ff2fbf08ed8b4c69ce781e1409?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="justdan23&#39;s gravatar image" /><p><span>justdan23</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="justdan23 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Nov '15, 09:26</strong> </span></p></div></div><div id="comments-container-47162" class="comments-container"><span id="47164"></span><div id="comment-47164" class="comment"><div id="post-47164-score" class="comment-score"></div><div class="comment-text"><p>Can you use openssl to check the pfx?</p><p><code>openssl pkcs12 -info -in ExportedCert.pfx</code></p></div><div id="comment-47164-info" class="comment-info"><span class="comment-age">(02 Nov '15, 10:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="47166"></span><div id="comment-47166" class="comment"><div id="post-47166-score" class="comment-score"></div><div class="comment-text"><p>I get the same error:</p><pre><code>C:\Projects\openssl&gt;C:\OpenSSL-Win32\bin\openssl.exe pkcs12 -info -in ExportedCert.pfx
3100:error:0D0680A8:asn1 encoding routines:ASN1_CHECK_TLEN:wrong tag:.\crypto\asn1\tasn_dec.c:1198:
3100:error:0D07803A:asn1 encoding routines:ASN1_ITEM_EX_D2I:nested asn1 error:.\crypto\asn1\tasn_dec.c:372:Type=PKCS12</code></pre><p>I generated a new one with openssl and the generated one is a binary format; unlike the original one which has "BEGIN CERTIFICATE" at the top.</p><p>Wireshark liked the generated version. So I suspect this is a PEM file of only the Certificate? And not a PFX?</p></div><div id="comment-47166-info" class="comment-info"><span class="comment-age">(02 Nov '15, 10:19)</span> <span class="comment-user userinfo">justdan23</span></div></div><span id="47175"></span><div id="comment-47175" class="comment"><div id="post-47175-score" class="comment-score">1</div><div class="comment-text"><p>pkcs#12 is a binary container. If you can read "BEGIN CERTIFICATE" then it's not a pcks#12 container.</p></div><div id="comment-47175-info" class="comment-info"><span class="comment-age">(02 Nov '15, 16:10)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47313"></span><div id="comment-47313" class="comment"><div id="post-47313-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I exported the pfx from IIS and added it successfully to Wireshark.</p></div><div id="comment-47313-info" class="comment-info"><span class="comment-age">(05 Nov '15, 12:39)</span> <span class="comment-user userinfo">justdan23</span></div></div></div><div id="comment-tools-47162" class="comment-tools"></div><div class="clear"></div><div id="comment-47162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

