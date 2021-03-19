+++
type = "question"
title = "decoding preexisting ldap connection"
description = '''I&#x27;m troubleshooting an AD/LDAP integrated application. If I start up Wireshark prior to starting the application/service (i.e. before the bind takes place) then my capture file is perfectly readable. However if a preexisting ldap/389 connection exists to the server, the LDAP packets show as LDAP, bu...'''
date = "2015-04-22T13:13:00Z"
lastmod = "2015-04-24T16:23:00Z"
weight = 41707
keywords = [ "decode", "sasl", "ldap" ]
aliases = [ "/questions/41707" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [decoding preexisting ldap connection](/questions/41707/decoding-preexisting-ldap-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41707-score" class="post-score" title="current number of votes">0</div><span id="post-41707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm troubleshooting an AD/LDAP integrated application.</p><p>If I start up Wireshark prior to starting the application/service (i.e. before the bind takes place) then my capture file is perfectly readable.</p><p>However if a preexisting ldap/389 connection exists to the server, the LDAP packets show as LDAP, but the INFO field is empty. If I look in the "packet bytes" window I can see the LDAP traffic. It is unencrypted/clear text but it is not being decoded into an LDAPMessage so it is incredibly difficult to read - especially when the need exists to look at hundreds of these.</p><p>The problem is that I cannot just restart the service to get a new bind because the issue I'm looking into is always resolved on service restart.</p><p>I'm trying to understand what the limitation of Wireshark is in properly decoding these packets. Since I can see the LDAP data in the bytes, and because wireshark seemingly knows they are LDAP, why can't they be constructed properly?</p><p>Is there anyway around this?</p><p>p.s. the traffic in question is also SASL GSS-API LDAP</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-sasl" rel="tag" title="see questions tagged &#39;sasl&#39;">sasl</span> <span class="post-tag tag-link-ldap" rel="tag" title="see questions tagged &#39;ldap&#39;">ldap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '15, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/389cac469a4dc1f0905ace13b8fc7532?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BenH&#39;s gravatar image" /><p><span>BenH</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BenH has no accepted answers">0%</span></p></div></div><div id="comments-container-41707" class="comments-container"><span id="41721"></span><div id="comment-41721" class="comment"><div id="post-41721-score" class="comment-score"></div><div class="comment-text"><p>can you show the effect in a pcap file? If so, please upload the file somewhere (google drive, dropbox, cloudshark.org) and post the link here.</p></div><div id="comment-41721-info" class="comment-info"><span class="comment-age">(23 Apr '15, 01:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="41808"></span><div id="comment-41808" class="comment"><div id="post-41808-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.cloudshark.org/captures/1ee3a895c06f">https://www.cloudshark.org/captures/1ee3a895c06f</a> with-bind - shows a capture from the startup of the service, which includes the bind to ldap. everything looks good here.</p><p><a href="https://www.cloudshark.org/captures/e1e92a699be9">https://www.cloudshark.org/captures/e1e92a699be9</a> pre-established - shows a capture starting after the bind has been completed. Note that the ldap packets 1-6 are basically identical to packets 8-13 from the with-bind capture.</p><p>If you drill down packet #9 in with-bind and packet #1 in pre-established all the way down to the LDAP data you'll see the byte data is pretty much identical except in the with-bind it's decoded and in the pre-established it is not. You can see my comparison here:</p><p><a href="http://oi60.tinypic.com/dhd2cl.jpg">http://oi60.tinypic.com/dhd2cl.jpg</a></p><p>thanks</p></div><div id="comment-41808-info" class="comment-info"><span class="comment-age">(24 Apr '15, 16:23)</span> <span class="comment-user userinfo">BenH</span></div></div></div><div id="comment-tools-41707" class="comment-tools"></div><div class="clear"></div><div id="comment-41707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

