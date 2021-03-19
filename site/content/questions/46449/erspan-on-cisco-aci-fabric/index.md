+++
type = "question"
title = "ERSPAN on Cisco ACI Fabric"
description = '''Dears, I have a setup in the lab where I have configured ERSPAN on Cisco ACI Fabric which pretty similar to ERSPAN on Nexus switches 7k or 5K , I got the capture where I can see only the outer header for the packets but it&#x27;s not helpful. So I want to decapsulate/decode the ERSPAN packets where I can...'''
date = "2015-10-11T02:58:00Z"
lastmod = "2017-06-19T03:33:00Z"
weight = 46449
keywords = [ "cisco", "vm", "vmware", "erspan" ]
aliases = [ "/questions/46449" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ERSPAN on Cisco ACI Fabric](/questions/46449/erspan-on-cisco-aci-fabric)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46449-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Dears,</p><p>I have a setup in the lab where I have configured ERSPAN on Cisco ACI Fabric which pretty similar to ERSPAN on Nexus switches 7k or 5K , I got the capture where I can see only the outer header for the packets but it's not helpful.</p><p>So I want to decapsulate/decode the ERSPAN packets where I can see the inner header for the captured pkts. I am using Wireshark 1.12.7 on windows 2008 server. it worth mentioning too that both source and destination are VMs.</p><p>I have attached a snapshot for the captured packets from wireshark.</p><p>How is this can be achieved ? I am looking for a decoder integrated with wireshark ?</p><p>Regards Mohammed ElSherbiny<img src="https://osqa-ask.wireshark.org/upfiles/ERSPAN_packet_capture.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">cisco vm vmware erspan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '15, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/d62492b62c78fcf873f5f3bc3cf49cdb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mohammedelsherbiny&#39;s gravatar image" /><p>mohammedelsh...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mohammedelsherbiny has no accepted answers">0%</span></p></img></div></div><div id="comments-container-46449" class="comments-container"><span id="46450"></span><div id="comment-46450" class="comment"><div id="post-46450-score" class="comment-score"></div><div class="comment-text"><p>Did you try setting the Erspan preference "FORCE to decode fake ERSPAN frame" to TRUE (as suggested in the expert message and which may or may not be helpful) ?<br />
</p><p>If setting the preference doesn't work, examining the capture will probably be the best way for us to help you.</p><p>Can you provide the capture ? (Upload it to something like dropbox) and provide a link here.</p></div><div id="comment-46450-info" class="comment-info"><span class="comment-age">(11 Oct '15, 04:35)</span> Bill Meier ♦♦</div></div><span id="58432"></span><div id="comment-58432" class="comment"><div id="post-58432-score" class="comment-score"></div><div class="comment-text"><p>I have the same problem although it was solved in the client by applying the "Force to decode fake ERSPAN" option. Does anyone know if/how this is possible using TSHARK?</p></div><div id="comment-58432-info" class="comment-info"><span class="comment-age">(30 Dec '16, 03:57)</span> xoomg</div></div><span id="58436"></span><div id="comment-58436" class="comment"><div id="post-58436-score" class="comment-score"></div><div class="comment-text"><p>Yes, you can add <code>-o erspan.fake_erspan:TRUE</code> to your tshark command.</p></div><div id="comment-58436-info" class="comment-info"><span class="comment-age">(30 Dec '16, 07:43)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-46449" class="comment-tools"></div><div class="clear"></div><div id="comment-46449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62118"></span>

<div id="answer-container-62118" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62118-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>choose „Preferences &gt; Protocols &gt; ERSPAN“ select “Force to decode fake ERSPAN frame”</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '17, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/15d2b06f613eb1ee16a4ee5df26dee94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="briantilburgs&#39;s gravatar image" /><p>briantilburgs<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="briantilburgs has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-62118" class="comments-container"></div><div id="comment-tools-62118" class="comment-tools"></div><div class="clear"></div><div id="comment-62118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

