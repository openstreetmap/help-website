+++
type = "question"
title = "how to get ethernet trailer with lua parser"
description = '''I have a protocol involving UDP over IP over Ethernet where the last byte of the Ethernet frame before the FCS is not part of the UDP/IP packet but appears as an Ethernet trailer. (I had to disable VSS-Monitoring protocol in Wireshark to see this as VSS-Monitoring keeps interpreting this byte which ...'''
date = "2015-05-21T12:13:00Z"
lastmod = "2015-06-27T20:12:00Z"
weight = 42608
keywords = [ "ethernet", "trailer", "lua" ]
aliases = [ "/questions/42608" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to get ethernet trailer with lua parser](/questions/42608/how-to-get-ethernet-trailer-with-lua-parser)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42608-score" class="post-score" title="current number of votes">0</div><span id="post-42608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a protocol involving UDP over IP over Ethernet where the last byte of the Ethernet frame before the FCS is not part of the UDP/IP packet but appears as an Ethernet trailer. (I had to disable VSS-Monitoring protocol in Wireshark to see this as VSS-Monitoring keeps interpreting this byte which has nothing to do with VSS.) I need to access this last byte using my lua parser but I can't find a way to do it. I tried the following:</p><pre><code>local f_eth_trailer = Field.new(&quot;eth.trailer&quot;) -- outside the dissector</code></pre><p>In the dissector:</p><pre><code>local eth_trailer = f_eth_trailer()
local x = tostring(eth_trailer)</code></pre><p>But x is always returned as nil. I tried this same approach for the Ethernet source address (i.e. "eth.src" instead of "eth.trailer" in the above) and that works fine and returns the string with the Ethernet source address.</p><p>Can anyone please provide an approach I can use to access this Ethernet trailer byte?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-trailer" rel="tag" title="see questions tagged &#39;trailer&#39;">trailer</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '15, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/f212ffc18ffdaf1765cce2e8eac0e403?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiredtotheshark&#39;s gravatar image" /><p><span>wiredtotheshark</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiredtotheshark has no accepted answers">0%</span></p></div></div><div id="comments-container-42608" class="comments-container"><span id="43620"></span><div id="comment-43620" class="comment"><div id="post-43620-score" class="comment-score"></div><div class="comment-text"><p>Are you sure there actually is a "eth.trailer" field in the packet? When you look at the packet in the GUI window and click on the Ethernet packet layer, does it actually show a "Trailer" field in the packet details window pane, and clicking on that field shows "eth.trailer" on the bottom left of the whole window?</p><p>I ask because most packet captures don't have one, and even if it does you usually have to set the preferences to show it (by setting the Edit-&gt;Preferences-&gt;Protocols-&gt;Ethernet entry for "Fixed ethernet trailer length" to the trailer length, which would be larger than the default of 0).</p></div><div id="comment-43620-info" class="comment-info"><span class="comment-age">(27 Jun '15, 20:12)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-42608" class="comment-tools"></div><div class="clear"></div><div id="comment-42608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

