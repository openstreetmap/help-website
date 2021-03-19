+++
type = "question"
title = "Format of info field for DNS packets"
description = '''Hello, I need to use regular expressions to extract some data from the &#x27;info&#x27; field in a psml file for a DNS query response packet. Since I am using regex, I need to know with certainty what the contents of this field might contain, to ensure that the regular expression doesn&#x27;t match with any text t...'''
date = "2016-08-22T09:32:00Z"
lastmod = "2016-08-22T11:27:00Z"
weight = 55052
keywords = [ "info", "regex", "dns" ]
aliases = [ "/questions/55052" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Format of info field for DNS packets](/questions/55052/format-of-info-field-for-dns-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55052-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I need to use regular expressions to extract some data from the 'info' field in a psml file for a DNS query response packet. Since I am using regex, I need to know with certainty what the contents of this field might contain, to ensure that the regular expression doesn't match with any text that it shouldn't and return the wrong data. I was wondering whether there exists a guide to the format, or if somebody would be able to explain it to me? Any help would be much appreciated.</p><p>Many thanks.</p></div><div id="question-tags" class="tags-container tags">info regex dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '16, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/05aa98a3a949c17526355a407a7c506e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lobster&#39;s gravatar image" /><p>Lobster<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lobster has no accepted answers">0%</span></p></div></div><div id="comments-container-55052" class="comments-container"></div><div id="comment-tools-55052" class="comment-tools"></div><div class="clear"></div><div id="comment-55052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55054"></span>

<div id="answer-container-55054" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55054-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can find the PSML format <a href="http://www.nbee.org/doku.php?id=netpdl:psml_specification">here</a>.</p><p>You'll need to find which section contains info, and work the packet data with that. Not sure if you could manage with a regexp alone.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '16, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55054" class="comments-container"><span id="55063"></span><div id="comment-55063" class="comment"><div id="post-55063-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap, thanks for the help. Looking at the link, it seems that PSML has a wider use than for Wireshark alone, and I think that the format of the DNS query response info section might be defined by Wireshark. I'm sure there is a specification - i.e. for an A record, the string always seems to take a form similar to:</p><p>Standard query response [a hex number] [record type] [domain] (CNAME [canonical domain])+ [record type] [IP Address] ([record type] [IP Address])+</p><p>... but I can't find it defined formally anywhere. It's this formal specification that I'm looking for.</p></div><div id="comment-55063-info" class="comment-info"><span class="comment-age">(23 Aug '16, 01:46)</span> Lobster</div></div><span id="55065"></span><div id="comment-55065" class="comment"><div id="post-55065-score" class="comment-score"></div><div class="comment-text"><p>No, there isn't. All you find in the PSML output is a PSML compliant representation of the columns as configured in Wireshark. Their actual contents is defined by the dissector handling the respective protocols, in this case the DNS dissector. There is no formal format for its output, although its algorithmically constructed based on the input data. That also means that it may change in future Wireshark releases.</p></div><div id="comment-55065-info" class="comment-info"><span class="comment-age">(23 Aug '16, 02:39)</span> Jaap ♦</div></div><span id="55077"></span><div id="comment-55077" class="comment"><div id="post-55077-score" class="comment-score"></div><div class="comment-text"><p>Ah, that's a pity :( Wireshark's open source, so I suppose that I could probably find the algorithm and deduce a format myself, though it is probably quite complicated.</p></div><div id="comment-55077-info" class="comment-info"><span class="comment-age">(23 Aug '16, 08:20)</span> Lobster</div></div><span id="55078"></span><div id="comment-55078" class="comment"><div id="post-55078-score" class="comment-score"></div><div class="comment-text"><p>Yes it would, and I think it's the wrong way to go about this. I would suggest using a more detailed output format (PDML for instance) where several fields are individually provided, which you can then (programmatically, eg through awk or other tools) combine into the format you desire.</p></div><div id="comment-55078-info" class="comment-info"><span class="comment-age">(23 Aug '16, 09:06)</span> Jaap ♦</div></div><span id="55080"></span><div id="comment-55080" class="comment"><div id="post-55080-score" class="comment-score"></div><div class="comment-text"><p>That's a good idea - thanks!</p></div><div id="comment-55080-info" class="comment-info"><span class="comment-age">(23 Aug '16, 11:34)</span> Lobster</div></div></div><div id="comment-tools-55054" class="comment-tools"></div><div class="clear"></div><div id="comment-55054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

