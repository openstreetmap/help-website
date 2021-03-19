+++
type = "question"
title = "[closed] What does the &quot;unbindRequest(19)&quot; LDAP message mean?"
description = '''I&#x27;m getting this error every time I try to bind to a domain in a different forest using DirectoryEntry in C#. Any Idea what it means?'''
date = "2015-01-19T09:54:00Z"
lastmod = "2015-01-19T10:34:00Z"
weight = 39282
keywords = [ "c#", "ldap", "wireshark" ]
aliases = [ "/questions/39282" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] What does the "unbindRequest(19)" LDAP message mean?](/questions/39282/what-does-the-unbindrequest19-ldap-message-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39282-score" class="post-score" title="current number of votes">0</div><span id="post-39282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting this error every time I try to bind to a domain in a different forest using DirectoryEntry in C#.</p><p>Any Idea what it means?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-ldap" rel="tag" title="see questions tagged &#39;ldap&#39;">ldap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '15, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/ca880190dda0a33ee736cf349ff6c4ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guyziv2110&#39;s gravatar image" /><p><span>guyziv2110</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guyziv2110 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>19 Jan '15, 13:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39282" class="comments-container"></div><div id="comment-tools-39282" class="comment-tools"></div><div class="clear"></div><div id="comment-39282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by grahamb 19 Jan '15, 13:56

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39284"></span>

<div id="answer-container-39284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39284-score" class="post-score" title="current number of votes">0</div><span id="post-39284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your question is a bit confusing. A LDAP unbindrequest from a bind request. LDAP Result code 19 is <a href="http://ldapwiki.com/wiki/LDAP_CONSTRAINT_VIOLATION">LDAP_CONSTRAINT_VIOLATION</a> , which could be caused by a couple of conditions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '15, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/aaec5375025024900e9118885097d713?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jwilleke&#39;s gravatar image" /><p><span>jwilleke</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jwilleke has no accepted answers">0%</span></p></div></div><div id="comments-container-39284" class="comments-container"><span id="39285"></span><div id="comment-39285" class="comment"><div id="post-39285-score" class="comment-score"></div><div class="comment-text"><p>What is confusing ? Can you please give me a direction on how to troubleshoot the issue?</p></div><div id="comment-39285-info" class="comment-info"><span class="comment-age">(19 Jan '15, 10:20)</span> <span class="comment-user userinfo">guyziv2110</span></div></div><span id="39286"></span><div id="comment-39286" class="comment"><div id="post-39286-score" class="comment-score"></div><div class="comment-text"><p>provide your code and full message from the results.</p></div><div id="comment-39286-info" class="comment-info"><span class="comment-age">(19 Jan '15, 10:21)</span> <span class="comment-user userinfo">jwilleke</span></div></div><span id="39287"></span><div id="comment-39287" class="comment"><div id="post-39287-score" class="comment-score"></div><div class="comment-text"><p>Okay just a second.</p></div><div id="comment-39287-info" class="comment-info"><span class="comment-age">(19 Jan '15, 10:22)</span> <span class="comment-user userinfo">guyziv2110</span></div></div><span id="39288"></span><div id="comment-39288" class="comment"><div id="post-39288-score" class="comment-score"></div><div class="comment-text"><p>I can't provide all the information as a comment so I wrote it as an answer.</p><p>Here is the code:</p><p>(line 1) DirectoryEntryWrapper deTrustedForest = new DirectoryEntryWrapper("LDAP://fullForestDnsName/RootDSE");</p><p>(line 2) string strConfigDN = string.Empty;</p><p>(line 3) strConfigDN = deTrustedForest.Properties["configurationNamingContext"].Value.ToString();</p><p>The unbindRequest error shows in wireshark as soon as I try to access the property "configurationNamingContext" of deTrustedForest (line 3).</p><p>And here is the unbindRequest full message:</p><p>0....X...c....O.. .. .......x.....objectclass0....+..subschemaSubentry. dsServiceName..namingContexts..defaultNamingContext..schemaNamingContext..configurationNamingContext..rootDomainNamingContext..supportedControl..supportedLDAPVersion..supportedLDAPPolicies..supportedSASLMechanisms..dnsHostName..ldapServiceName. serverName..supportedCapabilities0........d.......0.....0....S..subschemaSubentry1....:.8CN=Aggregate,CN=Schema,CN=Configuration,DC=tstb,DC=local0...... dsServiceName1....n.lCN=NTDS Settings,CN=SERVERXX,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=tstb,DC=local0.......namingContexts1.......DC=tstb,DC=local.!CN=Configuration,DC=tstb,DC=local.+CN=Schema,CN=Configuration,DC=tstb,DC=local."DC=DomainDnsZones,DC=tstb,DC=local."DC=ForestDnsZones,DC=tstb,DC=local0.......defaultNamingContext1.......DC=tstb,DC=local0....H..schemaNamingContext1....-.+CN=Schema,CN=Configuration,DC=tstb,DC=local0....E..configurationNamingContext1....#.!CN=Configuration,DC=tstb,DC=local0....1..rootDomainNamingContext1.......DC=tstb,DC=local0.......supportedControl1.......1.2.840.113556.1.4.319..1.2.840.113556.1.4.801..1.2.840.113556.1.4.473..1.2.840.113556.1.4.528..1.2.840.113556.1.4.417..1.2.840.113556.1.4.619..1.2.840.113556.1.4.841..1.2.840.113556.1.4.529..1.2.840.113556.1.4.805..1.2.840.113556.1.4.521..1.2.840.113556.1.4.970..1.2.840.113556.1.4.1338..1.2.840.113556.1.4.474..1.2.840.113556.1.4.1339..1.2.840.113556.1.4.1340..1.2.840.113556.1.4.1413..2.16.840.1.113730.3.4.9..2.16.840.1.113730.3.4.10..1.2.840.113556.1.4.1504..1.2.840.113556.1.4.1852..1.2.840.113556.1.4.802..1.2.840.113556.1.4.1907..1.2.840.113556.1.4.1948..1.2.840.113556.1.4.1974..1.2.840.113556.1.4.1341..1.2.840.113556.1.4.2026..1.2.840.113556.1.4.2064..1.2.840.113556.1.4.2065..1.2.840.113556.1.4.20660...."..supportedLDAPVersion1.......3..20....&lt;..supportedLDAPPolicies1.......MaxPoolThreads..MaxDatagramRecv..MaxReceiveBuffer..InitRecvTimeout..MaxConnections..MaxConnIdleTime..MaxPageSize..MaxQueryDuration..MaxTempTableSize..MaxResultSetSize. MinResultSets..MaxResultSetsPerConn..MaxNotificationPerConn..MaxValRange..ThreadMemoryLimit..SystemMemoryLimitPercent0....I..supportedSASLMechanisms1....*..GSSAPI. GSS-SPNEGO..EXTERNAL. DIGEST-MD50....'..dnsHostName1.......serverxx.tstb.local0....7..ldapServiceName1.... ..tstb.local:<span class="__cf_email__" data-cfemail="82f1e7f0f4e7f0fafaa6c2d6d1d6c0accecdc1c3ceb2acacacacedac">[email protected]</span> serverName1....].[CN=SERVERXX,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=tstb,DC=local0.......supportedCapabilities1....|..1.2.840.113556.1.4.800..1.2.840.113556.1.4.1670..1.2.840.113556.1.4.1791..1.2.840.113556.1.4.1935..1.2.840.113556.1.4.20800........e..... ......0........B.</p></div><div id="comment-39288-info" class="comment-info"><span class="comment-age">(19 Jan '15, 10:30)</span> <span class="comment-user userinfo">guyziv2110</span></div></div><span id="39289"></span><div id="comment-39289" class="comment"><div id="post-39289-score" class="comment-score"></div><div class="comment-text"><p>Does it help you?</p></div><div id="comment-39289-info" class="comment-info"><span class="comment-age">(19 Jan '15, 10:34)</span> <span class="comment-user userinfo">guyziv2110</span></div></div></div><div id="comment-tools-39284" class="comment-tools"></div><div class="clear"></div><div id="comment-39284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

