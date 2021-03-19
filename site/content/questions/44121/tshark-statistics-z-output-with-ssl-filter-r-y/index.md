+++
type = "question"
title = "tshark statistics(-z) output with “ssl” filter(-R/-Y)"
description = '''As I mentioned in title I want to filter tshark&#x27;s dests,tree statistics output to show only encrypted(ssl) traffic. I tried tshark -a duration:30 -Y &quot;ssl&quot; -z dests,tree &amp;gt; output.txt but that doesn&#x27;t work as I expected. But from wireshark(gui) Statistics &amp;gt; IP Destinations filter:ssl works just ...'''
date = "2015-07-14T00:54:00Z"
lastmod = "2015-07-15T13:11:00Z"
weight = 44121
keywords = [ "filter", "statistics", "destination", "tshark", "ssl" ]
aliases = [ "/questions/44121" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark statistics(-z) output with “ssl” filter(-R/-Y)](/questions/44121/tshark-statistics-z-output-with-ssl-filter-r-y)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44121-score" class="post-score" title="current number of votes">0</div><span id="post-44121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As I mentioned in title I want to filter tshark's dests,tree statistics output to show only encrypted(ssl) traffic.</p><p>I tried <code>tshark -a duration:30 -Y "ssl" -z dests,tree &gt; output.txt</code> but that doesn't work as I expected. But from wireshark(gui) <code>Statistics &gt; IP Destinations filter:ssl</code> works just fine.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_VxKGv9s.png" alt="alt text" /></p><p>Are there any ways to do this with tshark or should I consider other tools?</p><p>Background: I'm writing a java application to automatically fetch scheduled tshark command output to show traffic bandwidth and incoming packets by ports per IP. I am absolutely not an expert in this job. If I'm looking for something wrong to do my job you should feel free to offer me better ways.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/e38b402a5635b121c60c316fcfca8da1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xmikro&#39;s gravatar image" /><p><span>xmikro</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xmikro has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jul '15, 01:06</strong> </span></p></div></div><div id="comments-container-44121" class="comments-container"><span id="44188"></span><div id="comment-44188" class="comment"><div id="post-44188-score" class="comment-score"></div><div class="comment-text"><p>It seems to work for me (tshark v1.99.8rc0-411-g89b375f), what is exactly not functioning? Can you see the normal dissection in the tshark output?</p></div><div id="comment-44188-info" class="comment-info"><span class="comment-age">(15 Jul '15, 13:11)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-44121" class="comment-tools"></div><div class="clear"></div><div id="comment-44121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

