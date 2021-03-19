+++
type = "question"
title = "How do I extract the x509 commonName from a capture of the SSL handshake?"
description = '''How do I extract the x509 commonName from a capture of the SSL handshake? I want all of the subject fields and all of the issuer fields from the signedCertificate(s). This works but only gets the last printableString from the signing authority. tshark -r ssl.pcap -E header=y -T fields -e x509sat.pri...'''
date = "2012-03-23T14:18:00Z"
lastmod = "2012-04-20T13:52:00Z"
weight = 9721
keywords = [ "x509", "ssl", "commonname" ]
aliases = [ "/questions/9721" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I extract the x509 commonName from a capture of the SSL handshake?](/questions/9721/how-do-i-extract-the-x509-commonname-from-a-capture-of-the-ssl-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9721-score" class="post-score" title="current number of votes">0</div><span id="post-9721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I extract the x509 commonName from a capture of the SSL handshake?</p><p>I want all of the subject fields and all of the issuer fields from the signedCertificate(s). This works but only gets the last printableString from the signing authority.</p><pre><code>tshark -r ssl.pcap -E header=y -T fields -e x509sat.printableString</code></pre><p>I want the first certificate and all fields from the subject and issuer. I started using the GUI and looking at the bottom pane to get the names of everything and using tshark -G but no luck so far.</p><p>I am using tshark -v 1.0.3, maybe there have been improvements in this area since this version?</p><p>Any help is appreciated. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-x509" rel="tag" title="see questions tagged &#39;x509&#39;">x509</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-commonname" rel="tag" title="see questions tagged &#39;commonname&#39;">commonname</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '12, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/e53e3a34f0128d92f4a5379b59fac7f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rafs&#39;s gravatar image" /><p><span>rafs</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rafs has one accepted answer">50%</span></p></div></div><div id="comments-container-9721" class="comments-container"><span id="9731"></span><div id="comment-9731" class="comment"><div id="post-9731-score" class="comment-score"></div><div class="comment-text"><p>I discovered the "-V" option and I can work with this, but if there is a way to traverse this tree and selectively print the elements that would be even better.</p></div><div id="comment-9731-info" class="comment-info"><span class="comment-age">(23 Mar '12, 23:54)</span> <span class="comment-user userinfo">rafs</span></div></div><span id="9732"></span><div id="comment-9732" class="comment"><div id="post-9732-score" class="comment-score"></div><div class="comment-text"><p>tshark -r ssl.pcap -R ssl.handshake.certificate -V</p></div><div id="comment-9732-info" class="comment-info"><span class="comment-age">(23 Mar '12, 23:55)</span> <span class="comment-user userinfo">rafs</span></div></div><span id="9738"></span><div id="comment-9738" class="comment"><div id="post-9738-score" class="comment-score"></div><div class="comment-text"><p>I am just wondering if I need to write my own parser or will the tshark parser allow me to get the information I want all as tab delimited fields, one-line per handshake, using the -Tfields option.</p></div><div id="comment-9738-info" class="comment-info"><span class="comment-age">(24 Mar '12, 18:31)</span> <span class="comment-user userinfo">rafs</span></div></div><span id="9740"></span><div id="comment-9740" class="comment"><div id="post-9740-score" class="comment-score"></div><div class="comment-text"><p>The first one works but not the second:</p><p>$ tshark -r $PCAP -R "ssl.handshake.certificate" -Tfields -e x509sat.CountryName</p><p>JP</p><p>$ tshark -r $PCAP -R "ssl.handshake.certificate" -Tfields -e x509sat.CommonName</p></div><div id="comment-9740-info" class="comment-info"><span class="comment-age">(24 Mar '12, 19:04)</span> <span class="comment-user userinfo">rafs</span></div></div><span id="9744"></span><div id="comment-9744" class="comment"><div id="post-9744-score" class="comment-score"></div><div class="comment-text"><p>Does the certificate in question <em>have</em> a commonName? If not, presumably <code>-e x509sat.CommonName</code> won't work.</p></div><div id="comment-9744-info" class="comment-info"><span class="comment-age">(25 Mar '12, 07:20)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="9878"></span><div id="comment-9878" class="comment not_top_scorer"><div id="post-9878-score" class="comment-score"></div><div class="comment-text"><p>yes, it has a id-at-commonName field</p></div><div id="comment-9878-info" class="comment-info"><span class="comment-age">(31 Mar '12, 16:01)</span> <span class="comment-user userinfo">rafs</span></div></div></div><div id="comment-tools-9721" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-9721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="10359"></span>

<div id="answer-container-10359" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10359-score" class="post-score" title="current number of votes">0</div><span id="post-10359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rafs has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, the aggregator field print option does the trick:</p><pre><code>$ tshark -r $PCAP -R &quot;ssl.handshake.certificate&quot; -Tfields -E header=y -E separator=/t -E occurrence=a -E aggregator=\| -e x509sat.CountryName -e x509sat.IA5String -e x509sat.printableString -e x509sat.teletexString -e x509sat.uTF8String -e x509sat.universalString &gt; out

x509sat.CountryName^Ix509sat.IA5String^Ix509sat.printableString^Ix509sat.teletexString^Ix509sat.uTF8String^Ix509sat.universalString$
ZA|US|US|ZA^I^IThawte Consulting (Pty) Ltd.|Thawte SGC CA|California|VeriSign, Inc.|Class 3 Public Primary Certification Authority|Thawte Consulting (Pty) Ltd.|Thawte SGC CA|PrivateLabel3-15^IMountain View|Google Inc|mail.google.com^I^I$</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '12, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/e53e3a34f0128d92f4a5379b59fac7f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rafs&#39;s gravatar image" /><p><span>rafs</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rafs has one accepted answer">50%</span></p></div></div><div id="comments-container-10359" class="comments-container"></div><div id="comment-tools-10359" class="comment-tools"></div><div class="clear"></div><div id="comment-10359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9905"></span>

<div id="answer-container-9905" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9905-score" class="post-score" title="current number of votes">0</div><span id="post-9905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You may have a problem, depending on the character encoding which was used for the various elements of the DN.<br />
By current X509 standards, they should all be either PrintableString or UTF8String (all recipients are required to be able to process those) or BMPString. But some Certificate Authorities (including Verisign) will still use T61String (TeletexString) or IA5String for any DN elements such as CN that contain characters outside the PrintableString character set. Some methods of standard Java certificate handling utilities will not process T61String in the most convenient way, if at all.</p><p>From RFC 2459:</p><p>The DirectoryString type is defined as a choice of PrintableString, TeletexString, BMPString, UTF8String, and UniversalString. The UTF8String encoding is the preferred encoding, <strong>and all certificates issued after December 31, 2003 MUST use the UTF8String encoding of DirectoryString (except as noted below)</strong>. Until that date, conforming CAs MUST choose from the following options when creating a distinguished name, including their own:</p><pre><code>  (a) if the character set is sufficient, the string MAY be
  represented as a PrintableString;

  (b) failing (a), if the BMPString character set is sufficient the
  string MAY be represented as a BMPString; and

  (c) failing (a) and (b), the string MUST be represented as a
  UTF8String.  If (a) or (b) is satisfied, the CA MAY still choose
  to represent the string as a UTF8String.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '12, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p><span>inetdog</span><br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span> </br></p></div></div><div id="comments-container-9905" class="comments-container"><span id="10360"></span><div id="comment-10360" class="comment"><div id="post-10360-score" class="comment-score"></div><div class="comment-text"><p>Thanks, inetdog. I also found this document (<a href="http://www.itu.int/ITU-T/studygroups/com17/languages/X.680-0207.pdf)">http://www.itu.int/ITU-T/studygroups/com17/languages/X.680-0207.pdf)</a> that apparently describes the character set encodings in way more detail than I can follow, but I think I got it.</p></div><div id="comment-10360-info" class="comment-info"><span class="comment-age">(20 Apr '12, 13:52)</span> <span class="comment-user userinfo">rafs</span></div></div></div><div id="comment-tools-9905" class="comment-tools"></div><div class="clear"></div><div id="comment-9905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10358"></span>

