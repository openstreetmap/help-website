+++
type = "question"
title = "SASL GSS-API Privacy"
description = '''Hi, Just wonder if it is possible to decrypt the signed LDAP packets to and from a Windows server. I have disabled LDAP signing on the client and server, plus implemented various registry settings that are also meant to disable this however after binding the next packets are all listed as SASL GSS-A...'''
date = "2012-05-01T04:24:00Z"
lastmod = "2012-05-01T11:51:00Z"
weight = 10545
keywords = [ "windows", "capture", "wireshark", "decryption" ]
aliases = [ "/questions/10545" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SASL GSS-API Privacy](/questions/10545/sasl-gss-api-privacy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10545-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Just wonder if it is possible to decrypt the signed LDAP packets to and from a Windows server. I have disabled LDAP signing on the client and server, plus implemented various registry settings that are also meant to disable this however after binding the next packets are all listed as SASL GSS-API Privacy. The changes have allowed me to see the bind request and response however the next packets are a mystery.</p><p>I'm trying to see the information returned when using Outlook 2007 and the autodiscover process internally (i.e. domain machine on the domain). Supposedly Outlook should query AD for a list of SCP objects and return these and I suspect this information is contain in these signed packets.</p><p>The client is Windows XP SP3 and the server is Windows 2003 R2.</p><p>Anyhelp would be appreciated.</p><p>Kind regards.</p></div><div id="question-tags" class="tags-container tags">windows capture wireshark decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '12, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/5fbcbd3028cfc7ae0dcffe0101e1b621?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ElasticSky&#39;s gravatar image" /><p>ElasticSky<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ElasticSky has no accepted answers">0%</span></p></div></div><div id="comments-container-10545" class="comments-container"></div><div id="comment-tools-10545" class="comment-tools"></div><div class="clear"></div><div id="comment-10545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10550"></span>

<div id="answer-container-10550" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10550-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>GSSS-API decryption should work with the KRB5 decryption of wireshark.</p><p>You'll need to change to protocol preference for KRB5 ("Try to decrypt Kerberos blobs") and you'll need a proper keytab file.</p><p><a href="http://wiki.wireshark.org/Kerberos">http://wiki.wireshark.org/Kerberos</a></p><p>Did you try that?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '12, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-10550" class="comments-container"><span id="10556"></span><div id="comment-10556" class="comment"><div id="post-10556-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for reply - feel like such a noob. Changing the protocol preference for KRB5 did the trick (with a correct keytab of course).</p><p>Thanks for the excellent repy, it is very much appreciated.</p><p>Kind regards.</p></div><div id="comment-10556-info" class="comment-info"><span class="comment-age">(01 May '12, 17:22)</span> ElasticSky</div></div><span id="10560"></span><div id="comment-10560" class="comment"><div id="post-10560-score" class="comment-score"></div><div class="comment-text"><p>Just wondering if you are able to help again :)</p><p>This worked in my lab but when I went to production fails and again I cannot decrypt the packets. The command I'm running to create the keytab file is:</p><p>ktpass /princ [email protected] /pass user-password /crypto RC4-HMAC-NT /ptype KRB5NTPRINCIPAL /out file.name</p><p>NB: ptype does have underscores but the editor ignores them.</p><p>I'm assuming the keytab is wrong which is why I cannot decode the packets however this might be a wrong assumption.</p><p>Thanks in advance.</p></div><div id="comment-10560-info" class="comment-info"><span class="comment-age">(01 May '12, 20:13)</span> ElasticSky</div></div><span id="10562"></span><div id="comment-10562" class="comment"><div id="post-10562-score" class="comment-score"></div><div class="comment-text"><p>1.) just by chance: did you mix up the different keytab files?</p><p>2.) You did not specify the /mapuser param. Is there any reason for that?</p><p>3.) Is there any larger difference between your lab and your production domain?</p><p>4.) Can you please try to use ktexport instead of ktpass (it's also in the wiki)?</p><p>Regards<br />
Kurt</p></div><div id="comment-10562-info" class="comment-info"><span class="comment-age">(01 May '12, 21:15)</span> Kurt Knochner ♦</div></div><span id="10563"></span><div id="comment-10563" class="comment"><div id="post-10563-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Answers as follows: 1) Created a new keytab file using the same command as above as this a different domain and user</p><p>2) Didn't think it was required as not mapping a service/account to a user</p><p>3) LAB is using 2003R2 DC's whereas PROD is 2008 R2**</p><p>4) Running ktexport crashes the lsass.exe service on the DC when run</p><p>** After trying again in the LAB but with a different user I'm again unable to decrypt the packets. This is on the same client but with a different account. Therefore thinking it cannot be the OS version of the DC's.</p><p>Thanks.</p></div><div id="comment-10563-info" class="comment-info"><span class="comment-age">(01 May '12, 21:39)</span> ElasticSky</div></div><span id="10580"></span><div id="comment-10580" class="comment"><div id="post-10580-score" class="comment-score"></div><div class="comment-text"><p>Okay - if I change the "LDAP Client signing requirements" from "Negotiate Signing" to "None" then I can decrypt the packets assuming they are captured while this is set to "None"</p><p>This seems to change the LDAP encryption from SPNEGO - Simple Protected Negotiation to NTLM SSP. This can be decrypted using the keytab from a domain user account. The SPNEGO however can not - not sure what I need to the get the keytab file from if that is possible.</p><p>Unfortunately disabling LDAP signing on a WinXP client connecting to a W2K8R2 DC doesn't seem to work as the client continues to use SPNEGO.</p><p>Thoughts?</p></div><div id="comment-10580-info" class="comment-info"><span class="comment-age">(02 May '12, 03:21)</span> ElasticSky</div></div><span id="10586"></span><div id="comment-10586" class="comment not_top_scorer"><div id="post-10586-score" class="comment-score"></div><div class="comment-text"><p>-- Thoughts?</p><p>I'm trying to understand the problem....</p></div><div id="comment-10586-info" class="comment-info"><span class="comment-age">(02 May '12, 04:38)</span> Kurt Knochner ♦</div></div><span id="10620"></span><div id="comment-10620" class="comment not_top_scorer"><div id="post-10620-score" class="comment-score"></div><div class="comment-text"><p>Okay - I hope this helps: What keytab file would I need to generate in order to decrypt packets using Simple Protected Negotiation authentication?</p><p>With a WinXP client connecting to a 2008R2 DC it does not appear to negotiate down to NTLM authentication and therefore I cannot decrypt the packets using the user account keytab.</p></div><div id="comment-10620-info" class="comment-info"><span class="comment-age">(02 May '12, 22:07)</span> ElasticSky</div></div></div><div id="comment-tools-10550" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-10550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

