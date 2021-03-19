+++
type = "question"
title = "Tshark pdml value"
description = '''Hi guys. I&#x27;m trying to extract multimedia content from an MMSE dumped pcap file from command line (Bash - Linux RHEL5). Well, with command:  tshark -R &quot;mmse&quot; -r mms.pcap -T pdml  i can see a smil tag nested in ip -&amp;gt; tcp -&amp;gt; wsp tags. This is the line i care for: &amp;lt;field name=&quot;smil.smil&quot; shown...'''
date = "2010-12-03T08:27:00Z"
lastmod = "2010-12-03T08:27:00Z"
weight = 1227
keywords = [ "field", "pdml", "tshark", "mmse" ]
aliases = [ "/questions/1227" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark pdml value](/questions/1227/tshark-pdml-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1227-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys. I'm trying to extract multimedia content from an MMSE dumped pcap file from command line (Bash - Linux RHEL5).</p><p>Well, with command:<br />
</p><p>tshark -R "mmse" -r mms.pcap -T pdml<br />
</p><p>i can see a smil tag nested in ip -&gt; tcp -&gt; wsp tags. This is the line i care for:</p>&lt;field name="smil.smil" showname="&amp;lt;smil&amp;gt;" size="522" pos="427" show="&amp;lt;smil&amp;gt;" value="...hex content..."&gt;<p>if a try to print it with:</p><p>tshark -R "mmse" -r mms.pcap -T pdml -e smil.smil -T fields</p><p>i get the content of showname and not of value property... i cannot get a clue about how to get value field... someone have an idea?</p><p>In second instance i want to ask you the best approach possible in writing a script or a program written in C that extract multimedia content from a MMSE filtered pcap file.</p><p>Thank you in advance, Davidone</p></div><div id="question-tags" class="tags-container tags">field pdml tshark mmse</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '10, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/551209e645a3740600b0391b21f37144?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davidone&#39;s gravatar image" /><p>Davidone<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davidone has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-1227" class="comments-container"></div><div id="comment-tools-1227" class="comment-tools"></div><div class="clear"></div><div id="comment-1227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

