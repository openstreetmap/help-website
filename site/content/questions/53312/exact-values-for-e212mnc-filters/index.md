+++
type = "question"
title = "Exact Values for e212.mnc filters"
description = '''At the moment we are using tshark (v2.0.3) to extract specific parameters from GTP traffic. in some cases when the value for mnc is 01 tshark returns 1 which technically is not equal to 01, the thing is in wireshark we can see the correct value from proto tree  tshark command: -l -n -r &quot;C:&#92;sample.pc...'''
date = "2016-06-08T04:01:00Z"
lastmod = "2016-06-08T04:01:00Z"
weight = 53312
keywords = [ "tshark" ]
aliases = [ "/questions/53312" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Exact Values for e212.mnc filters](/questions/53312/exact-values-for-e212mnc-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53312-score" class="post-score" title="current number of votes">0</div><span id="post-53312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At the moment we are using tshark (v2.0.3) to extract specific parameters from GTP traffic. in some cases when the value for mnc is <strong>01</strong> tshark returns <strong>1</strong> which technically is not equal to <strong>01</strong>, the thing is in wireshark we can see the correct value from proto tree</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_4kmUfD9.PNG" alt="alt text" /></p><p><em>tshark command:</em></p><pre><code>-l -n -r &quot;C:\sample.pcap&quot; -2 -R &quot;((gtp.message == 0x10 or gtp.message == 0x11 or gtpv2.message_type == 32   or gtpv2.message_type == 33) and not (icmp))&quot; -T fields -e e212.mcc -e e212.mnc</code></pre><p>and in PDML exportو we can see correct value (f210) in <strong>Value</strong> attribute, but it seems -T field command is returning values found in <strong>Show</strong> attribute.</p><pre><code>field name=&quot;e212.mnc&quot; showname=&quot;Mobile Network Code (MNC): Telekom Deutschland GmbH (01)&quot; size=&quot;2&quot; pos=&quot;187&quot; show=&quot;1&quot; value=&quot;f210&quot;/&gt;</code></pre><p>Is there any argument or configuration forcing tshark to extract raw values?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '16, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/6ed60f06c812665ce60b6e6c2d8c9eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hja&#39;s gravatar image" /><p><span>hja</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hja has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53312" class="comments-container"></div><div id="comment-tools-53312" class="comment-tools"></div><div class="clear"></div><div id="comment-53312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

