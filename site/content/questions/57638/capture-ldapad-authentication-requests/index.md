+++
type = "question"
title = "capture LDAP/AD authentication requests"
description = '''I have an apache server where the .htaccess file on a specific directory look like this: AuthType CAS AuthName &quot;Network Services&quot; AuthLDAPUrl &quot;ldaps://ldap.here.ca/ou=people,dc=here,dc=com?uid?sub?(objectclass=*)&quot; AuthLDAPBindDN uid=user1,ou=nsids,ou=people,dc=here,dc=com AuthLDAPBindPassword &amp;lt;pa...'''
date = "2016-11-25T09:42:00Z"
lastmod = "2016-11-26T12:44:00Z"
weight = 57638
keywords = [ "apache", "active", "directory", "ldap" ]
aliases = [ "/questions/57638" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capture LDAP/AD authentication requests](/questions/57638/capture-ldapad-authentication-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57638-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an apache server where the .htaccess file on a specific directory look like this:</p><p>AuthType CAS<br />
AuthName "Network Services"<br />
AuthLDAPUrl "ldaps://ldap.here.ca/ou=people,dc=here,dc=com?uid?sub?(objectclass=*)"<br />
AuthLDAPBindDN uid=user1,ou=nsids,ou=people,dc=here,dc=com<br />
AuthLDAPBindPassword &lt;password&gt;<br />
<br />
Require ldap-group cn=xct_staff,ou=ancillaryGroups,ou=groups,dc=here,dc=com<br />
</p><p>what I want to do is capthere all the traffic going to and coming from ldap.here.ca when the Require ldap-group is being used I tried ldap||msdp but no luck anyone have an idea I can try?</p></div><div id="question-tags" class="tags-container tags">apache active directory ldap</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '16, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/4537d314d22bc237cef6559c45b6d0ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="merrittr&#39;s gravatar image" /><p>merrittr<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="merrittr has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-57638" class="comments-container"></div><div id="comment-tools-57638" class="comment-tools"></div><div class="clear"></div><div id="comment-57638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57647"></span>

<div id="answer-container-57647" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57647-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello</p><p>I am newish to Wireshark, but I may be able to offer a tip. I believe I have the basics of your question (although I am not sure about the ldap-group part of your question)</p><p>Any way start of with</p><p>LDAP &amp;&amp; (tcp contains ldap.here.ca || udp contains ldap.here.ca)</p><p>Hope this is some assistance</p><p>Ernie</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '16, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/ff39c11ae2cb05528da757366e76d84b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EBrant&#39;s gravatar image" /><p>EBrant<br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EBrant has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-57647" class="comments-container"><span id="57649"></span><div id="comment-57649" class="comment"><div id="post-57649-score" class="comment-score"></div><div class="comment-text"><p>err... I believe <code>ldap.here.ca</code> in the example is an FQDN, not an IP number, so <code>udp contains "ldap.here.ca"</code> would show packets which contain that string. Unfortunately, the FQDN of the LDAP server is not sent inside the LDAP PDUs themselves, so it won't show anything.</p></div><div id="comment-57649-info" class="comment-info"><span class="comment-age">(26 Nov '16, 12:01)</span> sindy</div></div><span id="57651"></span><div id="comment-57651" class="comment"><div id="post-57651-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy, thanks for the info, I am new to Wireshark so learning too :) thanks for the tip, I hope someone can answer Merrittr's question</p><p>Ernue</p></div><div id="comment-57651-info" class="comment-info"><span class="comment-age">(26 Nov '16, 12:14)</span> EBrant</div></div><span id="57652"></span><div id="comment-57652" class="comment"><div id="post-57652-score" class="comment-score"></div><div class="comment-text"><p>working on it ;-)</p><p>I've converted your previous post from an Answer (which it wasn't as it did not answer the original Question) to a Comment.</p></div><div id="comment-57652-info" class="comment-info"><span class="comment-age">(26 Nov '16, 12:22)</span> sindy</div></div></div><div id="comment-tools-57647" class="comment-tools"></div><div class="clear"></div><div id="comment-57647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57653"></span>

<div id="answer-container-57653" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57653-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are two key aspects here.</p><p>First, a display filter expression <code>ldap</code> only matches frames for which the LDAP dissector has been successfully invoked. As your configuration requires use of LDAP<strong>S</strong> (secure), the dissection ends at the TLS layer unless you provide sufficient key material and configuration (see details at <a href="https://wiki.wireshark.org/SSL">Wireshark wiki</a>). If you don't, the undecrypted TLS payload is shown as just "Encrypted Application Data" in the dissection tree.</p><p>Second, in order to display-filter (or even capture-filter) only the communication with <code>ldap.here.ca</code>, you have to convert the fqdn to an IP number first. As we deal with a single fqdn here, use <code>dig</code> (on *x systems) or <code>nslookup</code> (on Windows) to obtain a list of IP numbers which represent that fqdn, and use all of them in your filter expression with <code>or</code> between them, as the httpd may establish the LDAPS connection to any of them. In your case, the DNS query returns a single IP number, so a capture filter <code>host 66.196.36.64</code> and/or display filter <code>ip.addr == 66.196.36.64</code> is sufficient.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '16, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '16, 14:06</p></div></div><div id="comments-container-57653" class="comments-container"></div><div id="comment-tools-57653" class="comment-tools"></div><div class="clear"></div><div id="comment-57653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

