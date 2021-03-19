+++
type = "question"
title = "Diameter AVP value with -E occurrence=a"
description = '''I am trying to dump diameter AVP values to CSV format using tshark.When I try -E occurrence=a ,the out put is not proper.I need -a to print all available occurrence.But looks like its printing same o/p multiple times. Command I am using:  tshark -r 6CCRI.pcap -d tcp.port==1080,diameter -Y diameter.a...'''
date = "2014-11-19T05:00:00Z"
lastmod = "2014-11-19T05:00:00Z"
weight = 37967
keywords = [ "diameter" ]
aliases = [ "/questions/37967" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Diameter AVP value with -E occurrence=a](/questions/37967/diameter-avp-value-with-e-occurrencea)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37967-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to dump diameter AVP values to CSV format using tshark.When I try -E occurrence=a ,the out put is not proper.I need -a to print all available occurrence.But looks like its printing same o/p multiple times.</p><p>Command I am using:</p><pre><code>tshark -r 6CCRI.pcap -d tcp.port==1080,diameter -Y diameter.applicationId==4 -T fields -E header=y -E separator=, -E occurrence=a  -E quote=d -e frame.number -e diameter.Origin-Host -e diameter.Origin-Realm -e diameter.CC-Request-Type -e diameter.CC-Request-Number
frame.number,diameter.Origin-Host,diameter.Origin-Realm,diameter.CC-Request-Type,diameter.CC-Request-Number</code></pre><p>Output:</p><pre><code>&quot;1&quot;,&quot;gy-pdn&quot;,&quot;starentnetworks.com&quot;,&quot;1&quot;,&quot;0&quot; &lt;---------Correct
&quot;2&quot;,&quot;gy-pdn&quot;,&quot;starentnetworks.com&quot;,&quot;1&quot;,&quot;0&quot;&lt;----------Correct
&quot;3&quot;,&quot;minid-gy&quot;,&quot;yahoo.com&quot;,&quot;1&quot;,&quot;0&quot;&lt;-----------Correct
&quot;4&quot;,&quot;gy-pdn,gy-pdn&quot;,&quot;starentnetworks.com,starentnetworks.com&quot;,&quot;1,1&quot;,&quot;0,0&quot;&lt;-------wrong
&quot;5&quot;,&quot;minid-gy&quot;,&quot;yahoo.com&quot;,&quot;1&quot;,&quot;0&quot;&lt;--------Correct
&quot;6&quot;,&quot;minid-gy,minid-gy,minid-gy,minid-gy,minid-gy&quot;,&quot;yahoo.com,yahoo.com,yahoo.com,yahoo.com,yahoo.com&quot;,&quot;1,1,1,1,1&quot;,&quot;0,0,0,0,0&quot;&lt;----Wrong</code></pre><p>Frame 4/6 also expected as frame 1/2/5.Can you please help to resolve this issue.</p></div><div id="question-tags" class="tags-container tags">diameter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '14, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/40f9d59a5fa42efbce2babebf69c2965?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Senapati&#39;s gravatar image" /><p>Senapati<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Senapati has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Nov '14, 07:42</p></div></div><div id="comments-container-37967" class="comments-container"><span id="37968"></span><div id="comment-37968" class="comment"><div id="post-37968-score" class="comment-score"></div><div class="comment-text"><p>One quick comment (traveling atm) is that there's a tshark -z option specifically for AVP value extraction that supports multiple occurrences which might serve your purpose.</p></div><div id="comment-37968-info" class="comment-info"><span class="comment-age">(19 Nov '14, 05:40)</span> Quadratic</div></div><span id="37971"></span><div id="comment-37971" class="comment"><div id="post-37971-score" class="comment-score"></div><div class="comment-text"><p>Same issue observed with tshark -z option.with -z option same frame observed multiple times.Also with this option it is difficult to convert the output to csv file as alignment will not be proper.</p></div><div id="comment-37971-info" class="comment-info"><span class="comment-age">(19 Nov '14, 08:49)</span> Senapati</div></div></div><div id="comment-tools-37967" class="comment-tools"></div><div class="clear"></div><div id="comment-37967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

