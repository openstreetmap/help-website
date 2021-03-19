+++
type = "question"
title = "Diameter value decode for AF-Application-Identifier and AF-Charging-Identifier"
description = '''Greetings, Is there a way to correct decoded value for AF-Application-Identifier and AF-Charging-Identifier AVP&#x27;s to show printable text / correct decode? Current version Wire shark displays: AVP: AF-Application-Identifier(504) l=72 f=VM- vnd=TGPP val=2b672e336770702e696373692d7265663d2275726e253341...'''
date = "2015-02-16T01:56:00Z"
lastmod = "2015-02-16T06:44:00Z"
weight = 39884
keywords = [ "diameter" ]
aliases = [ "/questions/39884" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Diameter value decode for AF-Application-Identifier and AF-Charging-Identifier](/questions/39884/diameter-value-decode-for-af-application-identifier-and-af-charging-identifier)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39884-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>Is there a way to correct decoded value for AF-Application-Identifier and AF-Charging-Identifier AVP's to show printable text / correct decode?</p><p>Current version Wire shark displays:</p><p>AVP: AF-Application-Identifier(504) l=72 f=VM- vnd=TGPP val=2b672e336770702e696373692d7265663d2275726e253341...</p><p>Printable text: +g.3gpp.icsi-ref="urn%3Aurn-7%3A3gpp-service.ims.icsi.mmtel"</p><p>AVP: AF-Charging-Identifier(505) l=69 f=VM- vnd=TGPP val=6f326c6a69317362673230302d70637363662e6c61622e69...</p><p>Printable Text o2lji1sbg200-pcscf.lab.ims.optus.com.au-1424-62704-257574</p></div><div id="question-tags" class="tags-container tags">diameter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/03f2f27531c964e2d1e381c2bfa207c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DazzaS&#39;s gravatar image" /><p>DazzaS<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DazzaS has no accepted answers">0%</span></p></div></div><div id="comments-container-39884" class="comments-container"></div><div id="comment-tools-39884" class="comment-tools"></div><div class="clear"></div><div id="comment-39884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39889"></span>

<div id="answer-container-39889" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39889-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to 3GPP specifications</p><blockquote><pre><code>6.5.5 AF-Application-Identifier AVP

The AF-Application-identifier AVP (AVP code 504) is of type OctetString,</code></pre><p>and it contains information that identifies the particular service that the AF service session belongs to. This information may be used by the PDF to differentiate QoS for different application services. For example the AF-Application-Identifier may be used as additional information together with the Media-Type AVP when the QoS class for the bearer authorization at the Go interface is selected. The AF-Application-Identifier may be used also to complete the QoS authorization with application specific default settings in the PDF if the AF does not provide full Session-Component-Description information.</p><pre><code>6.5.6 AF-Charging-Identifier AVP

The AF-Charging-Identifier AVP (AVP code 505) is of type OctetString,</code></pre><p>contains the AF Charging Identifier that is sent by the AF. This information may be used for charging correlation with bearer layer.</p></blockquote><p>So there's no guarantee that the AVPs will contain printable test so in that respect Wiresharks presentation is correct.</p><p>If you want to change that you would have to add code to packet-diameter_3gpp.c to check if the content is prinatble text and if so add it to the protocol tree. see</p><p><code>dissect_diameter_3gpp_visited_nw_id().</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '15, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '15, 07:08</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-39889" class="comments-container"></div><div id="comment-tools-39889" class="comment-tools"></div><div class="clear"></div><div id="comment-39889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

