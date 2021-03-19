+++
type = "question"
title = "Unknown CA site"
description = '''Hi, I have analyzed the comunication from my server to site credemtel and I have one anomaly. In source my server and destination credemtel server I have &quot;Alert (level: Fatal, Description: Unknown CA)&quot;. What does this mean? The server does not recognize CA to the site credemtel? What should I do? Th...'''
date = "2017-07-20T02:47:00Z"
lastmod = "2017-07-21T09:30:00Z"
weight = 62916
keywords = [ "unknown", "authority", "certificate" ]
aliases = [ "/questions/62916" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unknown CA site](/questions/62916/unknown-ca-site)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62916-score" class="post-score" title="current number of votes">0</div><span id="post-62916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,<br />
I have analyzed the comunication from my server to site credemtel and I have one anomaly. In source my server and destination credemtel server I have <em>"Alert (level: Fatal, Description: Unknown CA)"</em>. What does this mean? The server does not recognize CA to the site credemtel? What should I do?</p><p>Thank you. Best regard</p><p>Riccardo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unknown" rel="tag" title="see questions tagged &#39;unknown&#39;">unknown</span> <span class="post-tag tag-link-authority" rel="tag" title="see questions tagged &#39;authority&#39;">authority</span> <span class="post-tag tag-link-certificate" rel="tag" title="see questions tagged &#39;certificate&#39;">certificate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jul '17, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/e8830ff77184c9f7c1acb6a5c0594259?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Riccardo1987&#39;s gravatar image" /><p><span>Riccardo1987</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Riccardo1987 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jul '17, 06:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-62916" class="comments-container"><span id="62924"></span><div id="comment-62924" class="comment"><div id="post-62924-score" class="comment-score">1</div><div class="comment-text"><p>My wild guess would be that the sender of that Alert message did not like the other party's certificate because the latter refers to an unknown Certification Authority (CA). As you haven't provided the capture, I don't know which side complains, so I cannot suggest what to do.</p></div><div id="comment-62924-info" class="comment-info"><span class="comment-age">(20 Jul '17, 04:48)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62965"></span><div id="comment-62965" class="comment"><div id="post-62965-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy, where can i send you the capture?</p></div><div id="comment-62965-info" class="comment-info"><span class="comment-age">(21 Jul '17, 02:26)</span> <span class="comment-user userinfo">Riccardo1987</span></div></div><span id="62971"></span><div id="comment-62971" class="comment"><div id="post-62971-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc?</p></div><div id="comment-62971-info" class="comment-info"><span class="comment-age">(21 Jul '17, 02:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="62972"></span><div id="comment-62972" class="comment"><div id="post-62972-score" class="comment-score"></div><div class="comment-text"><p>I activate cloudshark . The ip destination is ip.addr ==193.43.5.203 . The site for view packet is <a href="https://www.cloudshark.org/captures/de953fadb58d">https://www.cloudshark.org/captures/de953fadb58d</a></p><p>Thank you</p></div><div id="comment-62972-info" class="comment-info"><span class="comment-age">(21 Jul '17, 03:04)</span> <span class="comment-user userinfo">Riccardo1987</span></div></div></div><div id="comment-tools-62916" class="comment-tools"></div><div class="clear"></div><div id="comment-62916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62978"></span>

<div id="answer-container-62978" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62978-score" class="post-score" title="current number of votes">0</div><span id="post-62978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The certificates all look good to me, I suspect that there is an issue on the client machine where it's unable to verify the certificate chain.</p><p>I (on Windows) extracted the certificates using tshark and then converted the hex strings to binary with PowerShell and then used certutil to verify:</p><pre><code># Use tshark to extract the certificate bytes
$x = tshark -r pi.cap -Y &quot;frame.number == 201&quot; -T fields -e ssl.handshake.certificate

# split the certs at the comma
$c1, $c2, $c3 = $x -split &quot;,+&quot;

# Convert strings of &quot;xx:xx...&quot; to bytes in a binary array
$b1 = @( $c1 -split &quot;:+&quot; | foreach-object { [System.Convert]::ToByte($_,16) } )
$b2 = @( $c2 -split &quot;:+&quot; | foreach-object { [System.Convert]::ToByte($_,16) } )
$b3 = @( $c3 -split &quot;:+&quot; | foreach-object { [System.Convert]::ToByte($_,16) } )

# Output the byte arrays to files
$b1 | Set-Content -Encoding Byte -Path cert1.der
$b2 | Set-Content -Encoding Byte -Path cert2.der
$b3 | Set-Content -Encoding Byte -Path cert3.der

# Use certutil to verify the cert chain
certutil -verify cert1.der cert2.der
certutil -verify cert2.der cert3.der

# Use certutil to very the root CA cert
certutil -verify cert3.der</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '17, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-62978" class="comments-container"><span id="62979"></span><div id="comment-62979" class="comment"><div id="post-62979-score" class="comment-score"></div><div class="comment-text"><p>The problem is on server 10.0.1.1?</p></div><div id="comment-62979-info" class="comment-info"><span class="comment-age">(21 Jul '17, 08:01)</span> <span class="comment-user userinfo">Riccardo1987</span></div></div><span id="62980"></span><div id="comment-62980" class="comment"><div id="post-62980-score" class="comment-score"></div><div class="comment-text"><p>Yes. Whatever software is running there is unable to verify the certifcate chain.</p></div><div id="comment-62980-info" class="comment-info"><span class="comment-age">(21 Jul '17, 08:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="62984"></span><div id="comment-62984" class="comment"><div id="post-62984-score" class="comment-score"></div><div class="comment-text"><p>Sorry Grahamb, i am not expert in this argument. Can you send/share cert3.der?</p><p>Thank you so much.</p></div><div id="comment-62984-info" class="comment-info"><span class="comment-age">(21 Jul '17, 08:45)</span> <span class="comment-user userinfo">Riccardo1987</span></div></div><span id="62987"></span><div id="comment-62987" class="comment"><div id="post-62987-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Can you send/share cert3.der?</p></blockquote><p>Not that doing so would be impossible, but if any root CA certificate should serve its purpose, you must never trust the one extracted from the certificate chain in server hello packet. Instead, you should obtain it via some other path, as the server operator might have forged it.</p><p>In this particular case, you have <a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a>'s word that he's tested it (<code>certutil</code> checks a root certificate by locating it in the root certificate store on the machine where it is running), and you have no sane reason to assume that <a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> acts in malicious agreement with the operator of the server which has provided that server hello packet, but in general this is a wrong way.</p><p>So what about downloading it from <a href="https://www.digicert.com/digicert-root-certificates.htm">DigiCert's web</a>?</p><p>Could be a better idea, but remember, I may have myself forged both the web you are accessing and the whole DigiCert's web.</p><p>So as for me, the best idea is to try to open that web on another machine within your reach which does have that DigiCert's certificate pre-installed in its trusted CA certificate store, and if it works fine, to export the certificate from that machine's trusted certificate store into a file and import that file on your machine.</p></div><div id="comment-62987-info" class="comment-info"><span class="comment-age">(21 Jul '17, 09:30)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62978" class="comment-tools"></div><div class="clear"></div><div id="comment-62978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

