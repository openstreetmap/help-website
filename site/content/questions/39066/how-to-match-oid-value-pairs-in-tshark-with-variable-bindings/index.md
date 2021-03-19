+++
type = "question"
title = "how to match oid-value pairs in tshark with variable-bindings"
description = '''Lets say I have a set-request with 3 variable-bindings. The first OID is set to an int, second OID is set to an octet string, and third OID is set to an int. When I use tshark to write the pcap to a csv file, use the following command:  tshark -r C:&#92;mypcap.pcapng -Y &quot;frame.number==24 and !snmp.value...'''
date = "2015-01-11T17:56:00Z"
lastmod = "2016-01-12T04:52:00Z"
weight = 39066
keywords = [ "variable-bindings", "oid", "snmp", "tshark", "value" ]
aliases = [ "/questions/39066" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to match oid-value pairs in tshark with variable-bindings](/questions/39066/how-to-match-oid-value-pairs-in-tshark-with-variable-bindings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39066-score" class="post-score" title="current number of votes">0</div><span id="post-39066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Lets say I have a set-request with 3 variable-bindings. The first OID is set to an int, second OID is set to an octet string, and third OID is set to an int. When I use tshark to write the pcap to a csv file, use the following command:</p><blockquote><p>tshark -r C:\mypcap.pcapng -Y "frame.number==24 and !snmp.value.null" -T fields -e snmp.value.int -e snmp.value.octets -E header=y -E separator=,</p></blockquote><p>This prints out all the data I need however it is impossible to see what OIDs match up with what values, since the values are printed in order based on type and not OID. So the result of the above query would show int,int,octet string when the actual order in the packet is int, octet string, int. Is there a different display filter combination for variable-bindings that will show me what each OID was set to?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-variable-bindings" rel="tag" title="see questions tagged &#39;variable-bindings&#39;">variable-bindings</span> <span class="post-tag tag-link-oid" rel="tag" title="see questions tagged &#39;oid&#39;">oid</span> <span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-value" rel="tag" title="see questions tagged &#39;value&#39;">value</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '15, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/378dec08c639d6c2c2979b244af9660e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lp4968&#39;s gravatar image" /><p><span>lp4968</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lp4968 has no accepted answers">0%</span></p></div></div><div id="comments-container-39066" class="comments-container"></div><div id="comment-tools-39066" class="comment-tools"></div><div class="clear"></div><div id="comment-39066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49115"></span>

<div id="answer-container-49115" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49115-score" class="post-score" title="current number of votes">0</div><span id="post-49115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have prepared a short groovy script to cover this issue. In my case I convert pcap files to snmpset scripts. I am extracting OID int g32 and octet values. Then I check the OID type with snmptranslate command. Finally when I know the type I take first value from concrete type.</p><p>I can share my script if you are interested.</p><p>The prerequisite is that you have snmp tools package installed in your system and have all MIBs you are interested in.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '16, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/730e0f8d561ff5f5756a68f216c1e401?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bartosz%20Michalik&#39;s gravatar image" /><p><span>Bartosz Mich...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bartosz Michalik has no accepted answers">0%</span></p></div></div><div id="comments-container-49115" class="comments-container"></div><div id="comment-tools-49115" class="comment-tools"></div><div class="clear"></div><div id="comment-49115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

