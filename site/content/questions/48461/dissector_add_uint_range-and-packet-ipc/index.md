+++
type = "question"
title = "Dissector_add_uint_range and packet-ip.c"
description = '''I have an experimental network which is running IP-UDP-IP-UDP-XXX. I&#x27;ve written a dissector plugin for the XXX protocol and used dissector_add_uint_range to bind it to multiple UDP ports (more or less like in packet-http). I also used prefs_register_range_preference to allow the user to specify the ...'''
date = "2015-12-11T13:05:00Z"
lastmod = "2015-12-11T13:05:00Z"
weight = 48461
keywords = [ "ip", "range", "dissector" ]
aliases = [ "/questions/48461" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector\_add\_uint\_range and packet-ip.c](/questions/48461/dissector_add_uint_range-and-packet-ipc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48461-score" class="post-score" title="current number of votes">0</div><span id="post-48461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an experimental network which is running IP-UDP-IP-UDP-XXX. I've written a dissector plugin for the XXX protocol and used dissector_add_uint_range to bind it to multiple UDP ports (more or less like in packet-http). I also used prefs_register_range_preference to allow the user to specify the UDP ports. That all works fine.</p><p>I then went into the epan/dissectors directory and made the same modifications in packet-ip (using dissector_add_uint_range to bind ip_handle to a udp.port range). The call to prefs_register_range_preference seems to be working: the config page allows me to set the udp.port range. However, the ip dissectors are not called.</p><p>I can use "decode as" to force the second level of ip decoding, but there are a lot of ports to do this for.</p><p>Any thoughts on why the changes to the (much more complicated) packet-ip code aren't working?</p><p>Thanks, Greg</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-range" rel="tag" title="see questions tagged &#39;range&#39;">range</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '15, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/da482d9ecd7ff40ab142c736c91e6262?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GSL&#39;s gravatar image" /><p><span>GSL</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GSL has no accepted answers">0%</span></p></div></div><div id="comments-container-48461" class="comments-container"></div><div id="comment-tools-48461" class="comment-tools"></div><div class="clear"></div><div id="comment-48461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

