+++
type = "question"
title = "tshark: Display filters aren&#x27;t supported when capturing and saving the captured packets."
description = '''Am new to tshark.I wanto capture some ipp data using wireshark for that am using following tshark terminal commnd  tshark -i 3 -a duration:20 -Y &quot;ipp contains 02:00:00&quot; -T pdml &amp;gt; gggggg.xml  In the above command am setting a duration of 20 sec after that tshark execution wil stop automaticlly and...'''
date = "2015-02-23T23:55:00Z"
lastmod = "2015-02-24T09:10:00Z"
weight = 40039
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/40039" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark: Display filters aren't supported when capturing and saving the captured packets.](/questions/40039/tshark-display-filters-arent-supported-when-capturing-and-saving-the-captured-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40039-score" class="post-score" title="current number of votes">0</div><span id="post-40039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Am new to tshark.I wanto capture some ipp data using wireshark</p><p>for that am using following tshark terminal commnd</p><blockquote><p>tshark -i 3 -a duration:20 -Y "ipp contains 02:00:00" -T pdml &gt; gggggg.xml</p></blockquote><p>In the above command am setting a duration of 20 sec after that tshark execution wil stop automaticlly and created an xml file</p><p>it is working properly fine</p><p>But some situations there is a delay in getting 'ipp' data and after 20 sec tashark caputing will stops .due this am not able to caputure the data.it exits after 20 sec. when i increase the time delay i will get the full data as xml file. Am looking another options like setting the file size and when the file size reaches particular kb stop tshark.for that i changed the tshar command as</p><blockquote><p>tshark -i 3 -Y "ipp contains 02:00:00" -b filesize:100 -b files:1 -l -w some.txt -T pdml &gt; gggggg.xml</p></blockquote><p>am getting the error</p><blockquote><p>tshark: Display filters aren't supported when capturing and saving the captured packets.</p></blockquote><p>How can i crerate an xml file with and when the file size reaches particular Kbs stop the tshark execution.also i need to use filter type as "ipp contains 02:00:00"(it will only outputs ipp packets data as xml)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '15, 23:55</strong></p><img src="https://secure.gravatar.com/avatar/879f5559fb8d7c49ede20e033c03cc99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kichuz&#39;s gravatar image" /><p><span>kichuz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kichuz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '15, 23:58</strong> </span></p></div></div><div id="comments-container-40039" class="comments-container"></div><div id="comment-tools-40039" class="comment-tools"></div><div class="clear"></div><div id="comment-40039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40052"></span>

<div id="answer-container-40052" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40052-score" class="post-score" title="current number of votes">1</div><span id="post-40052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kichuz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try a 2-step approach?</p><p>First, capture general traffic of interest using <code>tshark</code> or even <code>dumpcap</code>:</p><pre><code>dumpcap -i 3 -f &quot;tcp port 631&quot; -a filesize:100 -n -w gggggg.pcapng</code></pre><p>Once <code>dumpcap</code> terminates, have <code>tshark</code> read the exact packets of interest from the capture file and process the packets as you'd like:</p><pre><code>tshark -r gggggg.pcapng -Y &quot;ipp contains 02:00:00&quot; -T pdml &gt; gggggg.xml</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '15, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-40052" class="comments-container"></div><div id="comment-tools-40052" class="comment-tools"></div><div class="clear"></div><div id="comment-40052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

