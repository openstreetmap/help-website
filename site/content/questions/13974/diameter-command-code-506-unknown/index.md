+++
type = "question"
title = "Diameter - Command code: 506 Unknown"
description = '''I&#x27;am investigating some issue about Diameter and HSS (AAA). In wireshark I keep having: Command Code: 506 Unknown The AVP 506 seem to be related to Mobile-Node-Identifier  source http://www.rfc-editor.org/rfc/rfc5779.txt (section 5.6) I tried to add this in the wireshark file dictionnary.xml but it ...'''
date = "2012-08-31T12:48:00Z"
lastmod = "2012-08-31T13:13:00Z"
weight = 13974
keywords = [ "diameter", "avp", "aaa", "hss" ]
aliases = [ "/questions/13974" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Diameter - Command code: 506 Unknown](/questions/13974/diameter-command-code-506-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13974-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'am investigating some issue about Diameter and HSS (AAA). In wireshark I keep having: Command Code: 506 Unknown</p><p>The AVP 506 seem to be related to Mobile-Node-Identifier source <a href="http://www.rfc-editor.org/rfc/rfc5779.txt">http://www.rfc-editor.org/rfc/rfc5779.txt</a> (section 5.6) I tried to add this in the wireshark file dictionnary.xml but it seem it doesn't work :( &lt;avp name="Mobile-Node-Identifier" code="506" mandatory="must" may-encrypt="no" protected="mustnot" vendor-bit="mustnot" vendor-id="TGPP"&gt; &lt;type type-name="UTF8String"/&gt; &lt;/avp&gt;</p></div><div id="question-tags" class="tags-container tags">diameter avp aaa hss</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '12, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/bf652eb73e52b2e88b1cb47803f0b45e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pokstar&#39;s gravatar image" /><p>pokstar<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pokstar has no accepted answers">0%</span></p></div></div><div id="comments-container-13974" class="comments-container"></div><div id="comment-tools-13974" class="comment-tools"></div><div class="clear"></div><div id="comment-13974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13975"></span>

<div id="answer-container-13975" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13975-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's a command code not an AVP and probably a proprietarry one as it's not assigned by IANA. <a href="http://www.iana.org/assignments/aaa-parameters/aaa-parameters.xml">http://www.iana.org/assignments/aaa-parameters/aaa-parameters.xml</a> If you know what it is add it after &lt;command name="IKEv2-SK" code="329" vendor-id="None"/&gt; using that format.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '12, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-13975" class="comments-container"></div><div id="comment-tools-13975" class="comment-tools"></div><div class="clear"></div><div id="comment-13975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

