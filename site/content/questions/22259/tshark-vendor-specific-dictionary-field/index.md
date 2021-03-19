+++
type = "question"
title = "Tshark Vendor specific dictionary field"
description = '''Hi, I&#x27;m trying to call an attribute from a vendor specific dictionary included for the following included radius dictionary &quot;dictionary.rfc4679&quot; How can I call attributes specified in this dictionary as a field in Tshark? e.g. I want to call the listed attribute ATTRIBUTE ADSL-Agent-Circuit-Id 1 str...'''
date = "2013-06-23T18:04:00Z"
lastmod = "2013-06-23T18:04:00Z"
weight = 22259
keywords = [ "radius", "tshark", "dictionary" ]
aliases = [ "/questions/22259" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark Vendor specific dictionary field](/questions/22259/tshark-vendor-specific-dictionary-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22259-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to call an attribute from a vendor specific dictionary included for the following included radius dictionary "dictionary.rfc4679"</p><p>How can I call attributes specified in this dictionary as a field in Tshark?</p><p>e.g. I want to call the listed attribute</p><pre><code>ATTRIBUTE       ADSL-Agent-Circuit-Id                   1       string</code></pre><p>As a field in the following command:</p><pre><code>tshark -i eth1 -T fields -e radius.Event_Timestamp  -e &quot;ADSL-Agent-Circuit-Id&quot;</code></pre><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">radius tshark dictionary</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '13, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/fad6f04e98254b85ab7301ab7c4425ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TsharkNewb&#39;s gravatar image" /><p>TsharkNewb<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TsharkNewb has no accepted answers">0%</span></p></div></div><div id="comments-container-22259" class="comments-container"></div><div id="comment-tools-22259" class="comment-tools"></div><div class="clear"></div><div id="comment-22259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

