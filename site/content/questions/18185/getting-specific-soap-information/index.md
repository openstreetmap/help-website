+++
type = "question"
title = "Getting specific SOAP-information"
description = '''Hey, I want to get information out of SOAP... In the SOAP-Body is a node called: &amp;lt;ns1:writeReport [..just a lot of unnecessary things..] xmlns:ns1=&#x27;http://writeReport.[domain].de&#x27;&amp;gt;  In this node is an other node called:  &amp;lt;PartnerID&amp;gt; 123456789 &amp;lt;/PartnerID&amp;gt;  I just want to get the in...'''
date = "2013-01-31T08:14:00Z"
lastmod = "2013-01-31T08:14:00Z"
weight = 18185
keywords = [ "envelope", "tshark", "soap" ]
aliases = [ "/questions/18185" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting specific SOAP-information](/questions/18185/getting-specific-soap-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18185-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I want to get information out of SOAP... In the SOAP-Body is a node called:</p><pre><code>&lt;ns1:writeReport [..just a lot of unnecessary things..]  xmlns:ns1=&#39;http://writeReport.[domain].de&#39;&gt;</code></pre><p>In this node is an other node called:</p><pre><code>&lt;PartnerID&gt;
123456789
&lt;/PartnerID&gt;</code></pre><p>I just want to get the information of the PartnerID with &gt;tShark&lt;. How do I do this?</p><p>When I try to use this parameter:</p><pre><code>-X env:Envelope</code></pre><p>I just get the names of the nodes, but not the content inside.</p></div><div id="question-tags" class="tags-container tags">envelope tshark soap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '13, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/494660c8c52c6a7060c13f80fc6e95f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bregnar&#39;s gravatar image" /><p>bregnar<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bregnar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Jan '13, 08:19</p></div></div><div id="comments-container-18185" class="comments-container"></div><div id="comment-tools-18185" class="comment-tools"></div><div class="clear"></div><div id="comment-18185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

