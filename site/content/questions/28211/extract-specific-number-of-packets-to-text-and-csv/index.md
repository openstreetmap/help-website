+++
type = "question"
title = "extract specific number of packets to text and csv."
description = '''Hi, I have a traffic sample in pcap format, I want to export the data as txt and csv files. Here is the code which I am using: for CSV: tshark -Y &quot;ip&quot; -r a.pcap -T fields -e frame.number -e ip.proto -e ip.src -e tcp.srcport -e udp.srcport -e ip.dst -e tcp.dstport -e udp.dstport -e frame.len -e frame...'''
date = "2013-12-17T05:15:00Z"
lastmod = "2013-12-17T22:17:00Z"
weight = 28211
keywords = [ "and", "text", "csv", "export" ]
aliases = [ "/questions/28211" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [extract specific number of packets to text and csv.](/questions/28211/extract-specific-number-of-packets-to-text-and-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28211-score" class="post-score" title="current number of votes">0</div><span id="post-28211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a traffic sample in pcap format, I want to export the data as txt and csv files. Here is the code which I am using:</p><p>for CSV:</p><p>tshark -Y "ip" -r a.pcap -T fields -e frame.number -e ip.proto -e ip.src -e tcp.srcport -e udp.srcport -e ip.dst -e tcp.dstport -e udp.dstport -e frame.len -e frame.time_delta -e tcp.flags -e frame.time -e frame.time_relative -E header=y -E separator=";" &gt; a.csv</p><p>for Text file:</p><p>tshark -Y "ip" -o column.format:'"No.","%m", "full time", "%Yt","src ip", "%us","des ip","%ud", "lenght", "%L",”transfered byte","%B","protocol","%p","srcmac","%uhs","destmac","%uhd","sourceport", "%uS", "destport", "%uD", "Info", "%i"' -r a.pcap &gt; a.txt</p><p>But as the traffic sample have 5 million packets and I need specific number of packets, can i import the packets detail for example from packet 1,234,567 to 4,567,567 ?</p><p>How is it possible?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-and" rel="tag" title="see questions tagged &#39;and&#39;">and</span> <span class="post-tag tag-link-text" rel="tag" title="see questions tagged &#39;text&#39;">text</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '13, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/a76f3e9f7708742d5869cf5353337891?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Payam365&#39;s gravatar image" /><p><span>Payam365</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Payam365 has no accepted answers">0%</span></p></div></div><div id="comments-container-28211" class="comments-container"></div><div id="comment-tools-28211" class="comment-tools"></div><div class="clear"></div><div id="comment-28211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28214"></span>

<div id="answer-container-28214" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28214-score" class="post-score" title="current number of votes">2</div><span id="post-28214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Payam365 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The -Y filter could be enhanced to -Y "ip and frame.number gt xxx and frame.number lt yyy"</p><p>Is this what you were looking for ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '13, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28214" class="comments-container"><span id="28219"></span><div id="comment-28219" class="comment"><div id="post-28219-score" class="comment-score"></div><div class="comment-text"><p>yes, thanks</p></div><div id="comment-28219-info" class="comment-info"><span class="comment-age">(17 Dec '13, 09:15)</span> <span class="comment-user userinfo">Payam365</span></div></div><span id="28233"></span><div id="comment-28233" class="comment"><div id="post-28233-score" class="comment-score"></div><div class="comment-text"><p>Don't forget to 'accept' the answer to mark it as closed, thanks</p></div><div id="comment-28233-info" class="comment-info"><span class="comment-age">(17 Dec '13, 22:17)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-28214" class="comment-tools"></div><div class="clear"></div><div id="comment-28214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

