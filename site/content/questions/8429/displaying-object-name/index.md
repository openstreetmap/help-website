+++
type = "question"
title = "displaying object name"
description = '''which function in which file displays the object name part in the wireshark?'''
date = "2012-01-17T03:29:00Z"
lastmod = "2012-01-17T03:29:00Z"
weight = 8429
keywords = [ "object", "name" ]
aliases = [ "/questions/8429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [displaying object name](/questions/8429/displaying-object-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8429-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>which function in which file displays the object name part in the wireshark?</p></div><div id="question-tags" class="tags-container tags">object name</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '12, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/92707c24fa77ae73d3dd88b6a93a32aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Premini%20Francis&#39;s gravatar image" /><p>Premini Francis<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Premini Francis has no accepted answers">0%</span></p></div></div><div id="comments-container-8429" class="comments-container"><span id="8430"></span><div id="comment-8430" class="comment"><div id="post-8430-score" class="comment-score"></div><div class="comment-text"><p>Your question is very unclear; could you specify some more details? What object name? Where in Wirehshark is it displayed? What protocol are you talking about, and is it a protocol at all?</p></div><div id="comment-8430-info" class="comment-info"><span class="comment-age">(17 Jan '12, 03:32)</span> Jasper ♦♦</div></div><span id="8432"></span><div id="comment-8432" class="comment"><div id="post-8432-score" class="comment-score"></div><div class="comment-text"><p>The object name that is displayed in packet details of the SNMP protocol.</p></div><div id="comment-8432-info" class="comment-info"><span class="comment-age">(17 Jan '12, 05:31)</span> Premini Francis</div></div><span id="8441"></span><div id="comment-8441" class="comment"><div id="post-8441-score" class="comment-score"></div><div class="comment-text"><p>When it comes to SNMP object names are (mostly?) gotten from the loaded MIBS with the aid of LIBSMI. Some OID names are also added from the code register_ber_oid_dissector_handle() which in turn cals oid_add_from_string() ASN1 based dissectors may also add OID names. If you explain the purpose of your questions it might be easier to help you.</p></div><div id="comment-8441-info" class="comment-info"><span class="comment-age">(17 Jan '12, 09:47)</span> Anders ♦</div></div><span id="8451"></span><div id="comment-8451" class="comment"><div id="post-8451-score" class="comment-score"></div><div class="comment-text"><p>Am working on compressed OIDs. Am able to decode the compressed OIDs. But the packet details shows:</p><pre><code>variable-bindings: 2 items

1.3.6.1.2.1.2: value (null)

   object Name: 1.3.6.1.2.1.2 (iso.3.6.1.2.1.2)

   value (Null)

1.3.6.1.2.1.2.2.1: value (null)

   object Name: 2.46.2.2.1 (joint-iso-itu-t.46.2.2.1)

   value (Null)</code></pre><p>Now, I want to change the line,</p><pre><code>  object Name: 2.46.2.2.1 (joint-iso-itu-t.46.2.2.1)</code></pre><p>to</p><pre><code>  object Name: 1.3.6.1.2.1.2.2.1 (iso.3.6.1.2.1.2.2.1)</code></pre></div><div id="comment-8451-info" class="comment-info"><span class="comment-age">(18 Jan '12, 03:56)</span> Premini Francis</div></div></div><div id="comment-tools-8429" class="comment-tools"></div><div class="clear"></div><div id="comment-8429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

