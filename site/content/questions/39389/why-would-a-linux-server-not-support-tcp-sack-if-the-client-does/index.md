+++
type = "question"
title = "[closed] Why would a linux server not support tcp SACK if the client does"
description = '''background: I am troubleshooting a intermittent performance problem we have with a Windows 7 client connecting to oracle 10g database running on a linux 2.4.x server. [ note: i do not have access to the server ]. the app runs once a day as a scheduled task on windows 7. it makes numerous queries to ...'''
date = "2015-01-24T23:22:00Z"
lastmod = "2015-01-24T23:22:00Z"
weight = 39389
keywords = [ "tcpwindowscaling", "sack", "linux" ]
aliases = [ "/questions/39389" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Why would a linux server not support tcp SACK if the client does](/questions/39389/why-would-a-linux-server-not-support-tcp-sack-if-the-client-does)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39389-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>background: I am troubleshooting a intermittent performance problem we have with a Windows 7 client connecting to oracle 10g database running on a linux 2.4.x server. [ note: i do not have access to the server ]. the app runs once a day as a scheduled task on windows 7. it makes numerous queries to the database and all the queries complete within 1 minute. the longest query is always the first one and that normally it takes 1-2 seconds.</p><p>this will happen for several days. then for a few days the first query will take 9.7 minutes to return the results, all other queries return quickly. then it will return to normal.</p><p>as part of that troubleshooting i noticed:</p><ol><li>the following options were supported by the server during the handshake for the slow query: MSS, SACK, and WS (128)</li><li>the following options were supported by the server during the handshake for the fast query: MSS.</li></ol><p>What would cause a server to support SACK for some connections and not support it at another time for the same client. In both cases the options supported by the client were the same.</p></div><div id="question-tags" class="tags-container tags">tcpwindowscaling sack linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '15, 23:22</strong></p><img src="https://secure.gravatar.com/avatar/e66a2644f8a1189cb900ec2f89777486?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark%20Nassy&#39;s gravatar image" /><p>Mark Nassy<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark Nassy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 26 Jan '15, 05:44</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-39389" class="comments-container"></div><div id="comment-tools-39389" class="comment-tools"></div><div class="clear"></div><div id="comment-39389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Jaap 26 Jan '15, 05:44

</div>

</div>

</div>

