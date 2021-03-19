+++
type = "question"
title = "LDAP: connection string"
description = '''Is there a way in wireshark that I can see the LDAP connection string? ie. LDAP://server:port/.... I have captured the traffic and see LDAP packets, but not sure where to look for this string. Thanks.'''
date = "2013-05-30T09:05:00Z"
lastmod = "2013-06-02T03:09:00Z"
weight = 21609
keywords = [ "ldap" ]
aliases = [ "/questions/21609" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [LDAP: connection string](/questions/21609/ldap-connection-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21609-score" class="post-score" title="current number of votes">0</div><span id="post-21609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way in wireshark that I can see the LDAP connection string? ie. <span>LDAP://server</span>:port/....</p><p>I have captured the traffic and see LDAP packets, but not sure where to look for this string.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ldap" rel="tag" title="see questions tagged &#39;ldap&#39;">ldap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '13, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/ed4374aa147ed1279961c32dccfe9e85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malhenry&#39;s gravatar image" /><p><span>malhenry</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malhenry has no accepted answers">0%</span></p></div></div><div id="comments-container-21609" class="comments-container"><span id="21610"></span><div id="comment-21610" class="comment"><div id="post-21610-score" class="comment-score"></div><div class="comment-text"><p>I am trying to debug a failed bind request...thanks.</p></div><div id="comment-21610-info" class="comment-info"><span class="comment-age">(30 May '13, 09:07)</span> <span class="comment-user userinfo">malhenry</span></div></div></div><div id="comment-tools-21609" class="comment-tools"></div><div class="clear"></div><div id="comment-21609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21612"></span>

<div id="answer-container-21612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21612-score" class="post-score" title="current number of votes">0</div><span id="post-21612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That string will not appear in the capture file. As it is a configuration item which tells the system to open an LDAP session to port "port" on "server". So when you do find the ldap packets, look at the requests and then use the IP destination as "server" and the TCP destination port as "port". Be aware though that there might have been a hostname configured, not an IP address. So if you are capturing on the device that is initiating the LDAP session, look for DNS requests too...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '13, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21612" class="comments-container"><span id="21614"></span><div id="comment-21614" class="comment"><div id="post-21614-score" class="comment-score"></div><div class="comment-text"><p>I know the server and port. I am really looking for what is being passed as the rest of the connection string...such as the user which can be specified in more than one format. My reason for doing this is one client program can successfully authenticate, but another fails with bad user or pw. Not that it matters, but I am authenticating (trying) to a windows AD LDS instance. Thanks.</p></div><div id="comment-21614-info" class="comment-info"><span class="comment-age">(30 May '13, 11:17)</span> <span class="comment-user userinfo">malhenry</span></div></div><span id="21615"></span><div id="comment-21615" class="comment"><div id="post-21615-score" class="comment-score"></div><div class="comment-text"><p>also I am attempting to use the same credentials in each of my two client programs.</p></div><div id="comment-21615-info" class="comment-info"><span class="comment-age">(30 May '13, 11:18)</span> <span class="comment-user userinfo">malhenry</span></div></div><span id="21621"></span><div id="comment-21621" class="comment"><div id="post-21621-score" class="comment-score"></div><div class="comment-text"><blockquote><p>such as the user which can be specified in more than one format. My reason for doing this is one client program can successfully</p></blockquote><p>Look for LDAP bind requests and for LDAP bind responses.</p><blockquote><p><code>Filter: ldap.bindRequest or ldap.bindResponse</code><br />
</p></blockquote><p>Then open the LDAP fields in Wireshark and check if you can find the reason.</p><p>However: There are several ways to protect the authentication information (SSL/TLS, SASL, etc.), so you might not see anything useful.</p><p>If the client does <strong>not</strong> use SSL/TLS and the authentication scheme is 'simple' you will be able to see the user and the password, as well as the error message of the LDAP server.</p><p>Regards<br />
Kurt</p></div><div id="comment-21621-info" class="comment-info"><span class="comment-age">(30 May '13, 12:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21612" class="comment-tools"></div><div class="clear"></div><div id="comment-21612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21690"></span>

<div id="answer-container-21690" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21690-score" class="post-score" title="current number of votes">0</div><span id="post-21690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As long as this is in clear text, you should be able to see the request:</p><p>27842 2013-06-02 06:00:28.623270000 macbkpro.willeke.com sa.willeke.com LDAP 135 bindRequest(1) "cn=user1,ou=users,dc=willeke,dc=com" simple</p><p>an d response: 42775 2013-06-02 06:03:53.739349000 sa.willeke.com macbkpro.willeke.com LDAP 119 bindResponse(1) invalidCredentials (NDS error: failed authentication (-669))</p><p>-jim</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '13, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/aaec5375025024900e9118885097d713?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jwilleke&#39;s gravatar image" /><p><span>jwilleke</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jwilleke has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-21690" class="comments-container"></div><div id="comment-tools-21690" class="comment-tools"></div><div class="clear"></div><div id="comment-21690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

