+++
type = "question"
title = "Intermittently get Communication link failure error"
description = '''I have two hyperV 2012 R2 servers, one is app server, another is DB server and SQL server 2012 installed on it. application installed in app server, connect to DB server through system DSN. Recently, our application keeps getting Communication link failure error, the error details from windows event...'''
date = "2016-08-28T14:47:00Z"
lastmod = "2016-08-28T14:47:00Z"
weight = 55149
keywords = [ "hyperv", "sqlserver", "wireshark" ]
aliases = [ "/questions/55149" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Intermittently get Communication link failure error](/questions/55149/intermittently-get-communication-link-failure-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55149-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two hyperV 2012 R2 servers, one is app server, another is DB server and SQL server 2012 installed on it. application installed in app server, connect to DB server through system DSN.</p><p>Recently, our application keeps getting Communication link failure error, the error details from windows event viewer:</p><p><strong>Operating System Error. 08S01 0 [SQL Driver]Communication link failure</strong></p><p>I have checked the SQL server log, no error reported. This issue happens intermittently, but we do found one patterns that it likely happen when application generating report.</p><p>I have searched some solutions from internet, some solutions suggest to disable TCP chimney Offload feature, but this feature is already disabled in server 2012 R2 by default, and we never touched that.</p><p>I started a Wireshark capture on app server, want to capture the network packet when issue happened. On 18/08/2016 6:47:38 p.m, I got same error in app server, and the Wireshark capture has been uploaded to Cloudshark, link is : <a href="https://www.cloudshark.org/captures/4192e8bc4c81">https://www.cloudshark.org/captures/4192e8bc4c81</a></p><p>I have little knowledge on network layer, could someone help me to check if anything wrong in network capture log? Any suggestion is appreciated.</p></div><div id="question-tags" class="tags-container tags">hyperv sqlserver wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '16, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/e0ea91a217fb8aa32b95a5e097d11c42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="growrain&#39;s gravatar image" /><p>growrain<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="growrain has no accepted answers">0%</span></p></div></div><div id="comments-container-55149" class="comments-container"></div><div id="comment-tools-55149" class="comment-tools"></div><div class="clear"></div><div id="comment-55149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