<div id="answer-container-10358" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10358-score" class="post-score" title="current number of votes">0</div><span id="post-10358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found what may be the best available solution for this problem.</p><pre><code>$ tshark -r $PCAP -R &quot;ssl.handshake.certificate&quot; -Tfields -E header=y -E separator=/t -E occurrence=a -E aggregator=, -E quote=d -e x509sat.CountryName -e x509sat.IA5String -e x509sat.printableString -e x509sat.teletexString -e x509sat.uTF8String -e x509sat.universalString

$ vi out (with &quot;:set invlist&quot; to display invisible chars)
x509sat.CountryName^Ix509sat.IA5String^Ix509sat.printableString^Ix509sat.teletexString^Ix509sat.uTF8String^Ix509sat.universalString$
&quot;ZA,US,US,ZA&quot;^I^I&quot;Thawte Consulting (Pty) Ltd.,Thawte SGC CA,California,VeriSign, Inc.,Class 3 Public Primary Certification Authority,Thawte Consulting (Pty) Ltd.,Thawte SGC CA,PrivateLabel3-15&quot;^I&quot;Mountain View,Google Inc,mail.google.com&quot;^I^I$</code></pre><p>In my opinion, the "-E quote=d|s|n" is implemented wrong. It should quote the individual fields, e.g. "Mountain View","Google Inc","mail.google.com". The current 1.6.7 version has no way for you to distinguish the x509sat strings that have commas and single quotes in the field values, e.g. sometimes the field value could be something like "Google, Inc.".</p><p>Minor complaint aside, I say thank you to the developers that have contributed their time and talent to wireshark and tshark. This is a great tool. Thank you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '12, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/e53e3a34f0128d92f4a5379b59fac7f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rafs&#39;s gravatar image" /><p><span>rafs</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rafs has one accepted answer">50%</span></p></div></div><div id="comments-container-10358" class="comments-container"></div><div id="comment-tools-10358" class="comment-tools"></div><div class="clear"></div><div id="comment-10358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

