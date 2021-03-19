+++
type = "question"
title = "Determine the direction of a conversation (client, server)"
description = '''I&#x27;m writing a dissector for a TCP-based protocol in C. Is it possible to determine whether a packet goes in the client-to-server or in the server-to-client direction? I have set up a conversation state, but I&#x27;m not sure what to put into it. I can recognize the first packet in the conversation (clien...'''
date = "2013-07-08T07:38:00Z"
lastmod = "2013-07-08T07:38:00Z"
weight = 22727
keywords = [ "conversation", "dissector" ]
aliases = [ "/questions/22727" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Determine the direction of a conversation (client, server)](/questions/22727/determine-the-direction-of-a-conversation-client-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22727-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a dissector for a TCP-based protocol in C.</p><p>Is it possible to determine whether a packet goes in the client-to-server or in the server-to-client direction?</p><p>I have set up a conversation state, but I'm not sure what to put into it. I can recognize the first packet in the conversation (client-to-server), and I use that to store <code>pinfo-&gt;srcport</code> and <code>pinfo-&gt;destport</code> in the conversation state, and in future packets I can compare <code>pinfo-&gt;srcport</code> against the stored value in the conversation. But that will break if the source and destination ports are the same.</p><p>I noticed that <code>*pinfo</code> contains source and destination <em>addresses</em>, too, but those are fixed for the entire conversation, i.e. they don't change between requests and responses.</p><p>What's the idiomatic way to track the direction of the conversation?</p></div><div id="question-tags" class="tags-container tags">conversation dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '13, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/3dcd36f51cf45ba2e5cfd351cbcf7127?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LouisDx&#39;s gravatar image" /><p>LouisDx<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LouisDx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '13, 07:38</p></div></div><div id="comments-container-22727" class="comments-container"></div><div id="comment-tools-22727" class="comment-tools"></div><div class="clear"></div><div id="comment-22727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

