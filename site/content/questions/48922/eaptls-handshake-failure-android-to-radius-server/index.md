+++
type = "question"
title = "EAP/TLS Handshake Failure - Android to RADIUS server"
description = '''Two Android clients trying to authenticate to a RADIUS server (Windows 2008 R2). WORKING = Android version 4.4, NON-WORKING = &amp;gt; Android version 5.1. TLS version seems to be negotiated fine. The only difference I can see between WORKING and NON-WORKING is the number of CIPHER SUITES presented by t...'''
date = "2016-01-06T11:03:00Z"
lastmod = "2016-01-09T12:05:00Z"
weight = 48922
keywords = [ "tls", "eap", "android", "handshake-failure" ]
aliases = [ "/questions/48922" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [EAP/TLS Handshake Failure - Android to RADIUS server](/questions/48922/eaptls-handshake-failure-android-to-radius-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48922-score" class="post-score" title="current number of votes">0</div><span id="post-48922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Two Android clients trying to authenticate to a RADIUS server (Windows 2008 R2). WORKING = Android version 4.4, NON-WORKING = &gt; Android version 5.1. TLS version seems to be negotiated fine. The only difference I can see between WORKING and NON-WORKING is the number of CIPHER SUITES presented by the clients (both clients are samsung android devices).</p><p>Here are the packet captures: Working EAP Success: <a href="https://drive.google.com/file/d/0B5ttjkGSReNeRnd6dUdNb0JiNkU/view?usp=sharing">https://drive.google.com/file/d/0B5ttjkGSReNeRnd6dUdNb0JiNkU/view?usp=sharing</a></p><p>NOT WORKING eap failure: <a href="https://drive.google.com/file/d/0B5ttjkGSReNeb0dDdllsd19INkE/view?usp=sharing">https://drive.google.com/file/d/0B5ttjkGSReNeb0dDdllsd19INkE/view?usp=sharing</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-eap" rel="tag" title="see questions tagged &#39;eap&#39;">eap</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-handshake-failure" rel="tag" title="see questions tagged &#39;handshake-failure&#39;">handshake-failure</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '16, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/f02147761f70caba11af646101a87d71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deckhopper&#39;s gravatar image" /><p><span>deckhopper</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deckhopper has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '16, 11:05</strong> </span></p></div></div><div id="comments-container-48922" class="comments-container"><span id="48970"></span><div id="comment-48970" class="comment"><div id="post-48970-score" class="comment-score"></div><div class="comment-text"><p>I looked at both file captures. I was able to see up to the UDP layer, but after that the Data portion was still encoded. Were you able to "see" EAP decoded information in the Packet Details section of Wireshark?</p></div><div id="comment-48970-info" class="comment-info"><span class="comment-age">(08 Jan '16, 05:24)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="49022"></span><div id="comment-49022" class="comment"><div id="post-49022-score" class="comment-score"></div><div class="comment-text"><p><span>@deckhopper</span>: Can you please add instructions how you successfully decoded these pcap files as TLS traffic in Wireshark (including the Wireshark version)?</p></div><div id="comment-49022-info" class="comment-info"><span class="comment-age">(09 Jan '16, 12:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-48922" class="comment-tools"></div><div class="clear"></div><div id="comment-48922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

