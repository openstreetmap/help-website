+++
type = "question"
title = "ieee 1722.1 dissect regression"
description = '''It seems that newer versions of wireshark does not dissect/display avdecc/ieee 1722.1 packets. Only the 1722 part of the packets are shown in the newer versions.  Versions tested: works: 1.12.13 (compiled from source), 1.10.6 (windows) doesn&#x27;t work: 2.2.3 (compiled from source), 2.2.3 (ubuntu 14.04)...'''
date = "2017-01-10T04:23:00Z"
lastmod = "2017-01-12T06:50:00Z"
weight = 58635
keywords = [ "avdecc", "ieee1722.1", "dissect" ]
aliases = [ "/questions/58635" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ieee 1722.1 dissect regression](/questions/58635/ieee-17221-dissect-regression)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58635-score" class="post-score" title="current number of votes">0</div><span id="post-58635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It seems that newer versions of wireshark does not dissect/display avdecc/ieee 1722.1 packets. Only the 1722 part of the packets are shown in the newer versions.</p><p>Versions tested:<br />
works: 1.12.13 (compiled from source), 1.10.6 (windows)<br />
doesn't work: 2.2.3 (compiled from source), 2.2.3 (ubuntu 14.04)<br />
</p><p>Using tshark the old version displays:<br />
5 3.703944766 Ieee1722_01:00:00 CadmusCo_e7:27:77 DISCONNECT_RX_COMMAND IEEE1722-1 AVDECC Connection Management Protocol<br />
While the new version displays:<br />
5 3.703944766 Ieee1722_01:00:00 PcsSyste_e7:27:77 IEEE1722 AVB Transportation Protocol</p><p>How can I enable the dissection in the new version? IEEE1722.1 is enabled in the list of enabled protocols. There is no option to force decoding as IEEE1722.1.</p><p><a href="https://drive.google.com/open?id=0B7mhcCfgZwjqUjFEdE1RTUhPNU0">relevant packet capture</a><br />
<a href="https://drive.google.com/open?id=0B7mhcCfgZwjqNElRMWpTUGhxdm8">tshark-1.12.13 -r ~/avdecc.pcapng -T text -V &gt; tshark_old.txt</a><br />
<a href="https://drive.google.com/open?id=0B7mhcCfgZwjqeTYxbmJ0SXU1QUE">tshark-2.2.3 -r ~/avdecc.pcapng -T text -V &gt; tshark_new.txt</a><br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-avdecc" rel="tag" title="see questions tagged &#39;avdecc&#39;">avdecc</span> <span class="post-tag tag-link-ieee1722.1" rel="tag" title="see questions tagged &#39;ieee1722.1&#39;">ieee1722.1</span> <span class="post-tag tag-link-dissect" rel="tag" title="see questions tagged &#39;dissect&#39;">dissect</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '17, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/8fe3d7db09cc206915914370b0d4224a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leon1234&#39;s gravatar image" /><p><span>leon1234</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leon1234 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jan '17, 05:47</strong> </span></p></div></div><div id="comments-container-58635" class="comments-container"><span id="58636"></span><div id="comment-58636" class="comment"><div id="post-58636-score" class="comment-score"></div><div class="comment-text"><p>We'll need a capture file to investigate. Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox etc.? Edit your question with a link to the capture.</p></div><div id="comment-58636-info" class="comment-info"><span class="comment-age">(10 Jan '17, 04:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="58637"></span><div id="comment-58637" class="comment"><div id="post-58637-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I've added the relevant dissections as well.</p></div><div id="comment-58637-info" class="comment-info"><span class="comment-age">(10 Jan '17, 05:49)</span> <span class="comment-user userinfo">leon1234</span></div></div></div><div id="comment-tools-58635" class="comment-tools"></div><div class="clear"></div><div id="comment-58635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58641"></span>

<div id="answer-container-58641" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58641-score" class="post-score" title="current number of votes">1</div><span id="post-58641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="leon1234 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the dissection of IEEE1722 has been "improved" so that the message type is now an element of dissection rather than text added to the tree, tshark output no longer shows the text you were looking for.</p><p>You can fix this by inspecting the packet in the Wireshark GUI (using the default profile), selecting the IEEE 1722.1 Message Type field, right-clicking and selecting "Apply As Column". Running tshark now give me:</p><pre><code>5 3.703944766 PcsCompu_e7:27:77 → Ieee1722_01:00:00 IEEE1722-1 70 DISCONNECT_RX_COMMAND AVDECC Connection Management Protocol</code></pre><p>You could also use the tshark <code>-T fields -e ieee17221.message_type -e ...</code> options to print out the exact fields you require, but this shows the field numeric value, not the text equivalent.</p><p>Note: I'm using 2.3.0, i.e. a dev build.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '17, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-58641" class="comments-container"><span id="58656"></span><div id="comment-58656" class="comment"><div id="post-58656-score" class="comment-score"></div><div class="comment-text"><p>There is no "IEEE 1722.1 Message Type" field to select in the new GUI. Setting the filter to ieee17221.message_type results in no packets being displayed.</p><p>Using <code>tshark -r ~/avdecc.pcapng -T fields -e ieee17221.message_type</code> shows the expected message type using the old version but just blank lines using the new version.</p><p>It seems that I'll have to use the dev build or an ancient version together with multiple -e options. This seems wrong given the nice -T json output available for other packets. Should I file a bug report?</p></div><div id="comment-58656-info" class="comment-info"><span class="comment-age">(10 Jan '17, 23:10)</span> <span class="comment-user userinfo">leon1234</span></div></div><span id="58658"></span><div id="comment-58658" class="comment"><div id="post-58658-score" class="comment-score"></div><div class="comment-text"><p>I think it would be best to try a dev build first. Changes to the stable release are meant to be bugfixes only and this falls in a grey area.</p><p>If the dev build doesn't produce the required output, then definitely file a bug report.</p><p>IMHO I think the dev dissection is wrong as the info column is showing the IEEE 1722 protocol subtype instead of the IEEE 1722.1 message type, I thought the info column should show the "highest" protocol seen, e.g. an HTTP GET, not a TCP frame, but I've no experience about this protocol so can't really say what would be useful.</p></div><div id="comment-58658-info" class="comment-info"><span class="comment-age">(11 Jan '17, 02:49)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="58700"></span><div id="comment-58700" class="comment"><div id="post-58700-score" class="comment-score"></div><div class="comment-text"><p>The dev build Version 2.3.0 (v2.3.0rc0-2014-gf8dc234) gave me exactly the output I was looking for.</p><p>Thanks for the help.</p></div><div id="comment-58700-info" class="comment-info"><span class="comment-age">(12 Jan '17, 06:50)</span> <span class="comment-user userinfo">leon1234</span></div></div></div><div id="comment-tools-58641" class="comment-tools"></div><div class="clear"></div><div id="comment-58641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

