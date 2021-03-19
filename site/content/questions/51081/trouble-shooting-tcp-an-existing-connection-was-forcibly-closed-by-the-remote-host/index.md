+++
type = "question"
title = "Trouble shooting TCP An existing connection was forcibly closed by the remote host"
description = '''Hi, I am receiving multiple errors like the ones below from a 3rd party application that connects to an SQL database, the application support this to be cause by a &#x27;network issue&#x27;, however I am having trouble detecting any faults out side the applications. *Unhandled Exception: A transport-level err...'''
date = "2016-03-22T04:12:00Z"
lastmod = "2016-03-22T04:12:00Z"
weight = 51081
keywords = [ "sql", "database", "network", "tcp", "error" ]
aliases = [ "/questions/51081" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trouble shooting TCP An existing connection was forcibly closed by the remote host](/questions/51081/trouble-shooting-tcp-an-existing-connection-was-forcibly-closed-by-the-remote-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51081-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am receiving multiple errors like the ones below from a 3rd party application that connects to an SQL database, the application support this to be cause by a 'network issue', however I am having trouble detecting any faults out side the applications.</p><p>*Unhandled Exception: A transport-level error has occurred when sending the request to the server. (provider: TCP Provider, error: 0 - An existing connection was forcibly closed by the remote host.)</p><p>A transport-level error has occurred when receiving results from the server. (provider: TCP Provider, error: 0 - The specified network name is no longer available.)*</p><p>SQL logs show no errors at all, pings test between the server and client have issues even while these errors are occurring, TCP chimney is disabled.</p><p>Database server also hosts two other SQL databases that are accessed by other client applications and appear to have no issues.</p><p>I have been running captures between the DB server and then clients and hopping to find some indication of why the connection is being broken (such as indications of faulty hardware) so far no luck.</p><p>What should I be looking for or am I wasting my time ?</p></div><div id="question-tags" class="tags-container tags">sql database network tcp error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '16, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/7df1bea98c3f32096974ef6808ea4ed2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Millard&#39;s gravatar image" /><p>Millard<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Millard has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '16, 05:10</p></div></div><div id="comments-container-51081" class="comments-container"></div><div id="comment-tools-51081" class="comment-tools"></div><div class="clear"></div><div id="comment-51081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

