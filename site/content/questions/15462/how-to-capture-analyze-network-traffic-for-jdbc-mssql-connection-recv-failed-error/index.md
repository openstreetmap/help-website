+++
type = "question"
title = "How to capture &amp; analyze network traffic for jdbc mssql &quot;connection recv failed&quot; error"
description = '''One of our customers has intermittent database connection problems. The error logs periodically show messages like this:  A database error occurred. : Software caused connection abort: recv failed  at which point someone must restart the application. (Connection pooling doesn&#x27;t recover from the erro...'''
date = "2012-11-01T05:54:00Z"
lastmod = "2012-11-01T05:54:00Z"
weight = 15462
keywords = [ "wireshark" ]
aliases = [ "/questions/15462" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture & analyze network traffic for jdbc mssql "connection recv failed" error](/questions/15462/how-to-capture-analyze-network-traffic-for-jdbc-mssql-connection-recv-failed-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15462-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>One of our customers has intermittent database connection problems. The error logs periodically show messages like this:</p><pre><code> A database error occurred. : Software caused connection abort: recv failed</code></pre><p>at which point someone must restart the application. (Connection pooling doesn't recover from the error)</p><p>This <a href="http://stackoverflow.com/questions/135919/java-net-socketexception-software-caused-connection-abort-recv-failed">post</a> describes a problem; one of the answers points to wireshark.</p><p><strong>Suspicions</strong></p><p>I suspect the problem is either:</p><ol><li>someone wrote a database script that runs on the server that closes sleeping connections</li><li>an error in their network</li></ol><p>As I can't find anyone owning up to #1, I need to hunt down #2.</p><p><strong>My question</strong></p><ul><li>Once I have captured the data, what do I look for in the captured data to point to a root cause?</li></ul><p><strong>Example</strong></p><p>For example, I assume based on past experience that the server logs will show everything "runs fine" until an error like this occurs:</p><pre><code>2012-11-01 04:02:14 A database error occurred. : Software caused connection abort: recv failed</code></pre><p>Then I'd like to look at the traffic the seconds/minutes before 04:02:14 for any "smoking gun".</p><p><strong>Pointers?</strong></p><p>Additionally, I ask for pointers on these items:</p><ul><li>setting up the traffic capture. (is capturing on the jdbc server's port 1433 enough?)</li><li>port-mirroring tips. I assume I can ask their "network guy" to set up port mirroring to a windows box running wireshark and he can do it easily ("Port mirroring" copies all network traffic for a particular connection off to another port for later analysis)</li><li>any wireshark 'scalability issues'--will the data overload wireshark ?</li><li>filtering through the data for "interesting events"</li><li>"smoking guns"--what to look for prior to that 'connection recv error'</li></ul><p><strong>Environment</strong></p><ul><li>MSSQL (2005 or later. It's on the customer site and I don't know the details)</li><li>Jboss 4.2.2</li><li>Microsoft jdbc driver</li><li>jdk 1.6 (not sure the exact version)</li></ul></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '12, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/647229a94efa207bdfd6c9e294724760?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milspec&#39;s gravatar image" /><p>milspec<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milspec has no accepted answers">0%</span></p></div></div><div id="comments-container-15462" class="comments-container"></div><div id="comment-tools-15462" class="comment-tools"></div><div class="clear"></div><div id="comment-15462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

