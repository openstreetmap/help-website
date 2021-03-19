+++
type = "question"
title = "ebtables bridge CMIP application layer to not shown in capture"
description = '''I applied a Linux Ethernet bridge over my connection and then ran wireshark to look at the packets. Before the bridge was applied, wireshark could parse the CMIP layer fine (so when the packet came in it was classified as a CMIP packet) however when the bridge was applied the packet was still captur...'''
date = "2015-06-29T13:31:00Z"
lastmod = "2015-06-29T13:31:00Z"
weight = 43686
keywords = [ "bridge", "ebtables", "cmip", "netfilter", "linux" ]
aliases = [ "/questions/43686" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ebtables bridge CMIP application layer to not shown in capture](/questions/43686/ebtables-bridge-cmip-application-layer-to-not-shown-in-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43686-score" class="post-score" title="current number of votes">0</div><span id="post-43686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I applied a Linux Ethernet bridge over my connection and then ran wireshark to look at the packets. Before the bridge was applied, wireshark could parse the CMIP layer fine (so when the packet came in it was classified as a CMIP packet) however when the bridge was applied the packet was still captured but it could only get as far as the ISO 8823 OSI Presentation Protocol layer so I couldn't see the CMIP data at all. Any idea why this is? I can't tell if this is just the bridge that cannot parse that layer and is leaving it off the packet or if it is wireshark not displaying it properly.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-ebtables" rel="tag" title="see questions tagged &#39;ebtables&#39;">ebtables</span> <span class="post-tag tag-link-cmip" rel="tag" title="see questions tagged &#39;cmip&#39;">cmip</span> <span class="post-tag tag-link-netfilter" rel="tag" title="see questions tagged &#39;netfilter&#39;">netfilter</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '15, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/378dec08c639d6c2c2979b244af9660e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lp4968&#39;s gravatar image" /><p><span>lp4968</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lp4968 has no accepted answers">0%</span></p></div></div><div id="comments-container-43686" class="comments-container"></div><div id="comment-tools-43686" class="comment-tools"></div><div class="clear"></div><div id="comment-43686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

