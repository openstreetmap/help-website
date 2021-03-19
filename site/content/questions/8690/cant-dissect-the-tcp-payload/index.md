+++
type = "question"
title = "can&#x27;t dissect the tcp payload!"
description = '''i&#x27;am working on a project, that is &quot;dissecting capture packets using libwireshark&quot; my code successfully dissected till tcp header but it cant dissect further the payload..the underlying protocol. how to do that.. any help! thanks! '''
date = "2012-01-30T03:38:00Z"
lastmod = "2012-01-30T03:55:00Z"
weight = 8690
keywords = [ "development", "dissector", "payload", "wireshark" ]
aliases = [ "/questions/8690" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [can't dissect the tcp payload!](/questions/8690/cant-dissect-the-tcp-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8690-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i'am working on a project, that is "dissecting capture packets using libwireshark"</p><p>my code successfully dissected till tcp header but it cant dissect further the payload..the underlying protocol.</p><p>how to do that.. any help!</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags">development dissector payload wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '12, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p>Sanny_D<br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-8690" class="comments-container"></div><div id="comment-tools-8690" class="comment-tools"></div><div class="clear"></div><div id="comment-8690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8692"></span>

<div id="answer-container-8692" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8692-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Register you dissector with the TCP dissectors port table, like do:</p><pre><code>dissector_add_uint(&quot;tcp.port&quot;, currentPort, PROTOABBREV_handle);</code></pre><p>Or, if there's no port relation, register your dissector as heuristic dissector, like so:</p><pre><code>heur_dissector_add(&quot;tcp&quot;, dissect_PROTOABBREV, proto_PROTOABBREV);</code></pre><p>All this can be found in <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.developer">doc/README.developer</a> and <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.heuristic">doc/README.heuristic</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '12, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8692" class="comments-container"><span id="8695"></span><div id="comment-8695" class="comment"><div id="post-8695-score" class="comment-score"></div><div class="comment-text"><p>thanks! but..i am not writing the dissector, just used epan_dissect_run() on the packet, but wireshark is not dissecting further down... :-|</p></div><div id="comment-8695-info" class="comment-info"><span class="comment-age">(30 Jan '12, 04:17)</span> Sanny_D</div></div><span id="8700"></span><div id="comment-8700" class="comment"><div id="post-8700-score" class="comment-score"></div><div class="comment-text"><p>What should it dissect then further down? What protocol are you referring too? Is that dissector registered and/or configured properly?</p></div><div id="comment-8700-info" class="comment-info"><span class="comment-age">(30 Jan '12, 06:59)</span> Jaap ♦</div></div><span id="8704"></span><div id="comment-8704" class="comment"><div id="post-8704-score" class="comment-score"></div><div class="comment-text"><p>Diameter protocol..rfc 3588</p><p>after tcp header it just prints.. proto-"data", and hex dump of the diameter message</p><p>its not showing the AVPS in the message.. thanks!</p></div><div id="comment-8704-info" class="comment-info"><span class="comment-age">(30 Jan '12, 09:54)</span> Sanny_D</div></div><span id="8712"></span><div id="comment-8712" class="comment"><div id="post-8712-score" class="comment-score"></div><div class="comment-text"><p>Is that dissector registered and/or configured properly?</p></div><div id="comment-8712-info" class="comment-info"><span class="comment-age">(30 Jan '12, 11:22)</span> Jaap ♦</div></div><span id="8716"></span><div id="comment-8716" class="comment"><div id="post-8716-score" class="comment-score"></div><div class="comment-text"><p>yes.. during the epan initialization i registered that protocol using "register all protocols" and in that callback register_diameter function is there.</p><p>version wireshark 1.6.4 with tha patch 39873.</p></div><div id="comment-8716-info" class="comment-info"><span class="comment-age">(30 Jan '12, 19:36)</span> Sanny_D</div></div><span id="8719"></span><div id="comment-8719" class="comment not_top_scorer"><div id="post-8719-score" class="comment-score"></div><div class="comment-text"><p>By default, <em>ONLY</em> TCP traffic to or from port 3868 will be dissected as Diameter traffic. What TCP ports is the traffic you're handing libwireshark going to and coming from?</p></div><div id="comment-8719-info" class="comment-info"><span class="comment-age">(30 Jan '12, 22:25)</span> Guy Harris ♦♦</div></div><span id="8721"></span><div id="comment-8721" class="comment not_top_scorer"><div id="post-8721-score" class="comment-score"></div><div class="comment-text"><p>Is that dissector configured properly?</p></div><div id="comment-8721-info" class="comment-info"><span class="comment-age">(30 Jan '12, 22:48)</span> Jaap ♦</div></div><span id="8722"></span><div id="comment-8722" class="comment not_top_scorer"><div id="post-8722-score" class="comment-score"></div><div class="comment-text"><p>thanks a ton! :)</p><p>wat if i want to change the default port for diameter :-/ wat i need to do ?</p></div><div id="comment-8722-info" class="comment-info"><span class="comment-age">(30 Jan '12, 22:49)</span> Sanny_D</div></div><span id="8724"></span><div id="comment-8724" class="comment not_top_scorer"><div id="post-8724-score" class="comment-score"></div><div class="comment-text"><p>Edit your Wireshark preference file (creating it if necessary) and change the "diameter.tcp.ports" preference to list the ports you want to be used as Diameter ports.</p></div><div id="comment-8724-info" class="comment-info"><span class="comment-age">(30 Jan '12, 23:34)</span> Guy Harris ♦♦</div></div><span id="8733"></span><div id="comment-8733" class="comment not_top_scorer"><div id="post-8733-score" class="comment-score"></div><div class="comment-text"><p>coudnt find the file in /share folder.. have no idea how to create it :-/ and dissector is dissecting diameter without using the xml dictionary :|</p></div><div id="comment-8733-info" class="comment-info"><span class="comment-age">(31 Jan '12, 10:14)</span> Sanny_D</div></div><span id="8734"></span><div id="comment-8734" class="comment not_top_scorer"><div id="post-8734-score" class="comment-score"></div><div class="comment-text"><p>I infer from the <code>/</code> in <code>/share</code> that this is a UN*X system of some sort; if so, the file is in the <code>.wireshark</code> subdirectory of your home directory.</p><p>If it's not using the XML dictionary, it's probably not finding the XML dictionary; it will look for it in whatever directory was configured as the "data file directory" when Wireshark was configured and built.</p></div><div id="comment-8734-info" class="comment-info"><span class="comment-age">(31 Jan '12, 10:44)</span> Guy Harris ♦♦</div></div><span id="8775"></span><div id="comment-8775" class="comment not_top_scorer"><div id="post-8775-score" class="comment-score"></div><div class="comment-text"><p>i have a client(port 5678) server(3668)</p><p>i have edited the preferences file diameter.tcp.ports=3000-7000</p><p>but still libwireshark is dissecting only the diameter traffic for port 3868.. if i change the port of server other than 3868... it doesnt dissect the diamter protocol</p></div><div id="comment-8775-info" class="comment-info"><span class="comment-age">(02 Feb '12, 03:18)</span> Sanny_D</div></div><span id="8777"></span><div id="comment-8777" class="comment not_top_scorer"><div id="post-8777-score" class="comment-score"></div><div class="comment-text"><p>Make sure to set 'diameter.desegment' to true, as well as 'tcp.desegment_tcp_streams'. Better yet, test your preferences with Wireshark first.</p></div><div id="comment-8777-info" class="comment-info"><span class="comment-age">(02 Feb '12, 05:16)</span> Jaap ♦</div></div><span id="8797"></span><div id="comment-8797" class="comment not_top_scorer"><div id="post-8797-score" class="comment-score"></div><div class="comment-text"><p>testing it with tshark does exactly what i want..</p><p>i set the preferences using prefs_set_pref(char *prefarg);</p><p>but when i use the same function in my code and set the port:4868 and print the preference file it shows that "diameter.tcp.ports:4868:</p><p>but still it dissecting the diameter protocol for only the 3868 (default port)</p><p>just cant figure out what is the problem</p></div><div id="comment-8797-info" class="comment-info"><span class="comment-age">(02 Feb '12, 22:38)</span> Sanny_D</div></div></div><div id="comment-tools-8692" class="comment-tools"><span class="comments-showing"> showing 5 of 14 </span> <a href="#" class="show-all-comments-link">show 9 more comments</a></div><div class="clear"></div><div id="comment-8692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

