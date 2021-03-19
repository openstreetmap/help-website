+++
type = "question"
title = "Show more characters on packet details fields."
description = '''I am having an issue in both Tshark and Wireshark. I am trying to export packet details from SNMP response packets that I receive. When viewing the packet details in both Tshark and wireshark they seem to only show a certain amount of characters for the field values I am trying to get. So this in tu...'''
date = "2014-03-30T17:31:00Z"
lastmod = "2014-03-31T01:35:00Z"
weight = 31301
keywords = [ "decode", "udp", "snmp", "tshark", "asn1" ]
aliases = [ "/questions/31301" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Show more characters on packet details fields.](/questions/31301/show-more-characters-on-packet-details-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31301-score" class="post-score" title="current number of votes">0</div><span id="post-31301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having an issue in both Tshark and Wireshark. I am trying to export packet details from SNMP response packets that I receive. When viewing the packet details in both Tshark and wireshark they seem to only show a certain amount of characters for the field values I am trying to get. So this in turn makes the data incomplete. Here is an example of this:</p><pre><code>Object Name: 1.3.6.1.4.1.1166.1.19.4.52.0 (iso.3.6.1.4.1.1166.1.19.4.52.0)                   
Value (OctetString): 0327308203233082020ba0030201020207014ceb4234d9f0...</code></pre><p>As you can see the Value ends with "..." to signify that it continues. How can I get these full values? Preferably in TShark although if you know how in Wireshark, that can set me on the right track atleast.</p><p>Every Object's value seems to cut off as long as it exceeds a certain length of chars. I want to be able to get the full value without it cutting off.</p><p>I have tried using the field options in wireshark to display only those fields, although none of them seem to return any values except for the "snmp.value.oid" field. The full syntax I used was:</p><p>tshark -i 1 -R "snmp" -O "snmp" -T fields -e snmp.value.oid -e snmp.value.octets -V</p><p>Also here is an image of the SNMP packet details, as you can see the ones labeled Values(octetstring) which is the returned value that I am looking at grabbing ends in "..." They have been shortened significantly and I would like to grab the full value.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/stackoverflowsnmp_1.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-asn1" rel="tag" title="see questions tagged &#39;asn1&#39;">asn1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '14, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/6438826b56b89f1ac63250ed5f455095?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joe%20Page&#39;s gravatar image" /><p><span>Joe Page</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joe Page has no accepted answers">0%</span></p></img></div></div><div id="comments-container-31301" class="comments-container"></div><div id="comment-tools-31301" class="comment-tools"></div><div class="clear"></div><div id="comment-31301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31308"></span>

<div id="answer-container-31308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31308-score" class="post-score" title="current number of votes">0</div><span id="post-31308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p>tshark -nr snmp.pcap -Y "snmp" -T fields -e frame.number -e ip.src -e ip.dst -e snmp.value.octet s -E header=y -E separator=;</p></blockquote><p>If -Y does not work, please use -R instead.</p><p>Then parse the output and convert it to whatever format you need.</p><p>See also the other SNMP fields: <a href="http://www.wireshark.org/docs/dfref/s/snmp.html">http://www.wireshark.org/docs/dfref/s/snmp.html</a></p><p>Regards<br />
Kurt</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '14, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-31308" class="comments-container"></div><div id="comment-tools-31308" class="comment-tools"></div><div class="clear"></div><div id="comment-31308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

