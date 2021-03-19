+++
type = "question"
title = "slow performance on aveva software"
description = '''We have a design software Aveva that we are having performance problems pulling up and instrument panel or valve panel after we add a symbol on the drawing. the software is installed on the workstation - 192.1.1.1 and it talks to the sql server - 192.1.1.2. I&#x27;m seening like between 5 to 28 seconds c...'''
date = "2016-06-28T18:49:00Z"
lastmod = "2016-06-28T18:49:00Z"
weight = 53703
keywords = [ "performance", "slow", "sql" ]
aliases = [ "/questions/53703" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [slow performance on aveva software](/questions/53703/slow-performance-on-aveva-software)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53703-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a design software Aveva that we are having performance problems pulling up and instrument panel or valve panel after we add a symbol on the drawing. the software is installed on the workstation - 192.1.1.1 and it talks to the sql server - 192.1.1.2. I'm seening like between 5 to 28 seconds calling sql batch but I'm not sure what is slow the applications or the sql server. I have the traces from the workstation and the server side. I'm seeing tcp keep alives but I'm not sure that is the problem</p><p><a href="https://www.dropbox.com/s/3nrh7fx67ny0xd2/sqlserver.pcap_anon.pcapng?dl=0">https://www.dropbox.com/s/3nrh7fx67ny0xd2/sqlserver.pcap_anon.pcapng?dl=0</a> <a href="https://www.dropbox.com/s/o4jhy6xd27ti3ks/workstationtest.pcap_anon.pcapng?dl=0">https://www.dropbox.com/s/o4jhy6xd27ti3ks/workstationtest.pcap_anon.pcapng?dl=0</a></p></div><div id="question-tags" class="tags-container tags">performance slow sql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '16, 18:49</strong></p><img src="https://secure.gravatar.com/avatar/1ace388d473a7dc2c6ffb774562b02ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrickwill&#39;s gravatar image" /><p>patrickwill<br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrickwill has no accepted answers">0%</span></p></div></div><div id="comments-container-53703" class="comments-container"><span id="53752"></span><div id="comment-53752" class="comment"><div id="post-53752-score" class="comment-score"></div><div class="comment-text"><p>do you have jumbo frames enabled on any of the network equipment?</p></div><div id="comment-53752-info" class="comment-info"><span class="comment-age">(30 Jun '16, 06:05)</span> net_tech</div></div><span id="53768"></span><div id="comment-53768" class="comment"><div id="post-53768-score" class="comment-score"></div><div class="comment-text"><p>FWIW There were some more details in the other (now closed) question on this topic: <a href="https://ask.wireshark.org/questions/53731/why-sql-batch-is-slow">https://ask.wireshark.org/questions/53731/why-sql-batch-is-slow</a></p></div><div id="comment-53768-info" class="comment-info"><span class="comment-age">(01 Jul '16, 07:15)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-53703" class="comment-tools"></div><div class="clear"></div><div id="comment-53703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

