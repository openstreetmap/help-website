+++
type = "question"
title = "Filtering Radius Attributes by length"
description = '''Hello, I am trying to discover any Radius attributes that don&#x27;t have a specific length. I have discovered that I can show all packets containing a specific attribute with a filter like this: radius.3Com_Connect_Id  but any attempt to perform further filtering based on the length of such an attribute...'''
date = "2015-01-06T03:56:00Z"
lastmod = "2015-01-06T03:56:00Z"
weight = 38902
keywords = [ "filter", "radius" ]
aliases = [ "/questions/38902" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering Radius Attributes by length](/questions/38902/filtering-radius-attributes-by-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38902-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to discover any Radius attributes that don't have a specific length. I have discovered that I can show all packets containing a specific attribute with a filter like this:</p><pre><code>radius.3Com_Connect_Id</code></pre><p>but any attempt to perform further filtering based on the length of such an attribute proves fruitless i.e.</p><pre><code>radius.3Com_Connect_Id.len &gt;= 0</code></pre><p>presents me with an empty window.</p><p>I have been looking at the documentation here: <a href="https://www.wireshark.org/docs/dfref/r/radius.html">https://www.wireshark.org/docs/dfref/r/radius.html</a></p><p>Am I misunderstanding the role of this '.len' suffix, or am I using it incorrectly?</p><p>Thanks and Best Regards, Robert</p></div><div id="question-tags" class="tags-container tags">filter radius</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '15, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/b2244263c61892ddd4d2b4d6b4786e6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robert_&#39;s gravatar image" /><p>robert_<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robert_ has no accepted answers">0%</span></p></div></div><div id="comments-container-38902" class="comments-container"></div><div id="comment-tools-38902" class="comment-tools"></div><div class="clear"></div><div id="comment-38902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

